# AI SEO Team — Operational Playbook

8 specialized AI agents powered by the `/seo` skill engine.
Each agent owns a domain, runs daily and weekly duties, and hands off to other agents as needed.
Full audits deploy up to 18 parallel AI agents under the hood.

---

## Agent 1: Technical Auditor

**Specialty:** Site health, crawlability, Core Web Vitals, and ongoing drift monitoring

**Skills:** `seo audit`, `seo technical`, `seo page`, `seo drift`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Crawl health check | `seo technical` | Scan for new 404s, indexability issues, redirect chains, and canonical errors |
| Core Web Vitals monitor | `seo technical` | Check CWV regressions on high-traffic pages vs. prior baseline |
| Drift detection | `seo drift` | Compare on-page signals against saved baselines across 17 rules; flag any deltas |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Full site audit | `seo audit` | Run 9-agent parallel audit, produce 0-100 health score, prioritize issues by severity |
| Technical category sweep | `seo technical` | Deep audit across all 9 technical categories: crawlability, security, mobile, structured data, etc. |
| Page-level deep dives | `seo page` | Analyze 3-5 underperforming pages for on-page issues |
| Baseline update | `seo drift` | Commit new SQLite baseline after any significant publish or site change |
| Technical issue tracker | — | Compile prioritized issue log from audit outputs for Strategy Lead |

### Key Outputs
- Weekly 0-100 site health score report
- Prioritized technical issue tracker (severity-ranked)
- Drift comparison report (17-rule delta)
- Per-page on-page analysis for underperformers

### Handoffs
- **Receives from:** Strategy Lead (new pages or URLs to monitor), Content & E-E-A-T Specialist (newly published content for technical review)
- **Hands off to:** Schema Specialist (pages with structured data issues), Strategy Lead (health score trends, crawl anomalies), Data & Intelligence Analyst (performance data for reporting)

---

## Agent 2: Content & E-E-A-T Specialist

**Specialty:** Content quality, search experience optimization, and evidence-led frameworks

**Skills:** `seo content`, `seo sxo`, `seo flow`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| E-E-A-T spot check | `seo content` | Audit 1-2 pages published in last 24 hours against 2025 Quality Rater Guidelines |
| SERP experience scan | `seo sxo` | Review SERP for priority keywords and flag format shifts (featured snippets, AI Overviews) |
| FLOW prompt application | `seo flow` | Apply one evidence-led FLOW prompt to the day's highest-priority optimization target |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| E-E-A-T content audit | `seo content` | Full E-E-A-T assessment across top 10 pages by traffic |
| SXO analysis | `seo sxo` | Run SERP-backward analysis for 3-5 target keywords; produce format and intent recommendations |
| FLOW framework review | `seo flow` | Run all four stages (Find, Leverage, Optimize, Win) across priority content |
| Content quality scorecard | `seo content` | Weekly average E-E-A-T score with category breakdowns |
| Thin content identification | `seo content` | Flag pages below quality threshold for rewrite or consolidation |

### Key Outputs
- Weekly E-E-A-T scorecard (per page and site-wide average)
- SXO format recommendations per keyword
- FLOW stage outputs (41 evidence-led prompts applied)
- Thin content list with consolidation/rewrite recommendations

### Handoffs
- **Receives from:** Technical Auditor (pages flagged for content issues), Strategy Lead (keyword targets for SXO analysis)
- **Hands off to:** Technical Auditor (new/rewritten pages for technical validation), AI Search Specialist (pages optimized for E-E-A-T ready for GEO pass), Strategy Lead (content quality data and format insights)

---

## Agent 3: Schema & Structure Specialist

**Specialty:** Structured data, XML sitemaps, and image optimization

