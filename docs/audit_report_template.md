# Bounded Replay Verification Report Template

# Bounded Replay Verification Report

## 1. Executive Summary

- Workflow:
- Bound:
- Status:
- Primary finding:

For `UNSAFE`: A forbidden state is reachable within the configured bound.

For `SAFE_WITHIN_BOUND`: No forbidden state was found within the configured bound.

## 2. Model Scope

- included system behavior:
- excluded system behavior:
- assumptions:
- bound:

## 3. Workflow Model Summary

- state variables:
- actions:
- forbidden condition:

## 4. Verification Result

- status:
- first_bad_step, if unsafe:
- violated condition, if unsafe:

## 5. Counterexample Trace

For unsafe findings, include each trace step:

- step
- action
- state_before
- state_delta
- state_after

The trace must be reconstructable.

For `SAFE_WITHIN_BOUND`, no counterexample trace was found within the configured bound.

## 6. Interpretation

Explain what the result means and does not mean. Tie the interpretation to the configured bound, workflow model, assumptions, and exclusions.

## 7. Remediation Notes

Use `docs/remediation_notes_template.md` for remediation analysis and retest notes.

## 8. Claim Boundary

This report is a bounded replay-risk audit artifact. It is not a production security guarantee, legal certification, compliance certification, or global workflow-safety proof.
