# Scientific skills and literature MCP resources

Links and descriptions checked 17 September 2026. The slides introduce resources; they do not install or configure them.

## Scientific Agent Skills

[K-Dense Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills), previously Claude Scientific Skills, provides reusable instructions and supporting scripts for scientific workflows. The repository supports Codex and other Agent Skills hosts.

Useful starting points:

- [literature-review](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/literature-review): evidence search and synthesis.
- [citation-management](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/citation-management): reference checking and citation records.
- [scientific-visualization](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-visualization): scientific plotting workflows.

Read the individual SKILL.md before choosing a skill. Check its dependencies, external services and outputs. Installation instructions are host-specific. A skill supplies a workflow; scientific validity still depends on the data, methods and review.

## BioMCP for literature

[BioMCP](https://github.com/genomoncology/biomcp) is a third-party biomedical tool from GenomOncology. It is not an official NCBI/PubMed service. Its [article guide](https://biomcp.org/user-guide/article/) describes searching papers, selecting identifiers and retrieving records or available full text. Sources include PubMed and Europe PMC. Full-text coverage and reuse rights depend on the source.

- [MCP client setup](https://biomcp.org/getting-started/mcp-clients/)
- [MCP server modes](https://biomcp.org/reference/mcp-server/)
- [PubMed integration](https://biomcp.org/sources/pubmed/)

Configure a local or appropriately hosted server using the current client instructions. Review the data sent to providers and any required API credentials. Confirm that the client lists the tools, then retrieve a known paper and compare its identifier and title with the source. These setup steps have not been executed as part of this slide update.

## A prompt to try

Use an available literature-review skill and a connected literature MCP tool:

> Find up to five primary studies on CD8 T-cell activation measured by flow cytometry in human samples. Record the exact query, database, filters and search date. For each paper, report the title, year, DOI or PMID, study system, markers, sample size and a supporting source passage with its location. Distinguish abstract-only evidence from full text. Mark fields you cannot verify. Save an evidence table and search log. If the literature tool is unavailable, identify the missing connection rather than inventing retrieval.

Check one table row against the actual paper. A five-paper shortlist is a learning exercise, not a systematic review. The protocol connects tools; it does not establish the reliability of a paper or the correctness of an extracted claim.
