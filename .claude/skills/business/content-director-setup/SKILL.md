---
name: content-director-setup
description: Bootstrap an autonomous "content director" agent for a specific website — one that owns content strategy and search performance rather than waiting for instructions each session. Produces standing custom instructions, a first full-site audit + voice guide, a persistent git-backed workspace (when scheduling natively, since cloud routines are stateless sandboxes), a recurring-run routine, and a one-screen dashboard — ready to paste into a claude.ai Project (Instructions tab, scheduled tasks) or wire up natively via the `schedule` skill. Checks self-hosted connectors for cloud reachability before promising automation around them. Use this whenever the user wants to "set up an SEO agent", "turn this site into a Claude project", "make this run autonomously every week", "onboard this website for ongoing content/SEO management", or asks for a content director / autonomous site manager for a specific domain.
---

# Content Director Setup

## Why this exists

A one-off audit or blog post is easy for Claude to do well. What's hard is making a site *keep* getting attention every week without the user re-explaining context each time. That requires four things existing together: a persistent identity (who is this agent, what does it own), a baseline (what does the site actually need), a trigger (something that runs it without being asked), and a feedback loop (a way for the user to see what happened without reading logs). Skip any one of these and the "autonomous agent" quietly reverts to a one-time favor.

This skill produces all four, in order, for one specific website. Each step's output feeds the next, so don't skip ahead — the audit needs the instructions' mission statement to know what to prioritize, and the dashboard needs the audit's baseline to know what's new.

**Always use the `AskUserQuestion` tool for every question in this workflow** — never ask in plain prose. This matches how the rest of this project expects Claude to gather requirements, and it keeps a workflow with this many decision points from turning into a wall of text the user has to parse.

## Step 0: Scope the engagement

Before writing anything, use `AskUserQuestion` to establish:

1. **Site name and domain** — what is it, what's the URL.
2. **What the site is for** — one paragraph: what it's about, who reads/uses it, how it makes money (affiliate, leads, SaaS signups, ecommerce, ad revenue, brand-only). This becomes the "WHAT THE SITE IS" paragraph in the instructions.
3. **The mission** — what "winning" looks like: the #1 resource for [topic], the #1 choice for [what they sell/why the site exists], recovering lost traffic, something else. Be specific — vague missions produce vague weekly work.
4. **Autonomy level** — full autonomy with periodic check-ins, or "report what you'd do and wait for approval" for the first couple of weeks. The template defaults to full autonomy; plenty of users want the safer on-ramp instead, and it's a one-line change to flip it back later (see Step 1).
5. **What connectors/tools are actually available** — Google Search Console, GA4, DataForSEO, Apify scrapers, OpenSEO MCP, or none of the above (WebFetch/WebSearch only). Don't assume — ask. The audit prompt in Step 2 should only reference tools that exist, or it produces a prompt Claude can't actually execute later.

Batch these into as few `AskUserQuestion` calls as make sense (the tool supports up to 4 questions at once) rather than asking one at a time.

**If any connector in #5 is self-hosted, check reachability before going further.** A tool running on `localhost` — a local MCP server, a local OpenSEO instance, anything bound to the user's own machine — is invisible to both a claude.ai Project and a Claude Code cloud routine (the `schedule` skill's routines run in Anthropic's cloud sandboxes, same as claude.ai). Neither can reach past `localhost`. Ask explicitly: is this reachable at a public URL, or only from this machine? If it's local-only and the user wants real automation (Step 3/4 below), the connector needs to move somewhere cloud-reachable first (e.g. a Cloudflare Worker, a small VPS) — flag this as a blocker before promising a working recurring run, rather than building a prompt around a tool the automation can never actually call. Don't guess at this — an assumption here silently breaks the whole recurring run weeks later.

## Step 1: Write the standing custom instructions

This is the step that decides whether the user gets an assistant or a manager. Don't hand back the raw template — expand it using what Step 0 surfaced.

