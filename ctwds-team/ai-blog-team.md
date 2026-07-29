# AI Blog Team — Operational Playbook

8 specialized AI agents powered by the `/blog` content engine.
Each agent owns a domain, runs daily and weekly duties, and hands off to other agents as needed.
All agents route through the `blog/SKILL.md` orchestrator.

---

## Agent 1: Content Writer

**Specialty:** Article creation, optimization, and brief development

**Skills:** `blog-write`, `blog-rewrite`, `blog-outline`, `blog-brief`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Draft new articles | `blog-write` | Write one new post using the research packet from Research Analyst |
| Optimize flagged posts | `blog-rewrite` | Rewrite posts flagged by Quality Editor for freshness or AI content signals |
| Outline review | `blog-outline` | Update outlines based on SERP shifts or new competitive gaps from Strategy Lead |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Content batch production | `blog-write` | Write 2-3 new posts from Strategy Lead's editorial calendar priorities |
| Brief development | `blog-brief` | Create detailed content briefs for next week's planned posts |
| Rewrite queue | `blog-rewrite` | Optimize 1-2 existing posts flagged as decaying by Quality Editor's audit |
| Outline bank | `blog-outline` | Build SERP-informed outlines for upcoming content cluster topics |
| Template selection review | `blog-brief` | Match content types (how-to, listicle, case study) to strategic goals |

### Key Outputs
- Published article drafts (platform-formatted)
- Weekly content brief library
- SERP-informed outlines for upcoming posts
- Rewrite reports with before/after quality scores

### Handoffs
- **Receives from:** Strategy Lead (topic priorities, editorial calendar, briefs), Research Analyst (research packets, discourse data, Google API data), Quality Editor (rewrite flags and score reports)
- **Hands off to:** Quality Editor (new drafts for scoring and SEO validation), AI Search Specialist (new posts for schema and GEO audit), Media Producer (posts needing images, audio, or charts)

---

## Agent 2: Strategy Lead

**Specialty:** Editorial planning, topic clustering, brand voice, and persona management

**Skills:** `blog-strategy`, `blog-calendar`, `blog-cluster`, `blog-persona`, `blog-brand`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Topic ideation | `blog-strategy` | Identify emerging topics, seasonal angles, and competitor content gaps |
| Calendar maintenance | `blog-calendar` | Update editorial calendar with new assignments and shift priorities based on signals |
| Persona consistency check | `blog-persona` | Verify that published content matches the active voice profile |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Editorial calendar | `blog-calendar` | Plan next 4 weeks of content with 60/30/10 mix (evergreen/topical/promotional) |
| Topic cluster planning | `blog-cluster` | Design or expand hub-and-spoke content clusters around core topics |
| Strategy session | `blog-strategy` | Generate 5-10 new topic ideas ranked by traffic potential and AI citation likelihood |
| Persona audit | `blog-persona` | Review and update voice profiles, tone sliders, and readability targets |
| Brand context refresh | `blog-brand` | Update BRAND.md and VOICE.md with new positioning, taboo phrases, or audience shifts |

### Key Outputs
- Weekly editorial calendar (4-week rolling)
- Topic cluster maps (hub + spoke structure)
- Blog strategy report (positioning, angles, priorities)
- Updated BRAND.md and VOICE.md context files
- Persona profiles for all content types

### Handoffs
- **Receives from:** Quality Editor (decay reports, cannibalization flags), AI Search Specialist (GEO scorecard, citation opportunities), Research Analyst (discourse data and SERP signals)
- **Hands off to:** Content Writer (topic briefs, editorial priorities, cluster assignments), Research Analyst (topic targets for research), Multilingual Manager (posts approved for international expansion)

---

## Agent 3: Research Analyst

**Specialty:** Source intelligence, discourse monitoring, and Google data integration

