# AI Ads Team — Operational Playbook

8 specialized AI agents powered by the `/ads` skill engine.
Each agent owns a platform or domain, runs daily and weekly duties, and hands off to other agents as needed.
Full audits run 250+ checks across all platforms with parallel subagent delegation.

---

## Agent 1: Audit Commander

**Specialty:** Cross-platform health scoring, audit orchestration, and prioritized action planning

**Skills:** `ads audit`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Platform health pulse | `ads audit` | Quick cross-platform performance check: flag anomalies vs. prior 7-day average |
| Spend pacing alert | `ads audit` | Verify all platforms are on pace for monthly budget targets |
| Conversion tracking status | `ads audit` | Confirm conversion events are firing correctly across all platforms |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Full multi-platform audit | `ads audit` | Run all 250+ checks across every active platform in parallel |
| Aggregate health score | `ads audit` | Calculate per-platform and aggregate Ads Health Score (0-100) |
| Quick wins report | `ads audit` | Surface top 5 highest-impact fixes from across all platform audits |
| Prioritized action plan | `ads audit` | Compile findings from all specialist agents into one ranked issue list |
| Client-ready PDF report | `ads audit` | Generate formatted report from audit results |

### Key Outputs
- Weekly aggregate Ads Health Score (0-100)
- Per-platform health scores
- Prioritized action plan (all platforms combined)
- Quick wins list (highest ROI fixes)
- Client-ready PDF audit report

### Handoffs
- **Receives from:** All platform specialists (per-platform audit data and findings)
- **Hands off to:** All platform specialists (platform-specific issues to investigate), Performance Optimizer (budget and landing page flags), Creative Director (creative fatigue and quality flags), Strategy & Intelligence (strategic gaps and opportunity signals)

---

## Agent 2: Google Ads Specialist

**Specialty:** Search, Performance Max, AI Max, Display, and Demand Gen campaigns

**Skills:** `ads google`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Search term report review | `ads google` | Check for new irrelevant queries, add negatives, flag wasted spend |
| PMax asset performance | `ads google` | Review asset group performance signals and low-performing asset flags |
| Bid strategy health | `ads google` | Monitor Smart Bidding signals for learning phase exits and target adjustments |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Full Google Ads audit | `ads google` | Run all 80 checks: conversion tracking, wasted spend, structure, keywords, ad strength, settings |
| Quality Score audit | `ads google` | Review QS by keyword, identify below-average landing page experience and ad relevance |
| PMax campaign review | `ads google` | Audit asset groups, audience signals, search themes, and placement exclusions |
| RSA performance review | `ads google` | Check ad strength, headline pinning usage, and underperforming ad combinations |
| Demand Gen performance | `ads google` | Review audience segments, creative performance, and cross-channel signals |

### Key Outputs
- Google Ads health score (0-100, 80 checks)
- Wasted spend report with negative keyword recommendations
- Quality Score improvement brief
- PMax asset group audit
- RSA and ad strength report

### Handoffs
- **Receives from:** Audit Commander (Google flags), Strategy & Intelligence (campaign briefs, keyword targets), Performance Optimizer (landing page match data)
- **Hands off to:** Audit Commander (health score and findings), Creative Director (RSA copy refresh needs), Performance Optimizer (landing page issues from QS data)

---

## Agent 3: Meta & Social Ads Specialist

**Specialty:** Facebook, Instagram, TikTok, and YouTube paid social campaigns

**Skills:** `ads meta`, `ads tiktok`, `ads youtube`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Creative fatigue check | `ads meta` | Monitor frequency metrics; flag ad sets with frequency > 3 for creative rotation |
| TikTok delivery check | `ads tiktok` | Review Smart+ campaign pacing and Shop ad performance |
| YouTube view-through audit | `ads youtube` | Check skippable vs. non-skippable completion rates and Shorts performance |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Full Meta audit | `ads meta` | Run 50 checks: Pixel/CAPI health, EMQ scores, creative fatigue, structure, Advantage+ |
| Full TikTok audit | `ads tiktok` | Run 28 checks: creative quality, Shop ads, Smart+ campaigns, post-USDS data access |
| Full YouTube audit | `ads youtube` | Audit skippable, Shorts, Demand Gen, and CTV formats |
| Audience overlap analysis | `ads meta` | Check for audience overlap between ad sets driving up CPMs |
| Advantage+ campaign review | `ads meta` | Evaluate Advantage+ Shopping and Advantage+ Audience performance |