Fill in this structure (adapt section content to the answers, don't just mail-merge placeholders):

```
You are the content director for [SITE NAME] at [DOMAIN] — not an
assistant waiting for instructions. You own the content strategy and the
search performance.

THE MISSION
[Mission from Step 0, made concrete and measurable where possible.]

WHAT THE SITE IS
[The paragraph from Step 0: what it's about, who reads it, how it makes money.]

HOW YOU WORK
- Read your memory index at the start of every session, before anything
  else. Know what's done, what's in progress and what's next.
- Verify before you write. Every business, price, opening time or
  factual claim gets checked against a live source before it goes on
  the site. If you can't verify it, soften the claim or cut it.
  Never invent a detail to fill a gap.
- Build and maintain a voice file from the existing writing on the site.
  Match it. Don't write like a brochure.
- Log every change you make to the live site in a changelog file, so I
  can spot-check anything without asking you.
- Ask before doing anything you can't undo.
[If Step 0 chose the cautious on-ramp: replace "Work autonomously" language
throughout with "Report what you'd do and wait for my approval" — see the
note in Step 4.]

WHAT NOT TO DO
- Don't bulk-rewrite content that already ranks well.
- Don't publish anything you haven't fact-checked.
- Don't change URLs of existing pages. Ever.
```

Two lines earn their place more than the rest, and should not be cut even when trimming: **"not an assistant waiting for instructions"** (stops it from asking what to do every session) and **"don't change URLs of existing pages, ever"** (protects search history that can't be recovered once broken).

Where this file lives depends on where the recurring run (Step 4) will actually live — decide that now, even if scheduling itself comes later, because it changes where every subsequent artifact gets saved:

- **Heading toward a claude.ai Project (Path A):** save to a scratch/working-directory file (e.g. `<site-slug>-project-instructions.md`), show it to the user, and tell them explicitly to *paste this into the claude.ai Project's Instructions tab, top right.* This skill produces the text — it can't create or configure a claude.ai Project itself.
- **Heading toward Claude Code native scheduling (Path B):** a scratch file is a dead end — a cloud routine only ever sees files inside its git repo checkout, never this local session's scratchpad. Save straight into the persistent workspace instead (see Step 3, which should run *before* this step in that case) — e.g. `knowledge/notes/custom-instructions.md`. If Step 3 hasn't happened yet, say so and come back to this once the repo exists rather than writing to scratch and forgetting to move it later.

## Step 2: Run (or hand off) the first full audit

Build the audit prompt from what Step 0 said is actually connected. Don't list connectors that don't exist — a prompt referencing GSC when nothing is connected just produces a Claude session that stalls or fabricates data.

Template:

```
Run a complete audit of [DOMAIN].

You have a live connection to the site[, and also:
LIST ONLY THE CONNECTORS STEP 0 CONFIRMED — e.g. Google Search Console,
Google Analytics, DataForSEO, Apify web scrapers]. Use them to get real
data rather than guessing.

I want:

1. What's performing well on the site, and what isn't
2. Any technical or content issues that need tidying up
3. Any pages that need updating — factual errors, businesses that have
   closed, out-of-date information, anything that would embarrass me
4. A forward-thinking SEO strategy that will raise the profile and
   traffic of this site over the next year — built as a 12-month plan
   we can execute week by week

Also read several pages of content from across the site to understand
the voice it's written in, and build a voice style guide we can
reference going forward.

Write your findings, the strategy and the voice guide to memory so you
can pick up from them in future sessions.
```

If the current session already has live access to the site and the confirmed connectors, offer to run this audit directly now rather than only handing over a prompt — that's strictly more useful when it's possible. If it doesn't (no site access from Claude Code, connectors live only in a claude.ai Project), save the prompt to a file and tell the user to run it as the first message in the new Project, after pasting in the Step 1 instructions.

Read back anything a fact-check turns up before letting later automation act on it — the corrections list is where surprises live, and it's cheaper for the user to catch a wrong one now than after it's published.

Save the findings, strategy, and voice guide to the same place Step 1's instructions file landed — scratch file for Path A, or `knowledge/tracking/` + `context/core/` inside the persistent workspace for Path B (see Step 3). A scratch-file audit is still useful to hand to the user directly, but it will not be visible to any future scheduled run.

## Step 3: Set up the persistent workspace (Path B only — skip for claude.ai Projects)

Skip this step entirely if Step 0/1 pointed toward a claude.ai Project — the Project itself is the persistent workspace there, with its own file storage and memory. This step exists only for Claude Code native scheduling, and it has to happen *before* Step 4's routine is created, because the routine depends on it existing.

**Why this is a separate, mandatory step:** a cloud routine created via the `schedule` skill spins up a brand-new, fully isolated sandbox on every single fire. Nothing survives between runs by default — not files, not conversation history, nothing. The standing instructions from Step 1 say "read your memory index at the start of every session" and "update your memory" at the end; that instruction is meaningless unless there's something outside the sandbox to read from and write to. In this system, that something is a **git repository the routine checks out fresh each run** — memory persists because it's committed to the repo, not because the sandbox remembers anything.

What to set up:

1. **A dedicated git repository for this site**, separate from any other project's. Recommended structure (mirrors this project's own `starter-project` conventions, and matches what a working sibling setup — a comparable towing site's own scheduled agent — actually uses in production):
   ```
   knowledge/
     notes/custom-instructions.md   ← Step 1's output goes here, not scratch
     tracking/memory-index.md       ← in-progress / next-up / completed, read+updated every run
     tracking/changelog.md          ← dated log of every change made to the live site
     strategy/12-month-plan-*.md    ← the week-by-week plan from Step 2's audit
   context/
     core/voice-style-guide.md      ← Step 2's voice guide goes here
     core/voice-dna.json            ← optional, structured version of the same
   ```
   Don't invent a different structure per project — a consistent layout is what lets a single skill/routine prompt work across every site the user runs this for.

2. **A dedicated Environment** (in the `schedule` skill's sense — an `environment_id`) pointing at that repo, separate from any other project's environment. This is a real isolation boundary, not just tidiness: any credential configured on an environment (a CMS login, an API key) is available to *every* routine that uses it. One environment per site keeps a bug or bad prompt in one site's routine from being able to touch another site's live content. Ask the user to confirm or create this environment before continuing — check existing environments first (a routine list via `RemoteTrigger` on a sibling project will show its `environment_id`, repo, and structure if one already exists as a template).

3. **Decide the commit pattern now, not later.** The safe default — consistent with Step 1's "ask before doing anything you can't undo" — is: the routine commits to a dated branch (`weekly/YYYY-MM-DD`) and opens a PR describing what changed and why, rather than pushing straight to the main branch. Only relax this to direct-push if the user explicitly wants full autonomy with no review step.

If the user already has a repo/environment for this exact site (check before assuming there isn't one), reuse it rather than creating a duplicate.

## Step 4: Set up the recurring run

Two paths exist depending on where the user actually wants this to live — ask which if it isn't already obvious from Step 0's connector answer (claude.ai connectors implies claude.ai Project; none/WebFetch-only leans toward Claude Code native).

**Path A — claude.ai Project scheduled task.** Give the user this to create *from inside the Project* (so it inherits the folder, instructions, and connectors automatically):

- Name: `[SITE NAME] website management`
- Description: `Manage and grow the [SITE NAME] website`
- Prompt:

```
Execute the [SITE NAME] SEO strategy, based on the information in this
project and in your memory.

Every time you run:

1. Read the project instructions
2. Read your memory to see what was completed last
3. Go and execute the next set of work in the strategy — whether that's
   updating pages, creating new content, running audits, or anything
   else detailed in the ongoing plan

Work autonomously. Execute as much of the work as you can during your
session. Don't bother me unless it's something manual that I have to go
and do myself.

At the end of every session, update your memory with what's been done
and what's next on the agenda.
```

If Step 0 chose the cautious on-ramp, swap the "Work autonomously..." paragraph for: *"Report what you'd do and wait for my approval."* Tell the user to run it that way for a couple of weeks, then switch the line back — they lose nothing but a short delay before full autonomy.

Frequency: weekly, at a time the user is unlikely to be using Claude heavily (Sunday afternoon is a common choice, so the week's work is waiting Monday morning). Flag the two gotchas: **the machine needs to be on** if this is self-hosted rather than claude.ai-hosted, and a sleeping laptop means a skipped week for anything that depends on local state.

**Path B — Claude Code native scheduling.** Confirm Step 3's workspace (repo + environment) exists first — the routine is useless without it. Then invoke the `schedule` skill rather than reimplementing scheduling logic here; it handles the actual `RemoteTrigger` create call. Give it what it needs up front so it doesn't have to re-derive this from scratch:

- The prompt body (adapt the Path A prompt above: point it at the workspace's actual file paths — `knowledge/tracking/memory-index.md`, `knowledge/strategy/*`, `context/core/voice-style-guide.md` — instead of generic "your memory", and specify the branch+PR or direct-push pattern decided in Step 3).
- The `environment_id` from Step 3.
- Which MCP connectors this routine needs attached (`mcp_connections`, each needing a `connector_uuid` — the `schedule` skill can look these up, or find them via the connector's detail panel at claude.ai's Connectors settings if not already listed).
- The cadence: weekly is the default (Sunday afternoon local time is a common choice, so results are ready Monday morning); note that the scheduler's minimum interval is 1 hour and cron expressions run in UTC — let the `schedule` skill handle the timezone conversion and confirm the resulting UTC time back to the user.
- This is a cloud sandbox on Anthropic's infrastructure, not the user's machine — unlike a self-hosted cron job, it does *not* require the user's computer to be on.

**A note on the two-routine split:** a working precedent splits this into two separate routines against the same environment — one that executes the actual weekly strategy work (writes content, runs checks, commits/PRs), and a second, lighter one that only refreshes a status dashboard (Step 5) a couple of hours after the first, so results are ready when the user checks in. This isn't mandatory, but it keeps "did real work" and "reported on real work" as separately debuggable, separately re-runnable pieces — if the dashboard refresh breaks, the actual site work isn't affected, and vice versa.

## Step 5: Build the dashboard (optional)

Ask whether the user wants a standing dashboard — a single artifact that reports what the agent did, so an autonomous agent working silently doesn't feel unnerving. If yes, ask what they specifically want to see (default list below is a starting point, not a requirement):

- What needs their attention, right at the top
- Top-level numbers
- Performance data and top queries
- Traffic quality
- Top pages
- New pages published this period
- What's been updated
- What's coming up next
- Any housekeeping that needs them specifically
- Anything important, flagged

If the current session can publish artifacts, build it now as a live artifact (load the `artifact-design` skill first, as with any artifact) using whatever real data is available from Step 2's audit as the baseline. Otherwise, hand over the build prompt and a refresh prompt for the user to run in their Project, with the same Path A/B scheduling choice as Step 4 — the refresh should run a few hours after the working task, so results are ready when the user next opens the dashboard (Monday morning if the working task ran Sunday). For Path B specifically, this is the second routine from Step 4's two-routine split — same environment, offset cadence, and it should update the *same* artifact in place (pass the existing artifact's `url` to the `Artifact` tool) rather than publishing a new one every week.

## Output summary

When all steps the user wants are done, summarize in one place: the file paths of anything saved, whether the audit ran now or was handed off, the scheduling path chosen and its cadence, and whether a dashboard was built or handed off. This is what tells the user the loop is actually closed, not just talked about.
