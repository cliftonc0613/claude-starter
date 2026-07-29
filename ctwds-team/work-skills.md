# Work Skills Reference

3 plugins from `anthropics/knowledge-work-plugins` — small business operations, legal, and finance.

> **Note:** These plugins are installed via the `work` group in `install-claude-company-os.sh`. This installer only names the plugins themselves (`small-business`, `legal`, `finance`), not their internal skill/command list. The categories below are inferred from each plugin's stated purpose — verify exact skill/command names inside each plugin after installing (`claude plugin install small-business@knowledge-work-plugins`, etc.) and update this file to match.

---

## 1. Small Business Operations
- `client-scoping` — Define engagement scope, deliverables, and boundaries for a new client
- `proposal-drafting` — Generate client proposals and statements of work
- `engagement-letter` — Draft engagement letters and service agreements
- `operations-review` — Assess internal agency workflows and bottlenecks

## 2. Legal
- `contract-review` — Review contracts for risk, ambiguous terms, and unfavorable clauses
- `agreement-drafting` — Draft service agreements, NDAs, and vendor contracts
- `compliance-check` — Check business practices against applicable regulations
- `terms-and-policies` — Draft terms of service, privacy policy, and disclaimers

## 3. Finance
- `budget-tracking` — Track project and client budgets against actuals
- `invoicing` — Generate and manage client invoices
- `profitability-analysis` — Analyze margin per client, project, or service line
- `cash-flow-forecast` — Project upcoming cash flow based on active engagements

---

## Related Existing Tools

This repo already has adjacent coverage worth reusing instead of duplicating:
- **Lawyer Mode** (`CLAUDE.md` custom mode) — contracts, legal risk, compliance review
- `client-discovery-script` skill — client intake and discovery
- `market-proposal` skill — proposal generation for market research engagements
