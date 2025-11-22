# Claude Code Starter Template

A production-ready starter repository for [Claude Code](https://claude.com/claude-code) containing pre-configured AI agents, custom commands, and design review workflows.

## What's Included

### 🤖 Specialized Agents
Pre-built AI agents in `.claude/agents/` for:
- **Content Creation**: Blog writing, newsletter drafting, SEO content
- **Market Research**: Competitive analysis, data analysis, market reports
- **Design & Development**: Design reviews, premium UI components, SEO optimization
- **Personal Development**: Daily reflections, weekly metrics tracking

### ⚡ Custom Commands
Ready-to-use slash commands in `.claude/commands/`:
- `/blog-research` - Analyze competitors and create SEO-optimized drafts
- `/market-research` - Generate comprehensive market research studies
- `/website-research` - SEO audits and competitive analysis
- `/press-release` - Create media-ready press releases
- `/youtube-research` - YouTube content and SEO analysis
- `/daily-checkin` - Personal reflection and well-being tracking
- `/weekly-checkin` - Intelligent progress tracking

### 🎨 Design Review System
World-class design review workflows in `context/`:
- S-tier SaaS dashboard design principles
- Automated visual regression testing
- Accessibility and responsiveness validation
- Playwright-powered browser automation

## Quick Start

1. **Clone this repository:**
   ```bash
   git clone <repository-url>
   cd _starter
   ```

2. **Setup zclaude (optional):**
   If you have both Claude Code Pro/Max and Z.AI Coding Plan subscriptions, you can use zclaude to switch between them without manual configuration:
   ```bash
   bash setup_zclaude.sh
   ```

   This setup script will:
   - Detect your shell (bash, zsh, fish, ksh, csh)
   - Create backups of your shell configuration
   - Add `zclaude` command alias for Z.AI access
   - Configure Z.AI MCP servers (glm-4.5-air and glm-4.6 models)
   - Keep your existing `claude` command for Anthropic's Claude

   After setup, use `zclaude` to access Z.AI features or `claude` for Anthropic's Claude.

   **Learn more:** [zclaude repository](https://github.com/dharmapurikar/zclaude)

3. **Add required MCP servers:**
   ```bash
   # Add Firecrawl MCP for web scraping
   claude mcp add -s project firecrawl "npx -y @modelcontextprotocol/server-firecrawl"

   # Add Playwright MCP for browser automation and design reviews
   claude mcp add -s project playwright "npx -y @modelcontextprotocol/server-playwright"
   ```

   These MCPs are already configured in `.mcp.json`, but you'll need to approve them when prompted by Claude Code.

4. **Customize for your project:**
   - Edit `.claude/agents/` to add project-specific agents
   - Modify `.claude/commands/` to include your workflows
   - Create a project-specific `CLAUDE.md` with your architecture

5. **Start using commands:**
   ```bash
   # In Claude Code
   /blog-research
   /market-research research-brief.md
   /website-research https://example.com
   ```

## Repository Structure

```
.claude/
├── agents/          # AI agents for specialized tasks
│   ├── blog-writer.md
│   ├── content-analyzer.md
│   ├── design-review-agent.md
│   ├── market-researcher.md
│   └── ... (15+ agents)
├── commands/        # Slash commands for workflows
│   ├── blog-research.md
│   ├── market-research.md
│   ├── daily-checkin.md
│   └── ... (10+ commands)
└── subagents/       # Supporting agents

context/
├── design-principles.md              # S-tier design checklist
├── design-review-claude-md-snippet.md
└── design-review-slash-command.md

CLAUDE.md            # Claude Code instructions (global)
```

## Key Features

### Content & Research Agents
- **Blog Writer**: Creates 1,200-2,000 word publication-ready posts
- **Content Analyzer**: Identifies trends and gaps in competitor content
- **Newsletter Writer**: Drafts newsletters in your authentic voice
- **Market Researcher**: Comprehensive market research with executive summaries

### Design & Development
- **Design Review Agent**: Automated visual testing with Playwright
- **Premium UI Designer**: Sophisticated components with premium aesthetics
- **Meta SEO Agent**: Implements SEO meta tags and schema markup

### Personal Development
- **Daily Checkin**: Personal reflection and mood tracking
- **Weekly Checkin**: Adaptive metrics tracking for your specific projects
- **Metrics Analyst**: Visual trends and insights over time

## Creating New Agents

Use the built-in meta-agent:

```bash
/meta-agent
```

Or manually create in `.claude/agents/` following this structure:

```markdown
---
name: your-agent-name
description: What this agent does
tools: Read, Write, WebFetch
color: blue
model: sonnet
---

[Agent instructions here]
```

## Design Review Workflow

### Quick Visual Check
After any UI change:
1. Navigate to modified pages using Playwright
2. Verify against `context/design-principles.md`
3. Capture screenshots (1440px viewport)
4. Check console for errors

### Comprehensive Review
Use the design-review agent:
```bash
/design-review
```

Based on Stripe, Airbnb, and Linear design standards.

## Using This Template

**For a new project:**
1. Copy `.claude/` and `context/` directories
2. Keep relevant agents and commands
3. Remove unused workflows
4. Create project-specific `CLAUDE.md`
5. Customize agents for your domain

**For an existing project:**
1. Copy individual agents/commands you need
2. Merge with existing `.claude/` structure
3. Update `CLAUDE.md` with new commands

## Requirements

- [Claude Code](https://claude.com/claude-code)

## Model Context Protocol (MCP) Servers

All MCP servers are pre-configured in `.mcp.json`. Here's what's included:

### Core MCPs
- **Firecrawl** - Web scraping, content extraction, and crawling for research features
  - Requires `FIRECRAWL_API_KEY` environment variable

- **Playwright** - Browser automation, visual testing, and design review workflows
  - Cross-browser testing (Chrome, Firefox, Safari, WebKit)

- **Sequential Thinking** - Extended thinking capabilities for complex problem-solving
  - Built-in Anthropic MCP for deep analysis tasks

### Data & API Integration
- **Context7** - Documentation and library reference lookup
  - Requires `CONTEXT7_API_KEY` environment variable
  - Fetches up-to-date docs for libraries and frameworks

- **Apify** - Web scraping and data extraction at scale
  - Requires `APIFY_TOKEN` environment variable
  - Access to 2,500+ pre-built scraping actors

### Communication & Social
- **Twitter MCP** - Post to Twitter and analyze social media
  - Requires `TWITTER_API_KEY`, `TWITTER_API_SECRET_KEY`, `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_TOKEN_SECRET`
  - Tweet creation and engagement analysis

- **Resend** - Email sending and newsletter delivery
  - Requires `RESEND_API_KEY` environment variable
  - Send transactional and marketing emails

### Setup MCPs

Add individual MCPs using:
```bash
# Firecrawl
claude mcp add -s project firecrawl "npx -y @modelcontextprotocol/server-firecrawl"

# Playwright
claude mcp add -s project playwright "npx -y @modelcontextprotocol/server-playwright"

# Sequential Thinking
claude mcp add -s project sequential-thinking "npx -y @modelcontextprotocol/server-sequential-thinking"

# Context7
claude mcp add -s project context7 "npx -y @upstash/context7-mcp@latest"

# Twitter MCP
claude mcp add -s project twitter-mcp "npx -y @enescinar/twitter-mcp"

# Resend
# Configure with your custom server path

# Apify
claude mcp add -s project apify "npx -y @apify/actors-mcp-server"
```

**Note:** MCPs configured in `.mcp.json` are already set up but may require approval in Claude Code on first use.

## Documentation

Full documentation in `CLAUDE.md` includes:
- Detailed command usage
- Agent capabilities and workflows
- Design principles and standards
- Creating custom agents and commands

## Examples

### Content Creation & Research
**Create a publication-ready blog post:**
```bash
/content-creation:blog-research
```
- Analyzes 5-10 competitor blogs from your niche
- Identifies trending topics, content gaps, and opportunities
- Performs keyword research and search intent analysis
- Writes SEO-optimized 1,200-2,000 word blog post
- Provides 5 headline options and strategic CTAs
- Outputs: competitive analysis, keywords, topic ideas, ready-to-publish draft

**Draft a newsletter from competitor analysis:**
```bash
/content-creation:newsletter-research
```
- Analyzes competitor newsletter content and trends
- Extracts content themes and successful formats
- Learns your authentic writing voice
- Creates 500-800 word newsletter draft
- Provides 3 compelling subject line options
- Outputs: research report, ready-to-send newsletter

**Generate a professional press release:**
```bash
/media-communications:press-release
```
- Creates AP Style-compliant press releases
- Researches target journalists and media outlets
- Generates media distribution lists with contact info
- Provides email templates and follow-up strategies
- Identifies newsworthy angles and timing
- Outputs: press release, media list, distribution strategy

### Research & Analysis
**Audit a website for SEO opportunities:**
```bash
/research-analysis:website-research https://competitor.com
```
- Technical SEO audit and recommendations
- On-page optimization analysis
- Keyword extraction and opportunities
- Competitive intelligence analysis
- Provides actionable improvement strategies
- Outputs: comprehensive SEO report with rankings

**Analyze YouTube channel strategy:**
```bash
/research-analysis:youtube-research https://youtube.com/c/channel-name
```
- Analyzes channel growth patterns and trends
- Identifies content gaps and opportunities
- Research SEO metrics and keyword opportunities
- Maps competitive positioning
- Suggests content strategy improvements
- Outputs: competitive analysis, opportunity report

### Personal Development & Tracking
**Daily personal reflection check-in:**
```bash
/personal-development:daily-checkin
```
- Personal mood and energy tracking
- Accomplishment logging and momentum scoring
- Reflection prompts for growth
- Visual trend analysis over time
- Outputs: daily journal entries, pattern insights

**Weekly intelligent progress check-in:**
```bash
/personal-development:weekly-checkin
```
- Metrics tracking adapted to your specific project
- Week-over-week progress comparison
- Visual trend visualization
- Insights and recommendations
- Outputs: weekly progress report

**Time-aware reflection check-ins:**
```bash
/personal-development:time-checkin
```
- Morning (before 10am), midday (10am-3pm), or evening (after 5pm) reflections
- Contextual questions based on time of day
- Timezone-aware scheduling
- Outputs: reflection entries with patterns

### Utilities & Automation
**Create custom agents for your workflows:**
```bash
/utilities:agent-creator
```
- Generate new Claude Code agent configurations
- Customizable tools, models, and descriptions
- Ready-to-use agent templates
- Outputs: new agent markdown files in `.claude/agents/`

**Build optimized prompts:**
```bash
/utilities:prompt-creator
```
- Refines and optimizes prompts for better results
- Analyzes prompt structure and effectiveness
- Provides prompt engineering best practices
- Outputs: improved prompt variations

### Project Management (Coming Soon)
These commands are available in `.claude/commands/`:
- `/start-phase` - Initialize development phases with planning
- `/generate-tasks` - Create structured task lists from requirements
- `/design-review` - Comprehensive visual design testing with Playwright

## Contributing

This is a starter template. Fork it, customize it, make it your own.

## License

MIT - Use freely for personal and commercial projects.

---

**Built for [Claude Code](https://claude.com/claude-code)** - AI-powered development automation
