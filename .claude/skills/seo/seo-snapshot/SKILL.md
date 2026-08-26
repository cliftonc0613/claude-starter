---
name: seo-snapshot
description: Run a multi-agent competitive standing snapshot for a local service business — competitive landscape, own-domain backlink audit, top-competitor backlink audit, GBP content readiness, and schema health — synthesized into one published client-facing artifact. Use when the user says "run a snapshot", "competitive snapshot", "run the agent team", "check where we stand against [competitor]", or wants a fresh client-ready update spanning backlinks, GBP, and competitive position in one pass.
---

# SEO Snapshot — Agent Team

## Goal

Answer, in one pass, the question a client actually asks: **"Where do we stand, and what's actually holding us back?"** — by running five focused agents in parallel/staged, then rolling their findings into a single plain-language artifact the client can be sent.

This is a **breadth** workflow, not a deep audit. If the user wants a full technical/content SEO audit, use `seo-audit` or `seo` instead — this skill stays scoped to competitive position + backlinks + GBP + schema.

## Required inputs

Gather these before launching anything — ask the user only for what can't be found:

- Client domain (check `context/core/business-profile.json` or the project's OpenSEO project first)
- OpenSEO `projectId` (check project memory / `context/core/business-profile.json` / prior tracking notes before asking)
- Known top local/organic competitor domain — optional. If not known, or the last competitive-landscape report is more than ~90 days old, run Phase 1 to (re)establish it.
- Path to the client's business profile (`context/core/business-profile.json`), voice DNA (`context/core/voice-dna.json`), and tracking notes (`knowledge/tracking/<month>/*.md`) — these brief the agents and are where results get logged.
- Any standing client constraints (e.g. no pricing published, no text-based review requests) — check project memory and business-profile.json before drafting anything; pass these explicitly into every agent prompt, don't assume the agent will find them unprompted.

## Team composition

Five agents, each briefed with full context (domain, project ID, client constraints, file paths) since each starts fresh with no memory of this conversation:

| # | Agent | Skill it loads | Writes to | Depends on |
|---|-------|-----------------|-----------|------------|
| 1 | Competitive landscape | `competitive-landscape` | `seo-workspace/competitors/competitive-landscape-<date>.md` | Nothing — run first if competitor is unknown/stale |
| 2 | Own-domain backlink audit | `seo-backlinks` | `seo-workspace/backlinks/backlink-audit-<date>.md` | Nothing |
| 3 | Competitor backlink audit | `seo-backlinks` | `seo-workspace/backlinks/<competitor>-backlink-audit-<date>.md` | Competitor domain (from agent 1, or user-supplied) |
| 4 | GBP content plan | `seo-local` | `seo-workspace/gbp/gbp-content-plan-<date>.md` | Nothing, but should read agent 1's output if available for positioning context |
| 5 | Schema health check | `seo-schema` | `seo-workspace/schema/schema-audit-<date>.md` | Nothing, but should flag anything the GBP plan's FAQ content (agent 4) needs to coordinate with |

## Orchestration

**Phase 1 — competitor identification (conditional).** If the competitor domain is already known and recent, skip this phase and go straight to Phase 2 using that domain. Otherwise, launch agent 1 alone via the `Agent` tool and wait for it to finish — every other agent that touches "the competitor" needs its output.

**Phase 2 — parallel fan-out.** Launch agents 2, 3, 4, and 5 together, in a single message with multiple `Agent` tool calls, so they run concurrently. Each agent prompt must include:
- The specific skill to load via the `Skill` tool, by name, and an instruction to follow it before ad-hoc analysis
- The exact file path to write its report to
- The exact tracking-notes file path and its existing `TELL CLIENT` convention (dated entry, technical note, then a `→ Client-facing:` plain-language line) — instruct the agent to read the file first and match the format
- Any client constraints (pricing, review-request method, brand voice) that must not be violated
- What the other agents are doing, so it doesn't duplicate work (e.g. the GBP agent shouldn't re-run a competitive analysis; the schema agent shouldn't rewrite GBP FAQ copy, just flag the coordination point)

Do not use the heavier `Workflow` tool for this unless the user has explicitly opted into multi-agent orchestration in their own words or ultracode is on — five `Agent` tool calls in one message already run concurrently and is the right scope here.

**Phase 3 — synthesis artifact.** Once all Phase 2 agents (and Phase 1, if run) have reported back, do this yourself in the main conversation, not via another subagent:
1. Read each report file in full.
2. Load the `artifact-design` skill before writing any HTML.
3. Build one client-facing summary: plain language, no SEO jargon left unexplained, organized around findings rather than around which agent produced them. Pull in the client's logo and website link from `seo-workspace/assets/` if present (embed images as base64 data URIs — Artifacts can't load external images).
4. Explicitly separate what's the client's action (e.g. verifying a GBP listing) from what the agency is already executing.
5. Publish via the `Artifact` tool. Artifacts are private by default — don't imply it's been sent to the client until the user shares it.
6. Log one final tracking-notes entry noting the snapshot was run, linking the published artifact URL, with its own `TELL CLIENT` line.

## Guardrails

- Never invent client-facing facts, mechanisms, or confirmations an agent didn't actually establish (e.g. a review-generation method the client hasn't specified) — flag as open instead.
- Enforce every standing client constraint (pricing, review method, voice) in every agent prompt, not just the synthesis step — an agent that doesn't get the constraint won't know to honor it.
- Prefer this project's own directory-scoped skills (`.claude/skills/seo/*`) over generic top-level equivalents (e.g. `market-competitors`) — they're tuned to the OpenSEO MCP tools and local-service business model already in use here.
- Don't commit anything to git as part of this skill.
- If a Phase 2 agent depends on Phase 1's output (the competitor backlink audit needs a domain), don't launch it until Phase 1 has actually returned — don't guess the competitor.
- If any report comes back materially different from what a prior snapshot found (e.g. competitor now has a live, strong GBP), say so plainly in the synthesis rather than smoothing it into the old narrative.