**Skills:** `blog-discourse`, `blog-notebooklm`, `blog-google`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Discourse scan | `blog-discourse` | Monitor what practitioners are saying about priority topics in the last 30 days |
| Performance data pull | `blog-google` | Pull GSC click/impression data and flag posts with declining impressions |
| Source freshness check | `blog-notebooklm` | Query NotebookLM for updated statistics relevant to posts in the rewrite queue |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Discourse research | `blog-discourse` | Produce DISCOURSE.md for each planned cluster topic (real-world practitioner signals) |
| Google API report | `blog-google` | Run PageSpeed, CrUX Core Web Vitals, and GSC performance reports across top 10 posts |
| Source research packets | `blog-notebooklm` | Prepare Tier 1-3 source packets for Content Writer's upcoming drafts |
| Keyword opportunity report | `blog-google` | Pull keyword ranking data and surface new opportunities for Strategy Lead |
| SERP analysis | `blog-discourse` | Identify current ranking formats (listicle vs. how-to vs. comparison) for target topics |

### Key Outputs
- DISCOURSE.md files per topic (practitioner voice, last 30 days)
- Research packets with Tier 1-3 sourced statistics
- Weekly Google Performance report (PSI, CrUX, GSC)
- Keyword opportunity report
- SERP format analysis per topic

### Handoffs
- **Receives from:** Strategy Lead (topic targets, cluster priorities), Quality Editor (posts flagged for stat freshness)
- **Hands off to:** Content Writer (research packets for drafting), Strategy Lead (SERP signals, keyword opportunities, discourse trends), Quality Editor (freshness data for factcheck queue)

---

## Agent 4: Media Producer

**Specialty:** Visual assets, audio narration, and data visualization

**Skills:** `blog-image`, `blog-audio`, `blog-chart`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Hero image generation | `blog-image` | Generate hero images for posts publishing today or tomorrow |
| Chart production | `blog-chart` | Create inline SVG charts for posts with data-heavy sections |
| Audio narration queue | `blog-audio` | Check narration requests and process summary-mode audio for high-priority posts |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Image batch production | `blog-image` | Generate hero and inline images for all posts planned in next week's calendar |
| Chart audit | `blog-chart` | Review charts in published posts for data freshness and visual variety |
| Audio narration batch | `blog-audio` | Produce full-article or dialogue narrations for top-performing evergreen posts |
| Alt text audit | `blog-image` | Verify all published post images have descriptive, keyword-natural alt text |
| Visual format diversification | `blog-chart` | Ensure no two charts in a single post use the same chart type |

### Key Outputs
- Hero images per post (platform-formatted)
- Inline SVG charts for data sections
- Audio narration files (summary, full, or dialogue mode)
- Alt text audit report
- Visual asset library for the week

### Handoffs
- **Receives from:** Content Writer (posts needing visual assets), Strategy Lead (brand direction and visual style guidelines from BRAND.md)
- **Hands off to:** Content Writer (asset files ready for embedding), Quality Editor (posts with assets ready for final scoring), AI Search Specialist (posts needing VideoObject schema for embedded media)

---

## Agent 5: Quality Editor

**Specialty:** Content scoring, SEO validation, factual accuracy, and site health

**Skills:** `blog-seo-check`, `blog-analyze`, `blog-audit`, `blog-cannibalization`, `blog-factcheck`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| New draft scoring | `blog-analyze` | Run 100-point quality audit on every new draft from Content Writer |
| SEO validation | `blog-seo-check` | Check title tag, meta description, heading hierarchy, and OG tags on posts ready to publish |
| Stat verification | `blog-factcheck` | Verify all statistics in drafts against cited sources before publishing |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Site-wide health audit | `blog-audit` | Run full-site assessment across all published posts for decay, thin content, and technical issues |
| Cannibalization scan | `blog-cannibalization` | Detect keyword overlap across posts, score severity, flag consolidation candidates |
| Factcheck queue | `blog-factcheck` | Verify statistics in posts flagged as stale by Research Analyst |
| Quality scorecard | `blog-analyze` | Produce weekly average quality score across all published content |
| SEO checklist audit | `blog-seo-check` | Audit last week's published posts for any missed SEO elements |

