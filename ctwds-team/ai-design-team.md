# Design Team — Operational Playbook

3 specialized AI agents powered by `ui-ux-pro-max`, `impeccable`, `taste` (`design-taste-frontend`), and `transitions.dev`.
Each agent owns a domain and hands off to the Marketing department's Web Developer agent (`ai-marketing-team.md` Agent 8), which implements what this team designs.

Impeccable and Taste both install and both do the same job — polishing and steering frontend design — so they overlap. Per the installer's own note: try both, then drop whichever you don't reach for; neither uninstall damages project files. Until that call is made, the UI/UX Builder and Design Auditor agents below list both as options for the same task rather than assuming one is primary.

---

## Agent 1: UI/UX Builder

**Specialty:** Interface structure, layout, and design system generation

**Skills:** `ui-ux-pro-max:ui-ux-pro-max`, `impeccable:arrange`, `impeccable:frontend-design` (or `design-taste-frontend` — pick one, they overlap), `impeccable:normalize`, `impeccable:extract`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Component build | `ui-ux-pro-max:ui-ux-pro-max` | Build or update one UI component/page per active request |
| Layout pass | `impeccable:arrange` | Arrange/compose layout for any in-progress page |
| Pattern normalization | `impeccable:normalize` | Fix spacing/sizing inconsistencies flagged the previous day |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Frontend build batch | `impeccable:frontend-design` | Produce distinctive, non-generic frontend interfaces for the week's page/component requests |
| Design token extraction | `impeccable:extract` | Extract reusable tokens/patterns from newly built pages for the design system library |
| Full normalization pass | `impeccable:normalize` | Site-wide consistency pass across recently shipped pages |

### Key Outputs
- Built UI components and pages
- Design system token library
- Normalization/consistency report

### Handoffs
- **Receives from:** Marketing Strategy Lead (design briefs, feature priorities), Blog Media Producer (visual style guidelines from BRAND.md)
- **Hands off to:** Design Auditor (built pages for quality review), Marketing Web Developer (specs for implementation — see `ai-marketing-team.md` Agent 8)

---

## Agent 2: Design Auditor

**Specialty:** Quality review, anti-AI-slop detection, and pre-ship polish

**Skills:** `impeccable:audit`, `impeccable:critique`, `impeccable:polish` (or `design-taste-frontend` — pick one, they overlap), `impeccable:harden`, `impeccable:clarify`, `impeccable:distill`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Slop detector pass | `impeccable:audit` | Run the generic-pattern detector on anything shipped in the last 24 hours |
| Clarity check | `impeccable:clarify` | Review one in-progress design for confusing flows or unclear hierarchy |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Full design critique | `impeccable:critique` | Structured critique of the week's shipped pages/components |
| Pre-ship polish pass | `impeccable:polish` | Final alignment/spacing/consistency pass before anything goes to production |
| Hardening pass | `impeccable:harden` | Check edge cases — empty states, overflow, error states, responsive breakpoints |
| Simplification review | `impeccable:distill` | Identify designs that can be reduced to their essentials without losing function |

### Key Outputs
- Weekly audit report (generic-pattern flags, per this repo's `frontend_aesthetics` CLAUDE.md rules)
- Pre-ship polish checklist (pass/fail per page)
- Hardening report (edge cases covered)

### Handoffs
- **Receives from:** UI/UX Builder (pages ready for review), Motion & Delight Specialist (animated components ready for critique)
- **Hands off to:** UI/UX Builder (fixes required before ship), Marketing Web Developer (final sign-off for implementation), QA (`/qa-personas` — persona-based validation post-ship)

---

## Agent 3: Motion & Delight Specialist

**Specialty:** Animation, micro-interactions, and page/component transitions

**Skills:** `impeccable:animate`, `impeccable:delight`, `impeccable:overdrive`, `transitions.dev`, `impeccable:colorize`, `impeccable:typeset`, `impeccable:bolder`, `impeccable:quieter`

### Daily Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Micro-interaction pass | `impeccable:delight` | Add one moment of delight to an in-progress component |
| Color/type spot check | `impeccable:colorize`, `impeccable:typeset` | Verify color and typography choices avoid clichéd/generic defaults per CLAUDE.md aesthetics rules |

### Weekly Tasks
| Task | Skill | Description |
|------|-------|-------------|
| Page transition build | `transitions.dev` | Implement page/component transitions for newly shipped pages |
| Animation batch | `impeccable:animate` | Build out staggered-reveal or high-impact page-load animations |
| Tone calibration | `impeccable:bolder` / `impeccable:quieter` | Adjust visual intensity per project context — bold statement vs. restrained minimalism |
| Statement-moment review | `impeccable:overdrive` | Identify one high-impact moment per project worth a stronger visual treatment |

### Key Outputs
- Animation and transition implementations
- Color/typography system decisions
- Tone calibration notes (bold vs. quiet, per project)

### Handoffs
- **Receives from:** UI/UX Builder (built components needing motion), Design Auditor (approved designs ready for motion pass)
- **Hands off to:** Design Auditor (animated components for final critique), Marketing Web Developer (motion specs for implementation)

---

## Team Communication Flow

```
   ┌──────────────┐
   │   UI/UX      │
   │   Builder    │
   │  (Agent 1)   │
   └──────┬───────┘
          │ built pages
          ▼
   ┌──────────────┐        ┌──────────────┐
   │    Design    │◄──────►│   Motion &   │
   │   Auditor    │        │   Delight    │
   │  (Agent 2)   │        │  (Agent 3)   │
   └──────┬───────┘        └──────────────┘
          │ approved specs
          ▼
   Marketing Web Developer (Agent 8, ai-marketing-team.md)
          │
          ▼
   QA: /qa-personas (post-ship validation)
```

**Daily standup order:** UI/UX Builder → Design Auditor → Motion & Delight Specialist

**Weekly sync:** Design Auditor's audit report and polish checklist gate what ships to Marketing's Web Developer for that week's build.