### Key Outputs
- Meta Ads health score (0-100, 50 checks)
- TikTok Ads health score (0-100, 28 checks)
- YouTube Ads performance report
- Creative fatigue report (frequency, CTR decay by ad set)
- Pixel/CAPI health report with EMQ scores

### Handoffs
- **Receives from:** Audit Commander (social platform flags), Creative Director (new creative for rotation), Strategy & Intelligence (audience briefs and campaign concepts)
- **Hands off to:** Audit Commander (health scores and findings), Creative Director (fatigued ads needing replacement), Performance Optimizer (post-click landing page issues)

---

## Agent 4: B2B Ads Specialist

**Specialty:** LinkedIn B2B campaigns and Microsoft/Bing search advertising

**Skills:** `ads linkedin`, `ads microsoft`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| LinkedIn lead quality check | `ads linkedin` | Review Lead Gen Form completion rates and lead quality signals |
| Microsoft import health | `ads microsoft` | Verify Google Ads import is syncing correctly and Copilot Ads are active |
| B2B audience signal review | `ads linkedin` | Check job title, seniority, and company size targeting performance |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Full LinkedIn audit | `ads linkedin` | Run 27 checks: B2B targeting, Lead Gen Forms, Thought Leader Ads, ABM campaigns |
| Full Microsoft audit | `ads microsoft` | Run 24 checks: Copilot Ads, Bing search, Google import validation, audience targeting |
| ABM campaign review | `ads linkedin` | Evaluate Account-Based Marketing campaign match rates and target account penetration |
| Thought Leader Ads performance | `ads linkedin` | Review employee advocacy ad engagement and organic boost metrics |
| Copilot Ads review | `ads microsoft` | Audit Microsoft Copilot ad placements and AI-served ad performance |

### Key Outputs
- LinkedIn Ads health score (0-100, 27 checks)
- Microsoft Ads health score (0-100, 24 checks)
- B2B audience targeting report
- Lead Gen Form conversion analysis
- ABM match rate and penetration report

### Handoffs
- **Receives from:** Audit Commander (B2B platform flags), Strategy & Intelligence (B2B campaign briefs and ICP targeting)
- **Hands off to:** Audit Commander (health scores and findings), Creative Director (B2B ad copy and creative briefs), Performance Optimizer (LinkedIn landing page conversion issues)

---

## Agent 5: Mobile & App Ads Specialist

**Specialty:** Apple Search Ads and Amazon Ads for app installs and e-commerce

**Skills:** `ads apple`, `ads amazon`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| ASA impression share check | `ads apple` | Monitor Apple Search Ads impression share by match type (Broad, Exact, Discovery) |
| Amazon ACOS monitor | `ads amazon` | Check ACOS trends across Sponsored Products and flag campaigns above target |
| App Store ranking signal | `ads apple` — | Review TAP coverage and conversion rate for App Store product pages |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Full Apple Search Ads audit | `ads apple` | Run 35+ checks: CPPs, AdAttributionKit, TAP coverage, match type distribution |
| Full Amazon Ads audit | `ads amazon` | Run 30+ checks: Sponsored Products, Sponsored Brands, Sponsored Display, ACOS |
| Custom Product Pages (CPP) review | `ads apple` | Audit CPP performance and test new page variants |
| AdAttributionKit health check | `ads apple` | Validate attribution setup and post-install event measurement |
| Amazon DSP performance | `ads amazon` | Review audience-based display targeting and retargeting ROAS |

### Key Outputs
- Apple Search Ads health score (35+ checks)
- Amazon Ads health score (30+ checks)
- ACOS performance report with kill/scale recommendations
- CPP variant test results
- AdAttributionKit attribution validation report

### Handoffs
- **Receives from:** Audit Commander (mobile/app platform flags), Strategy & Intelligence (seasonal campaign briefs, new product launches)
- **Hands off to:** Audit Commander (health scores and findings), Creative Director (CPP and Amazon creative briefs), Performance Optimizer (product page and app store landing page issues)

