# Synthetic audit demonstration

Use `inputs/metadata.csv` and `inputs/counts.csv`. All identifiers, labels and values are artificial; they have no biological interpretation. The files intentionally disagree.

Start a fresh Codex task with these files available. Save any live result under a new `live_outputs` folder and keep the inputs and answer key unchanged.

> Read the two CSV files. In counts.csv, the first column holds feature IDs and the other columns are samples; metadata.csv uses sample_id. Report dimensions, duplicate IDs, missing metadata, sample mismatches and ordering. Check matrix values. Save a readable audit and the checks used; reopen the report. Keep source files unchanged. Do not guess corrections, drop or impute data, run differential expression, install packages or share the files with another service.

Compare the actual result with `expected_audit.md`. Audit checks can pass while data readiness fails: that is the intended result here.

For a no-account exercise, read the CSV files in a spreadsheet or text viewer and write down the issues before opening the answer key.
