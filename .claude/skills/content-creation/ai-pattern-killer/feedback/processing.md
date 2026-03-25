# Feedback Processing Pipeline

## How Feedback Is Captured

During post-process mode, every interaction is logged:

- **Accept**: User accepts a suggested rewrite -> logged as confirmed pattern
- **Reject**: User rejects a flag (the original was fine) -> logged as false positive
- **Edit**: User modifies the suggested rewrite -> logged as partial match with user's preferred version
- **Skip**: User skips without deciding -> not logged

## Feedback Log Format

Each entry in feedback_log.json follows this structure:

- `timestamp` — ISO 8601
- `pattern_type` — word | phrase | structure
- `pattern_value` — the specific pattern flagged
- `action` — accept | reject | edit
- `context` — surrounding sentence for word/phrase, paragraph for structure
- `user_alternative` — only for edit actions, what the user preferred
- `source_skill` — which skill generated the content (e.g., "upwork-cover-letter")

## Processing Rules

1. Feedback is logged immediately during the session
2. The learning engine processes the log at the END of each post-process session
3. Raw feedback is never deleted — it accumulates as training data
4. Processing checks thresholds defined in config.yaml (default: 3 rejections, 5 confirmations)

## What Triggers Updates

- **3 rejections** of the same pattern -> auto-add to exceptions.json
- **5 accepts** of the same pattern -> elevate confidence tier (medium -> high)
- **3 edits** providing the same alternative -> add to examples.json as preferred rewrite
- **Manual override** by the user -> immediate update, bypasses thresholds

## Conflict Resolution

- If a pattern has BOTH accepts and rejects, only count the net difference
- If exceptions.json and banned lists conflict, exceptions.json wins
- User can manually promote/demote patterns regardless of thresholds
