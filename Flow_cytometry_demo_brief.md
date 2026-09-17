# Flow cytometry demonstration: preparation brief

Status: the FCS dataset, analysis, statistics and final experimental figure remain pending. The workshop slides describe a planned workflow. They do not report completed cytometry results.

## Agree the question before analysis

Select the data source, biological population, comparison and reference group. Establish the independent replicate unit, pairing and technical replicate structure. Define the endpoint, its parent population and measurement scale. Resolve these choices from source documentation and scientific judgement.

## Required inputs

- Original FCS files and their acquisition and processing history.
- Sample metadata with stable sample and donor or experimental identifiers.
- Panel and channel-to-marker mapping.
- Relevant controls and documented compensation or spectral-unmixing records.
- Reviewed gates, transformations and workspace files where available.

Confirm which corrections have already been applied. Do not assume that an FCS extension means untouched acquisition data or apply compensation twice.

## Analysis and figure checks

Inspect acquisition quality, channel ranges and event losses. Preserve a per-sample gate audit, including numerator and parent denominator. Define fluorescence summaries and units explicitly. Perform sample- or donor-aware inference using the agreed design; do not treat events as biological replicates.

The planned figure has gating evidence, event distributions, biological replicate summaries and effect estimates with defined uncertainty. All plotted values must come from the executed analysis. Until then, the data areas remain empty.

## Required handoff

Save the notebook or analysis script, input manifest, software versions, parameters, reviewed gates, sample-level measurements, statistical outputs, plotted tables, figure, legend and Methods. Reopen the saved files and trace plotted values to the underlying measurements. Preserve the source FCS files.

Before using non-public files, check the chosen account, model, retention rules and connected services. The [source guide](Sources_and_further_reading.md) links the relevant policies and the cytometry guidelines.

For a ready-to-use workshop exercise, use the [synthetic CSV audit](demo/README.md).
