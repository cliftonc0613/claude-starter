# AI Marketing Team — Operational Playbook

8 specialized AI agents powered by `coreyhaines31/marketingskills`.
Each agent owns a domain, runs daily and weekly duties, and hands off to other agents as needed.

---

## Agent 1: SEO Scout

**Specialty:** Search visibility, technical health, and AI search optimization

**Skills:** `seo-audit`, `ai-seo`, `programmatic-seo`, `schema-markup`, `site-architecture`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Crawl health check | `seo-audit` | Scan for new 404s, broken links, crawl errors, and indexability issues |
| Schema validation | `schema-markup` | Verify structured data on any pages published or modified in the last 24 hours |
| AI citation monitor | `ai-seo` | Check brand mention signals and AI crawler accessibility for key landing pages |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Full technical audit | `seo-audit` | Comprehensive audit across on-page, technical, and Core Web Vitals |
| AI search optimization review | `ai-seo` | Audit llms.txt compliance, citation readiness, and LLM visibility across top pages |
| Site architecture review | `site-architecture` | Evaluate internal linking, URL structure, and page hierarchy for new content |
| Programmatic page health | `programmatic-seo` | Audit template pages for thin content, index bloat, and canonicalization |
| Schema expansion | `schema-markup` | Identify new pages eligible for rich results and generate JSON-LD |

### Key Outputs
- Weekly SEO health score report
- Technical issue tracker (prioritized by severity)
- Schema markup recommendations
- AI search readiness scorecard

### Handoffs
- **Receives from:** Content Writer (new pages needing SEO review), Strategy Lead (keyword targets)
- **Hands off to:** Content Writer (content gaps and thin content flags), CRO Specialist (page performance data)

---

## Agent 2: Content Writer

**Specialty:** Marketing copy, content creation, and editorial management

**Skills:** `copywriting`, `copy-editing`, `content-strategy`, `social-content`, `cold-email`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Social content creation | `social-content` | Write and schedule 1-3 social posts aligned with content calendar |
| Copy polish queue | `copy-editing` | Review and tighten any copy flagged by other agents or team members |
| Email outreach drafts | `cold-email` | Write or refine cold email sequences for active campaigns |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Content calendar update | `content-strategy` | Plan next week's topics, map to clusters, and assign priorities |
| Landing page copy | `copywriting` | Write or rewrite copy for 1-2 marketing pages based on CRO or strategy briefs |
| Social performance review | `social-content` | Analyze engagement on past week's posts, adjust tone and format |
| Cold email sequence audit | `cold-email` | Review reply rates and iterate on underperforming sequences |
| Editorial standards check | `copy-editing` | Audit all published content from the week for consistency and quality |

### Key Outputs
- Weekly content calendar
- Social media post queue (formatted per platform)
- Landing page copy drafts
- Cold email sequences and follow-ups
- Copy edit reports with tracked changes

### Handoffs
- **Receives from:** Strategy Lead (messaging briefs, topic priorities), SEO Scout (content gaps, keyword targets), Ad Manager (ad landing page copy needs)
- **Hands off to:** SEO Scout (new pages for technical review), CRO Specialist (landing pages for conversion review), Ad Manager (copy for ad creative)

---

## Agent 3: CRO Specialist

**Specialty:** Conversion optimization across all user touchpoints

**Skills:** `page-cro`, `form-cro`, `signup-flow-cro`, `popup-cro`, `onboarding-cro`, `paywall-upgrade-cro`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Conversion anomaly scan | `page-cro` | Check key page conversion rates for drops or spikes vs. 7-day average |
| Signup flow friction check | `signup-flow-cro` | Monitor registration completion rates and identify new drop-off points |
| Popup performance review | `popup-cro` | Check impression-to-conversion rates on active popups and modals |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Full page CRO audit | `page-cro` | Deep analysis of 2-3 highest-traffic pages for conversion improvement |
| Form optimization review | `form-cro` | Audit all active lead capture and contact forms for friction |
| Onboarding flow analysis | `onboarding-cro` | Review post-signup activation rates and time-to-value metrics |
| Paywall/upgrade screen audit | `paywall-upgrade-cro` | Evaluate upsell modals and feature gates for conversion lift opportunities |
| A/B test results handoff | — | Compile test results and pass winning variants to Strategy Lead |

### Key Outputs
- Weekly conversion rate dashboard (by page, form, flow)
- CRO recommendations report (prioritized by impact)
- Form optimization specs
- Onboarding improvement recommendations
- Popup/modal A/B test briefs

### Handoffs
- **Receives from:** SEO Scout (page performance data), Content Writer (new landing pages), Ad Manager (post-click landing pages)
- **Hands off to:** Content Writer (copy changes for winning variants), Strategy Lead (test results for strategic decisions), Growth Manager (onboarding data for retention analysis)

---

## Agent 4: Ad Manager

**Specialty:** Paid advertising strategy, creative production, and competitive positioning

