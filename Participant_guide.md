# AI for science: workshop guide

This guide accompanies the original 39-slide workshop. The updated 17 September presentation has 29 slides; the slide numbers below refer to the original version.

The workshop uses Codex desktop to turn a scientific request into an output that can be checked. Bring one small task from your own work, using material you are permitted to share.

## The 90-minute session

| Time | Topic |
|---|---|
| 0–10 min | Why AI and which tools? |
| 10–28 min | Agents and task briefs |
| 28–38 min | Models, tokens and usage |
| 38–50 min | Privacy before sharing |
| 50–78 min | Flow cytometry and practice |
| 78–90 min | Verification and discussion |

The flow-cytometry exercise requires a completed FCS analysis project. Its dataset, analysis and experimental figure are still pending. Until that project is ready, the supplied synthetic CSV audit can serve as the practical exercise; adjust the session timing accordingly.

## Choose the working mode — slide 11

Discuss these requests in pairs:

1. Explain why a confidence interval can be wide.
2. Build an evidence table from five supplied papers.
3. Audit two CSV files and save an exact list of problems.

For each request, identify the inputs, tools and output you would inspect. These are discussion examples. Chat, Work and Codex have overlapping abilities; explain why your starting mode fits the task.

## Improve the brief — slide 13

Start with: “Analyse my experiment and make a nice graph.”

Write three or four sentences specifying the exact inputs, desired output, boundaries, checks and stopping point. Use the synthetic sample files below as the concrete example. Swap briefs and ask whether another person could verify completion.

## Review a plan — slide 15

Challenge the proposals to remove duplicates, fill missing batches or start differential expression. Ask what evidence is missing and which decisions require scientific judgement. The immediate task is an audit; the files should remain unchanged.

## Inspect a cytometry figure — slide 31

Once the FCS project is prepared, work in pairs for nine minutes:

- 0–2 minutes: open the notebook, metadata and figure.
- 2–5 minutes: trace one plotted value to its sample and gate denominator.
- 5–7 minutes: check pairing, biological replicate support and effect direction.
- 7–9 minutes: improve a label or caption, export and reopen the figure.

Report one checked claim and one unresolved scientific decision. The blank data areas on slide 30 are a figure plan, not numerical results.

## Audit the synthetic files — slides 38–39

Inputs: [metadata.csv](demo/inputs/metadata.csv) and [counts.csv](demo/inputs/counts.csv). All identifiers, labels and values are artificial. They have no biological interpretation.

Open the folder in Codex and use this task brief:

> Audit `demo/inputs/metadata.csv` and `demo/inputs/counts.csv`. Use only these two input files for the audit; do not read the answer key first. In counts.csv, the first column contains feature IDs and the remaining columns are samples. Metadata uses sample_id. Check dimensions, identifier uniqueness, missing metadata, sample membership, shared sample ordering and matrix values. Save a readable report and the checks used under `demo/live_outputs/`, then reopen the output. Keep the source files unchanged. Do not infer missing labels, drop or impute records, run differential expression, install packages or upload the files to another service.

Compare the saved report with [expected_audit.md](demo/expected_audit.md) and [the computed audit](demo/prepared_audit.json). A successful audit should reveal that the inputs need reconciliation. It should not quietly repair them.

Without tool access, inspect the CSVs in a spreadsheet or text viewer, write down the problems, then compare with the answer key.

## Your first task after the workshop

Choose one manageable job in a project you understand. Give exact inputs and a clear output, and decide how you will check it. Resolve biological labels, comparisons and replicate units from evidence before analysis.

The slide notes contain source links. The [source guide](Sources_and_further_reading.md) collects the references for later reading.
