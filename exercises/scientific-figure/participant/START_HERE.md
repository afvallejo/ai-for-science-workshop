# One dataset, three attempts

Create a scientific figure from synthetic CD8 activation measurements. Complete the rounds in order. You have 30 minutes including setup and discussion.

| Minutes | Activity |
|---|---|
| 0–3 | Download, unzip and open round_1_naive |
| 3–9 | Round 1: naïve prompt |
| 9–15 | Round 2: advanced prompt |
| 15–25 | Round 3: Plan mode, review, then execution |
| 25–30 | Compare the three results |

## Setup

Use Codex desktop with a signed-in account and an existing environment that can read CSV files and create plots. The facilitator's reference uses Python, pandas and Matplotlib, but you may use another available plotting library. Check availability before the session. Do not spend the exercise installing packages.

Each round folder has the same data.csv and study_context.md, plus its own PROMPT.txt. Open only that round's folder as your project and start a fresh task. Keep the same model, reasoning effort and permissions for all rounds. Do not carry earlier conversations or outputs into the next round. Record any active global instructions or skills: these can influence all three results.

If tools or account access are unavailable, work with a partner. You can still write a plan and use the review sheet. Label that work as a planning exercise rather than a generated figure.

## Round 1: naïve prompt

Open round_1_naive. Paste PROMPT.txt in normal execution mode. Let the assistant make the figure. Open its actual image and write down what you can and cannot verify. Preserve the first result. Do not repair it before the comparison.

## Round 2: advanced prompt

Open round_2_advanced in a new task. Paste PROMPT.txt in normal execution mode. Inspect the figure and source table. Compare the explicit brief with what the assistant actually delivered.

## Round 3: Plan mode

Open round_3_plan in a new task. Select Plan mode in Codex, then paste PROMPT.txt. If your interface has no Plan mode, the prompt requests a manual planning-only pause. Record which approach you used.

Spend about three minutes reviewing the plan before execution. Check the replicate unit, aggregation, donor pairing, percentage units, stimulation groups and proposed verification. Ask the assistant to revise any incorrect or unsupported step. A plan can be wrong even when it sounds convincing.

Once satisfied, use the interface's implement/execute action or return to normal execution mode and send:

> Implement the reviewed plan now. Keep the input files unchanged. Save the deliverables in outputs/, run the code, inspect the saved figure and verify the plotted values. Report any checks you could not complete.

Plan for about seven minutes of execution and review. Preserve the plan and any changes you requested alongside the output. If execution runs longer, record the round as incomplete and compare what is available. Time spent waiting is part of the observation.

## Comparison

Complete REVIEW_SHEET.md using evidence from each result. Count a criterion as verified only when you have inspected the supporting artifact. Longer prompts and Plan mode do not guarantee a better figure. This is a learning exercise with one attempt per condition, not a controlled product benchmark.

Take away one improvement to your next task brief and one decision you would review before execution.