**Skills:** `paid-ads`, `ad-creative`, `competitor-alternatives`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Campaign performance check | `paid-ads` | Review ROAS, CPA, and spend pacing across all active campaigns |
| Ad creative rotation | `ad-creative` | Generate fresh headline/description variants for fatiguing ad sets |
| Competitive ad scan | `competitor-alternatives` | Monitor competitor positioning for reactive creative opportunities |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Campaign strategy review | `paid-ads` | Audit campaign structure, bidding, and targeting across platforms |
| Creative batch production | `ad-creative` | Produce a full week's worth of ad copy variations (headlines, descriptions, primary text) |
| Competitor comparison pages | `competitor-alternatives` | Create or update "vs" and "alternatives to" pages based on competitive shifts |
| Budget reallocation brief | `paid-ads` | Recommend spend shifts based on platform performance data |

### Key Outputs
- Daily campaign performance snapshot
- Weekly ad creative library (platform-formatted)
- Competitor comparison/alternatives pages
- Budget reallocation recommendations
- Platform-specific campaign briefs

### Handoffs
- **Receives from:** Content Writer (copy for ad creative), Strategy Lead (campaign briefs, audience segments), Ops Manager (tracking/attribution data)
- **Hands off to:** CRO Specialist (post-click landing pages for review), Content Writer (landing page copy needs), Ops Manager (new campaigns needing tracking setup)

---

## Agent 5: Growth Manager

**Specialty:** User acquisition loops, retention systems, and lifecycle engagement

**Skills:** `churn-prevention`, `referral-program`, `email-sequence`, `lead-magnets`, `free-tool-strategy`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Churn signal monitor | `churn-prevention` | Review cancellation attempts, failed payments, and at-risk user signals |
| Email sequence performance | `email-sequence` | Check open/click/reply rates on active drip campaigns |
| Lead magnet conversion check | `lead-magnets` | Monitor download/signup rates on gated content offers |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Churn prevention audit | `churn-prevention` | Audit cancellation flows, save offers, and dunning sequences |
| Email sequence optimization | `email-sequence` | Rewrite underperforming emails, test new subject lines and CTAs |
| Referral program review | `referral-program` | Analyze referral rates, reward redemption, and viral coefficient |
| Lead magnet strategy | `lead-magnets` | Evaluate existing magnets, propose new ones aligned with content calendar |
| Free tool assessment | `free-tool-strategy` | Evaluate ROI of existing marketing tools or propose new tool concepts |

### Key Outputs
- Churn risk report with save offer recommendations
- Email sequence performance dashboard
- Referral program health scorecard
- Lead magnet conversion report
- Free tool ROI analysis and new tool proposals

### Handoffs
- **Receives from:** CRO Specialist (onboarding data, signup flow insights), Strategy Lead (retention targets, lifecycle strategy), Ops Manager (event tracking for lifecycle triggers)
- **Hands off to:** Content Writer (email copy, lead magnet content), CRO Specialist (cancellation flow and onboarding UX), Strategy Lead (churn and retention data for strategic decisions)

---

## Agent 6: Strategy Lead

**Specialty:** Market intelligence, positioning, and strategic planning

**Skills:** `marketing-ideas`, `marketing-psychology`, `pricing-strategy`, `launch-strategy`, `customer-research`, `product-marketing-context`, `ab-test-setup`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Test hypothesis log | `ab-test-setup` | Document new test ideas from team signals and queue for prioritization |
| Psychology insight brief | `marketing-psychology` | Identify one behavioral principle applicable to an active campaign or page |
| Market signal scan | `marketing-ideas` | Flag emerging trends, competitor moves, or channel opportunities |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Customer research synthesis | `customer-research` | Analyze support tickets, reviews, or interview transcripts for insights |
| Positioning review | `product-marketing-context` | Update ICP definition, messaging pillars, and value propositions |
| A/B test planning | `ab-test-setup` | Design 2-3 new experiments with hypotheses, metrics, and sample sizes |
| Pricing analysis | `pricing-strategy` | Review pricing page performance, evaluate tier structure and packaging |
| Launch planning | `launch-strategy` | Advance go-to-market plans for upcoming features or products |
| Marketing ideas session | `marketing-ideas` | Generate and prioritize 5-10 new growth tactics for the next sprint |

### Key Outputs
- Weekly strategy brief (trends, opportunities, risks)
- Customer research insights report
- A/B test design documents
- Pricing recommendations
- Launch playbooks
- Updated product marketing context document

### Handoffs
- **Receives from:** All agents (performance data, test results, market signals)
- **Hands off to:** Content Writer (messaging briefs, topic priorities), Ad Manager (campaign strategy, audience segments), CRO Specialist (test designs), Growth Manager (retention strategy, lifecycle briefs)

---

## Agent 7: Ops Manager

**Specialty:** Analytics infrastructure, sales enablement, and revenue operations

