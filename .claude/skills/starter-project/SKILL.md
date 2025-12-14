---
name: starter-project
description: This skill should be used when initializing a new project with pre-configured Claude Code setup. It guides users through project naming and context, syncs agents/commands/skills from the central repository, creates essential folder structures (context/core, knowledge with subfolders), and generates placeholder JSON files for business profile, voice DNA, and ideal client profile.
---

# Starter Project Skill

## Purpose

This skill bootstraps a new project with a complete Claude Code setup by:
1. Gathering project context and naming
2. Syncing pre-built agents, commands, and skills from your central repository
3. Creating essential folder structures for knowledge management and context
4. Generating placeholder JSON files for business profiles, voice DNA, and client profiles

This ensures every new project has a consistent, production-ready foundation.

## When to Use This Skill

Use this skill when:
- Starting a brand new project from scratch
- Setting up a project based on your starter template
- Initializing a project that will use Claude Code automation
- Creating a new venture, product, or initiative that needs structured setup
- Ensuring consistency across all your projects

## How to Use This Skill

### Step 1: Gather Project Information

Ask the user the following questions **one at a time**:

1. **Project Name**: "What is the name of your project?"
2. **Project Description**: "What is this project about? (Brief 1-2 sentence description)"
3. **Project Type**: "What type of project is this?" (e.g., SaaS, Blog, Service Business, Content Hub, etc.)

### Step 2: Determine Sync Scope

Ask the user: "What would you like to sync from your central repository?"

Provide options:
- **All** - Sync everything (agents, commands, and skills)
- **Agents only** - Sync just the agents
- **Commands only** - Sync just the commands
- **Skills only** - Sync just the skills
- **Custom** - Let me choose individual items

Wait for their selection.

### Step 3: Run sync-claude-config

Run the `/development:sync-claude-config` command (or equivalent sync command) based on the user's selection from Step 2.

Document what was synced and confirm success with the user.

### Step 4: Create Folder Structure

Create the following directory structure in the project root:

```
context/
└── core/

knowledge/
├── drafts/
├── published/
├── notes/
└── research/
```

### Step 5: Generate Placeholder JSON Files

In the `context/core/` directory, create the following placeholder JSON files:

#### business-profile.json
Template with empty structure for documenting business overview, positioning, offerings, audience, and operations.

#### voice-dna.json
Template with empty structure for documenting communication style, personality, core values, storytelling approach, language patterns, and audience connection.

#### ideal-client-profile.json (icp.json)
Template with empty structure for documenting ideal client personas with demographics, psychographics, pain points, goals, budget, decision-making, preferences, and buying signals.

See `references/` directory for complete schema templates.

### Step 6: Create Project Documentation

Create a project-specific `CLAUDE.md` file in the project root with:
- Project name and description
- Project type
- Overview of synced components
- Quick start instructions for common tasks
- References to available agents, commands, and skills

### Step 7: Confirm and Next Steps

Display a summary of what was created and ask if the user wants to:
- Start filling out business profile, voice DNA, or ICP
- Begin working on their first project task
- Review the documentation

## Reference Schemas

See `references/` directory for complete JSON templates:
- `business-profile-schema.json`
- `voice-dna-schema.json`
- `icp-schema.json`

## Bundled Resources

- `references/` - JSON schema templates for all three profile types
- `scripts/create_project.py` - Python script to automate directory and file creation
- `templates/CLAUDE.md.template` - Template for project-specific CLAUDE.md file

## Key Considerations

- **Tone**: Keep the setup process encouraging and clear. Explain what each component does.
- **Flexibility**: Allow users to choose which components to sync.
- **Documentation**: Generate helpful initial documentation so users understand their new setup.
- **Next Steps**: Point users toward filling out their profiles or starting their first task.
- **Consistency**: Ensure all placeholder files follow the same structure as existing projects.

## Important Notes

- Ensure sync-claude-config completes successfully before proceeding with folder creation
- All placeholder JSON files should include `_instructions` and `_metadata` sections
- The project-specific CLAUDE.md should reference the available agents and commands
- Confirm successful creation of all directories and files with the user