### Key Outputs
- Per-post quality scorecards (0-100, 5-category breakdown)
- SEO validation checklists (pass/fail per element)
- Weekly site health report (decay signals, thin content, technical issues)
- Cannibalization map with severity scores and consolidation recommendations
- Factcheck reports with source verification status

### Handoffs
- **Receives from:** Content Writer (new drafts), Media Producer (posts with final assets), Research Analyst (freshness data for factcheck queue)
- **Hands off to:** Content Writer (rewrite flags with score reports), Strategy Lead (decay data and cannibalization flags for editorial planning), AI Search Specialist (posts passing quality gates for citation and schema work)

---

## Agent 6: AI Search Specialist

**Specialty:** AI citation optimization, schema markup, and evidence-led content frameworks

**Skills:** `blog-geo`, `blog-schema`, `blog-flow`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| GEO audit — new posts | `blog-geo` | Run AI citation readiness audit on every post that clears the Quality Editor gate |
| Schema validation | `blog-schema` | Verify JSON-LD on newly published posts (BlogPosting, FAQ, Breadcrumb, Person) |
| FLOW prompt check | `blog-flow` | Apply one FLOW evidence-led prompt to the day's highest-priority content |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| GEO scorecard | `blog-geo` | Run citation readiness audit across top 10 posts and produce 0-100 GEO score report |
| Schema batch | `blog-schema` | Generate or update JSON-LD for posts missing structured data |
| FLOW framework review | `blog-flow` | Run find/optimize/win prompts across recent content to surface citation opportunities |
| AI citation gap analysis | `blog-geo` | Identify which posts lack answer-first formatting or 40-60 word extractable passages |
| FAQ schema generation | `blog-schema` | Add FAQ JSON-LD to posts that have question-format headings but no structured data |

### Key Outputs
- Weekly GEO scorecard (citation readiness by post, 0-100)
- Schema markup files (JSON-LD per post)
- FLOW framework report (find, optimize, win outputs)
- AI citation gap report (posts missing extractable passages)
- FAQ schema library

### Handoffs
- **Receives from:** Quality Editor (posts passing quality gates), Media Producer (posts with embedded video needing VideoObject schema)
- **Hands off to:** Strategy Lead (GEO data and citation opportunities for editorial planning), Content Writer (posts flagged for answer-first formatting fixes), Multilingual Manager (posts with strong GEO scores flagged for international expansion)

---

## Agent 7: Multilingual Manager

**Specialty:** International publishing, translation, cultural adaptation, and hreflang

**Skills:** `blog-multilingual`, `blog-translate`, `blog-localize`, `blog-locale-audit`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Translation queue | `blog-translate` | Translate posts approved for international expansion by Strategy Lead |
| Locale-audit spot check | `blog-locale-audit` | Verify hreflang tags are correct on any posts published or updated in the last 24 hours |
| Freshness parity check | `blog-locale-audit` | Flag translated posts where the source has been updated but the translation has not |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| International post launch | `blog-multilingual` | Run full write + translate + localize + hreflang pipeline for approved posts |
| Cultural adaptation | `blog-localize` | Deep-adapt top posts for DACH, FR, ES, JA, or other target locales |
| Locale audit | `blog-locale-audit` | Full multilingual content QA (completeness, hreflang integrity, parity, freshness) |
| Translation batch | `blog-translate` | Process 2-3 posts through SEO-optimized translation with format preservation |
| Hreflang audit | `blog-locale-audit` | Validate hreflang implementation across all language variants site-wide |

### Key Outputs
- Translated posts (format-preserved: markdown, MDX, frontmatter, JSON-LD)
- Culturally adapted posts per locale
- Hreflang implementation files
- Multilingual QA report (completeness, freshness parity, hreflang errors)
- International publishing calendar

### Handoffs
- **Receives from:** Strategy Lead (posts approved for international expansion), AI Search Specialist (posts with strong GEO scores as priority candidates for translation)
- **Hands off to:** Quality Editor (translated posts for scoring in target language), AI Search Specialist (translated posts needing locale-specific schema), Strategy Lead (international performance data)

