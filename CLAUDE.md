# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **starter template** repository containing pre-configured Claude Code agents, commands, and design review workflows. It serves as a reusable foundation for new projects rather than an active application codebase.

---

## ⚠️ CRITICAL: Development Workflow Rules

**THESE RULES ARE SUPER IMPORTANT AND NON-NEGOTIABLE WHEN CODING ON ANY TASK.**

1. **Plan First** - Before writing any code, think through the problem, read the codebase for relevant files, and write a plan to `tasks/todo.md`

2. **Create Todo Items** - The plan must have a checklist of specific todo items that can be marked as complete as work progresses

3. **Checkpoint with User** - Before beginning any work, present the plan to the user and wait for verification/approval

4. **Interview for Spec** - Read the plan file and interview the user using the `AskUserQuestion` tool:
   - Ask about: technical implementation, UI/UX, concerns, tradeoffs
   - Make sure the questions are not obvious
   - Be very in-depth and continue until it's complete
   - Then write the spec

5. **Execute & Track** - Work through todo items one at a time, marking each as complete as you finish it

6. **Communicate Progress** - At every step, provide a high-level explanation of what changes you made (not verbose, just clear summaries)

7. **Simplicity First** - Make every task and code change as simple as possible:
   - Each change should impact as little code as possible
   - Avoid massive or complex refactoring
   - Only modify code necessary for the task
   - Everything is about minimalism and clarity

8. **Add Review Section** - When complete, add a review section to `tasks/todo.md` with:
   - Summary of all changes made
   - Any relevant information about the work
   - Lessons learned or edge cases discovered

9. **No Lazy Fixes** - This is non-negotiable:
   - If there's a bug, find and fix the ROOT CAUSE
   - Never use temporary or band-aid fixes
   - You are a senior developer - act like one
   - Thorough investigation = better code

10. **Minimal Code Impact** - ALL fixes and changes must be as simple as humanly possible:
   - Only impact necessary code relevant to the task
   - Touch as little code as possible to solve the problem
   - Your goal is to NOT introduce new bugs
   - **SIMPLICITY IS THE PRIORITY**

**These rules apply to EVERY task, EVERY PR, EVERY code change. There are no exceptions.**

---

## Repository Structure

```
.claude/
├── agents/                    # Main agents (8 built-in agents)
├── agents/my-team/            # 177+ specialized domain experts (14 categories)
├── commands/                  # Custom slash commands for common workflows
└── subagents/                 # Supporting agents for specific sub-tasks

context/                       # Design principles and review guidelines
├── design-principles.md       # S-tier SaaS dashboard design checklist
├── design-review-claude-md-snippet.md  # Quick visual check protocol
└── design-review-slash-command.md     # Comprehensive design review agent template
```

## Available Agents (.claude/agents/)

**Content & Research:**
- `blog-writer.md` - Creates publication-ready blog posts from research
- `content-analyzer.md` - Analyzes competitor content for trends and gaps
- `content-researcher.md` - Gathers content intelligence from multiple sources
- `newsletter-writer.md` - Drafts newsletters in authentic voice
- `competitor-analyzer.md` - Performs competitive intelligence analysis
- `keyword-extractor.md` - Extracts SEO keywords and opportunities

**Market Research & Business:**
- `data-analyzer.md` - Analyzes market data and metrics
- `market-researcher.md` - Creates comprehensive market research reports
- `press-release-writer.md` - Generates media-ready press releases
- `media-researcher.md` - Identifies target journalists and publications

**Design & Development:**
- `design-review-agent.md` - Conducts world-class design reviews with Playwright
- `premium-ui-designer.md` - Creates sophisticated UI with premium aesthetics
- `meta-seo-agent.md` - Implements SEO meta tags and schema markup for Astro
- `meta-agent.md` - Generates new sub-agent configuration files

**Personal Development:**
- `daily-reflection.md` - Analyzes daily check-in patterns
- `metrics-analyst.md` - Tracks and visualizes weekly metrics

## Available Commands (.claude/commands/)

Run these with the `/` prefix (e.g., `/blog-research`)

**Content Creation:**
- `/blog-research` - Analyze competitor blogs and create SEO-optimized drafts
- `/newsletter-research` - Create newsletter drafts from competitor analysis
- `/press-release` - Generate professional press releases with media distribution plans

**Research & Analysis:**
- `/market-research [brief.md]` - Create comprehensive market research studies
- `/website-research [url]` - SEO audit, keyword extraction, competitive analysis
- `/youtube-research [search|url]` - Analyze YouTube content for SEO and strategy

**Personal Development:**
- `/daily-checkin` - Personal reflection and well-being tracking
- `/weekly-checkin` - Intelligent weekly progress tracking with adaptive metrics
- `/time-checkin` - Time-aware check-ins (morning/midday/evening)

