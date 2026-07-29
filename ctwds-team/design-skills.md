# Design Skills Reference

4 sources from the `design` group in `install-claude-company-os.sh`: `ui-ux-pro-max`, `impeccable`, `taste` (`design-taste-frontend`), `transitions.dev`.

Impeccable and Taste both install and both target the same job — polishing and steering frontend design — so they overlap. The installer's own note: try both, then drop whichever you don't reach for; neither uninstall damages project files. Until you've made that call, treat them as two competing options for the same agent role rather than two agents.

---

## 1. UI/UX Foundation
- `ui-ux-pro-max:ui-ux-pro-max` — Full UI/UX design system generation and component work

## 2. Impeccable — Structure & Layout
- `impeccable:arrange` — Layout and composition
- `impeccable:frontend-design` — Distinctive, production-grade frontend interfaces; avoids generic AI aesthetics
- `impeccable:normalize` — Normalize inconsistent spacing/sizing/patterns
- `impeccable:extract` — Extract design tokens/patterns from existing work

## 3. Impeccable — Quality & Review
- `impeccable:audit` — Detector pass — flags generic/AI-slop patterns
- `impeccable:critique` — Structured design critique
- `impeccable:polish` — Final quality pass: alignment, spacing, consistency before shipping
- `impeccable:harden` — Production-hardening pass (edge cases, robustness of the UI)
- `impeccable:clarify` — Improve clarity of a design or flow
- `impeccable:distill` — Simplify/reduce a design to its essentials

## 4. Impeccable — Style & Tone
- `impeccable:colorize` — Color system work
- `impeccable:typeset` — Typography system work
- `impeccable:bolder` — Push a design toward a stronger, more confident visual statement
- `impeccable:quieter` — Pull a design back toward restraint/minimalism
- `impeccable:adapt` — Adapt an existing design system to a new context

## 5. Impeccable — Motion & Delight
- `impeccable:animate` — Motion and animation design
- `impeccable:delight` — Micro-interactions and moments of surprise
- `impeccable:overdrive` — High-impact, statement motion/visual treatment

## 6. Impeccable — Performance & Onboarding
- `impeccable:optimize` — Performance optimization of the implemented design
- `impeccable:onboard` — Onboarding flow design
- `impeccable:teach-impeccable` — Teach the Impeccable design system approach to a team/project

## 7. Taste — Alternative Frontend Design Skill
- `design-taste-frontend` — Frontend design steering and polish (`Leonxlnx/taste-skill`). Overlaps `impeccable:frontend-design`/`impeccable:polish` — same job, competing approach.

## 8. Motion Library
- `transitions.dev` — Page and component transitions (`Jakubantalik/transitions.dev`)

---

## Related Existing Tools

This repo already has adjacent design coverage worth cross-referencing instead of duplicating:
- `page-layout` skill
- `stitch-design`, `stitch-loop` skills (Google Stitch UI generation)
- `taste-design` skill — separate from `design-taste-frontend` above; a Semantic Design System skill for Google Stitch. Confirm which one is meant before invoking — names are easy to confuse.
- `shadcn-ui`, `vercel:shadcn` skills — component library implementation
- `dataviz` skill — chart/dashboard-specific design system
