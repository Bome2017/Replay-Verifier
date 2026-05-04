# Starter Packet Manifest

## Minimal External Packet

- `README.md`
- `docs/external_one_page_brief.md`
- `docs/value_proposition_nontechnical.md`
- `docs/before_after_examples.md`
- `docs/buyer_decision_guide.md`
- `docs/public_demo_packet.md`
- `docs/demo_quickstart.md`
- `docs/repeatability_validation_matrix.md`
- `docs/DEMO_REVIEW_PACKET.md`
- `docs/SERVICE_READINESS_CHECKLIST.md`
- `docs/TRACKB_PUBLIC_PACKET_FREEZE_REPORT.md`
- `docs/audit_package.md`
- `docs/customer_input_template.md`
- `docs/audit_report_template.md`
- `docs/remediation_notes_template.md`
- `docs/service_scope.md`

Selected examples:

- `examples/agent_email_exfiltration/workflow.json`
- `examples/agent_email_requires_approval/workflow.json`
- `examples/agent_delete_without_confirmation/workflow.json`
- `examples/agent_delete_requires_confirmation/workflow.json`

Selected dry run:

- `dry_runs/customer_style_agent_support_escalation/intake.md`
- `dry_runs/customer_style_agent_support_escalation/workflow.json`
- `dry_runs/customer_style_agent_support_escalation/result_summary.md`
- `dry_runs/customer_style_agent_support_escalation/audit_report.md`
- `dry_runs/customer_style_agent_support_escalation/remediation_notes.md`
- `dry_runs/customer_style_agent_support_escalation/assumptions_and_exclusions.md`
- `dry_runs/customer_style_agent_support_escalation/safe_variant_workflow.json`
- `dry_runs/customer_style_agent_support_escalation/safe_variant_result_summary.md`

Repeatability dry-run indexes:

- `dry_runs/customer_style_refund_without_approval/`
- `dry_runs/customer_style_permission_escalation/`
- `dry_runs/customer_style_sensitive_data_export/`

Selected outputs:

- `outputs/agent_email_exfiltration/result.json`
- `outputs/agent_email_exfiltration/report.md`
- `outputs/agent_email_requires_approval/result.json`
- `outputs/agent_email_requires_approval/report.md`
- `outputs/agent_delete_without_confirmation/result.json`
- `outputs/agent_delete_without_confirmation/report.md`
- `outputs/agent_delete_requires_confirmation/result.json`
- `outputs/agent_delete_requires_confirmation/report.md`
- `outputs/support_agent_external_reply_risk/result.json`
- `outputs/support_agent_external_reply_risk/report.md`
- `outputs/support_agent_external_reply_requires_approval/result.json`
- `outputs/support_agent_external_reply_requires_approval/report.md`

Optional technical evidence:

- `docs/TECHNICAL_APPENDIX_FORMAL_CONTEXT.md`
- `docs/TRACKB_CROSS_AUDIT_CONTEXT_NOTES.md`
- `outputs/agent_email_exfiltration_z3/result.json`
- `outputs/agent_email_exfiltration_compare/comparison.json`
- `outputs/agent_delete_without_confirmation_z3/result.json`
- `outputs/agent_delete_without_confirmation_compare/comparison.json`
- `outputs/support_agent_external_reply_risk_z3/result.json`
- `outputs/support_agent_external_reply_risk_compare/comparison.json`

## Exclude From Starter Packet

- `.venv/`
- `__pycache__/`
- `.DS_Store`
- raw scratch files
- Track A formal proof package
- current RSVT paper
- real customer-sensitive data if added later
- internal pricing or sales strategy
- unfinished implementation work beyond current design docs

## Packaging Notes

- Do not move source project files to make the starter packet.
- Use copies or lightweight index files only.
- Keep the bounded claim language intact.
- Include only selected outputs unless a technical evaluator asks for complete generated artifacts.
- Confirm that no file implies unrestricted workflow safety, production certification, or broader theorem completion.
