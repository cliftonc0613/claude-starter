---
name: course-creator
description: This skill should be used when creating comprehensive training courses and educational materials. Use for developing instructor guides, student workbooks, session plans, and complete course packages. Ideal for trade schools, corporate training, workshops, and educational programs that need structured, professional course content.
---

# Course Creator

## Overview

This skill enables the creation of comprehensive training courses through a conversational, question-by-question approach. It guides educators through designing complete course packages including instructor notes, student handouts, session playbooks, and supporting documentation. The skill follows the proven structure from AI Trade School materials, adapting it to any subject or audience.

## Conversational Course Creation Process

### Phase 1: Course Foundation

Begin by understanding the course requirements. Ask these questions one at a time, waiting for each answer before proceeding:

1. **Course Subject & Topic**
   - "What subject or topic will this course cover?"
   - Listen for: Technical domain, skill area, academic subject
   - Next: Determine course level based on topic complexity

2. **Target Audience**
   - "Who is this course designed for? Tell me about their background and experience level."
   - Listen for: Age range, prior knowledge, professional background, technical comfort
   - Next: Session duration based on audience attention span

3. **Session Duration**
   - "How long will each session be? (e.g., 2 hours, 3 hours, full day)"
   - Listen for: Time constraints, attention span, depth of content needed
   - Next: Learning objectives based on time available

4. **Primary Learning Objectives**
   - "By the end of this course, what should participants be able to do?"
   - Listen for: Specific skills, knowledge outcomes, practical applications
   - Next: Session structure based on objectives

### Phase 2: Session Structure

After understanding the basics, design the session flow:

5. **Session Format Preference**
   - "Do you prefer a TEACH → BUILD → SHOWCASE structure like the AI Trade School model, or a different format?"
   - If yes: Follow the 3-phase structure (Teach theory, Build practice, Showcase results)
   - If no: Ask about their preferred format and adapt accordingly
   - Next: Content breakdown

6. **Hands-on Activities**
   - "What practical exercises or activities should participants complete?"
   - Listen for: Number of activities, complexity, tools needed, individual vs group work
   - Next: Material requirements

7. **Materials & Resources**
   - "What materials will you need? (handouts, software, equipment, etc.)"
   - Listen for: Technology requirements, physical materials, prep work
   - Next: Instructor support needs

### Phase 3: Documentation Creation

With the course design clear, create the complete package:

8. **Package Components Confirmation**
   - "Based on our discussion, I'll create: [list components]. Does this cover everything you need?"
   - Typical components:
     - Instructor Notes (complete scripts, timing, troubleshooting)
     - Student Handout (workbook, activities, reflection questions)
     - Session Playbook (quick reference for delivery)
     - Complete Package Guide (how-to documentation)
   - Next: Begin document creation

## Document Templates & Structure

### Instructor Notes Format

Follow this structure for comprehensive instructor guidance:

```markdown
# SESSION [X] INSTRUCTOR NOTES
## [Session Title]

### Pre-Session Checklist
- Timeline: What to prepare and when
- Materials: Everything needed for the session
- Tech Setup: Requirements and testing procedures

### Phase 1: TEACH ([Time] minutes)
- Welcome & Introduction ([Time] min)
  - Complete script for opening
  - Icebreaker activities
- Core Concepts ([Time] min)
  - Key talking points
  - Visual aids/demos needed
- Examples & Stories ([Time] min)
  - Relevant career stories
  - Real-world applications

### Phase 2: BUILD ([Time] minutes)
- Activity [Number]: [Title] ([Time] min)
  - Problem statement
  - Step-by-step instructions
  - Expected outcomes
  - Troubleshooting tips

### Phase 3: SHOWCASE ([Time] minutes)
- Peer sharing format
  - How to select participants
  - Celebration techniques
  - Feedback guidelines

### Troubleshooting Guide
- Common issues and solutions
- Tech backup plans
- Time management strategies
```

### Student Handout Format

Create engaging workbook materials:

```markdown
# STUDENT WORKBOOK
## Session [X]: [Title]

### Today's Activities
- Brief overview of what we'll accomplish
- Space for notes and reflections

### Activity [Number]: [Title]
**Problem:** [Clear problem statement]
**Instructions:** [Step-by-step guidance]
**Your Response:** [Space for work]
**Reflection:** [Question for deeper thinking]

### Key Terms
- Glossary of important concepts
- Simple definitions
- Space for personal notes

### Portfolio Summary
- What you created today
- How you can use this
- Next steps for learning
```

### Session Playbook Format

One-page quick reference for delivery:

```markdown
# SESSION [X] PLAYBOOK
## One-Page Quick Reference

## Timing Roadmap
| Time | Phase | Activity | Instructor Role |
|------|-------|----------|----------------|

## Key Messages
- Critical points to emphasize
- Transition phrases
- Energy cues

## Activity Quick Reference
- Brief description of each activity
- Time warnings
- Success indicators

## Red Flags Checklist
- Common problems to watch for
- Quick interventions
- Backup plans

## Success Checklist
- What completion looks like
- Celebration moments
- Next session prep
```

## Resources

### references/
Store course creation templates and examples:
- `course_templates.md` - Additional format variations
- `assessment_strategies.md` - Different approaches to measuring learning
- `engagement_techniques.md` - Methods for maintaining energy and participation

### assets/
Include reusable course materials:
- `templates/` - Markdown templates for each document type
- `examples/` - Sample completed courses for reference
- `worksheets/` - Generic activity worksheets that can be adapted

### scripts/
Automate course material generation:
- `generate_course_package.py` - Creates all documents from course specifications
- `format_handout.py` - Formats student workbooks consistently
- `validate_timing.py` - Checks session timing and pacing

## Implementation Guidelines

1. **Ask questions one at a time** - Never overwhelm with multiple questions
2. **Wait for complete answers** - Ensure each response is fully understood
3. **Reference the AI Trade School materials** - Use the Session 1A package as a proven model
4. **Adapt, don't just copy** - Tailor the structure to each unique course
5. **Create complete packages** - Ensure all necessary documents are generated
6. **Include practical details** - Timing, materials, troubleshooting, and success metrics

## Special Considerations

- **Adult Learners**: Focus on practical application, respect their experience
- **Technical Subjects**: Include hands-on practice, progress from simple to complex
- **Soft Skills**: Incorporate role-play, real-world scenarios, peer feedback
- **Short Sessions**: Maximize engagement, limit theoretical content
- **Multi-Session Courses**: Build progression, reference previous learning