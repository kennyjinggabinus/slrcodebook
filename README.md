# LMS–RS systematic literature review and coverage audit

This repository contains the extraction workbook and search materials for a systematic literature review of LMS–recommender system architectures. The supplementary coverage audit supports the revised manuscript, *A Kubernetes-Orchestrated Reference Architecture for LMS–Recommender System Integration: Scalability, Adaptability, and Robustness*.

## Repository contents

| File or directory | Purpose |
|---|---|
| `SLR_Extraction_Template_with_Codebook_update.xlsx` | Original extraction workbook and codebook. |
| `search/` | Original search materials. |
| `SLR_Gap_Coverage_Audit.csv` | Derived G1–G9 scores for the 48 included studies, with study identifiers, source-row references, totals, and evidence notes. |
| `SLR_Scoring_Definitions.md` | Operational definitions, scoring rules, targeted source checks, and interpretation limits. |
| `SLR_Extraction_Snapshot.json` | Export of the 48 study rows and 55 columns used for reproducible calculation, including the header row. |
| `SLR_Audit_Summary.json` | Corpus totals, mean score, score distribution, and counts for each concern. |
| `recalculate_audit.py` | Python script that reproduces the coverage CSV and summary from the extraction snapshot and the declared coding decisions. |

The original workbook is preserved. The supplementary CSV is a derived analysis, as documented in the scoring definitions.

## Source provenance

The audit uses the workbook at source commit [`71a307cba10cf203bbaed9a1060ce39a27421962`](https://github.com/kennyjinggabinus/slrcodebook/tree/71a307cba10cf203bbaed9a1060ce39a27421962), sheet `SLR_Extraction_Template_with_Co`. Study identifiers and workbook-row references connect the derived matrix to the original extraction.

The JSON snapshot contains the header and 48 study rows. It preserves the exported workbook values used by the audit; it does not reproduce workbook formatting or constitute a newly recoded workbook. Targeted primary-source checks for ECLAIR and Axak et al. are documented in `SLR_Scoring_Definitions.md` and the CSV evidence notes.

## Reproduce the results

Keep the five audit files in the same directory. From that directory, run:

```bash
python3 recalculate_audit.py
```

Python 3 is required; the script uses only the standard library. It reads `SLR_Extraction_Snapshot.json`, writes `SLR_Gap_Coverage_Audit.csv` and `SLR_Audit_Summary.json`, and checks the expected total and distribution. Running it replaces those two generated output files.

The script reproduces the declared decisions for this fixed corpus, including explicit study-specific coding decisions. It does not automatically infer architectural evidence from publications or independently repeat the literature review.

Expected results:

- Included studies: **48**.
- Sum of coverage scores: **37.5**.
- Mean coverage score: **0.78125 out of 9**, reported as **0.78/9**.
- Distribution: **23** studies score 0; **17** score 1; **6** score 2; **1** scores 4; **1** scores 4.5.
- ECLAIR: **4.5/9**; Axak et al.: **4/9**.

## Interpretation and limitations

Each included study contributes equally. A score of 1 records qualifying coverage under the stated criterion. Partial G7 credit of 0.5 records historical-data recovery evidence, without implying continuity of live recommendation requests. Zero records no qualifying evidence in the extraction, including non-reporting; it does not establish that an implementation lacks the capability.

The audit contains the 48 reviewed studies. The manuscript's separate 9/9 Reference Architecture assessment concerns specified design coverage and is not an additional empirical study in the CSV. Neither the coverage scores nor the reproduction script establish runtime quality-attribute attainment.

The audit was not independently double-coded. A complete report-level screening/retrieval log is not included in the available materials; the reasons for the 36 reports described as unavailable in the manuscript cannot be reconstructed from these audit files.

When citing this repository, use the commit containing the supplementary files being cited. The source commit above remains the provenance of the extraction snapshot.
