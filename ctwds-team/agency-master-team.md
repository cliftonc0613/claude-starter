# CT Web Design Shop — Agency Master Team

8 AI-powered departments. 41 specialized agents. 120+ skills.
This is the top-level orchestration document for running the full agency team across clients and campaigns.

---

## Department Overview

| Department | Agents | Skills | Invoke |
|------------|--------|--------|--------|
| Marketing | 8 | 34 (`coreyhaines31/marketingskills`) | See `ai-marketing-team.md` |
| Blog | 8 | 30 (`/blog` engine) | See `ai-blog-team.md` |
| SEO | 8 | 24 (`/seo` engine) | See `ai-seo-team.md` |
| Ads | 8 | 18 (`/ads` engine) | See `ai-ads-team.md` |
| Work | 3 | 3 plugins (`anthropics/knowledge-work-plugins`) | See `ai-work-team.md` |
| Social | 3 | `charlie947/social-media-skills` | See `ai-social-team.md` |
| Design | 3 | `ui-ux-pro-max`, `impeccable`, `taste`, `transitions.dev` | See `ai-design-team.md` |
| QA | — | 1 (`/qa-personas`) | See `qa-skills.md` |

`dev` (Superpowers, Context7, Claude-Mem, 97-dev) from the installer is agency infrastructure — debugging discipline, doc lookup, session memory — not a client-facing department with its own agents/cadence, so it has no team doc.

`astro-business-builder` (site scaffolding — installed separately, not part of `install-claude-company-os.sh`) is grouped alongside `dev` tooling for the same reason: it's a capability invoked directly, not a department with daily/weekly cadences or agent handoffs. Its skill reference lives in `site-builder-skills.md`.

**Reference files in this folder:**
- `marketing-skills.md` + `ai-marketing-team.md`
- `blog-skills.md` + `ai-blog-team.md`
- `seo-skills.md` + `ai-seo-team.md`
- `ads-skills.md` + `ai-ads-team.md`
- `work-skills.md` + `ai-work-team.md`
- `social-skills.md` + `ai-social-team.md`
- `design-skills.md` + `ai-design-team.md`
- `qa-skills.md` (QA persona testing)
- `site-builder-skills.md` (`astro-business-builder` — dev tooling, no team doc)

---

## Full Agent Roster

### Marketing Department
| Agent | Specialty | Key Skills |
|-------|-----------|------------|
| SEO Scout | Search visibility and technical health | `seo-audit`, `ai-seo`, `schema-markup`, `site-architecture` |
| Content Writer | Copy, editorial, social, cold email | `copywriting`, `copy-editing`, `content-strategy`, `social-content` |
| CRO Specialist | Conversion optimization | `page-cro`, `form-cro`, `signup-flow-cro`, `onboarding-cro` |
| Ad Manager | Paid strategy, creative, competitor pages | `paid-ads`, `ad-creative`, `competitor-alternatives` |
| Growth Manager | Retention, lifecycle, lead gen | `churn-prevention`, `email-sequence`, `lead-magnets` |
| Strategy Lead | Market intelligence and positioning | `marketing-ideas`, `customer-research`, `launch-strategy`, `ab-test-setup` |
| Ops Manager | Analytics, RevOps, sales enablement | `analytics-tracking`, `revops`, `sales-enablement` |
| Web Developer | Site builds, CMS, performance | `frontend-design`, `html-css`, `performance-optimization` |

### Blog Department
| Agent | Specialty | Key Skills |
|-------|-----------|------------|
| Content Writer | Article creation and briefs | `blog-write`, `blog-rewrite`, `blog-outline`, `blog-brief` |
| Strategy Lead | Editorial planning and clustering | `blog-strategy`, `blog-calendar`, `blog-cluster`, `blog-brand` |
| Research Analyst | Source intelligence and data | `blog-discourse`, `blog-notebooklm`, `blog-google` |
| Media Producer | Images, audio, charts | `blog-image`, `blog-audio`, `blog-chart` |
| Quality Editor | Scoring, SEO, factcheck | `blog-analyze`, `blog-seo-check`, `blog-audit`, `blog-factcheck` |
| AI Search Specialist | GEO, schema, FLOW | `blog-geo`, `blog-schema`, `blog-flow` |
| Multilingual Manager | Translation and hreflang | `blog-multilingual`, `blog-translate`, `blog-localize` |
| Distribution Manager | Repurposing and taxonomy | `blog-repurpose`, `blog-taxonomy` |

