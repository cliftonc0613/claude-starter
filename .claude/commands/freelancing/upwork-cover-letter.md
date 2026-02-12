---
description: Generate a tailored Upwork cover letter from a project URL using your live profile and resume
---

**CRITICAL: You MUST use the `AskUserQuestion` tool for ALL questions and interactions throughout this skill. Never ask questions as plain text.**

---

## Step 1: Gather Input from User

Use `AskUserQuestion` to collect the information needed:

**Question 1** - Ask for the Upwork project URL:
- header: "Project URL"
- question: "What is the Upwork project URL you want to apply to?"
- options:
  - "I'll paste the URL" (description: "Provide the full Upwork project/job posting URL")
  - "I have it open in Chrome" (description: "Use browser automation to read the currently open Upwork tab")

If the user provides a URL (via `$ARGUMENTS` or their answer), proceed. If they say it's open in Chrome, use browser tools to read the active tab.

**Question 2** - Ask about tone preference:
- header: "Tone"
- question: "What tone should the cover letter have?"
- options:
  - "Professional & confident (Recommended)" (description: "Polished but personable, shows authority without being stiff")
  - "Casual & friendly" (description: "Conversational, approachable, like messaging a colleague")
  - "Formal & detailed" (description: "Traditional business tone, thorough and structured")

**Question 3** - Ask about any special emphasis:
- header: "Emphasis"
- question: "Is there anything specific you want to highlight or mention in this cover letter?"
- options:
  - "No, just match my skills to the job" (description: "Auto-match based on profile, resume, and job requirements")
  - "Yes, I have something specific" (description: "I want to mention a particular project, skill, or angle")

If the user wants to highlight something specific, use a follow-up `AskUserQuestion` to ask what they want to emphasize.

**Question 4** - Ask about frameworks/methodologies:
- header: "Frameworks"
- question: "Do you use any specific design or marketing frameworks you want referenced in this cover letter?"
- options:
  - "StoryBrand (Donald Miller)" (description: "Position the client as the hero with a guide, plan, and transformation arc")
  - "Other framework" (description: "I use a different methodology I'd like to mention")
  - "No specific framework" (description: "Skip this and focus on skills and experience")

If the user selects StoryBrand or another framework, weave it into the cover letter as a differentiator.

**Question 5** - Ask about portfolio attachments:
- header: "Attachments"
- question: "Are you attaching portfolio samples to this proposal?"
- options:
  - "Yes, and I want to call them out" (description: "I'll tell you what's notable about the attached samples so the cover letter can reference them")
  - "Yes, but no special mention needed" (description: "Attachments speak for themselves")
  - "No attachments" (description: "Cover letter only")

If the user wants to call out attachments, use a follow-up `AskUserQuestion` to ask what's notable about them.

---

## Step 2: Gather Project Details

Fetch the Upwork project posting using the URL from Step 1.

**Primary method**: Use `WebFetch` on the project URL with the prompt:
"Extract ALL project details: job title, description, required skills, budget/hourly rate, project length, experience level required, client history (jobs posted, hire rate, total spent), client location, number of proposals, and any specific questions the client asks applicants to answer."

**Fallback 1**: If WebFetch returns a 403 or fails, use `AskUserQuestion` to offer the user to paste the job description directly:
- header: "Job Details"
- question: "I couldn't access the Upwork posting directly. How would you like to provide the job details?"
- options:
  - "I'll paste the description" (description: "Copy and paste the job posting text here")
  - "Try browser automation" (description: "Use Chrome to read the page — requires the tab to be open and logged in")

**Fallback 2**: If the user chooses browser automation, use the `mcp__claude-in-chrome__` browser tools:
1. Call `tabs_context_mcp` to get available tabs
2. Create a new tab with `tabs_create_mcp`
3. Navigate to the project URL
4. Use `get_page_text` to extract the full page content
5. Parse out: job title, full description, required skills, budget, project length, experience level, client info, and any application questions

**CRITICAL**: Capture the EXACT job title, ALL listed required skills, and any specific questions the client wants answered in the proposal. These drive the cover letter.

---

## Step 3: Fetch Current Upwork Profile

**IMPORTANT**: Always fetch the live profile every time because it changes frequently.

Fetch: `https://www.upwork.com/freelancers/~01963827fee19ce894`

**Primary method**: Use `WebFetch` with the prompt:
"Extract ALL freelancer profile details: name, professional title, overview/bio, hourly rate, job success score, total earnings, skills listed, work history (job titles, client feedback, dates), portfolio items, certifications, and any specializations."

**Fallback**: If WebFetch returns a 403 or fails, use browser tools:
1. Navigate to the profile URL in a tab
2. Use `get_page_text` to extract the full profile content
3. Parse out all profile details

---

## Step 4: Fetch Website Resume

Fetch: `https://cliftoncanady.com/resume/`

Use `WebFetch` with the prompt:
"Extract the complete resume: name, title, professional summary, all work experience (company, role, dates, descriptions), education, certifications, and skills."

---

## Step 5: Clarify Anything Unclear

After reviewing the project details, if ANYTHING is ambiguous, confusing, or could be interpreted multiple ways, use `AskUserQuestion` to clarify BEFORE writing the cover letter.

