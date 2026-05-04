# Public / Internal Boundary for Track B

## Public-Facing Materials

| File/Folder | Public Use | Notes |
|---|---|---|
| `docs/external_one_page_brief.md` | First-pass overview | Suitable for nontechnical or mixed technical review. |
| `docs/value_proposition_nontechnical.md` | Buyer-facing value explanation | Keep bounded-scope language intact. |
| `docs/before_after_examples.md` | Concrete before/after framing | Useful for explaining remediation/retest flow. |
| `docs/buyer_decision_guide.md` | Evaluation framing | Good for buyer qualification and fit. |
| `docs/public_demo_packet.md` | Public demo narrative | Use as the main demo packet document. |
| `docs/demo_quickstart.md` | Reviewer runbook | Useful for technical evaluators who will run commands locally. |
| `docs/repeatability_validation_matrix.md` | Repeatability evidence | Shows multiple workflow families checked without source changes. |
| `docs/DEMO_REVIEW_PACKET.md` | Technical review packet | Share when evaluator wants more detail. |
| `docs/SERVICE_READINESS_CHECKLIST.md` | Service-readiness evidence | Share when discussing delivery process. |
| `docs/TRACKB_PUBLIC_PACKET_FREEZE_REPORT.md` | Packet freeze evidence | Use to explain the curated public subset. |
| `docs/TECHNICAL_APPENDIX_FORMAL_CONTEXT.md` | Optional formal background | Keep separate from the main product narrative. |
| `examples/` | Canonical demo models | Include the four scoped Boolean examples. |
| selected `outputs/` | Reconstructable results | Prefer selected result/report/comparison outputs, not the whole folder by default. |
| selected `dry_runs/` | Customer-style audit evidence | Start with support-agent dry run and repeatability dry runs as needed. |

## Internal / Restricted Materials

| File/Folder | Reason to Restrict | Notes |
|---|---|---|
| `.venv/` | Local environment contents | Never include in a first external packet. |
| `__pycache__/` | Runtime cache clutter | Remove before packaging if present. |
| `~/ag_scoreboard/Partially Built Expansion Path/CRSL_RSVT_Formal_Proofs_Package` | Separate Track A formal proof package | Keep out of Track B packet. |
| Current RSVT paper | Separate research artifact | Keep out of the curated Track B packet. |
| Broad CRSL/RSVT theory materials not needed for Track B demo | Can confuse scoped demo value | Include only bounded Track B context when needed. |
| Unfinished v0.3 implementation work if added later | Not part of the frozen verifier demo | v0.3 CNF/DIMACS remains design-only here. |
| Real customer materials if ever added | May contain sensitive information | Sanitize and approve separately. |
| Pricing/sales strategy if created later | Business-internal material | Share only in a dedicated business packet. |

## Conditional Materials

| Material | Share If | Hold Back If |
|---|---|---|
| `src/` | A technical evaluator needs to inspect implementation semantics. | The packet is only for buyer overview or nontechnical review. |
| `tests/` | A technical evaluator wants local verification evidence. | The packet should stay concise. |
| v02/v03 design docs | The evaluator asks about optional Z3 or design-only CNF/DIMACS direction. | The discussion is focused on current bounded service value. |
| backend comparison JSON | The evaluator wants brute-force/Z3 agreement evidence. | Raw JSON would distract from the main review. |
| `docs/TRACKB_CROSS_AUDIT_CONTEXT_NOTES.md` | The evaluator wants a short Track B audit-context summary. | Internal audit context would distract from the starter packet. |
| dry run reports | The evaluator wants customer-style audit detail. | The packet is meant to be a short starter set. |
| full `outputs/` | The evaluator wants complete generated artifacts. | Selected outputs are enough to show reconstructable evidence. |

## Boundary Principle

Share enough to show bounded replay-risk audit value, reconstructable evidence, and repeatability. Keep formal context in the technical appendix, and do not share materials that convert a narrow demo into an implied deployment-security or theorem-completion claim.
