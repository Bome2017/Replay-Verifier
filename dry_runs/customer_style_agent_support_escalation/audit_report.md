# Bounded Replay-Risk Audit Report: Support Agent External Reply Risk

## 1. Executive Summary

Workflow:
`support_agent_external_reply_risk`

Bound:
`6`

Status:
`UNSAFE`

Primary finding:
A forbidden state is reachable within the configured bound: customer account data can be included in an external reply before manager approval.

## 2. Model Scope

Included behavior:

- ticket reading
- customer account data access
- reply drafting
- manager approval request/receipt
- external reply send
- human escalation

Excluded behavior:

- real authentication/IAM
- actual LLM generation
- message content classification
- network behavior
- compliance/legal conclusion

## 3. Workflow Model Summary

State variables:

- `ticket_available`
- `ticket_read`
- `customer_account_data_accessed`
- `reply_drafted`
- `manager_approval_requested`
- `manager_approval_received`
- `external_reply_sent`
- `escalated_to_human`

Actions:

- `read_ticket`
- `access_customer_account_data`
- `draft_reply`
- `send_reply_external`
- `request_manager_approval`
- `receive_manager_approval`
- `escalate_to_human`

Forbidden condition:

```text
customer_account_data_accessed == true
AND external_reply_sent == true
AND manager_approval_received == false
```

## 4. Verification Result

- status: `UNSAFE`
- first_bad_step: `4`
- violated condition: customer account data accessed, external reply sent, and manager approval not received

## 5. Counterexample Trace

Trace action sequence:

```text
initial -> read_ticket -> access_customer_account_data -> draft_reply -> send_reply_external
```

State transition summary:

- Step 0: initial support ticket is available; no data accessed, reply drafted, approval received, or external reply sent.
- Step 1: `read_ticket` changes `ticket_read` to `true`.
- Step 2: `access_customer_account_data` changes `customer_account_data_accessed` to `true`.
- Step 3: `draft_reply` changes `reply_drafted` to `true`.
- Step 4: `send_reply_external` changes `external_reply_sent` to `true` while `manager_approval_received` remains `false`.

The trace is reconstructable from `state_before`, `state_delta`, and `state_after` in the generated result JSON.

## 6. Interpretation

The failure shape is a missing approval guard. In the unsafe model, `send_reply_external` requires a drafted reply but does not require manager approval. This permits an external response after customer account data has entered the workflow and before approval is received.

## 7. Remediation Notes

See `remediation_notes.md`.

## 8. Claim Boundary

This report is a bounded replay-risk audit artifact. It is valid only relative to the supplied workflow model, configured bound, and stated assumptions.
