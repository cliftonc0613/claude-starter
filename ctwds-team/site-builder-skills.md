# Site Builder Skills Reference

2 skills from the `astro-business-builder` Claude Code plugin — a Storybrand-driven Astro 5 site generator for local service businesses, built and maintained by CT Web Design Shop.

**Source:** `cliftonc0613/astro-business-builder` (installed separately from `install-claude-company-os.sh` — see Install below)

**Placement:** This lives under `dev` tooling in `agency-master-team.md`, alongside Superpowers/Context7/Claude-Mem/97-dev — it does not have its own department or `ai-*-team.md` playbook. It's still listed here as a standalone reference because, unlike the other `dev` tools, it's invoked directly by name for a concrete task (scaffolding or extending a client site) rather than running quietly in the background.

---

## 1. Site Scaffolding
- `build-business-site` — One-shot scaffold of a complete Astro 5 static site in an empty project directory. Runs a Storybrand-driven discovery interview (Character, Problem, Guide, Plan, Success, Stakes), gathers services/areas, brand colors, fonts, and deploy target, then generates the full site: 12-section Storybrand homepage, service/area/blog/quote/faq/gallery page set, custom CSS design system, Schema.org markup on every page. Supports a non-interactive `brief.yaml` mode for scripted/batch builds.

## 2. Page Extension
- `add-business-page` — Adds a new page to a site this generator already built: new service, new service area, new blog post, custom SEO landing page, or an edit to an existing page. Reads the site's existing data files first so brand voice, design tokens, and conventions stay locked and consistent.

---

## What you get out of the box (per site)

- **Homepage:** 12-section Storybrand template (Hero, Social Proof Bar, Problem, Guide Introduction, The Plan, Services, Success Vision, Failure/Stakes, Warranty + Pricing Anchor, Social Proof Bridge, Local/Service Areas, Final CTA)
- **Page set:** index, about, contact, faq, gallery, get-quote, privacy-policy, 404, services/{index,[slug]}, service-areas/{index,[slug]}, blog/{index,[...page],[slug],category/[slug],tag/[slug]}, plus service × area combo pages
- **Design system:** custom CSS layer (not a Tailwind-default look), two-color brand palette (primary 50-950, accent 50-900), WCAG 2.1 AA contrast verification, Google or Adobe font pairing
- **Data files:** `business.ts`, `serviceAreas.ts`, `serviceTypes.ts`, `seoContent.ts`, `storybrand.ts`, `brandVoice.ts`
- **Deploy targets:** static, Netlify, or Cloudflare Pages
- **Optional:** GitHub repo creation + initial push via `gh` CLI, 3-post blog seed

## Hard rules (both skills)

- Never use em dashes anywhere, in any file
- Never invent testimonials, reviews, or client names — placeholder structure only
- Brand colors/fonts/design system are locked after the initial build — `add-business-page` never changes them
- Always run `npm run build` and resolve every error before declaring done
- Ask before destructive actions (project creation, `npm install`, overwrites, repo creation)
- Pre-commit/pre-push secret scan before any git operation; never force-push or amend

## Install

```bash
claude plugin marketplace add cliftonc0613/astro-business-builder
claude plugin install astro-business-builder@astro-business-builder
```

Not part of the `work/marketing/social/dev/design` groups in `install-claude-company-os.sh` — install separately, once per machine.

## Related Existing Tools

This repo already has adjacent site-build coverage worth cross-referencing instead of duplicating:
- `build-local-site` skill
- `astro-business-builder:build-business-site`, `astro-business-builder:add-business-page` (same plugin, listed for skill-name lookup)
- `development:new-spec-site`, `development:wordpress-starter` skills — for non-Astro / non-Storybrand builds
- Marketing Department's Web Developer agent (`ai-marketing-team.md` Agent 8) — implements pages generally; this plugin is the specialized fast-path for local-service-business Astro builds specifically