### SEO Department
| Agent | Specialty | Key Skills |
|-------|-----------|------------|
| Technical Auditor | Site health, CWV, drift | `seo audit`, `seo technical`, `seo page`, `seo drift` |
| Content & E-E-A-T Specialist | Quality and search experience | `seo content`, `seo sxo`, `seo flow` |
| Schema & Structure Specialist | Structured data and sitemaps | `seo schema`, `seo sitemap`, `seo images` |
| AI Search Specialist | GEO, clusters, planning | `seo geo`, `seo cluster`, `seo plan` |
| Local & Maps Specialist | GBP, geo-grid, citations | `seo local`, `seo maps` |
| International SEO Manager | Hreflang and i18n | `seo hreflang` |
| Competitor & Growth Strategist | Programmatic, comparison pages | `seo competitor-pages`, `seo programmatic`, `seo ecommerce` |
| Data & Intelligence Analyst | Google APIs, backlinks, SERP | `seo google`, `seo backlinks`, `seo dataforseo` |

### Ads Department
| Agent | Specialty | Key Skills |
|-------|-----------|------------|
| Audit Commander | Cross-platform health scoring | `ads audit` |
| Google Ads Specialist | Search, PMax, AI Max | `ads google` |
| Meta & Social Specialist | FB, IG, TikTok, YouTube | `ads meta`, `ads tiktok`, `ads youtube` |
| B2B Ads Specialist | LinkedIn, Microsoft | `ads linkedin`, `ads microsoft` |
| Mobile & App Specialist | Apple Search Ads, Amazon | `ads apple`, `ads amazon` |
| Creative Director | Creative audit and AI generation | `ads creative`, `ads generate`, `ads photoshoot` |
| Strategy & Intelligence | Campaign planning and briefs | `ads plan`, `ads competitor`, `ads dna`, `ads create` |
| Performance Optimizer | Landing pages and budget | `ads landing`, `ads budget` |

### Work Department
| Agent | Specialty | Key Skills |
|-------|-----------|------------|
| Legal & Compliance Agent | Contract review, agreements, compliance | `contract-review`, `agreement-drafting`, `compliance-check` |
| Finance Agent | Budgeting, invoicing, profitability | `budget-tracking`, `invoicing`, `profitability-analysis` |
| Small Business Ops Agent | Client scoping, proposals, internal ops | `client-scoping`, `proposal-drafting`, `engagement-letter` |

### Social Department
| Agent | Specialty | Key Skills |
|-------|-----------|------------|
| Voice Builder / Brand Agent | Brand voice foundation (runs first) | `voice-builder` |
| Platform Content Agent | Per-platform posts and short-form video | `instagram-content`, `tiktok-content`, `linkedin-content`, `x-content`, `reels-scripting` |
| Social Analytics Agent | Post scoring, engagement analysis, scheduling | `post-scorer`, `engagement-analysis`, `content-calendar` |

### Design Department
| Agent | Specialty | Key Skills |
|-------|-----------|------------|
| UI/UX Builder | Interface structure and layout | `ui-ux-pro-max`, `impeccable:arrange`, `impeccable:frontend-design` or `design-taste-frontend` |
| Design Auditor | Quality review, anti-slop detection, polish | `impeccable:audit`, `impeccable:critique`, `impeccable:polish` or `design-taste-frontend`, `impeccable:harden` |
| Motion & Delight Specialist | Animation, transitions, micro-interactions | `impeccable:animate`, `impeccable:delight`, `impeccable:overdrive`, `transitions.dev` |

---

## Agency Operating Cadence

### Daily Loop — Run Every Morning

These tasks run across all four departments to keep every active client healthy.

