# Bounded Replay Verification Report

Workflow: agent_email_exfiltration
Schema version: 0.1
Bound: 5
Status: UNSAFE

## Result

UNSAFE: A forbidden state is reachable within the configured bound.

## First Bad Step

3

## Violated Condition

```json
{
  "approval_received": false,
  "emailed_external": true,
  "has_customer_data": true
}
```

## Counterexample Trace

- step: 0
  action: None
  state_delta: {}
  state_after: {"approval_received": false, "approval_requested": false, "emailed_external": false, "file_deleted": false, "has_customer_data": false, "has_file": true, "summary_created": false}
- step: 1
  action: access_customer_data
  state_delta: {"has_customer_data": true}
  state_after: {"approval_received": false, "approval_requested": false, "emailed_external": false, "file_deleted": false, "has_customer_data": true, "has_file": true, "summary_created": false}
- step: 2
  action: summarize_file
  state_delta: {"summary_created": true}
  state_after: {"approval_received": false, "approval_requested": false, "emailed_external": false, "file_deleted": false, "has_customer_data": true, "has_file": true, "summary_created": true}
- step: 3
  action: email_external
  state_delta: {"emailed_external": true}
  state_after: {"approval_received": false, "approval_requested": false, "emailed_external": true, "file_deleted": false, "has_customer_data": true, "has_file": true, "summary_created": true}

Human-readable trace:

step 0: initial; delta={}; state_after={"approval_received": false, "approval_requested": false, "emailed_external": false, "file_deleted": false, "has_customer_data": false, "has_file": true, "summary_created": false}
step 1: access_customer_data; delta={"has_customer_data": true}; state_after={"approval_received": false, "approval_requested": false, "emailed_external": false, "file_deleted": false, "has_customer_data": true, "has_file": true, "summary_created": false}
step 2: summarize_file; delta={"summary_created": true}; state_after={"approval_received": false, "approval_requested": false, "emailed_external": false, "file_deleted": false, "has_customer_data": true, "has_file": true, "summary_created": true}
step 3: email_external; delta={"emailed_external": true}; state_after={"approval_received": false, "approval_requested": false, "emailed_external": true, "file_deleted": false, "has_customer_data": true, "has_file": true, "summary_created": true}

## Scope and Assumptions

- Boolean transition model.
- Bound-limited search.
- One action per step.
- Deterministic action order from workflow.json.
- Preconditions must hold for action eligibility.
- Variables not affected by an action persist.
- No probabilistic LLM behavior modeled.
- No real network, cloud, file-system, identity, or IAM semantics modeled.
- Result is valid only relative to the workflow.json model.
- Findings are bounded to the supplied workflow model and configured bound.

## Claim Boundary

This is a bounded replay-risk demo for the supplied workflow model and configured bound. It is not an unrestricted security assessment, deployment approval, or broad theorem result.