---

## Agent 6: Creative Director

**Specialty:** Ad creative quality, AI image generation, and product photography

**Skills:** `ads creative`, `ads generate`, `ads photoshoot`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Creative fatigue monitor | `ads creative` | Flag ad sets with decaying CTR or high frequency across all platforms |
| Creative rotation queue | `ads creative` | Pull list of ads due for replacement based on performance thresholds |
| Asset generation | `ads generate` | Generate replacement creatives for fatigued ad sets using `campaign-brief.md` |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Cross-platform creative audit | `ads creative` | Full creative quality review: copy, video, image, format diversity, platform-native compliance |
| Weekly creative batch | `ads generate` | Generate a full week's ad creative library from the active campaign brief |
| Product photography session | `ads photoshoot` | Generate 5 product photography styles (Studio, Floating, Ingredient, In Use, Lifestyle) for new products |
| Creative performance analysis | `ads creative` | Identify top and bottom performers by creative format and message angle |
| Format diversity check | `ads creative` | Ensure each platform has at least 3 active ad formats to reduce delivery risk |

### Key Outputs
- Weekly creative quality audit report (per platform)
- Creative fatigue report (frequency, CTR decay, rotation schedule)
- AI-generated ad creative library (platform-sized assets)
- Product photography set (5 styles × 2 aspect ratios)
- Top/bottom performer analysis by format and message

### Handoffs
- **Receives from:** All platform specialists (fatigued and underperforming creatives), Strategy & Intelligence (`campaign-brief.md` and `brand-profile.json` for generation)
- **Hands off to:** All platform specialists (new creative assets for deployment), Audit Commander (creative health data for aggregate scoring)

---

## Agent 7: Strategy & Intelligence

**Specialty:** Campaign planning, brand extraction, competitor intelligence, and brief development

**Skills:** `ads plan`, `ads competitor`, `ads dna`, `ads create`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Competitor ad scan | `ads competitor` | Monitor ad libraries (Google Transparency, Meta Ad Library, LinkedIn) for competitor moves |
| Campaign brief maintenance | `ads create` | Update `campaign-brief.md` with new angles, offers, or messaging pivots |
| Market signal log | `ads competitor` | Flag new competitor creative themes or keyword entries for Strategic Lead review |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Competitor intelligence report | `ads competitor` | Full analysis of competitor ad copy, creative strategy, spend estimates, and targeting gaps |
| Campaign brief generation | `ads create` | Produce new `campaign-brief.md` from brand profile and audit findings |
| Strategic ad plan | `ads plan` | Build or update industry-specific plan: platform selection, architecture, budget model, creative roadmap |
| Brand DNA extraction | `ads dna` | Scan new or updated URLs to refresh `brand-profile.json` |
| Platform mix review | `ads plan` | Evaluate whether current platform allocation matches business goals and audience behavior |

### Key Outputs
- Weekly competitor intelligence report (copy, creative, spend, gaps)
- `campaign-brief.md` (structured campaign concepts and copy briefs)
- `brand-profile.json` (colors, typography, tone, imagery style)
- Industry-specific strategic ad plan
- Platform mix and architecture recommendation

### Handoffs
- **Receives from:** Audit Commander (strategic gaps surfaced by audit), Performance Optimizer (budget and conversion data), all platform specialists (platform-specific insights)
- **Hands off to:** Creative Director (`campaign-brief.md` and `brand-profile.json` for generation), all platform specialists (campaign briefs and keyword/audience targets), Performance Optimizer (budget model from strategic plan)

---

## Agent 8: Performance Optimizer

**Specialty:** Landing page conversion, budget allocation, and bidding strategy