```
MARKETING DEPARTMENT — Daily
  Ops Manager          → tracking integrity check (GA4, GTM, pixels)
  Content Writer       → social content creation (1-3 posts)
  Ad Manager           → campaign performance check (ROAS, CPA, pacing)
  CRO Specialist       → conversion anomaly scan
  Strategy Lead        → market signal scan + test hypothesis log

BLOG DEPARTMENT — Daily
  Research Analyst     → discourse scan + GSC performance pull
  Content Writer       → draft new article OR optimize flagged post
  Quality Editor       → score new drafts + SEO validation
  AI Search Specialist → GEO audit on new posts + schema validation

SEO DEPARTMENT — Daily
  Data & Intelligence  → GSC performance pull + SERP snapshot
  Technical Auditor    → crawl health check + drift detection
  Schema Specialist    → schema validation on new pages
  Local & Maps         → GBP signal check + geo-grid spot check (local clients)

ADS DEPARTMENT — Daily
  Audit Commander      → platform health pulse + spend pacing alert
  Google Specialist    → search term review + bid strategy health
  Meta & Social        → creative fatigue check
  Performance Optimizer → conversion anomaly scan + budget pacing
```

### Weekly Loop — Run Every Monday

Full-team weekly execution for each active client.

```
WEEK START — Monday
  Strategy Lead (Marketing)   → weekly strategy brief + A/B test planning
  Blog Strategy Lead          → editorial calendar update (4-week rolling)
  SEO AI Search Specialist    → GEO audit + topic cluster coverage report
  Ads Strategy & Intelligence → competitor intelligence report + campaign brief update

MID-WEEK — Tuesday–Wednesday
  Blog Content Writer         → write 2-3 posts from calendar
  Blog Research Analyst       → research packets + Google API report
  SEO Technical Auditor       → full site audit (0-100 health score)
  SEO Data & Intelligence     → Google API report (PSI, CrUX, GSC, GA4)
  Ads Creative Director       → weekly creative batch + fatigue audit
  Ads Audit Commander         → full multi-platform audit (250+ checks)
  Marketing Content Writer    → landing page copy + content calendar

END OF WEEK — Thursday–Friday
  Blog Quality Editor         → site-wide health audit + cannibalization scan
  Blog AI Search Specialist   → schema batch + FLOW framework review
  SEO Competitor Strategist   → comparison pages + programmatic audit
  Ads Performance Optimizer   → budget allocation review + kill/scale list
  Marketing Ops Manager       → analytics audit + RevOps pipeline review
  Marketing CRO Specialist    → full page CRO audit + form optimization
  Blog Distribution Manager   → full repurpose batch for the week's posts
```

### Monthly Loop — Run First Week of Month

Strategic review and recalibration across all departments.

```
MONTH START — Cross-Team Strategy Session
  Marketing Strategy Lead     → customer research synthesis + positioning review
  Blog Strategy Lead          → brand context refresh (BRAND.md + VOICE.md)
  SEO AI Search Specialist    → strategic plan update (industry-specific)
  Ads Strategy & Intelligence → brand DNA refresh + platform mix review

MONTH-END — Reporting and Planning
  All SEO agents              → full site audit → monthly SEO health report
  All Ads agents              → full platform audit → monthly Ads health report
  Blog Quality Editor         → monthly quality scorecard (avg score all posts)
  Marketing Ops Manager       → attribution and UTM audit report
  → Synthesize into: monthly client report (see Client Reporting Loop below)
```

---

## Cross-Team Workflows

These are the key agency playbooks where multiple departments work together on a single objective.

---

### Playbook 1: New Client Onboarding

Run this when a new client is signed. Takes 1-2 weeks end-to-end.