**Skills:** `seo schema`, `seo sitemap`, `seo images`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Schema validation | `seo schema` | Verify JSON-LD on any pages published or updated in the last 24 hours |
| Sitemap health check | `seo sitemap` | Confirm sitemap reflects latest published content and all URLs return 200 |
| Image alt text audit | `seo images` | Check alt text on new images added to the site in the last 24 hours |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Schema expansion | `seo schema` | Identify pages eligible for new rich result types and generate JSON-LD |
| Full sitemap audit | `seo sitemap` | Validate entire XML sitemap: HTTP statuses, canonical alignment, index coverage |
| Image optimization pass | `seo images` | Audit all images published this week for file size, format (WebP/AVIF), and alt text |
| Schema type library | `seo schema` | Maintain inventory of all active schema types and their validation status |
| Rich result monitoring | `seo schema` | Track which pages are earning rich results in Google Search Console |

### Key Outputs
- JSON-LD schema files per page (BlogPosting, Product, FAQ, LocalBusiness, etc.)
- Sitemap validation report (URL count, HTTP statuses, coverage gaps)
- Image optimization report (format, size, alt text compliance)
- Rich result eligibility map

### Handoffs
- **Receives from:** Technical Auditor (pages with structured data issues), AI Search Specialist (pages needing FAQ or Speakable schema for citation optimization)
- **Hands off to:** Technical Auditor (schema-enriched pages for re-audit), AI Search Specialist (pages with FAQ schema for GEO pass), International Manager (schema files needing locale variants)

---

## Agent 4: AI Search Specialist

**Specialty:** GEO/AEO optimization, topic clustering, and strategic planning

**Skills:** `seo geo`, `seo cluster`, `seo plan`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| AI Overview monitor | `seo geo` | Check if priority pages are appearing in Google AI Overviews or ChatGPT responses |
| Cluster gap scan | `seo cluster` | Identify gaps in active topic clusters based on SERP-overlap signals |
| Citation readiness check | `seo geo` | Audit one page per day for answer-first formatting and extractable passage quality |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| GEO audit | `seo geo` | Full AI citation readiness audit across top 10 pages (Google AI Overviews, ChatGPT, Perplexity, Copilot) |
| Topic cluster build | `seo cluster` | Design or expand hub-and-spoke clusters using SERP-overlap analysis |
| Strategic plan | `seo plan` | Run industry-specific planning with competitive analysis and content pillar mapping |
| AI search readiness scorecard | `seo geo` | Weekly citation readiness scores with per-page recommendations |
| Cluster coverage report | `seo cluster` | Map existing content to cluster slots; flag missing spoke pages |

### Key Outputs
- Weekly AI search readiness scorecard (GEO score per page)
- Topic cluster maps (hub + spoke structure with coverage gaps)
- Industry-specific strategic plan with content pillars
- AI citation gap report (pages missing extractable passages or answer-first formatting)

### Handoffs
- **Receives from:** Content & E-E-A-T Specialist (pages optimized and ready for GEO pass), Schema Specialist (pages with FAQ schema)
- **Hands off to:** Strategy Lead (GEO scores and citation opportunities), Content & E-E-A-T Specialist (pages flagged for answer-first formatting fixes), Competitor & Growth Strategist (cluster gaps that need new pages)

---

## Agent 5: Local & Maps Specialist

**Specialty:** Local SEO, Google Business Profile, and geo-grid rank tracking

**Skills:** `seo local`, `seo maps`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| GBP signal check | `seo local` | Monitor Google Business Profile for new reviews, Q&As, and post performance |
| NAP consistency scan | `seo local` | Check for NAP inconsistencies across key citation sources |
| Geo-grid spot check | `seo maps` | Review rank changes in priority geo-grid cells for top keywords |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Full local audit | `seo local` | GBP audit, citation analysis, review sentiment, and map pack ranking report |
| Geo-grid rank report | `seo maps` | Full geo-grid rank tracking across service area with competitor radius mapping |
| Review response audit | `seo local` | Ensure all new reviews (positive and negative) have been responded to |
| Citation building recommendations | `seo local` | Identify top citation gaps vs. competitors and queue for cleanup |
| Competitor local analysis | `seo maps` | Map competitor GBP presence and identify proximity ranking opportunities |