**Skills:** `ads landing`, `ads budget`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Conversion anomaly scan | `ads landing` | Check key landing page conversion rates for drops vs. 7-day average |
| Budget pacing check | `ads budget` | Verify spend pacing across platforms; flag over/under-spend vs. plan |
| Bidding strategy health | `ads budget` | Monitor Smart Bidding learning phase status across active campaigns |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Landing page audit | `ads landing` | Full assessment: message match, page speed, mobile, trust signals, form optimization |
| Budget allocation review | `ads budget` | Apply 70/20/10 rule across platforms; produce kill list and scale list |
| Bidding strategy audit | `ads budget` | Evaluate bid strategy appropriateness per campaign goal; flag misaligned strategies |
| Message match report | `ads landing` | Audit headline, offer, CTA, and visual match between ads and landing pages |
| Scaling readiness assessment | `ads budget` | Apply 3x Kill Rule and 20% scaling rule; identify campaigns ready to scale |

### Key Outputs
- Landing page audit report (message match, speed, mobile, trust, form)
- Weekly budget allocation report (70/20/10 breakdown)
- Kill list and scale list (ranked by ROAS and CPA performance)
- Bidding strategy audit (per campaign, with recommendations)
- Scaling readiness scorecard

### Handoffs
- **Receives from:** All platform specialists (CPA and ROAS data), Audit Commander (budget and conversion flags), Strategy & Intelligence (budget model from strategic plan)
- **Hands off to:** Audit Commander (performance data for aggregate scoring), Strategy & Intelligence (conversion and ROAS data for planning), all platform specialists (landing page fix recommendations and budget reallocation directives)

---

## Team Communication Flow

```
                    ┌──────────────────┐
                    │  Strategy &      │
                    │  Intelligence    │
                    │   (Agent 7)      │
                    └────────┬─────────┘
           Briefs & │              ▲ Competitive &
          Platform  │              │ Performance Data
          Targets   ▼              │
        ┌────────────────────────────────────────┐
        │                                        │
   ┌────▼──────┐  ┌───────────┐  ┌──────────────▼─┐
   │  Google   │  │ Meta &    │  │  Performance   │
   │   Ads     │  │  Social   │  │  Optimizer     │
   │ (Agent 2) │  │ (Agent 3) │  │  (Agent 8)     │
   └────┬──────┘  └─────┬─────┘  └────────┬───────┘
        │               │                 │
        └───────┬────────┘                │
                ▼                         │
   ┌────────────────────┐                 │
   │   Audit Commander  │◄────────────────┘
   │     (Agent 1)      │
   └────────────────────┘
          ▲        ▲
          │        │
   ┌──────┴──┐  ┌──┴──────────────┐
   │  B2B    │  │ Mobile & App    │
   │  Ads    │  │  Specialist     │
   │(Agent 4)│  │   (Agent 5)     │
   └─────────┘  └────────────────-┘
          ▲
          │
   ┌──────┴──────┐
   │  Creative   │
   │  Director   │
   │  (Agent 6)  │
   └─────────────┘
```

**Daily standup order:** Performance Optimizer → Audit Commander → Google Ads Specialist → Meta & Social Specialist → B2B Ads Specialist → Mobile & App Specialist → Creative Director → Strategy & Intelligence

**Weekly sync:** Audit Commander runs an 8-agent weekly review using the aggregate health score and per-platform findings to set optimization priorities. Strategy & Intelligence sets the following week's campaign and creative direction based on competitive signals and performance data.

---

## Campaign Build Pipeline (New Campaign)

```
Strategy & Intelligence   → brand-profile.json (ads dna)
Strategy & Intelligence   → campaign-brief.md (ads create)
Creative Director         → ad creative assets (ads generate)
Creative Director         → product photography (ads photoshoot)
Platform Specialists      → campaign setup and targeting
Performance Optimizer     → landing page validation (ads landing)
Performance Optimizer     → budget model (ads budget)
Audit Commander           → post-launch health check (ads audit)
```

## Audit Pipeline (Existing Account)

```
Audit Commander           → full 250+ check audit across all platforms
Google Ads Specialist     → 80-check Google deep dive
Meta & Social Specialist  → 50-check Meta + 28-check TikTok + YouTube
B2B Ads Specialist        → 27-check LinkedIn + 24-check Microsoft
Mobile & App Specialist   → 35-check Apple + 30-check Amazon
Creative Director         → cross-platform creative quality audit
Performance Optimizer     → landing page + budget review
Strategy & Intelligence   → competitive gap analysis and plan update
```

Every audit runs in parallel. Audit Commander synthesizes all findings into the aggregate health score and client-ready report.
