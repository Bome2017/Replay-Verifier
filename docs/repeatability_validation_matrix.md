# Customer-Style Dry-Run Matrix

This matrix summarizes customer-style bounded replay-risk dry runs across multiple workflow families. Each row is a self-constructed dry run; together they exercise the audit pattern (intake → model → check → trace → remediate → retest) without verifier source-code changes.

The canonical demo example workflows (including the larger `agent_vendor_payment_*` pair) are documented separately in [validation_run_evidence.md](validation_run_evidence.md).

The Z3 column is an optional sanity cross-check against the dependency-free reference checker on supported examples; agreement is necessary and useful for implementation QA, but it is not independent real-world validation.

| Workflow family | Unsafe workflow name | Forbidden condition | Bound | Reference status | Z3 sanity status | Status agreement | First bad step | Trace action sequence | Safe variant status | Safe variant Z3 status | Safe variant agreement | Source-code changes needed? | Report created? | Remediation created? |
|---|---|---|---:|---|---|---|---:|---|---|---|---|---|---|---|
| Support agent external reply | `support_agent_external_reply_risk` | `customer_account_data_accessed == true AND external_reply_sent == true AND manager_approval_received == false` | 6 | `UNSAFE` | `UNSAFE` | true | 4 | `[null, "read_ticket", "access_customer_account_data", "draft_reply", "send_reply_external"]` | `SAFE_WITHIN_BOUND` | `SAFE_WITHIN_BOUND` | true | No | Yes | Yes |
| Refund issued without approval | `refund_without_manager_approval` | `refund_issued == true AND manager_approval_received == false` | 6 | `UNSAFE` | `UNSAFE` | true | 4 | `[null, "read_refund_request", "access_customer_billing_record", "draft_refund", "issue_refund"]` | `SAFE_WITHIN_BOUND` | `SAFE_WITHIN_BOUND` | true | No | Yes | Yes |
| Permission escalation | `permission_escalation_without_authorization` | `elevated_access_granted == true AND admin_authorization_received == false` | 6 | `UNSAFE` | `UNSAFE` | true | 4 | `[null, "read_access_request", "inspect_user_account", "prepare_permission_change", "grant_elevated_access"]` | `SAFE_WITHIN_BOUND` | `SAFE_WITHIN_BOUND` | true | No | Yes | Yes |
| Sensitive data export | `sensitive_data_export_without_authorization` | `sensitive_data_exported == true AND export_authorization_received == false` | 6 | `UNSAFE` | `UNSAFE` | true | 3 | `[null, "select_sensitive_records", "prepare_export", "export_data"]` | `SAFE_WITHIN_BOUND` | `SAFE_WITHIN_BOUND` | true | No | Yes | Yes |

## Interpretation

These customer-style dry runs show that the same audit pattern can be applied to multiple scoped workflow shapes without changing verifier source code. They support the bounded service workflow on self-constructed examples; they do not establish independent benchmark validation, third-party repeatability, production-security validation, or any unrestricted safety claim.