---

## Agent 8: Distribution Manager

**Specialty:** Content repurposing and taxonomy management across platforms

**Skills:** `blog-repurpose`, `blog-taxonomy`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Repurpose queue | `blog-repurpose` | Convert the day's published post into 2-3 platform-specific formats (social, email, Reddit) |
| Tag/category assignment | `blog-taxonomy` | Apply correct taxonomy to newly published posts across CMS |
| Distribution calendar | `blog-repurpose` | Schedule repurposed content across channels aligned with editorial calendar |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Full repurpose batch | `blog-repurpose` | Repurpose top-performing evergreen posts into social threads, email sequences, and YouTube scripts |
| Taxonomy audit | `blog-taxonomy` | Review tag and category consistency across all published posts |
| Platform sync | `blog-taxonomy` | Sync taxonomy updates to WordPress, Shopify, Ghost, Strapi, or Sanity as needed |
| Distribution performance review | `blog-repurpose` | Analyze which repurposed formats drive the most return traffic and adjust strategy |
| New tag/category proposal | `blog-taxonomy` | Suggest taxonomy additions based on new content clusters from Strategy Lead |

### Key Outputs
- Repurposed content library (social posts, email copy, YouTube scripts, Reddit posts)
- Taxonomy audit report (tag/category consistency scores)
- Platform sync confirmation (CMS taxonomy updates)
- Distribution performance report (channel-by-channel return traffic)
- Weekly distribution calendar

### Handoffs
- **Receives from:** Content Writer (newly published posts for repurposing), Strategy Lead (cluster topics requiring taxonomy updates)
- **Hands off to:** Strategy Lead (distribution performance data for editorial decisions), Quality Editor (repurposed content for brand consistency check)

---

## Team Communication Flow

```
                    ┌──────────────┐
                    │  Strategy    │
                    │   Lead       │
                    │  (Agent 2)   │
                    └──────┬───────┘
            Briefs & │          ▲ Signals &
           Priorities│          │ Performance
                     ▼          │
        ┌────────────────────────────────────┐
        │                                    │
   ┌────▼──────┐  ┌────────────┐  ┌─────────▼──┐
   │  Content   │  │  Research  │  │Distribution│
   │  Writer    │◄─┤  Analyst   │  │  Manager   │
   │  (Agent 1) │  │  (Agent 3) │  │  (Agent 8) │
   └────┬───────┘  └────┬───────┘  └─────┬──────┘
        │               │                │
        ▼               ▼                │
   ┌──────────┐   ┌──────────┐           │
   │  Media   │   │ Quality  │◄──────────┘
   │ Producer │──►│  Editor  │
   │ (Agent 4)│   │ (Agent 5)│
   └──────────┘   └────┬─────┘
                       │
                       ▼
                ┌──────────────┐
                │  AI Search   │
                │ Specialist   │
                │  (Agent 6)   │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ Multilingual │
                │   Manager    │
                │  (Agent 7)   │
                └──────────────┘

            ORCHESTRATOR: blog/SKILL.md
```

**Daily standup order:** Research Analyst → Strategy Lead → Content Writer → Media Producer → Quality Editor → AI Search Specialist → Distribution Manager → Multilingual Manager

**Weekly sync:** Strategy Lead runs an 8-agent weekly review using outputs from all agents to set editorial priorities. Quality Editor's site health report and Research Analyst's Google performance data are the two primary inputs for setting the following week's priorities.

---

## Content Pipeline (Post Lifecycle)

```
Research Analyst          → research packet + DISCOURSE.md
Strategy Lead             → topic brief + editorial calendar slot
Content Writer            → draft article
Media Producer            → hero image + charts + audio
Quality Editor            → 100-point score + SEO check + factcheck
AI Search Specialist      → GEO audit + JSON-LD schema
Distribution Manager      → repurpose + taxonomy
Multilingual Manager      → translate + localize + hreflang (if approved)
```

Every post moves left to right. A post does not advance to the next agent until the current agent's gate is cleared.