### Key Outputs
- Weekly GBP performance report (views, clicks, calls, direction requests)
- Geo-grid rank visualization (keyword × location matrix)
- Citation gap and NAP inconsistency report
- Competitor local positioning map
- Review sentiment analysis

### Handoffs
- **Receives from:** Strategy Lead (target service areas and keywords), Schema Specialist (LocalBusiness schema for GBP alignment)
- **Hands off to:** Strategy Lead (local ranking data for strategic decisions), Schema Specialist (GBP data needing LocalBusiness schema updates)

---

## Agent 6: International SEO Manager

**Specialty:** Hreflang implementation, i18n auditing, and cross-domain international SEO

**Skills:** `seo hreflang`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Hreflang validation | `seo hreflang` | Check hreflang tags on any pages published or updated in the last 24 hours |
| Locale parity check | `seo hreflang` | Verify translated pages have corresponding hreflang entries for each live language |
| Return tag audit | `seo hreflang` | Confirm all hreflang relationships are bidirectional (source and target both declared) |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Full hreflang audit | `seo hreflang` | Validate hreflang implementation site-wide: syntax, return tags, x-default, cross-domain |
| International coverage report | `seo hreflang` | Map which pages have language variants vs. which are English-only |
| i18n error fix queue | `seo hreflang` | Compile and prioritize hreflang errors by severity for development handoff |
| Locale signal report | `seo hreflang` | Identify top pages by traffic that lack international variants (expansion opportunities) |

### Key Outputs
- Weekly hreflang validation report (errors by type and severity)
- International coverage map (pages × languages)
- i18n error fix queue (prioritized for dev)
- Locale expansion opportunity list (high-traffic pages without translations)

### Handoffs
- **Receives from:** Strategy Lead (pages approved for international expansion), Schema Specialist (schema files needing locale-specific variants)
- **Hands off to:** Strategy Lead (international coverage data), Technical Auditor (hreflang fixes needing technical implementation)

---

## Agent 7: Competitor & Growth Strategist

**Specialty:** Competitor positioning, programmatic SEO, and e-commerce optimization

**Skills:** `seo competitor-pages`, `seo programmatic`, `seo ecommerce`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Competitor content scan | `seo competitor-pages` | Monitor for new competitor comparison pages or "alternatives to" content |
| Programmatic page health | `seo programmatic` | Check template pages for thin content, index bloat, and canonicalization |
| Product schema validation | `seo ecommerce` | Verify product schema and pricing data on new or updated product pages |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Competitor comparison pages | `seo competitor-pages` | Create or update "vs" and "alternatives to X" pages based on competitive shifts |
| Programmatic SEO audit | `seo programmatic` | Audit all template pages for quality gates, duplication, and scale opportunities |
| E-commerce SEO review | `seo ecommerce` | Full product schema audit, Google Shopping visibility check, and pricing intelligence |
| New comparison page briefs | `seo competitor-pages` | Brief 2-3 new comparison pages based on competitor keyword movements |
| Programmatic template expansion | `seo programmatic` | Identify new template opportunities (location pages, use-case pages, integration pages) |

### Key Outputs
- Comparison and "alternatives to" page drafts
- Programmatic SEO health report (template quality, index coverage)
- E-commerce schema validation report
- Google Shopping visibility audit
- Competitive positioning gap analysis

### Handoffs
- **Receives from:** AI Search Specialist (cluster gaps needing new pages), Data & Intelligence Analyst (live SERP and competitor keyword data)
- **Hands off to:** Schema Specialist (new pages needing structured data), Technical Auditor (new pages for technical review and indexing), Strategy Lead (competitive positioning data)

---

## Agent 8: Data & Intelligence Analyst

**Specialty:** Google API integrations, backlink intelligence, live SERP data, and SEO asset generation

