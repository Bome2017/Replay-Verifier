# Validation Run Evidence

This document records the evidence that the bounded replay-risk audit demo behaves as the public site claims. The numbers are taken from the validation run on April 29, 2026.

## What Was Run

The following commands were executed from the demo's root directory:

```bash
python -m unittest discover -s tests
.venv/bin/python -m unittest discover -s tests
python -m src.solver_bruteforce examples/agent_email_exfiltration/workflow.json
python -m src.solver_bruteforce examples/agent_email_requires_approval/workflow.json
python -m src.solver_bruteforce examples/agent_delete_without_confirmation/workflow.json
python -m src.solver_bruteforce examples/agent_delete_requires_confirmation/workflow.json
.venv/bin/python -c 'from src.solver_z3 import z3_available; print(z3_available())'
.venv/bin/python -m src.backend_compare examples/agent_email_exfiltration/workflow.json
.venv/bin/python -m src.backend_compare examples/agent_delete_without_confirmation/workflow.json
```

## Results

- System Python tests: `Ran 37 tests`, `OK (skipped=8)`.
- Z3-enabled environment tests: `Ran 37 tests`, `OK`.
- Z3 availability in the validated environment: `True`.
- Brute-force reference checker on the four canonical examples returned the expected statuses:
  - `agent_email_exfiltration` → `UNSAFE`
  - `agent_email_requires_approval` → `SAFE_WITHIN_BOUND`
  - `agent_delete_without_confirmation` → `UNSAFE`
  - `agent_delete_requires_confirmation` → `SAFE_WITHIN_BOUND`
- Backend comparison (brute-force vs. optional Z3) on `agent_email_exfiltration` and `agent_delete_without_confirmation`: both reported `status_match: True`.
- Overclaim text scan against the published packet: no matches.

## What This Evidence Supports

The brute-force reference checker and the optional Z3 backend agree on the supported example workflows. Test suites pass in both the system and the Z3-enabled environments. The repeatability matrix on the [Validation page](../validation.html) extends this pattern to additional workflow families (support reply, refund, permission escalation, sensitive data export, email exfiltration, delete confirmation) using the same audit pattern, without changes to verifier source code.

## What This Evidence Does Not Support

`SAFE_WITHIN_BOUND` is tied to the supplied workflow model and the configured search bound. These results do not establish unrestricted system safety, do not certify the demo as production-safe, do not replace security review, and do not model probabilistic or hidden tool behavior outside the supplied model.
