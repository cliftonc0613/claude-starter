---
name: handoff
description: Produce a plain text handoff summary of the full conversation for pasting into a new Claude session. Triggers on the word "handoff" or any request to summarise the chat for a new session.
---

You have been asked to produce a handoff summary. Follow these instructions exactly.

1. Read through the ENTIRE conversation from start to finish.
2. Produce a single plain text block with exactly five sections, each labeled with the section name followed by a colon. Use ONLY plain sentences. No markdown, no bullet points, no formatting characters, no headers with # or *, no dashes as list markers.
3. The five sections are:

Who this is for: One or two sentences describing who the user is and what they are working on, based on what was discussed in this conversation.

What we covered: A paragraph summarising the main topics, decisions made, and work completed during this conversation. Be specific about file names, features, and outcomes.

Still in progress: Anything that was started but not finished, flagged for later, or left open. If nothing is unfinished, write "Nothing was left unfinished."

Next steps: What should be picked up in the next session. Be concrete and actionable.

Rules for the new session: Any preferences, constraints, or working agreements established during this conversation that the next Claude should follow.

4. Rules for writing:
   - No markdown whatsoever. No bullet points. No asterisks. No hash symbols. No code blocks.
   - Write in plain sentences only.
   - Be specific. Reference actual file names, decisions, and outcomes.
   - Do not pad or add filler. Do not invent anything that was not discussed.
   - Write it as if briefing a new Claude who has never seen this conversation.
   - Keep it concise but complete.

5. After producing the handoff block, tell the user: "You can edit any section before pasting this into a new chat."