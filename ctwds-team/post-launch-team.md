# Post-Launch Team — Operational Playbook

Run after every local business website goes live.
Covers analytics, conversion tracking, GSC, schema, crawlability, OG images, and citations.
Powered by the `/post-launch` skill.

---

## How to Run

```
/post-launch
```

Run this immediately after a site goes live. The skill will:
1. Read the codebase to discover what's already in place
2. Generate a project-specific `tasks/post-launch-checklist.md`
3. Execute all code-level fixes automatically
4. Guide you through the GTM/GA4 UI steps
5. Note what's deferred to the client or a separate service

---

## What Gets Automated (Code Changes)

| Item | What It Does |
|------|-------------|
| `robots.txt` | Creates or fixes — explicitly allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended |
| `llms.txt` | Creates business summary for AI crawlers (ChatGPT, Perplexity, Claude) |
| Sitemap | Ensures dynamic generation (not static) with thank-you/tag pages filtered out |
| Schema — LocalBusiness | Confirms geo, openingHours, areaServed cities, priceRange, hasOfferCatalog on every page |
| Schema — Service | Adds Service schema to each service page |
| Schema — BlogPosting | Adds BlogPosting schema to each blog post |
| Schema — BreadcrumbList | Adds BreadcrumbList to every page type |
| OG images | Wires blog heroImage as OG; wires service images for service pages |
| Form tracking | Adds dataLayer push on thank-you page for GTM generate_lead event |

---

## What Requires GTM UI (Guided Steps)

| Step | Notes |
|------|-------|
| GTM container creation | Create account + container at tagmanager.google.com |
| GA4 tag | Measurement ID → All Pages trigger |
| CTA click trigger | Click - All Elements, `{{Click Classes}}` contains `gtm-cta` |
| Phone click trigger | Click - Just Links, `{{Click URL}}` contains `tel:` |
| Form submission trigger | Custom Event, event name: `generate_lead` |
| Publish workspace | Must publish before testing — common miss |

---

## What's Deferred to Client or Separate Service

| Item | Notes |
|------|-------|
| Google Business Profile | Setup + video verification — offer as add-on service |
| Citations | Bing Places, Apple Maps, Yelp, Angi, BBB, Nextdoor — separate service |
| Business data placeholders | Email, owner name, year established — client must provide |
| Custom city OG images | Needs real job photos from client |

---

## Critical Rules

- **Never add FAQPage schema** — Google restricted it to gov/healthcare only (Aug 2023)
- **NAP must match exactly** across site, schema, GBP, and all citations
- **AJAX form tracking:** use `dataLayer.push` on thank-you page, NOT GTM Form Submission trigger
- **Always remind:** publish GTM workspace before testing — events won't fire otherwise
- **Matrix pages:** cap at ~24 service × location pages to maintain content quality

---

## Skills Used

| Skill | When |
|-------|------|
| `/post-launch` | Core orchestrator — run first |
| `/seo-schema` | After post-launch for deep schema validation |
| `/seo-sitemap` | Validate sitemap coverage |
| `/seo-technical` | After GSC is live — full technical audit |
| `/marketing-skills:analytics-tracking` | After GTM is live — verify events |
| `/seo-content` | Before launching matrix pages |
| `/seo-geo` | Phase 3 — optimize for AI Overviews |
| `/seo-audit` | End of Phase 2 — full parallel audit |
