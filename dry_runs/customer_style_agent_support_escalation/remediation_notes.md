# Remediation Notes: Support Agent External Reply Risk

## Unsafe Finding

External reply can be sent after customer account data has been accessed but before manager approval is received.

## Root Cause Pattern

Missing approval precondition on `send_reply_external`.

## Candidate Remediation

Require:

```text
manager_approval_received == true
```

as a precondition for `send_reply_external`.

Optional additional remediation:

- split `draft_reply` into sanitized and unsanitized variants
- add explicit `contains_customer_data` variable if modeling content risk later
- route unresolved cases to `escalate_to_human`
- require approval before account data enters the reply path

## Retest Requirement

After remediation, update `workflow.json` or create `safe_variant_workflow.json` and rerun bounded verification.

A `SAFE_WITHIN_BOUND` result means no violation was found within the configured bound and model assumptions; it does not prove global safety.

## Residual Risk

- bound choice
- model omissions
- unmodeled LLM content behavior
- real system permissions
- human approval quality
