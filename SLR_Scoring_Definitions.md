# Derived SLR coverage matrix

This supplementary matrix is a reproducible correction of the manuscript's comparison, not a replacement of the author's extraction workbook. Source: `SLR_Extraction_Template_with_Codebook_update.xlsx`, sheet `SLR_Extraction_Template_with_Co`, 48 study rows, repository commit `71a307cba10cf203bbaed9a1060ce39a27421962`.

Repository: https://github.com/kennyjinggabinus/slrcodebook/tree/71a307cba10cf203bbaed9a1060ce39a27421962

| Concern | Credit rule | Evidence used |
|---|---|---|
| G1 | 1 for explicit primary architectural-style classification; 0 for NR. | Column M, `Arch_Style_Primary`. This is not a claim that a system with NR has no architecture. |
| G2 | 1 for explicitly reported API gateway. | Column V, `API_Gateway_Present`. Only RPID_47 is Y. |
| G3 | 1 for an explicitly described runtime autoscaling mechanism. | Deployment, packaging, scaling-mechanism, trigger, and tagged-mechanism fields. No qualifying evidence recorded in this extraction. |
| G4 | 1 for explicit asynchronous/event-driven integration; a named broker is not mandatory. | Event and connection descriptions plus tagged mechanisms. RPID_46 uses MongoDB change streams. RPID_47 describes asynchronous behavior events even though its dedicated broker field is NR. |
| G5 | 1 for a model registry or retained model versions; hot adoption is a separate design capability. | RPID_46 component/connection descriptions and ECLAIR Section 4, p. 426, explicitly describe timestamped models and historical version snapshots. |
| G6 | 1 when training–serving separation is explicitly coded Yes. No extra infrastructure-only criterion. | Column AI, `Training_Serving_Separation`: eight Yes values. |
| G7 | 1 for a specified runtime serving-failure response; 0.5 for recovery evidence limited to historical data; 0 for no qualifying evidence. | RPID_46 describes manually initiated backfilling (partial). RPID_47's security/access control is not failure-recovery evidence. |
| G8 | 1 for an explicit operational observability toolchain. | Column AP and connection descriptions: RPID_47; its paper specifies Prometheus and ELK. |
| G9 | 1 for live runtime configuration adoption without deployment restart. | Adaptability/update/trigger/mechanism fields. No qualifying evidence recorded in this extraction. |

A zero means no qualifying evidence in the available extraction, including non-reporting. It does not prove that the implementation lacks the capability. All concerns can be affected by reviewer interpretation. The analysis was not independently double-coded.

## Targeted primary-source checks

- ECLAIR: https://library.apsce.net/index.php/ICCE/article/download/4708/4582/5693 — Sections 3–4, pp. 425–426, support asynchronous ingestion, manually initiated backfilling, and timestamped historical model versions. Version storage receives full G5 credit under the existing registry-or-versioning concern; no evidence of atomic hot adoption is inferred.
- Axak et al.: https://ceur-ws.org/Vol-3955/Paper_2.pdf — Section 3.1 and Figure 2 support asynchronous event handling, API gateway, and operational monitoring/logging. No training–serving separation or runtime failure recovery is inferred from security controls.

## Recalculated results

Total = 37.5; mean = 37.5/48 = 0.78125, reported as 0.78/9.

Distribution: 23 studies score 0; 17 score 1; 6 score 2; 1 scores 4; 1 scores 4.5. ECLAIR scores 4.5/9; Axak et al. scores 4/9. Four additional studies join the two displayed comparators in the 2/9 tier; the comparison table no longer calls its four rows the complete upper tail.

Full/partial/no-qualifying-report counts: G1 24/0/24; G2 1/0/47; G3 0/0/48; G4 2/0/46; G5 1/0/47; G6 8/0/40; G7 0/1/47; G8 1/0/47; G9 0/0/48.

The eight G6-positive study IDs are RPID_18, RPID_20, RPID_23, RPID_37, RPID_42, RPID_43, RPID_44, and RPID_46. G1+G6-only cases are RPID_18, RPID_20, RPID_37, RPID_42, RPID_43, and RPID_44. RPID_23 has G6 but no explicit primary style.

## Reproduction

`recalculate_audit.py` reads the accompanying original extraction snapshot `SLR_Extraction_Snapshot.json`, recreates the CSV/summary, and asserts the reported distribution and totals. The snapshot is a read-only export of the public workbook values; it is not a recoded workbook. Repository-provided screening decisions and independent coding agreement cannot be reconstructed from this matrix.