```
WEEK 1 — Discovery & Baseline

Day 1-2: Brand Extraction
  Ads: Strategy & Intelligence     → /ads dna <client-url>
                                      → outputs brand-profile.json
  Marketing: Strategy Lead         → customer-research + product-marketing-context
                                      → outputs ICP, positioning, messaging pillars

Day 3-4: Technical Baseline
  SEO: Technical Auditor           → /seo audit <client-url>
                                      → outputs 0-100 health score + issue tracker
  SEO: Data & Intelligence         → /seo google gsc <url> + /seo backlinks <url>
                                      → outputs ranking baseline + backlink snapshot
  SEO: Schema Specialist           → /seo schema <url> + /seo sitemap <url>
                                      → outputs structured data audit + sitemap health

Day 5: Ads Baseline
  Ads: Audit Commander             → /ads audit (if running ads)
                                      → outputs per-platform health scores
  Ads: Performance Optimizer       → /ads landing <url>
                                      → outputs landing page quality report

WEEK 2 — Strategy & Quick Wins

Day 6-7: Strategic Planning
  Blog: Strategy Lead              → /blog strategy <niche>
                                      → outputs blog strategy + topic clusters
  SEO: AI Search Specialist        → /seo plan <type>
                                      → outputs industry SEO strategic plan
  Ads: Strategy & Intelligence     → /ads plan <business-type>
                                      → outputs ad platform selection + campaign architecture
  Marketing: Strategy Lead         → launch-strategy + pricing-strategy
                                      → outputs GTM brief

Day 8-9: Content Foundation
  Blog: Research Analyst           → /blog discourse <main-topic>
                                      → outputs DISCOURSE.md (what market is saying)
  Blog: Content Writer             → /blog write <hero-topic>
                                      → outputs first cornerstone article
  Marketing: Content Writer        → copywriting (homepage, core landing pages)
  SEO: Competitor Strategist       → /seo competitor-pages
                                      → outputs comparison page brief

Day 10: Onboarding Report
  → Compile all outputs into: Client Onboarding Report
     - Site health score (SEO)
     - Ads health score (if applicable)
     - Brand profile (brand-profile.json)
     - ICP and positioning
     - Strategic plan: SEO + Blog + Ads
     - Quick wins list (top 10 actions, ranked by impact)
     - 90-day roadmap
```

---

### Playbook 2: Weekly Client Report Loop

Run every Friday. Synthesizes all four departments into one client-facing report.

```
INPUTS — Collect from each department:

  SEO Department
  → Technical Auditor:        weekly health score (0-100)
  → Data & Intelligence:      GSC performance (impressions, clicks, position)
  → AI Search Specialist:     GEO scorecard (citation readiness)
  → Local & Maps:             GBP performance (if local client)

  Blog Department
  → Quality Editor:           posts published + average quality score
  → Research Analyst:         top keywords gaining traction (GSC)
  → AI Search Specialist:     new schema deployed + GEO wins
  → Distribution Manager:     repurpose performance (channel traffic)

  Ads Department
  → Audit Commander:          aggregate health score + platform scores
  → Performance Optimizer:    ROAS, CPA, conversion rate, budget pacing
  → Creative Director:        creative fatigue flags + new assets deployed
  → Strategy & Intelligence:  competitive shifts observed

  Marketing Department
  → Ops Manager:              tracking health + pipeline velocity
  → CRO Specialist:           conversion rate changes by page/form
  → Growth Manager:           email performance + lead magnet conversions
  → Strategy Lead:            test results + strategic observations

REPORT STRUCTURE
  1. Executive Summary (3 bullet points: wins, risks, next week focus)
  2. SEO Health (score, top gains, critical issues)
  3. Content Performance (posts published, top performers, GEO wins)
  4. Paid Ads Performance (spend, ROAS, CPA, health score)
  5. Conversion & Funnel (CVR by stage, form performance, email stats)
  6. Priority Action Items (top 5 for next week, owner per item)
```

---

### Playbook 3: Content-to-Revenue Pipeline

The full loop from blog post to ranking to ad to conversion. Run for each cornerstone content piece.

```
STAGE 1 — Research (Blog Department)
  Research Analyst    → /blog discourse <topic>        (what market is saying)
  Research Analyst    → /blog google keywords <topic>  (search volume data)
  Strategy Lead       → /blog cluster plan <seed>      (hub + spoke map)

STAGE 2 — Content Creation (Blog Department)
  Content Writer      → /blog outline <topic>          (SERP-informed structure)
  Content Writer      → /blog write <topic>            (full article)
  Media Producer      → /blog image generate           (hero + inline images)
  Quality Editor      → /blog analyze <file>           (100-point score)
  Quality Editor      → /blog seo-check <file>         (SEO validation)
  AI Search Specialist → /blog geo <file>              (citation readiness)
  AI Search Specialist → /blog schema <file>           (JSON-LD)

STAGE 3 — SEO Optimization (SEO Department)
  Technical Auditor   → /seo page <url>                (on-page deep dive)
  Schema Specialist   → /seo schema <url>              (validate deployed schema)
  Content Specialist  → /seo content <url>             (E-E-A-T assessment)
  AI Search Specialist → /seo geo <url>                (GEO audit)

STAGE 4 — Paid Amplification (Ads Department)
  Strategy & Intelligence → /ads competitor            (competitive gap check)
  Strategy & Intelligence → /ads create                (campaign brief from content)
  Creative Director   → /ads generate                  (ad creatives from post)
  Performance Optimizer → /ads landing <url>           (landing page validation)
  Platform Specialists → deploy campaigns (Google, Meta, LinkedIn as appropriate)

STAGE 5 — Distribution (Blog + Marketing Departments)
  Blog Distribution   → /blog repurpose <file>         (social, email, Reddit, YouTube)
  Marketing Content   → social-content                 (platform-native social posts)
  Growth Manager      → email-sequence                 (nurture sequence from topic)

STAGE 6 — Measure & Loop
  SEO Data & Intelligence → /seo google gsc <url>      (ranking and traffic)
  Ads Performance Optimizer → budget review            (ROAS check, scale or kill)
  Blog Research Analyst → /blog google gsc             (impression growth)
  → Feed results back to Stage 1 for next cluster topic
```

