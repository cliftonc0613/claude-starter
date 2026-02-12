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

**Question 6** - Ask about personal philosophy or values:
- header: "Philosophy"
- question: "Do you have a personal philosophy or value you want woven into this cover letter?"
- options:
  - "Yes, I'll share it" (description: "I have a mindset, principle, or approach I want reflected in the letter")
  - "No, keep it skills-focused" (description: "Stick to experience and qualifications only")

If the user has a philosophy to share, use a follow-up `AskUserQuestion` to capture it.

---

## Step 2: Gather Project Details

Fetch the Upwork project posting using the URL from Step 1.

**Primary method**: If the user provided the job description directly via `$ARGUMENTS` or pasted it, use that. This is the most reliable method since Upwork consistently blocks automated fetching.

**Fallback**: If no job description was provided, use `AskUserQuestion` to ask the user to paste it:
- header: "Job Details"
- question: "Please paste the full job description from the Upwork posting."
- options:
  - "I'll paste it now" (description: "Copy and paste the job posting text")
  - "I'll provide the URL to try fetching" (description: "Provide the URL and I'll attempt WebFetch, though Upwork often blocks this")

If the user provides a URL, attempt `WebFetch`. If it returns a 403 or fails, ask the user to paste the description directly. Do NOT attempt browser automation.

**CRITICAL**: Capture the EXACT job title, ALL listed required skills, and any specific questions the client wants answered in the proposal. These drive the cover letter.

---

## Step 3: Gather Upwork Profile Context

**IMPORTANT**: Upwork consistently blocks automated profile fetching (403 errors). Do NOT attempt WebFetch or browser automation on the Upwork profile URL.

Instead, use `AskUserQuestion` to gather relevant profile context directly from the user:
- header: "Projects"
- question: "What projects or experience from your Upwork history should I reference in this cover letter?"
- options:
  - "I'll list relevant projects" (description: "I'll describe specific Upwork projects, clients, or outcomes to include")
  - "Use my resume only" (description: "Skip Upwork-specific projects and work from the resume data")

If the user provides project details, incorporate them into the cover letter. If they choose resume only, proceed with resume data from Step 4.

Additionally, if the job posting involves collaboration or working under a creative director, proactively ask about agency background:
- header: "Agency Work"
- question: "This role involves working under a creative director/team. Do you have relevant agency or collaborative experience to highlight?"
- options:
  - "Yes, I'll describe it" (description: "I have agency experience working under creative directors or in team environments")
  - "No, skip this" (description: "Focus on independent work and skills")

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

## Step 8: Answer Client Questions

If the job posting includes specific questions for applicants to answer (e.g., "Please describe your experience with X" or "Provide links to past work"), draft responses for each question.

- Write responses in the same tone as the cover letter
- Keep answers focused and specific to what was asked
- If a question requires information you don't have (e.g., links to active sites), use `AskUserQuestion` to gather it from the user before drafting the response
- Present all question responses alongside the cover letter in Step 9

If there are no client questions in the posting, skip this step.

---

## Step 9: Review with User

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

5. After the user approves the final cover letter, use `AskUserQuestion` to offer saving:
   - header: "Save"
   - question: "Want to save this cover letter to knowledge/drafts/ as a markdown file?"
   - options:
     - "Yes, save it" (description: "Save cover letter, client question responses, skills matched, talking points, and bid range to a markdown file")
     - "No thanks" (description: "Skip saving, I'll copy it directly")

If saving, write to `knowledge/drafts/upwork-cover-letter-[short-job-title].md` with all metadata.

---

## Notes

- **ALWAYS use `AskUserQuestion`** for every interaction - never ask questions as plain text
- If the Upwork project URL is invalid or the page can't be loaded, use `AskUserQuestion` to ask for a corrected URL
- If the project requires skills not found in the profile or resume, acknowledge gaps honestly and suggest how adjacent experience applies
- Always prioritize the most recent and relevant experience from the live Upwork profile
- The cover letter must feel handcrafted for THIS specific project - never generic
