# Track B Public Packet Freeze Report

## Freeze Status

Status: frozen for the curated Track B public packet after this pass, subject to the validation summary below.

The packet is frozen because:

- public-facing docs preserve bounded-claim language;
- downloadable and public-facing artifacts are curated, not a repository dump;
- Track A and the separate formal proof package are not included;
- `.venv`, cache files, `.DS_Store`, and development clutter are excluded from the curated packet;
- formal context is separated into `docs/TECHNICAL_APPENDIX_FORMAL_CONTEXT.md`;
- tests pass in the recorded validation run;
- the overclaim scan passes;
- no files outside `TrackB_Replay_Verifier_Demo` were modified.

## Public Packet Contents

Static site pages:

- `site/index.html`
- `site/validation.html`
- `site/examples.html`
- `site/audit.html`
- `site/service.html`
- `site/boundaries.html`
- `site/downloads.html`

Downloadable docs:

- `docs/external_one_page_brief.md`
- `docs/public_demo_packet.md`
- `docs/demo_quickstart.md`
- `docs/value_proposition_nontechnical.md`
- `docs/before_after_examples.md`
- `docs/buyer_decision_guide.md`
- `docs/customer_input_template.md`
- `docs/audit_report_template.md`
- `docs/remediation_notes_template.md`
- `docs/service_scope.md`
- `docs/TECHNICAL_APPENDIX_FORMAL_CONTEXT.md`

Selected workflow examples:

- `examples/agent_email_exfiltration/workflow.json`
- `examples/agent_email_requires_approval/workflow.json`
- `examples/agent_delete_without_confirmation/workflow.json`
- `examples/agent_delete_requires_confirmation/workflow.json`

Selected output artifacts:

- `outputs/agent_email_exfiltration/result.json`
- `outputs/agent_email_exfiltration/report.md`
- `outputs/agent_email_requires_approval/result.json`
- `outputs/agent_email_requires_approval/report.md`
- `outputs/agent_delete_without_confirmation/result.json`
- `outputs/agent_delete_without_confirmation/report.md`
- `outputs/agent_delete_requires_confirmation/result.json`
- `outputs/agent_delete_requires_confirmation/report.md`

Selected audit reports:

- `dry_runs/customer_style_agent_support_escalation/audit_report.md`
- `dry_runs/customer_style_agent_support_escalation/remediation_notes.md`
- `dry_runs/customer_style_agent_support_escalation/result_summary.md`
- `dry_runs/customer_style_agent_support_escalation/safe_variant_result_summary.md`
- `docs/TRACKB_CROSS_AUDIT_CONTEXT_NOTES.md`

Repeatability matrix:

- `docs/repeatability_validation_matrix.md`

Service-readiness docs:

- `docs/DEMO_REVIEW_PACKET.md`
- `docs/SERVICE_READINESS_CHECKLIST.md`
- `docs/STARTER_PACKET_MANIFEST.md`
- `docs/EXTERNAL_PACKET_INDEX.md`
- `docs/PUBLIC_PRIVATE_BOUNDARY.md`
- `docs/DO_NOT_SHARE_INTERNAL.md`
- `docs/TRACKB_PUBLIC_PACKET_FREEZE_REPORT.md`

## External Reader Path

1. `site/index.html`
2. `site/validation.html`
3. `site/examples.html`
4. `site/audit.html`
5. `site/service.html`
6. `site/boundaries.html`
7. `site/downloads.html`
8. `docs/external_one_page_brief.md`
9. `docs/repeatability_validation_matrix.md`
10. `docs/TECHNICAL_APPENDIX_FORMAL_CONTEXT.md`, only if the reader wants formal background

## What Is Included

- bounded workflow replay-risk audit description;
- examples;
- outputs;
- dry-run reports;
- repeatability validation matrix;
- public-safe service explanation;
- limitations and assumptions.

## What Is Not Included

- Track A Lean proof package;
- current RSVT paper;
- unfinished theorem claims;
- `.venv`;
- cache files;
- internal strategy docs;
- real customer data;
- production deployment claims.

## Claim Boundary

The public packet presents Track B as a bounded replay-risk audit demo for scoped Boolean workflow models. Results are limited to supplied models and configured bounds.

## Validation Summary

Commands run from `TrackB_Replay_Verifier_Demo` on April 29, 2026:

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest discover -s tests
PYTHONDONTWRITEBYTECODE=1 python -m src.solver_bruteforce examples/agent_email_exfiltration/workflow.json
PYTHONDONTWRITEBYTECODE=1 python -m src.solver_bruteforce examples/agent_email_requires_approval/workflow.json
PYTHONDONTWRITEBYTECODE=1 python -m src.solver_bruteforce examples/agent_delete_without_confirmation/workflow.json
PYTHONDONTWRITEBYTECODE=1 python -m src.solver_bruteforce examples/agent_delete_requires_confirmation/workflow.json
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -c 'from src.solver_z3 import z3_available; print(z3_available())'
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m src.backend_compare examples/agent_email_exfiltration/workflow.json
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m src.backend_compare examples/agent_delete_without_confirmation/workflow.json
rg -n <overclaim-pattern-list> . --glob '!.venv/**'
find . -path './.venv' -prune -o -type f -print | sort
git status --short
```

Results:

- System Python tests: `Ran 37 tests`, `OK (skipped=8)`.
- `.venv` tests: `Ran 37 tests`, `OK`.
- Canonical brute-force examples refreshed selected `outputs/` artifacts and returned expected statuses: email exfiltration `UNSAFE`, email approval `SAFE_WITHIN_BOUND`, delete without confirmation `UNSAFE`, delete with confirmation `SAFE_WITHIN_BOUND`.
- `.venv` Z3 availability: `True`.
- Backend comparisons: email exfiltration and delete without confirmation both reported `status_match: True`.
- Overclaim scan: no matches.
- File listing: completed with `.venv` pruned; local `.DS_Store` files remain in the workspace but are excluded from the curated public packet.
- Git status: this folder is not a git repository, so no git status could be reported.
- Confinement: edits in this pass stayed inside `TrackB_Replay_Verifier_Demo`; `cross_track_audit` was read-only context only; Track A was untouched.