**Examples of when to ask:**
- The project description is vague about scope or deliverables
- It's unclear which of your skills/experiences would be most relevant to highlight
- The project spans multiple disciplines and you need to know which angle to lead with
- The budget seems misaligned with the scope (should you address this in the letter?)
- The client asks questions in the posting that need your input to answer well
- There are technologies or tools mentioned you want to confirm your experience with
- The project could be approached multiple ways and you want to confirm the right angle

**Format**: Use `AskUserQuestion` with specific, targeted questions based on what you found in the posting. Make the options reflect the actual ambiguity - not generic choices. Ask as many rounds of questions as needed until everything is clear.

If the project is straightforward and requirements are crystal clear, skip this step and proceed.

---

## Step 6: Analyze & Match

Before writing, perform this analysis silently:

1. **Extract client pain points** - What problem is the client trying to solve? What outcomes do they need?
2. **Identify required skills** - List every skill mentioned or implied in the posting
3. **Match experience** - For each required skill/need, find the strongest matching evidence from:
   - Upwork profile (job history, success score, client feedback)
   - Website resume (work experience, certifications)
   - Portfolio items or relevant projects
   - **IMPORTANT**: Use the user's specific platform/tool years (e.g., "20 years of WordPress", "9 years of Elementor") rather than generalizing to "web development." Always reference the exact technology and duration the user claims.
4. **Spot differentiators** - What makes Clifton uniquely qualified vs. generic applicants?
5. **Note client questions** - If the posting asks specific questions, prepare answers
6. **Identify client type** - Small business, startup, agency, enterprise? Adjust tone accordingly

---

## Step 7: Generate Cover Letter

Write a compelling, personalized cover letter following these rules:

### Format & Length
- **Maximum 5,000 characters** (this is a hard limit - count characters)
- Short paragraphs (2-4 sentences max)
- Use line breaks between sections for readability on Upwork's interface
- No headers, bullet points should be minimal - this reads as a personal message

### Structure

**Opening (1-2 sentences)**
- Reference something SPECIFIC from their project description (not generic)
- Show you actually read and understood their needs
- Hook them immediately with relevance

**The Bridge (2-3 sentences)**
- Connect their specific problem to your direct experience
- Name a similar project you completed or a directly relevant skill
- Be concrete - mention actual technologies, tools, or outcomes

**Proof of Competence (3-5 sentences)**
- Draw from Upwork work history, job success score, and client feedback
- Reference specific projects from resume/portfolio that align
- Include measurable results where possible (years of experience, number of projects, specific outcomes)
- Mention relevant certifications (Jasper AI, WordPress expertise, etc.) ONLY if they apply to this job

**Understanding Their Needs (2-3 sentences)**
- Demonstrate you understand the project scope and challenges
- Mention your approach or how you'd tackle their specific requirements
- If they asked questions in the posting, weave answers in naturally

**Call to Action (1-2 sentences)**
- Express interest in discussing things further without specifying a medium (do NOT suggest jumping on a call)
- Express genuine interest without being desperate
- Keep it confident and professional

### Tone & Voice
- Apply the tone preference the user selected in Step 1
- Direct and specific - no filler phrases
- Write like a real person, not a template
- Match energy to the client's posting tone (casual vs. formal)

### What to AVOID
- Generic openings ("I am writing to express my interest...")
- Listing every skill you have (only relevant ones)
- Desperation or begging language
- Repeating the job description back to the client
- Overusing "I" at the start of sentences
- Buzzwords and jargon the client didn't use
- Mentioning that AI helped write this
- Going over 5,000 characters
- Em-dashes — use periods, commas, or natural sentence breaks instead

---

## Step 8: Review with User

Present the cover letter in a clean, copy-paste ready format:

1. Display a brief summary header:
   - Project title
   - Key skills matched
   - Character count

2. Display the cover letter inside a code block so formatting is preserved and easy to copy

3. After the cover letter, provide:
   - **Character count** (must be under 5,000)
   - **Skills matched** - list of project requirements you addressed
   - **Talking points** - 2-3 key differentiators to emphasize if you get an interview
   - **Suggested bid range** - based on project budget, your rate, and job complexity

4. Use `AskUserQuestion` to ask for feedback:
   - header: "Feedback"
   - question: "How does this cover letter look?"
   - options:
     - "Looks great, I'm done" (description: "Cover letter is ready to submit")
     - "Make it shorter" (description: "Trim it down, keep only the strongest points")
     - "Make it more detailed" (description: "Add more specifics about experience and approach")
     - "I have specific edits" (description: "I'll tell you what to change")

If the user wants changes, revise and present again. Repeat until they're satisfied.

---

## Notes

- **ALWAYS use `AskUserQuestion`** for every interaction - never ask questions as plain text
- If the Upwork project URL is invalid or the page can't be loaded, use `AskUserQuestion` to ask for a corrected URL
- If the project requires skills not found in the profile or resume, acknowledge gaps honestly and suggest how adjacent experience applies
- Always prioritize the most recent and relevant experience from the live Upwork profile
- The cover letter must feel handcrafted for THIS specific project - never generic