---

### Playbook 4: Full Site SEO + Content Audit

Run quarterly or when taking on a new client with existing content.

```
PARALLEL — Run all simultaneously:

  SEO Department (full audit)
  → Technical Auditor:         /seo audit <url>              (0-100 health)
  → Technical Auditor:         /seo technical <url>          (9-category deep dive)
  → Schema Specialist:         /seo schema <url>             (structured data audit)
  → Schema Specialist:         /seo sitemap <url>            (XML sitemap health)
  → Schema Specialist:         /seo images <url>             (image optimization)
  → Content Specialist:        /seo content <url>            (E-E-A-T assessment)
  → AI Search Specialist:      /seo geo <url>                (GEO audit)
  → AI Search Specialist:      /seo cluster <seed>           (topic cluster gaps)
  → Competitor Strategist:     /seo competitor-pages         (comparison gaps)
  → Competitor Strategist:     /seo programmatic             (template page health)
  → Data & Intelligence:       /seo google gsc + backlinks   (ranking + links)
  → Local & Maps (if local):   /seo local + /seo maps        (GBP + geo-grid)
  → International (if i18n):   /seo hreflang <url>           (hreflang audit)

  Blog Department (content audit)
  → Quality Editor:            /blog audit                   (site-wide quality)
  → Quality Editor:            /blog cannibalization         (keyword overlap)
  → Research Analyst:          /blog google gsc              (GSC performance)
  → AI Search Specialist:      /blog geo (top 10 posts)      (citation readiness)

SYNTHESIZE → Master Audit Report
  - Site health score (0-100)
  - Content quality average (0-100)
  - Top 20 priority issues (ranked by impact)
  - Quick wins (can fix in < 1 hour)
  - 30/60/90 day fix roadmap
```

---

### Playbook 5: Paid Ads Launch (New Campaign)

Run when launching a new client campaign or new offer for existing client.

```
PRE-LAUNCH (Week 1)
  Ads: Strategy & Intelligence → /ads dna <url>              (brand-profile.json)
  Ads: Strategy & Intelligence → /ads competitor             (competitive intelligence)
  Ads: Strategy & Intelligence → /ads plan <business-type>   (platform + architecture)
  SEO: Data & Intelligence     → /seo dataforseo keywords    (keyword research)
  Marketing: Strategy Lead     → product-marketing-context   (ICP + messaging)
  Marketing: Strategy Lead     → marketing-psychology        (behavioral angles)

CREATIVE BUILD (Week 1-2)
  Ads: Strategy & Intelligence → /ads create                 (campaign-brief.md)
  Ads: Creative Director       → /ads generate               (ad image library)
  Ads: Creative Director       → /ads photoshoot             (product photography)
  Marketing: Content Writer    → copywriting                 (landing page copy)
  Blog: Content Writer         → /blog write <topic>         (content for retargeting)

PRE-LAUNCH VALIDATION
  Ads: Performance Optimizer   → /ads landing <url>          (landing page audit)
  Ads: Performance Optimizer   → /ads budget                 (budget model)
  Marketing: Ops Manager       → analytics-tracking          (tracking setup)
  SEO: Schema Specialist       → /seo schema <landing-url>   (schema on landing pages)

LAUNCH & MONITOR
  Ads: All Platform Specialists → deploy campaigns
  Ads: Audit Commander         → /ads audit (Day 3 post-launch check)
  Marketing: Ops Manager       → tracking integrity check

POST-LAUNCH LOOP (Weekly)
  → Run Weekly Client Report Loop (Playbook 2)
  → Run Content-to-Revenue Pipeline for top ad topics (Playbook 3)
```

