"""Descriptive reference figure for synthetic teaching data; no hypothesis tests."""
import argparse
import hashlib
import json
import platform
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=Path, required=True)
parser.add_argument('--out', type=Path, required=True)
args = parser.parse_args()
if args.out.exists():
    raise SystemExit('Output directory exists. Choose a new directory.')
df = pd.read_csv(args.data)
required = ['donor_id','sample_id','technical_replicate','treatment','stimulation','activation_percent','data_origin']
assert df.columns.tolist() == required
assert df.shape == (80, 7) and not df.isna().any().any()
assert not df.duplicated(['sample_id','technical_replicate']).any()
assert set(df.donor_id) == {f'D{i:02d}' for i in range(1,11)}
assert set(df.treatment) == {'Vehicle','Compound_X'}
assert set(df.stimulation) == {'Unstimulated','Stimulated'}
assert df.data_origin.eq('synthetic').all()
assert df.activation_percent.between(0,100).all()
keys = ['donor_id','treatment','stimulation']
groups = df.groupby(keys, sort=True)
assert len(groups) == 40 and groups.size().eq(2).all()
assert groups.sample_id.nunique().eq(1).all()
assert df.groupby('sample_id')[keys].nunique().eq(1).all().all()
assert groups.technical_replicate.apply(lambda x: set(x)=={1,2}).all()
cultures = groups.activation_percent.mean().reset_index()
wide = cultures.pivot(index=['donor_id','stimulation'],columns='treatment',values='activation_percent')
assert wide.shape == (20,2) and not wide.isna().any().any()
differences = (wide.Compound_X-wide.Vehicle).rename('difference_pp').reset_index()
summary = differences.groupby('stimulation').difference_pp.agg(['count','mean','min','max']).reset_index()
args.out.mkdir(parents=True)
cultures.to_csv(args.out/'plot_data.csv',index=False)
differences.to_csv(args.out/'donor_differences.csv',index=False)
summary.to_csv(args.out/'descriptive_summary.csv',index=False)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'pdf.fonttype':42,'svg.fonttype':'none'})
fig, axes = plt.subplots(1,3,figsize=(10.8,4.5),gridspec_kw={'width_ratios':[1,1,1.2]})
colours=['#287A96','#B36B29']
for ax,stim in zip(axes[:2],['Unstimulated','Stimulated']):
    pair=wide.xs(stim,level='stimulation').sort_index()
    for donor,row in pair.iterrows():
        ax.plot([0,1],row[['Vehicle','Compound_X']],color='#A4ADB5',lw=0.9,zorder=1)
    for i,treatment in enumerate(['Vehicle','Compound_X']):
        ax.scatter([i]*len(pair),pair[treatment],c=colours[i],s=24,marker=['o','s'][i],zorder=2)
    ax.set_xticks([0,1],['Vehicle','Compound_X'])
    ax.set_xlim(-0.3,1.3); ax.set_ylim(0,100); ax.set_title(stim,loc='left',fontweight='bold')
    ax.set_ylabel('CD69+CD137+ within CD8 parent (%)')
ax=axes[2]
for i,stim in enumerate(['Unstimulated','Stimulated']):
    vals=differences.loc[differences.stimulation.eq(stim),'difference_pp'].to_numpy()
    offsets=[(j-4.5)*0.025 for j in range(10)]
    ax.scatter(vals,[i+v for v in offsets],s=24,color='#287A96',label='Donor' if i==0 else None)
    ax.scatter([vals.mean()],[i],s=65,color='#182B45',marker='D',label='Mean' if i==0 else None,zorder=3)
ax.axvline(0,color='#808080',linestyle='--',lw=0.8)
ax.set_yticks([0,1],['Unstimulated','Stimulated']); ax.set_ylim(1.5,-0.5)
ax.set_xlabel('Compound_X − Vehicle\n(percentage points)')
ax.set_title('Treatment differences',loc='left',fontweight='bold')
ax.legend(frameon=False,loc='lower left',fontsize=9)
for label,ax in zip('abc',axes):
    ax.text(-0.13,1.08,label,transform=ax.transAxes,fontweight='bold',fontsize=13)
    ax.spines[['top','right']].set_visible(False)
fig.suptitle('Synthetic CD8 activation data',x=0.06,ha='left',fontweight='bold',fontsize=14)
fig.text(0.06,0.02,'10 simulated donors. Each endpoint averages two technical aliquots. Descriptive teaching example.',fontsize=9)
fig.subplots_adjust(left=0.07,right=0.98,top=0.79,bottom=0.22,wspace=0.72)
for ext in ['pdf','svg','png']:
    fig.savefig(args.out/f'figure.{ext}',dpi=300)
plt.close(fig)
(args.out/'figure_legend.md').write_text('''# Synthetic CD8 activation data

(a,b) Each point is one culture endpoint for one simulated donor, calculated as the arithmetic mean of two technical aliquots. Lines join Vehicle and Compound_X within the same donor and stimulation condition. n=10 independent simulated donors, each represented in all four conditions, giving 40 culture endpoints from 80 technical measurements. Activation is the percentage of CD69+CD137+ events among live singlet CD3+CD8+ T cells. Both axes use the same 0–100% scale.

(c) Individual donor differences are Compound_X minus Vehicle, in percentage points, within each stimulation condition. Vertical offsets separate the donor points and have no quantitative meaning. Diamonds mark arithmetic mean differences, with equal weight for every donor. No error bars, hypothesis tests or significance labels are used. All donors are retained and no missing values occur.

Every identifier, measurement and Compound_X is synthetic. These descriptive patterns are teaching examples and provide no evidence of real treatment efficacy or mechanism.
''')
(args.out/'versions.json').write_text(json.dumps({'python':platform.python_version(),'pandas':pd.__version__,'matplotlib':matplotlib.__version__},indent=2)+'\n')
(args.out/'input_sha256.txt').write_text(hashlib.sha256(args.data.read_bytes()).hexdigest()+'  data.csv\n')
(args.out/'regenerate.txt').write_text('From the scientific-figure directory, choose a new output directory:\npython facilitator/reference_figure.py --data participant/round_1_naive/data.csv --out facilitator/reference_outputs_new\n')
print(summary.to_string(index=False))
