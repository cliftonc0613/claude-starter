---
name: ascii-wireframe
description: Use when the user asks to wireframe, mockup, sketch, diagram, or draw any UI layout. Generates detailed ASCII/Unicode wireframes printed directly to the terminal for web pages, mobile screens, dashboards, components, multi-screen flows, email templates, and any other interface.
---

# ASCII Wireframe Generator

Generate detailed, high-fidelity ASCII wireframes using Unicode box-drawing characters. Output prints directly to the terminal — no files, fully copy-pasteable.

## When to Use

- User says "wireframe", "mockup", "sketch", "layout", "draw", "diagram" + any UI
- User asks to visualize a page, screen, component, or flow
- User wants rapid layout prototyping before coding

**Do NOT use for:** Code generation, Figma exports, flowcharts that aren't UI

---

## Component Symbol Library

Use these representations consistently across all wireframes.

### Form Elements

| Element | Symbol |
|---------|--------|
| Button (primary) | `[ Button Text ]` |
| Button (secondary) | `( Button Text )` |
| Button (icon) | `[+]` `[✕]` `[⚙]` |
| Text input | `[________________]` |
| Input with label | `Label: [________________]` |
| Input with placeholder | `[  placeholder text   ]` |
| Textarea | Multi-line box with `│` sides, 3+ rows tall |
| Checkbox checked | `[x] Label` |
| Checkbox unchecked | `[ ] Label` |
| Radio selected | `(●) Label` |
| Radio unselected | `( ) Label` |
| Dropdown / select | `[  Option Text      ▾]` |
| Toggle ON | `[●━━━] ON` |
| Toggle OFF | `[━━━●] OFF` |
| Search input | `[🔍 Search...          ]` |
| Password input | `[  ••••••••           ]` |
| Slider | `○━━━━━●━━━━━━━ 67%` |
| File upload | `[📎 Choose file... ]` |
| Date picker | `[📅 03/25/2026      ]` |

### Media & Placeholders

| Element | Symbol |
|---------|--------|
| Image (small) | Box filled with `╱╲╱╲` crosshatch |
| Image (large) | Box with `[ 800 x 400 ]` centered |
| Avatar | `(👤)` or small crosshatch circle |
| Video | Box with `▶ Play` centered |
| Logo | `◆ LOGO` or `[LOGO]` |
| Map | Box with `📍 Map` centered |
| Icon | Single emoji or `[ico]` |
| Illustration | Box labeled `~ illustration ~` |

### Data Display

| Element | Symbol |
|---------|--------|
| Progress bar | `[████████░░░░] 67%` |
| Star rating | `★★★★☆ 4.0` |
| Badge / tag | `〔 Tag 〕` |
| Status pill | `⟨ Active ⟩` |
| Divider (horizontal) | `────────────────────` |
| Divider (vertical) | `│` |
| Breadcrumb | `Home › Products › Detail` |
| Pagination | `‹ 1 2 [3] 4 5 ›` |
| Tab (active) | `┌─ Active ─┐` with content below |
| Tab (inactive) | `  Inactive  ` underlined |
| Stepper | `(●1)━━━(2)━━━(3)━━━(4)` |
| Tooltip | Small box with `▼` or `▲` pointer |
| Notification dot | `🔔•` |
| Sparkline | `▁▂▃▅▇▅▃▂▁` |
| KPI metric | Large number + label + trend arrow |

### Charts

| Element | Symbol |
|---------|--------|
| Bar chart (vertical) | `█` blocks of varying height with axis |
| Bar chart (horizontal) | `████████` bars with labels |
| Line chart | Connected `╱` `╲` `─` segments |
| Pie / donut | Labeled percentage segments |
| Area under line | Filled with `░` below line |
| Sparkline (inline) | `▁▂▃▅▇▅▃▂▁` |

### Navigation

| Element | Symbol |
|---------|--------|
| Navbar | Full-width box: logo left, links center, actions right |
| Sidebar | Vertical box, stacked items, active marked `▸` |
| Hamburger | `☰` |
| Close | `✕` |
| Back | `← Back` |
| Breadcrumbs | `Home › Section › Page` |
| Bottom tab bar | `  🏠   🔍   ➕   💬   👤  ` |

### Layout Chrome

