# Study context: synthetic CD8 activation experiment

## Provenance and question
Every identifier and measurement in this dataset is synthetic. There are
no human participant records, clinical data or real drug results. Compound_X
is fictional. This dataset was constructed for a teaching exercise, not to
support a biological claim. Keep its synthetic status explicit in the legend.

Question: How does Compound_X, relative to Vehicle, affect the percentage
of activated CD8 T cells under Unstimulated and Stimulated conditions?
Describe the data; the core exercise does not request hypothesis tests,
p values, significance stars or mechanistic conclusions.

## Experimental design
There are 10 simulated independent donors, D01 to D10. Material from each
donor is represented in all four combinations of treatment (Vehicle or
Compound_X) and stimulation (Unstimulated or Stimulated), at one endpoint.
There is one treated culture per donor per treatment per stimulation status.
Each culture was split into two technical aliquots for staining/acquisition.
These are repeated measurements of the same culture, not independently
treated wells and not additional biological donors.

There are 40 cultures and 80 technical measurements in total. All four
condition combinations involve the same 10 donors. Technical replicate numbers 1 and 2
identify aliquots within a culture; they do not create matching biological
units across different cultures. Match comparisons using donor_id and the
appropriate experimental factors, never CSV row order.

## Endpoint and units
activation_percent is the percentage of CD69+CD137+ events among live,
singlet CD3+CD8+ T cells. This parent is the denominator, not all PBMCs,
all T cells or all acquired events. Values are already percentages on a
0 to 100 scale. A value of 25 means 25%, not 0.25% or 2,500%.

The predeclared endpoint per culture is the arithmetic mean of its two
technical measurements. Donors have equal weight in across-donor summaries.
A difference between two percentages is reported in percentage points.
The sign convention for a treatment contrast is Compound_X minus Vehicle,
computed within each donor and stimulation status.

No cells or event-level counts are supplied. Do not reconstruct counts,
change the endpoint, pool across stimulation status, infer an acquisition
batch, or invent metadata. This is a complete, clean starter dataset with
no missing measurements and no predeclared exclusions. Retain every donor.

## Columns
| Column | Meaning |
| --- | --- |
| donor_id | Simulated donor identifier and pairing key. |
| sample_id | Culture identifier. It occurs twice, once per technical aliquot. |
| technical_replicate | Technical aliquot number, 1 or 2. |
| treatment | Vehicle or Compound_X. |
| stimulation | Unstimulated or Stimulated. |
| activation_percent | CD69+CD137+ frequency within the specified CD8 parent, in percent. |
| data_origin | Always synthetic. |

The unique measurement key is sample_id plus technical_replicate.
Row order has no experimental meaning.

## Common deliverables for all workshop conditions
Save a PDF and a PNG of the figure, an executable plotting script, a figure
legend and plot_data.csv in outputs/. The figure may contain more than one
panel. No particular chart type, colour palette or journal template is
prescribed. Use a conventional scientific plotting library, not a generated
illustration of quantitative results.

For comparison and validation, plot_data.csv must contain the 40 culture
endpoints with these columns: donor_id, treatment, stimulation,
activation_percent. Additional clearly named columns or supplementary
source-data tables are allowed. Explain any further figure summaries in
the code and legend. Include a regeneration command and the software
versions used. Do not overwrite data.csv or study_context.md.
