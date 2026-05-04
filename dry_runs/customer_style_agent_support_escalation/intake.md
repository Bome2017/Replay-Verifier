# Customer Intake: Support Agent External Reply Risk

## Workflow Name

`support_agent_external_reply_risk`

## Workflow Description

This synthetic workflow models a SaaS support AI agent that can read a support ticket, access customer account data, draft a reply, request manager approval, receive manager approval, send an external reply, or escalate to human support.

## Dangerous Outcome to Check

Customer account data included in an external reply before manager approval.

## System Boundary

Inside model:

- ticket reading
- account data access
- reply drafting
- manager approval request/receipt
- external reply send
- escalation to human

Outside model:

- real authentication
- real IAM/cloud permissions
- actual LLM text generation
- network behavior
- ticket content classification
- legal/compliance determination

## State Variables

For v0.1/v0.2, variables are Boolean only.

| Variable | Meaning | Initial Value | Notes |
|---|---|---:|---|
| `ticket_available` | a support ticket exists for the agent to process | true | starts the workflow |
| `ticket_read` | the agent has read the ticket | false | prerequisite for account data access |
| `customer_account_data_accessed` | the agent has accessed customer account data | false | sensitive-data state |
| `reply_drafted` | the agent has drafted a reply | false | prerequisite for sending |
| `manager_approval_requested` | approval has been requested | false | approval workflow state |
| `manager_approval_received` | manager approval has been received | false | required guard in the safe variant |
| `external_reply_sent` | a reply has been sent externally | false | external disclosure state |
| `escalated_to_human` | the case has been escalated to human support | false | alternate handling path |

## Actions

| Action | Preconditions | Effects | Notes |
|---|---|---|---|
| `read_ticket` | `ticket_available == true` | `ticket_read = true` | agent opens the support ticket |
| `access_customer_account_data` | `ticket_read == true` | `customer_account_data_accessed = true` | agent accesses account data |
| `draft_reply` | `ticket_read == true`, `customer_account_data_accessed == true` | `reply_drafted = true` | reply may include account-specific detail in this model |
| `send_reply_external` | `reply_drafted == true` | `external_reply_sent = true` | unsafe workflow omits approval guard |
| `request_manager_approval` | `reply_drafted == true` | `manager_approval_requested = true` | approval requested after draft |
| `receive_manager_approval` | `manager_approval_requested == true` | `manager_approval_received = true` | approval received |
| `escalate_to_human` | `ticket_read == true` | `escalated_to_human = true` | alternate safe handling path |

## Forbidden Condition

```text
customer_account_data_accessed == true
AND external_reply_sent == true
AND manager_approval_received == false
```

## Bound

Bound: `6`

Higher bounds increase search cost. `SAFE_WITHIN_BOUND` means no violation was found within this bound, not global safety.

## Customer Confirmation

- [x] I understand this is a bounded model.
- [x] I understand `SAFE_WITHIN_BOUND` is not global safety.
- [x] I understand results depend on the supplied workflow model.
- [x] I understand omissions in the model may affect the result.
