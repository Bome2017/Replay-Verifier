# Bounded Replay Verification Report

Workflow: agent_vendor_payment_unauthorized
Schema version: 0.1
Bound: 8
Status: UNSAFE

## Result

UNSAFE: A forbidden state is reachable within the configured bound.

## First Bad Step

5

## Violated Condition

```json
{
  "vendor_verified": false,
  "wire_sent": true
}
```

## Counterexample Trace

- step: 0
  action: None
  state_delta: {}
  state_after: {"compliance_review_passed": false, "invoice_read": false, "invoice_received": true, "manager_approved": false, "payment_system_accessed": false, "vendor_record_accessed": false, "vendor_verified": false, "wire_prepared": false, "wire_sent": false}
- step: 1
  action: read_invoice
  state_delta: {"invoice_read": true}
  state_after: {"compliance_review_passed": false, "invoice_read": true, "invoice_received": true, "manager_approved": false, "payment_system_accessed": false, "vendor_record_accessed": false, "vendor_verified": false, "wire_prepared": false, "wire_sent": false}
- step: 2
  action: access_vendor_record
  state_delta: {"vendor_record_accessed": true}
  state_after: {"compliance_review_passed": false, "invoice_read": true, "invoice_received": true, "manager_approved": false, "payment_system_accessed": false, "vendor_record_accessed": true, "vendor_verified": false, "wire_prepared": false, "wire_sent": false}
- step: 3
  action: access_payment_system
  state_delta: {"payment_system_accessed": true}
  state_after: {"compliance_review_passed": false, "invoice_read": true, "invoice_received": true, "manager_approved": false, "payment_system_accessed": true, "vendor_record_accessed": true, "vendor_verified": false, "wire_prepared": false, "wire_sent": false}
- step: 4
  action: prepare_wire
  state_delta: {"wire_prepared": true}
  state_after: {"compliance_review_passed": false, "invoice_read": true, "invoice_received": true, "manager_approved": false, "payment_system_accessed": true, "vendor_record_accessed": true, "vendor_verified": false, "wire_prepared": true, "wire_sent": false}
- step: 5
  action: send_wire
  state_delta: {"wire_sent": true}
  state_after: {"compliance_review_passed": false, "invoice_read": true, "invoice_received": true, "manager_approved": false, "payment_system_accessed": true, "vendor_record_accessed": true, "vendor_verified": false, "wire_prepared": true, "wire_sent": true}

Human-readable trace:

step 0: initial; delta={}; state_after={"compliance_review_passed": false, "invoice_read": false, "invoice_received": true, "manager_approved": false, "payment_system_accessed": false, "vendor_record_accessed": false, "vendor_verified": false, "wire_prepared": false, "wire_sent": false}
step 1: read_invoice; delta={"invoice_read": true}; state_after={"compliance_review_passed": false, "invoice_read": true, "invoice_received": true, "manager_approved": false, "payment_system_accessed": false, "vendor_record_accessed": false, "vendor_verified": false, "wire_prepared": false, "wire_sent": false}
step 2: access_vendor_record; delta={"vendor_record_accessed": true}; state_after={"compliance_review_passed": false, "invoice_read": true, "invoice_received": true, "manager_approved": false, "payment_system_accessed": false, "vendor_record_accessed": true, "vendor_verified": false, "wire_prepared": false, "wire_sent": false}
step 3: access_payment_system; delta={"payment_system_accessed": true}; state_after={"compliance_review_passed": false, "invoice_read": true, "invoice_received": true, "manager_approved": false, "payment_system_accessed": true, "vendor_record_accessed": true, "vendor_verified": false, "wire_prepared": false, "wire_sent": false}
step 4: prepare_wire; delta={"wire_prepared": true}; state_after={"compliance_review_passed": false, "invoice_read": true, "invoice_received": true, "manager_approved": false, "payment_system_accessed": true, "vendor_record_accessed": true, "vendor_verified": false, "wire_prepared": true, "wire_sent": false}
step 5: send_wire; delta={"wire_sent": true}; state_after={"compliance_review_passed": false, "invoice_read": true, "invoice_received": true, "manager_approved": false, "payment_system_accessed": true, "vendor_record_accessed": true, "vendor_verified": false, "wire_prepared": true, "wire_sent": true}

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