**Freelancing:**
- `/upwork-cover-letter [project-url]` - Generate tailored Upwork cover letters from project URLs

**Utilities:**
- `/agent-creator` - Create new Claude Code agent configurations
- `/prompt-creator` - Generate optimized prompts

## Available Specialized Agents

Located in `.claude/agents/my-team/`, this repository contains 177+ specialized AI agents organized into 14 categories. These agents are designed for deep expertise in specific domains and can be invoked when the task requires specialized knowledge.

### How to Use These Agents

To invoke a specialized agent, you can use the Skill tool (recommended) or invoke it directly. Most agents follow a consistent format:
- **Frontmatter**: name, description, color, emoji, vibe
- **Main body**: Detailed persona, capabilities, workflows, and deliverables

### Agent Categories

#### Design (8 agents)
Expert visual and user experience design agents specializing in:
- UI Design (pixel-perfect interfaces, component libraries)
- UX Research (user research, usability testing)
- Brand Design (brand guardianship, visual systems)
- Creative Design (visual storytelling, whimsy injection)
- AI-Assisted Design (image prompt engineering)

#### Engineering (13 agents)
Full-stack and specialized engineering agents including:
- Frontend Development (React, Vue, Angular, performance)
- Backend Architecture (API design, databases, microservices)
- DevOps & Security (CI/CD, security, infrastructure)
- Mobile Development (iOS, Android, cross-platform)
- Specialized Engineering (WebXR, embedded systems, blockchain)

#### Game Development (20 agents)
Comprehensive game development support across platforms:
- **Unity** (5 agents): Architecture, tools, multiplayer, shaders
- **Unreal Engine** (4 agents): Multiplayer, systems, technical art, world building
- **Godot** (3 agents): Gameplay scripting, multiplayer, shaders
- **Roblox Studio** (3 agents): Avatar creation, experience design, systems scripting
- **General** (5 agents): Design, audio, narrative, level design

#### Marketing (17 agents)
Strategic marketing and content creation specialists:
- **General Marketing** (3): Content creation, growth hacking, SEO
- **China Platforms** (5): Baidu SEO, Bilibili, China e-commerce
- **Social Media** (5): Instagram, TikTok, Twitter, Reddit, WeChat
- **Specialized** (4): App Store optimization, carousel growth, Xiaohongshu, Zhihu

#### Paid Media (8 agents)
Paid media strategy and execution across platforms:
- PPC Campaign Strategist, Paid Social Strategist, Search Query Analyst
- Programmatic Buyer, Creative Strategist, Auditor, Tracker Specialist

#### Product (4 agents)
Product management and feedback synthesis:
- Feedback Synthesizer, Behavioral Nudge Engine
- Sprint Prioritizer, Trend Researcher

#### Project Management (7 agents)
Project lifecycle management and execution:
- Senior Project Manager, Project Shepherd, Studio Operations
- Studio Producer, Jira Workflow Steward, Experiment Tracker, PM Producer

#### Sales (6 agents)
Pre-sales and sales enablement specialists:
- Sales Engineer, Account Strategist, Deal Strategist
- Proposal Strategist, Discovery Coach, Coach

#### Spatial Computing (6 agents)
XR and immersive technology development:
- XR Immersive Developer, XR Cockpit Interaction Specialist
- VisionOS Spatial Engineer, macOS Spatial/Metal Engineer
- Terminal Integration Specialist, XR Interface Architect

#### Specialized (15 agents)
Domain-specific expert agents:
- Agents Orchestrator, Agentic Identity & Trust Architect
- Compliance Auditor, Blockchain Security Auditor, ZK Steward
- Data Consolidation Agent, Report Distribution Agent, Sales Data Extraction Agent
- Accounts Payable Agent, Developer Advocate, Model QA Specialist
- Cultural Intelligence Strategist, LSP Index Engineer, Identity Graph Operator

#### Testing (8 agents)
Quality assurance and testing specialists:
- API Tester, Accessibility Auditor, Test Results Analyzer
- Performance Benchmarker, Evidence Collector, Tool Evaluator
- Reality Checker, Workflow Optimizer

#### Strategy (17 agents)
Strategic planning and execution frameworks:
- **Coordination** (2): Agent activation prompts, handoff templates
- **Playbooks** (6): Phase 0-6 discovery, strategy, foundation, build, hardening, launch, operate
- **Runbooks** (4): Enterprise feature, incident response, marketing campaign, startup MVP
- **Strategic Docs**: Executive brief, nexus strategy, quickstart

#### Integrations (13 agents)
Platform and tool integrations:
- **MCP**: memory, backend architect with memory
- **AI Code Editors**: Aider, Antigravity, Claude Code, Cursor, Gemini CLI
- **Platform**: GitHub Copilot, Opencode, Windsurf
- Plus integration directories and READMEs