---

### Playbook 6: Monthly Client Deliverable

Run at the end of each month. Produces the full client-facing monthly report.

```
WEEK 1 OF MONTH — Data Collection
  All departments run their monthly loops (see Monthly Loop above)

WEEK 2 — Analysis
  Marketing: Strategy Lead    → customer-research (review month's feedback/tickets)
  SEO: AI Search Specialist   → GEO scorecard (top 20 pages)
  Blog: Quality Editor        → monthly quality scorecard
  Ads: Audit Commander        → full audit → aggregate health score

WEEK 2 — Synthesis
  Marketing: Strategy Lead    → monthly strategy brief
  SEO: Technical Auditor      → monthly technical health report
  Blog: Strategy Lead         → monthly editorial performance + next month calendar
  Ads: Strategy & Intelligence → monthly campaign intelligence + next month plan

DELIVERABLE — Monthly Client Report
  Section 1: Executive Summary + Month-over-Month KPIs
  Section 2: SEO Health Report (health score trend, ranking changes, wins)
  Section 3: Content Performance (posts published, traffic, GEO citations earned)
  Section 4: Paid Ads Performance (spend, ROAS, CPA trends, creative winners)
  Section 5: Funnel Performance (CVR by stage, email, lead gen)
  Section 6: Competitive Intelligence (what competitors did this month)
  Section 7: Next Month Plan (priorities, calendar, budget allocation)
```

---

## Cross-Team Handoff Map

Where each department's output feeds the others.

```
MARKETING → BLOG
  Content Writer: messaging briefs, topic priorities
  Strategy Lead: customer research insights, ICP data, launch plans
  Growth Manager: email sequences needing content backing

MARKETING → SEO
  SEO Scout: keyword targets, schema requirements
  Web Developer: new pages for technical review + indexing

MARKETING → ADS
  Content Writer: landing page copy, ad creative copy
  CRO Specialist: conversion data for landing page optimization
  Strategy Lead: campaign strategy, audience segments, ICP

BLOG → SEO
  Content Writer: new posts for technical audit
  Quality Editor: posts clearing quality gates → schema and GEO pass
  AI Search Specialist: GEO scores and citation gaps

BLOG → ADS
  Content Writer: cornerstone posts to repurpose as ad content
  Distribution Manager: social posts that become paid social ads
  AI Search Specialist: high-GEO posts as retargeting content

BLOG → MARKETING
  Strategy Lead: topic performance data, audience engagement signals
  Distribution Manager: repurposed social content queue
  Research Analyst: discourse data and audience voice insights

SEO → BLOG
  Technical Auditor: thin content flags and decay reports
  AI Search Specialist: cluster gaps needing new posts
  Data & Intelligence: keyword ranking opportunities

SEO → ADS
  AI Search Specialist: GEO gaps → target with paid search
  Competitor Strategist: comparison pages → use for competitor keywords
  Data & Intelligence: keyword data for ad targeting

SEO → MARKETING
  Technical Auditor: site health data for Ops Manager
  Data & Intelligence: organic performance for strategy planning

ADS → SEO
  Performance Optimizer: landing page CRO data → on-page opportunities
  Strategy & Intelligence: competitor ad intelligence → content gaps

ADS → BLOG
  Creative Director: winning ad angles → new content topics
  Strategy & Intelligence: brand DNA (brand-profile.json) → BRAND.md sync

ADS → MARKETING
  Audit Commander: ROAS and CPA data → budget strategy
  Performance Optimizer: conversion data → CRO recommendations
```

---

## On-Demand Triggers

Run these when a specific event happens, regardless of cadence.