**Skills:** `seo google`, `seo backlinks`, `seo dataforseo`, `seo image-gen`, `seo firecrawl`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| GSC performance pull | `seo google` | Pull overnight Search Console impression/click data and flag ranking drops |
| Toxic link monitor | `seo backlinks` | Scan for new referring domains and flag any toxic or spammy links |
| SERP snapshot | `seo dataforseo` | Pull live SERP data for priority keywords and log position changes |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Google API report | `seo google` | Run PageSpeed Insights, CrUX CWV, GSC, and GA4 organic data — compile into weekly report |
| Full backlink audit | `seo backlinks` | Toxic link detection via Moz, Bing Webmaster, and Common Crawl; produce disavow candidates |
| Keyword intelligence report | `seo dataforseo` | Live keyword ranking, volume, and competitor data for Strategy Lead's planning session |
| Full-site crawl | `seo firecrawl` | JavaScript-rendered full-site crawl to surface dynamic content issues missed by standard crawlers |
| SEO asset generation | `seo image-gen` | Generate OG preview images and infographics for top-performing posts and landing pages |

### Key Outputs
- Weekly Google performance report (PSI, CrUX, GSC, GA4 organic)
- Backlink health report (new links, toxic links, disavow candidates)
- Live SERP ranking report (position changes, SERP feature wins/losses)
- Full-site crawl report (JavaScript rendering issues, dynamic content gaps)
- SEO image asset library (OG images, infographics)

### Handoffs
- **Receives from:** All agents (data requests and reporting needs)
- **Hands off to:** Technical Auditor (CWV and performance data), Strategy Lead (ranking, keyword, and competitive intelligence), Competitor & Growth Strategist (live SERP and competitor keyword data), Schema Specialist (GSC rich result data)

---

## Team Communication Flow

```
                    ┌──────────────┐
                    │   Strategy   │
                    │    Lead      │
                    │  (external)  │
                    └──────┬───────┘
            Targets & │          ▲ Rankings &
           Priorities  │          │ Insights
                       ▼          │
        ┌──────────────────────────────────────┐
        │                                      │
   ┌────▼──────┐  ┌───────────┐  ┌────────────▼──┐
   │ Technical  │  │ Content & │  │  Data &       │
   │  Auditor   │  │  E-E-A-T  │  │ Intelligence  │
   │  (Agent 1) │  │ (Agent 2) │  │   (Agent 8)   │
   └────┬───────┘  └────┬──────┘  └──────┬────────┘
        │               │                │
        ▼               ▼                ▼
   ┌──────────┐   ┌──────────────┐  ┌──────────────┐
   │  Schema & │   │  AI Search   │  │  Competitor  │
   │Structure  │──►│ Specialist   │  │  & Growth    │
   │ (Agent 3) │   │  (Agent 4)   │  │  (Agent 7)   │
   └──────────┘   └──────────────┘  └──────────────┘
        │
        ├──────────────────┐
        ▼                  ▼
   ┌──────────┐     ┌──────────────┐
   │  Local & │     │International │
   │  Maps    │     │  SEO Mgr     │
   │ (Agent 5)│     │  (Agent 6)   │
   └──────────┘     └──────────────┘
```

**Daily standup order:** Data & Intelligence Analyst → Technical Auditor → Schema Specialist → Content & E-E-A-T Specialist → AI Search Specialist → Competitor & Growth Strategist → Local & Maps Specialist → International SEO Manager

**Weekly sync:** Strategy Lead reviews all 8 agent outputs to set priorities for the following week. Technical Auditor's health score and Data & Intelligence Analyst's ranking report are the two primary inputs.

---

## Audit Pipeline (Full Site)

```
Data & Intelligence Analyst   → GSC baseline, backlink snapshot, live SERP data
Technical Auditor             → 0-100 health score + prioritized issue list
Schema Specialist             → structured data validation + sitemap check
Content & E-E-A-T Specialist  → quality assessment + thin content flags
AI Search Specialist          → GEO/AIO citation readiness + cluster gaps
Competitor & Growth Strategist → programmatic health + comparison page gaps
Local & Maps Specialist       → GBP + geo-grid rank snapshot (if local)
International SEO Manager     → hreflang validation (if multilingual)
```

Every audit moves left to right. Findings from each agent feed the next agent's context before Strategy Lead receives the consolidated report.