| Element | Symbol |
|---------|--------|
| Card / box | `┌─────┐` `│     │` `└─────┘` |
| Card with header | `┌─ Title ─────┐` with `├──────────────┤` separator |
| Modal | Centered box with `✕` top-right |
| Toast | Small box bottom-right area |
| Accordion closed | `▸ Section Title ──────────────` |
| Accordion open | `▾ Section Title ──────────────` + content |
| Dropdown menu | Box below trigger with `│` items |
| Skeleton loader | `░░░░░░░░░░░░` blocks |

### Device Frames

| Device | Frame |
|--------|-------|
| Mobile (iPhone) | `╭──────────────────╮` with `⌐▬▬⌐` notch, rounded corners |
| Mobile (Android) | `╭──────────────────╮` no notch |
| Tablet | Wider rounded box, landscape or portrait |
| Browser window | `┌─ ○ ○ ○ ──────────────────────┐` with address bar |
| Desktop app | `┌─ □ ─ ✕ ─────────────────────┐` |

### Flow Connectors (for multi-screen)

| Connector | Symbol |
|-----------|--------|
| Right arrow | `──────▶` |
| Down arrow | `│` repeated + `▼` |
| Branch (conditional) | `──┬──▶ Yes` / `└──▶ No` |
| Loop back | `◄──────` |
| Step label | `(Step 1)` above screen |

---

## Layout Annotations

Add annotations as comment lines using `//` syntax:

```
// w:1200px  h:auto
// grid: 3-col, gap:24px
// p:24px  mt:32px
// @desktop (1200px+)
// @tablet (768px)
// @mobile (375px)
// [HERO SECTION]
// flex-row, justify:space-between
```

Place annotations:
- **Above** a section for section labels: `// [HERO SECTION]`
- **Below** a section for dimensions: `// w:100%, h:400px`
- **Right-aligned** for inline notes when space allows

---

## Workflow

### Phase 1: Understand

If the user provided a description with the command, skip to Phase 2.

Otherwise, use AskUserQuestion:
- "What would you like me to wireframe?" with options: Landing page, Dashboard, Mobile screen, Component, Multi-screen flow, Other
- Ask 1-2 follow-up questions max (key sections, specific elements, target device)
- Do NOT over-interview. Get enough to start, then iterate.

### Phase 2: Generate

Print the wireframe directly to the terminal. Follow these rules:

1. Start with a section label comment: `// === [WIREFRAME NAME] @device (width) ===`
2. Use the component symbol library consistently
3. Include realistic placeholder content ("Jane Cooper", "$12,450", "3 items")
4. Add layout annotations for major sections
5. Add a **Component Legend** at the bottom if the wireframe has 5+ unique element types
6. Target 80-100 chars wide; never exceed 120 chars
7. Wrap the wireframe in a markdown code block for clean terminal rendering

### Phase 3: Revisions (MANDATORY)

You MUST always ask for revisions after generating a wireframe. Never skip this step.

After printing, use AskUserQuestion to ask:
- "What revisions would you like?" with options:
  - Add sections or elements
  - Remove sections or elements
  - Adjust sizing, spacing, or layout
  - Show responsive variant (mobile/tablet/desktop)
  - Done - looks good

Accept natural language revision requests: "make the sidebar wider", "add a search bar to the header", "swap the chart and table", "show me the mobile version", "add a footer with social links"

After each revision:
1. Re-print the **full updated wireframe** (never try to diff — always show complete)
2. Ask for revisions again
3. Continue this loop until the user selects "Done - looks good"

**Never assume the wireframe is final. Always ask.**

---

## Quality Standards

1. **Unicode box-drawing characters only** for all borders: `┌ ┐ └ ┘ │ ─ ├ ┤ ┬ ┴ ┼ ╭ ╮ ╰ ╯ ═ ║`
2. **Consistent alignment** — even padding inside all boxes, no ragged edges
3. **Labeled sections** — every major area gets a semantic comment label
4. **Realistic placeholder data** — real names, real numbers, real dates. Never "Lorem ipsum" or "Text here"
5. **Dimension annotations** — annotate overall width + any non-obvious heights
6. **Component legend** — include for wireframes with 5+ unique element types
7. **Max width: 120 chars** — prefer 80-100 for terminal readability
8. **Monospace-safe** — all alignment must work in monospace font

---

## Edge Cases

