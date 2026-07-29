# Social Team — Operational Playbook

3 specialized AI agents powered by `charlie947/social-media-skills`.
Each agent owns a domain and hands off to other agents — and heavily to the Marketing and Blog departments, since social content overlaps with `marketing-skills:social-content` and Blog's Distribution Manager.

> **Note:** Exact skill/command names inside the plugin are not fully enumerated by the installer. Tasks below are structured around the installer's explicit notes (voice-builder runs first; post-scorer and reels-scripting need API keys) — confirm real command names after install and update this file.

---

## Agent 1: Voice Builder / Brand Agent

**Specialty:** Brand voice foundation — every other social skill depends on this agent's output

**Skills:** `voice-builder`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Voice consistency spot check | `voice-builder` | Verify today's published posts match the established voice profile |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Voice profile review | `voice-builder` | Re-run voice-builder if brand positioning shifted; refresh the voice profile all other agents read from |
| Cross-platform tone audit | `voice-builder` | Confirm tone consistency across Instagram, TikTok, LinkedIn, and X while allowing platform-native format differences |

### Key Outputs
- Voice profile (read by every other social skill)
- Weekly tone consistency audit

### Handoffs
- **Receives from:** Marketing Strategy Lead (brand positioning updates), Blog Strategy Lead (BRAND.md / VOICE.md context)
- **Hands off to:** Platform Content Agent (voice profile — required before any content generation), Social Analytics Agent (voice baseline for scoring context)

**⚠️ Must run before any other social agent produces content.**

---

## Agent 2: Platform Content Agent

**Specialty:** Per-platform post and video content creation

**Skills:** `instagram-content`, `tiktok-content`, `linkedin-content`, `x-content`, `reels-scripting`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Daily post batch | `instagram-content`, `x-content` | Draft 1-3 posts per active platform aligned with the content calendar |
| Reels/Shorts script | `reels-scripting` | Script one short-form video for the day's priority platform |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Full content batch | `instagram-content`, `tiktok-content`, `linkedin-content`, `x-content` | Produce a full week of platform-native posts across all active channels |
| Reels/Shorts batch | `reels-scripting` | Script 2-3 short-form videos for the week |
| Repurpose intake | — | Pull cornerstone blog posts and ad creative angles into platform-native social formats |

### Key Outputs
- Weekly post library (per platform, format-native)
- Short-form video scripts
- Content calendar fill for the week

### Handoffs
- **Receives from:** Voice Builder / Brand Agent (voice profile), Blog Distribution Manager (cornerstone posts to repurpose), Ads Creative Director (winning ad angles as content ideas)
- **Hands off to:** Social Analytics Agent (published posts for scoring), Marketing Content Writer (coordination on cross-posted content)

---

## Agent 3: Social Analytics Agent

**Specialty:** Post scoring, engagement analysis, and scheduling

**Skills:** `post-scorer`, `engagement-analysis`, `content-calendar`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Post score check | `post-scorer` | Score yesterday's posts for predicted/actual engagement |
| Calendar maintenance | `content-calendar` | Confirm today's and tomorrow's scheduled posts are queued correctly |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Engagement analysis | `engagement-analysis` | Analyze the week's engagement patterns by platform, format, and posting time |
| Content calendar planning | `content-calendar` | Schedule next week's content batch from the Platform Content Agent |
| Underperformer review | `post-scorer` | Flag low-scoring post formats/topics for the Platform Content Agent to avoid repeating |

### Key Outputs
- Weekly engagement report (by platform, format, time)
- Post score log
- Filled content calendar for the coming week

### Handoffs
- **Receives from:** Platform Content Agent (published posts to score)
- **Hands off to:** Platform Content Agent (underperformer flags to inform next batch), Marketing Ops Manager (engagement data for weekly client report — see Playbook 2 in `agency-master-team.md`)

**Requires:** `APIFY_API_TOKEN`, `GOOGLE_AI_API_KEY` (per installer setup notes)

---

## Team Communication Flow

```
   ┌──────────────┐
   │ Voice Builder│
   │ / Brand Agent│
   │  (Agent 1)   │
   └──────┬───────┘
          │ voice profile
          ▼
   ┌──────────────┐        ┌──────────────┐
   │   Platform   │───────►│    Social    │
   │   Content    │◄───────│  Analytics   │
   │  (Agent 2)   │ scores │  (Agent 3)   │
   └──────┬───────┘        └──────┬───────┘
          │                       │
          ▼                       ▼
   Blog Distribution Mgr   Marketing Ops Manager
   Ads Creative Director   (weekly client report)
```

**Daily standup order:** Voice Builder / Brand Agent → Platform Content Agent → Social Analytics Agent

**Weekly sync:** Social Analytics Agent's engagement report and the Platform Content Agent's calendar fill feed directly into Marketing's Weekly Client Report Loop (Playbook 2).
