# Work Team — Operational Playbook

3 specialized AI agents powered by `anthropics/knowledge-work-plugins` (`small-business`, `legal`, `finance`).
Each agent owns a domain and runs agency-internal duties — this team supports the agency itself and its client engagements, rather than producing client-site deliverables like the Marketing/Blog/SEO/Ads teams.

> **Note:** Exact skill/command names inside each plugin are not enumerated by the installer. Tasks below are structured around each plugin's stated purpose — confirm real command names after install and update this file.

---

## Agent 1: Legal & Compliance Agent

**Specialty:** Contract review, compliance, and agreement drafting

**Skills:** `contract-review`, `agreement-drafting`, `compliance-check`, `terms-and-policies`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Contract intake review | `contract-review` | Review any new client or vendor contract signed or received today |
| Compliance spot check | `compliance-check` | Verify one active engagement against applicable regulatory requirements |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Full contract audit | `contract-review` | Review all active contracts for risk, renewal dates, and unfavorable terms |
| Agreement drafting queue | `agreement-drafting` | Draft or update NDAs, service agreements, and vendor contracts for the week's new engagements |
| Terms & policy review | `terms-and-policies` | Audit client-facing terms of service and privacy policies for currency |

### Key Outputs
- Weekly contract risk report (renewal dates, red-flag clauses)
- Drafted agreements ready for signature
- Compliance status log per active engagement

### Handoffs
- **Receives from:** Small Business Ops Agent (new engagement scopes needing agreements), Marketing Strategy Lead (client positioning that affects terms)
- **Hands off to:** Small Business Ops Agent (finalized agreements for onboarding), Finance Agent (contract terms affecting invoicing schedule)

---

## Agent 2: Finance Agent

**Specialty:** Budgeting, invoicing, and profitability tracking

**Skills:** `budget-tracking`, `invoicing`, `profitability-analysis`, `cash-flow-forecast`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Budget pacing check | `budget-tracking` | Verify active client budgets are on pace vs. plan |
| Invoice queue | `invoicing` | Issue any invoices due today |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Profitability review | `profitability-analysis` | Calculate margin per client and per service line (SEO, Ads, Blog, Marketing) |
| Cash flow forecast | `cash-flow-forecast` | Project the next 4 weeks of cash flow based on active and pipeline engagements |
| Budget reconciliation | `budget-tracking` | Reconcile actuals against budgeted spend for all active clients |

### Key Outputs
- Weekly profitability report (per client, per service line)
- Cash flow forecast (4-week rolling)
- Invoice log and outstanding balances

### Handoffs
- **Receives from:** Legal & Compliance Agent (contract terms affecting billing), Ads Performance Optimizer (ad spend data feeding client budgets), Small Business Ops Agent (new engagement value)
- **Hands off to:** Small Business Ops Agent (profitability data for scoping decisions), Marketing Strategy Lead (budget constraints for campaign planning)

---

## Agent 3: Small Business Ops Agent

**Specialty:** Client scoping, proposals, and internal operations

**Skills:** `client-scoping`, `proposal-drafting`, `engagement-letter`, `operations-review`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Scope clarification | `client-scoping` | Resolve any scope questions raised by active client work |
| Proposal drafting | `proposal-drafting` | Draft or refine a proposal for a prospect in the pipeline |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| New engagement scoping | `client-scoping` | Define deliverables and boundaries for any new client signed this week |
| Engagement letter batch | `engagement-letter` | Draft engagement letters for confirmed new clients |
| Operations review | `operations-review` | Assess agency workflow bottlenecks across all departments |

### Key Outputs
- Client scope documents
- Draft proposals and engagement letters
- Weekly operations health review

### Handoffs
- **Receives from:** Finance Agent (profitability data informing scope decisions), Marketing Strategy Lead (positioning for proposals)
- **Hands off to:** Legal & Compliance Agent (scopes needing formal agreements), Marketing Strategy Lead (new client context for onboarding — see Playbook 1 in `agency-master-team.md`), Finance Agent (new engagement value for budget setup)

---

## Team Communication Flow

```
   ┌─────────────┐        ┌──────────────┐
   │  Legal &    │◄──────►│   Finance    │
   │ Compliance  │        │    Agent     │
   │  (Agent 1)  │        │  (Agent 2)   │
   └──────┬──────┘        └──────┬───────┘
          │                      │
          └──────────┬───────────┘
                      ▼
             ┌─────────────────┐
             │  Small Business │
             │   Ops Agent     │
             │   (Agent 3)     │
             └─────────────────┘
                      │
                      ▼
        Feeds into Playbook 1: New Client Onboarding
        (see agency-master-team.md)
```

**Daily standup order:** Small Business Ops Agent → Legal & Compliance Agent → Finance Agent

**Weekly sync:** Small Business Ops Agent compiles contract risk, profitability, and cash flow data into an internal agency health review — separate from client-facing weekly reports.
