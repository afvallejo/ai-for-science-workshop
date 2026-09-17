# Expected demonstration audit

This is a checked teaching example using entirely synthetic data. It is not a research analysis or the result of an independently run classroom agent session.

**Data readiness: blocked. Audit detection checks: passed.**

| Check | Result |
| --- | --- |
| Metadata size | 7 rows; 6 unique sample IDs |
| Matrix size | 4 synthetic features × 6 sample columns |
| Duplicate metadata ID | S03 occurs twice (CSV lines 3 and 5) |
| Metadata-only ID | S06 |
| Matrix-only ID | S99 |
| Missing metadata | S05 has a blank batch value |
| Shared sample IDs | 5: S01, S02, S03, S04, S05 |
| Shared sample ordering | Different: metadata S01,S03,S02,S04,S05; matrix S03,S01,S02,S04,S05 |
| Matrix sample IDs | Unique |
| Feature IDs | Unique |
| Values | 24 non-negative integers, range 0–51; no missing or non-finite values |

The unique metadata samples comprise three A and three B labels, with six synthetic donors. The extra S03 row repeats an A-labelled record; treating rows as independent samples would overcount A. Group and batch labels are artificial and have no biological interpretation. Among the unique records with a stated batch, B1 has three samples and B2 has two; S05 is missing batch.

No records were dropped, merged, imputed or relabelled. No statistical model was fitted. A researcher would need to resolve the duplicate, unmatched samples and missing batch from source records before a biological analysis. Do not silently repair these teaching inputs.

After resolving identifiers, align by sample_id rather than row position. Integer-like values alone are not proof of raw-count provenance for a real dataset.

## Input fingerprints

- `metadata.csv`: SHA-256 `93212a6b6ac11ea37561ed66001f6f71ecc4b283b727a8bbef158d55fa519178`
- `counts.csv`: SHA-256 `485aefe57b6c6ef346595d9fa347c383eda49d303690f250327324d2b759400d`