### Notable Agents to Know

**Design:**
- `design-ui-designer.md` - Creates visual design systems, component libraries
- `design-ux-architect.md` - Designs user experiences and interaction flows
- `design-brand-guardian.md` - Maintains visual brand consistency

**Engineering:**
- `engineering-frontend-developer.md` - React/Vue/Angular development, performance
- `engineering-senior-developer.md` - Senior-level full-stack development
- `engineering-ai-engineer.md` - AI/ML integration and development

**Game Development:**
- `unity-architect.md` - Unity game architecture and development
- `unreal-multiplayer-architect.md` - Unreal Engine multiplayer systems
- `game-designer.md` - Game design and mechanics

**Marketing:**
- `marketing-social-media-strategist.md` - Cross-platform social strategy
- `marketing-seo-specialist.md` - SEO and content optimization
- `marketing-content-creator.md` - Content creation and curation

**Paid Media:**
- `paid-media-ppc-strategist.md` - PPC campaign strategy
- `paid-media-paid-social-strategist.md` - Social advertising strategy

**Product:**
- `product-feedback-synthesizer.md` - Collects and analyzes user feedback

**Project Management:**
- `project-management-senior.md` - Converts specs to tasks
- `project-management-project-shepherd.md` - Project lifecycle management

**Sales:**
- `sales-engineer.md` - Pre-sales technical specialist
- `sales-deal-strategist.md` - Sales deal strategy and negotiation

**Spatial Computing:**
- `spatial-computing/xr-immersive-developer.md` - WebXR and AR/VR development
- `spatial-computing/visionos-spatial-engineer.md` - VisionOS spatial computing

**Specialized:**
- `specialized-developer-advocate.md` - Developer community and documentation
- `specialized-blockchain-security-auditor.md` - Blockchain security auditing
- `specialized-compliance-auditor.md` - Compliance and audit support

**Testing:**
- `testing-api-tester.md` - API testing and quality assurance
- `testing-accessibility-auditor.md` - Accessibility compliance testing
- `testing-performance-benchmarker.md` - Performance testing and optimization

### Agent Invocation Best Practices

1. **Use the Skill tool for invoke**: `Skill: name: design-ui-designer` or `Skill: name: engineering-frontend-developer`
2. **Search by category**: For broad task types, specify the category: `Skill: name: design`
3. **Combine with context**: Provide specific project context when invoking agents
4. **Chain agents**: Multiple agents can work together by handoff or sequential invocation
5. **Review agent files**: Each agent includes detailed personality, capabilities, and deliverables in its markdown file

### Example Usage

**For UI/UX Design:**
```
Skill: design-ui-designer
Context: Building a SaaS dashboard component library
```

**For Frontend Development:**
```
Skill: engineering-frontend-developer
Context: Implementing a React table component with virtualization
```

**For API Testing:**
```
Skill: testing-api-tester
Context: Validating a REST API with security testing
```

**For Game Development:**
```
Skill: game-development/unity-architect
Context: Designing a multiplayer game architecture for Unity
```

**For Sales Engineering:**
```
Skill: sales-engineer
Context: Technical discovery and POC design for enterprise deal
```

## Design Review Workflow

This repository includes a comprehensive design review system based on Stripe, Airbnb, and Linear standards:

### Quick Visual Check
After any front-end change:
1. Review modified components/pages
2. Navigate to affected pages using Playwright
3. Verify design compliance against `context/design-principles.md`
4. Validate feature implementation
5. Capture full-page screenshots (1440px viewport)
6. Check for console errors

### Comprehensive Design Review
Use the `design-review-agent` for thorough validation:
- Before finalizing PRs with visual changes
- After completing significant UI/UX features
- For accessibility and responsiveness testing

## Design Principles

The `context/design-principles.md` file contains an S-tier SaaS dashboard checklist covering:
- Core design philosophy (users first, meticulous craft, speed, simplicity)
- Design system foundation (color palettes, typography, spacing, components)
- Layout and visual hierarchy
- Interaction design and animations
- Module-specific tactics (multimedia moderation, data tables, configuration panels)
- CSS architecture recommendations (utility-first/Tailwind preferred)

## Using This Template

To use this starter for a new project:
1. Copy the `.claude/` directory to your new project
2. Copy `context/` files if you need design review workflows
3. Customize agents and commands for your specific project needs
4. Create a new project-specific `CLAUDE.md` with your application architecture
5. Remove or modify commands that don't apply to your project

## Creating New Agents

Use `/agent-creator` or `/meta-agent` to generate new agent configurations.

- **Main agents** (`.claude/agents/`): Built-in general-purpose agents
- **My-team agents** (`.claude/agents/my-team/`): 177+ specialized domain experts organized into 14 categories