**Skills:** `sales-enablement`, `analytics-tracking`, `revops`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Tracking integrity check | `analytics-tracking` | Verify GA4 events, GTM tags, and conversion pixels are firing correctly |
| Pipeline health scan | `revops` | Check lead flow through stages — flag stuck leads or routing failures |
| Sales asset requests | `sales-enablement` | Fulfill or queue incoming requests for pitch decks, one-pagers, or battle cards |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Analytics audit | `analytics-tracking` | Full audit of UTM hygiene, event tracking coverage, and attribution accuracy |
| RevOps pipeline review | `revops` | Analyze MQL-to-SQL conversion rates, lead scoring model accuracy, and handoff quality |
| Sales collateral refresh | `sales-enablement` | Update pitch decks and objection handling docs with latest data and positioning |
| Tracking setup for new campaigns | `analytics-tracking` | Configure tracking for any campaigns launching next week |
| Lead scoring calibration | `revops` | Review scoring thresholds against actual conversion data and adjust |

### Key Outputs
- Tracking health dashboard
- Pipeline velocity report
- Updated sales collateral library
- Lead scoring model updates
- Attribution and UTM audit report

### Handoffs
- **Receives from:** Ad Manager (new campaigns needing tracking), Strategy Lead (updated positioning for sales materials), Growth Manager (lifecycle event definitions)
- **Hands off to:** Ad Manager (attribution data for budget decisions), Strategy Lead (pipeline and revenue data for strategic planning), All agents (tracking confirmation for new initiatives)

---

## Agent 8: Web Developer

**Specialty:** Website architecture, page implementation, and technical excellence

**Skills:** `stitch-mcp`, `frontend-design`, `html-css`, `responsive-design`, `javascript`, `performance-optimization`, `deployment`, `cms-integration`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Deployment health check | `deployment` | Verify site uptime, error logs, and performance metrics (Core Web Vitals) |
| Code review queue | `html-css`, `javascript` | Review and merge pull requests, fix critical bugs blocking other agents |
| Performance monitoring | `performance-optimization` | Check page load times, identify new performance regressions |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Design system → UI generation | `stitch-mcp`, `frontend-design` | Load design-system.md → Generate UI in Stitch MCP → Refine with frontend-design skill → Create design specs for developers |
| Build new pages | `html-css`, `responsive-design`, `javascript` | Implement 1-2 pages from Stitch designs (forms, CTAs, components per specs) |
| Component integration | `javascript` | Build form handlers, popup triggers, and interactive elements per CRO specs |
| Mobile responsiveness validation | `responsive-design` | Test all pages across breakpoints (320px, 768px, 1024px), ensure mobile conversion flows work |
| Performance optimization | `performance-optimization` | Optimize images, minify assets, reduce bundle size, improve Core Web Vitals |
| CMS/backend sync | `cms-integration` | Ensure copy changes, tracking code, and new features deploy cleanly |

### Key Outputs
- Weekly deployment report (new features, bug fixes, performance gains)
- Site health dashboard (uptime, Core Web Vitals, error tracking)
- Performance optimization recommendations
- Feature implementation specs and architecture docs
- Responsive design validation report

### Handoffs
- **Receives from:** Strategy Lead (website briefs, feature priorities), Content Writer (copy integration, content updates), SEO Scout (technical requirements, schema markup specs), CRO Specialist (conversion-focused page builds, form specs), Ad Manager (landing page specs, post-click experiences)
- **Hands off to:** SEO Scout (completed pages for technical review and indexing), CRO Specialist (pages ready for A/B testing), Ops Manager (tracking implementation confirmation), Content Writer (CMS access and deployment windows)

---

## Team Communication Flow

```
                    ┌──────────────┐
                    │ Strategy Lead│
                    │   (Agent 6)  │
                    └──────┬───────┘
            Briefs & │          ▲ Data &
           Priorities│          │ Results
                     ▼          │
        ┌────────────────────────────────┐
        │                                │
   ┌────▼─────┐  ┌──────────┐  ┌───────▼────┐
   │  Content  │  │    Ad    │  │   Growth   │
   │  Writer   │◄─┤ Manager  │  │  Manager   │
   │ (Agent 2) │  │(Agent 4) │  │ (Agent 5)  │
   └────┬──────┘  └────┬─────┘  └──────┬─────┘
        │              │               │
        ▼              ▼               ▼
   ┌─────────┐   ┌──────────┐   ┌───────────┐
   │   SEO   │   │   CRO    │   │    Ops    │
   │  Scout  │──►│Specialist│   │  Manager  │
   │(Agent 1)│   │(Agent 3) │   │ (Agent 7) │
   └────┬────┘   └────┬─────┘   └──────┬────┘
        │             │                │
        └─────────┬───┴────────────────┘
                  ▼
           ┌─────────────┐
           │     Web     │
           │  Developer  │
           │  (Agent 8)  │
           └─────────────┘
```

**Daily standup order:** Ops Manager → Web Developer → SEO Scout → Content Writer → Ad Manager → CRO Specialist → Growth Manager → Strategy Lead

**Weekly sync:** Strategy Lead runs an 8-agent weekly review using outputs from all agents to set priorities for the following week. Web Developer reports on deployments, performance, and blockers from other agents.
