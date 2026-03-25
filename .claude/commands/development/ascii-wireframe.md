---
description: Generate detailed ASCII wireframes in the terminal for any UI — web pages, mobile screens, dashboards, components, multi-screen flows, email templates, and more.
---

# ASCII Wireframe Generator

Generate a detailed ASCII/Unicode wireframe based on the user's request. Use the `ascii-wireframe` skill from `.claude/skills/development/ascii-wireframe/SKILL.md` for the full component library, workflow, and quality standards.

## Usage

- `/ascii-wireframe` — Interactive mode: asks what to wireframe
- `/ascii-wireframe SaaS pricing page with feature comparison table` — Direct mode: generates immediately
- `/ascii-wireframe mobile checkout flow 3 screens` — Generates multi-screen flow

## What It Does

1. **Understands** your request (asks 1-2 clarifying questions if needed)
2. **Generates** a high-detail wireframe using Unicode box-drawing characters
3. **Annotates** with dimensions, grid info, and section labels
4. **Iterates** until you're satisfied — add, remove, or adjust any section

## Arguments

`$ARGUMENTS` is the optional wireframe description. If provided, skip the interview and generate directly. If empty, ask what to wireframe.

## Instructions

1. Read the full skill file at `.claude/skills/development/ascii-wireframe/SKILL.md`
2. Follow the Component Symbol Library for consistent element rendering
3. Follow the Interactive Workflow (Phase 1 → 2 → 3)
4. If `$ARGUMENTS` is not empty, treat it as the wireframe description and skip to Phase 2
5. Always use AskUserQuestion for any questions or iteration prompts
6. Print wireframes inside markdown code blocks for clean terminal rendering