New agents should be created in the appropriate directory following the existing template structure.

## Notes

- This template contains no application code - it's purely a collection of automation tools
- Agents are designed to work independently and can be mixed/matched for different projects
- Commands often chain multiple agents together for complex workflows
- The design review system assumes Playwright MCP is available for browser automation

## User Interaction Requirements

**CRITICAL: ALWAYS use the `AskUserQuestion` tool when asking questions.**

When you need to:
- Gather user preferences or requirements
- Clarify ambiguous instructions
- Get decisions on implementation choices
- Offer choices about direction to take
- Confirm understanding before proceeding

You **MUST** use the `AskUserQuestion` tool instead of asking questions in plain text. This provides:
- Structured, selectable options for the user
- Better UX with clickable choices
- Clearer decision points in the workflow
- Consistent interaction patterns

**DO NOT** ask questions as plain text in your responses. Always structure questions through the tool with clear options.

## Code Style Guidelines

### Styling Practices
- Never, ever use inline styles; always use the global style sheet.

<frontend_aesthetics>
## Frontend Design Aesthetics

**CRITICAL: Avoid generic "AI slop" aesthetics. Create distinctive, surprising frontends that delight users.**

### Typography
- Choose fonts that are beautiful, unique, and interesting
- **Avoid generic fonts**: Arial, Inter, Roboto, system fonts
- **Avoid overused "creative" fonts**: Space Grotesk (commonly AI-selected)
- Opt for distinctive choices that elevate the frontend's character
- Each project should feel intentionally designed, not template-generated

### Color & Theme
- Commit to a cohesive aesthetic using CSS variables for consistency
- **Dominant colors with sharp accents** outperform timid, evenly-distributed palettes
- Draw inspiration from IDE themes and cultural aesthetics
- **Avoid clichéd schemes**: purple gradients on white backgrounds
- Vary between light and dark themes based on context
- Make unexpected color choices that feel genuinely designed for the specific project

### Motion & Animation
- Use animations for effects and micro-interactions
- Prioritize CSS-only solutions for HTML projects
- Use Motion library for React when available
- **Focus on high-impact moments**: One well-orchestrated page load with staggered reveals (`animation-delay`) creates more delight than scattered micro-interactions

### Backgrounds & Atmosphere
- Create atmosphere and depth rather than defaulting to solid colors
- Layer CSS gradients for visual interest
- Use geometric patterns or contextual effects matching the overall aesthetic
- Build environments that immerse users in the design

### What to Avoid
- Overused font families (Inter, Roboto, Arial, system fonts)
- Clichéd color schemes (purple gradients, generic blues)
- Predictable layouts and component patterns
- Cookie-cutter design lacking context-specific character
- Convergence toward "safe" AI-common choices

### Design Philosophy
Interpret creatively and make unexpected choices. Think outside the box—each frontend should feel handcrafted for its specific context, not generated from a template. Surprise and delight should be the goal.
</frontend_aesthetics>

---

## Custom Modes

**IMPORTANT: When user activates a mode, read `/context/core/claude-modes.json` for full mode configuration.**

Claude has specialized modes that activate different thinking styles and approaches. When the user mentions a mode name, Claude MUST:
1. Read `/context/core/claude-modes.json` to get the full mode configuration
2. Apply all behavior settings, focus areas, and voice guidelines from that mode
3. Stay in that mode until told otherwise or a different mode is called

**Note**: In addition to these built-in modes, the repository contains 177+ specialized agents in `.claude/agents/my-team/` organized into 14 categories. These agents provide domain-specific expertise beyond the built-in modes.

### Available Modes

| Mode | Trigger | Best For |
|------|---------|----------|
| **Genius Mode** | "Genius Mode" | Strategic thinking, complex decisions, deep analysis |
| **Lawyer Mode** | "Lawyer Mode" | Contracts, legal risk, WIOA compliance, agreements |
| **Content Creator Mode** | "Content Creator Mode" | Social media, YouTube, blogs, marketing copy |
| **WordPress Architect Mode** | "WordPress Architect Mode" | Site architecture, code decisions, technical planning |
| **Sports Journalist Mode** | "Sports Journalist Mode" | Clemson Sports Media articles, game coverage |
| **Editor Mode** | "Editor Mode" | Refining and tightening any written content |
| **Teaching Mode** | "Teaching Mode" | Curriculum, explanations, student-facing content |
| **Interview/Research Mode** | "Interview/Research Mode" | Discovery, preparation, clarifying decisions |

### How to Activate

- Say the mode name directly: "Genius Mode"
- Use natural phrases: "Switch to Editor Mode", "Let's use Teaching Mode for this"
- Combine with request: "Sports Journalist Mode — write a recap of last night's game"

### How to Exit

- Say "Exit mode"
- Call a different mode name

---