- **Wide layouts (>120 chars):** Stack sections vertically; annotate "// side-by-side at @desktop"
- **Multi-screen flows (>3 screens):** Show screens vertically connected with `│` and `▼` arrows
- **Responsive variants:** Produce separate wireframes labeled `@desktop`, `@tablet`, `@mobile` stacked
- **Complex dashboards:** Show grid layout overview first, then detail each cell as sub-wireframe
- **Small components:** Show at approximate character width without device frame
- **User asks to save:** Remind them output is terminal-only but copy-pasteable; offer to wrap in markdown code block

---

## Gold-Standard Example

```
// === SaaS Dashboard @desktop (1100px) ===

┌─ ○ ○ ○ ─── app.example.com/dashboard ──────────────────────────────────────────────────┐
│                                                                                         │
│  ◆ Acme      Dashboard   Analytics   Users   Settings       [🔍 Search... ]  🔔•  (👤) │
│                                                                                         │
├──────────┬──────────────────────────────────────────────────────────────────────────────┤
│          │                                                                              │
│ // [NAV] │  // [KPI CARDS] grid: 4-col, gap:16px                                       │
│          │                                                                              │
│ ▸ Dash   │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
│   Analyt │  │ Revenue      │ │ Users        │ │ Orders       │ │ Conversion   │        │
│   Users  │  │ $12,450      │ │ 1,234        │ │ 842          │ │ 3.2%         │        │
│   Orders │  │ ▲ 12.5%      │ │ ▲ 8.3%       │ │ ▼ 2.1%       │ │ ▲ 0.4%       │        │
│   Config │  │ ▁▂▃▅▇▅▃▂▁   │ │ ▁▃▅▇▇▅▃▁▂   │ │ ▇▅▃▂▁▂▃▅▇   │ │ ▁▁▂▃▅▅▇▇▇   │        │
│          │  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘        │
│ ──────── │                                                                              │
│          │  // [CHART]                                                                  │
│ REPORTS  │  ┌─ Revenue Over Time ──────────────────────────────────────────────┐        │
│   Daily  │  │                                                    ●             │        │
│   Weekly │  │                                          ●╱╲      ╱              │        │
│   Custom │  │                              ●──────●╱╱    ╲●╱╱                  │        │
│          │  │                    ●╱╲╱╲╱╱╱╱                                     │        │
│ ──────── │  │  ●──────●╱╱╱╱╱╱╱                                                │        │
│          │  │  Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct               │        │
│ SETTINGS │  └──────────────────────────────────────────────────────────────────┘        │
│   ⚙ Gen  │                                                                              │
│   🔒 Sec  │  // [DATA TABLE]                                                            │
│   💳 Bill │  ┌──────────────────────────────────────────────────────────────────┐        │
│          │  │ Name             Email                  Role      Status         │        │
│          │  ├──────────────────────────────────────────────────────────────────┤        │
│          │  │ Jane Cooper      jane@example.com       Admin     ⟨ Active ⟩    │        │
│          │  │ Alex Morgan      alex@example.com       Editor    ⟨ Active ⟩    │        │
│          │  │ Sam Rivera       sam@example.com        Viewer    ⟨ Pending ⟩   │        │
│          │  │ Jordan Lee       jordan@example.com     Editor    ⟨ Inactive ⟩  │        │
│          │  │ Casey Kim        casey@example.com      Admin     ⟨ Active ⟩    │        │
│          │  ├──────────────────────────────────────────────────────────────────┤        │
│          │  │ Showing 1-5 of 24                            ‹ 1 [2] 3 4 5 ›   │        │
│          │  └──────────────────────────────────────────────────────────────────┘        │
│          │                                                                              │
├──────────┴──────────────────────────────────────────────────────────────────────────────┤
│  © 2026 Acme Inc.    Privacy    Terms    Status: All systems operational ●              │
└─────────────────────────────────────────────────────────────────────────────────────────┘

// Sidebar: w:120px, fixed left
// Main content: flex-grow, p:24px
// KPI cards: grid 4-col, gap:16px, h:auto
// Chart: w:100%, h:240px
// Table: w:100%, paginated 5/page

LEGEND:
  ▸ Active nav item       ⟨ Status ⟩ Status pill
  ▲▼ Trend indicator      ▁▂▃▅▇ Sparkline
  🔔• Has notifications   (👤) User avatar
  ◆ Logo mark             ‹ › Pagination controls
```

This example demonstrates: device frame, sidebar + main layout, KPI cards, chart, data table, annotations, and legend. Match this level of detail and polish for all outputs.