| Trigger | Run This |
|---------|---------|
| New client signed | Playbook 1: New Client Onboarding |
| New campaign launching | Playbook 5: Paid Ads Launch |
| Ranking drop detected | SEO: Technical Auditor + Data & Intelligence full audit |
| ROAS drops below target | Ads: Audit Commander full audit + Performance Optimizer |
| New competitor appears | SEO: Competitor Strategist + Ads: Strategy & Intelligence |
| Site update / redesign | SEO: All agents full audit + Blog Quality Editor + QA: `/qa-personas` |
| New product / offer | Marketing: Strategy Lead launch-strategy + Ads: full campaign build |
| Content decay signal | Blog: Quality Editor + SEO: Content Specialist rewrite queue |
| Algorithm update | SEO: Full audit + Blog: Quality Editor + Content Specialist |
| Lead gen drops | Marketing: CRO Specialist + Growth Manager + Blog: GEO audit + QA: `/qa-personas` |
| Creative fatigue | Ads: Creative Director batch generation |
| Bad review surge | Local & Maps Specialist + Marketing: Strategy Lead |

---

## Agent Overlap Map

These agents do similar work across departments and should coordinate:

| Function | Marketing | Blog | SEO | Ads |
|----------|-----------|------|-----|-----|
| Strategy & Planning | Strategy Lead | Strategy Lead | AI Search Specialist | Strategy & Intelligence |
| Content / Copy | Content Writer | Content Writer | Content & E-E-A-T | Creative Director |
| Research | Strategy Lead | Research Analyst | Data & Intelligence | Strategy & Intelligence |
| SEO / Search | SEO Scout | AI Search Specialist | Technical Auditor | — |
| AI / GEO | SEO Scout | AI Search Specialist | AI Search Specialist | — |
| Schema | SEO Scout | AI Search Specialist | Schema Specialist | — |
| Data / Analytics | Ops Manager | Research Analyst | Data & Intelligence | Audit Commander |
| Creative / Media | Content Writer | Media Producer | Data & Intelligence | Creative Director |
| Distribution | Growth Manager | Distribution Manager | — | Platform Specialists |
| Performance / CRO | CRO Specialist | Quality Editor | Content Specialist | Performance Optimizer |
| International | — | Multilingual Manager | International SEO Mgr | — |

---

## Quick Command Reference

```bash
# Run a full client audit (all departments)
/seo audit <url>
/blog audit
/ads audit
→ Synthesize into Master Audit Report

# Start a new blog post (full pipeline)
/blog discourse <topic>
/blog write <topic>
/blog geo <file>
/blog schema <file>
/blog repurpose <file>

# Build a new ad campaign
/ads dna <url>
/ads competitor
/ads plan <type>
/ads create
/ads generate
/ads landing <url>

# Full SEO audit
/seo audit <url>
/seo technical <url>
/seo content <url>
/seo geo <url>
/seo cluster <seed>

# Weekly report inputs
/seo google gsc <url>
/blog google gsc
/ads audit
→ Compile into Weekly Client Report
```

---

## Department Files

| File | Purpose |
|------|---------|
| `marketing-skills.md` | 34 marketing skills reference |
| `ai-marketing-team.md` | Marketing team: 8 agents, daily/weekly tasks |
| `blog-skills.md` | 30 blog skills reference |
| `ai-blog-team.md` | Blog team: 8 agents, daily/weekly tasks |
| `seo-skills.md` | 24 SEO skills reference |
| `ai-seo-team.md` | SEO team: 8 agents, daily/weekly tasks |
| `ads-skills.md` | 18 ads skills reference |
| `ai-ads-team.md` | Ads team: 8 agents, daily/weekly tasks |
| `work-skills.md` | Small business, legal, finance skills reference (`anthropics/knowledge-work-plugins`) |
| `ai-work-team.md` | Work team: 3 agents, daily/weekly tasks |
| `social-skills.md` | Social media skills reference (`charlie947/social-media-skills`) |
| `ai-social-team.md` | Social team: 3 agents, daily/weekly tasks |
| `design-skills.md` | Design skills reference (`ui-ux-pro-max`, `impeccable`, `taste`, `transitions.dev`) |
| `ai-design-team.md` | Design team: 3 agents, daily/weekly tasks |
| `qa-skills.md` | QA persona testing — `/qa-personas` skill reference |
| `post-launch-team.md` | Post-launch checklist playbook (one-shot, not an ongoing department) |
| `install-claude-company-os.sh` | Installs the underlying skill plugins for Work, Marketing, Social, Dev, Design groups |
| `agency-master-team.md` | This file — cross-team orchestration |
