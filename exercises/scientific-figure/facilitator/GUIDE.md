# Facilitator guide

## Before participants arrive

Open the exercise slides. Give participants participant_pack.zip, which contains only the three round folders, instructions and review sheet. Confirm access to Codex and an environment capable of plotting. Have a partner arrangement for participants without access. The suggested Python environment already has pandas and Matplotlib; do not introduce package installation during the timed exercise.

## Timing

Allow 3 minutes for setup, 6 for the naïve round, 6 for the advanced round, 10 for Plan mode and execution, and 5 for comparison. The Plan-mode interval includes approximately 3 minutes for plan review and 7 for execution. If a run does not finish, record it as incomplete rather than fabricating a comparison.

Do not show the reference figure before the three attempts. Preserve each first completed output. Have participants record the same model and reasoning effort in each task. Global instructions and earlier experience can affect results even in fresh tasks. Order, learning, stochastic generation and unequal planning time prevent causal claims about which mode is best.

## Scientific checks

The input has 10 simulated donors, 40 cultures and 80 technical measurements. Each donor has all four combinations of treatment and stimulation. Each culture has two technical aliquots. The mean of those aliquots is the registered culture endpoint. The independent biological unit in the teaching design is the donor.

Match on donor_id. Show treatment pairing within each stimulation condition. Retain all donors. The endpoint is CD69+CD137+ frequency among live singlet CD3+CD8+ T cells, in percent. Differences are Compound_X minus Vehicle in percentage points. All results are descriptive and synthetic.

A valid figure need not match the reference layout, palette or panel count. Judge the data representation, source table and legend. Do not assume the naïve round will fail or Plan mode will succeed.

## Plan review questions

- What does each point represent, and what is n?
- Which columns define a culture and which define a measurement?
- How does the proposed aggregation handle the two aliquots?
- How will pairing survive shuffled CSV rows?
- Are Unstimulated and Stimulated conditions separate?
- Which files will let another person reproduce and check the figure?
- Does the plan introduce tests, exclusions or metadata that the brief does not authorize?

## Reference and answer key

Run from this exercise directory using an environment with pandas and Matplotlib:

```sh
python facilitator/reference_figure.py --data participant/round_1_naive/data.csv --out facilitator/reference_outputs_new
```

The script refuses to overwrite an existing output directory. The supplied reference_outputs contains the executed figure, 40 culture averages, 20 donor treatment differences, summaries, caption, versions and an input checksum. Use these to check participants' numbers. The supplied reference is a separate implementation; it is not an AI round result.

Use numerical_checks.json for the structural checks and independently checked example values. Inspect the actual PNG/PDF and rerun the saved code before calling a participant result reproducible. Never treat a model's own success statement as verification.

## Provenance

The dataset is copied unchanged from the workshop's existing synthetic CD8 activation exercise prepared on 15 September 2026. No real participant data or experimental observations are included. The study context preserves the original descriptive scope and clarifies that the four groups are condition combinations. The naive, advanced and Plan-mode instructions are new for this exercise.
