# Conversation State

Conversation state allows a chatbot to understand the current session without treating the entire transcript as permanent memory.

## Useful state

- conversation ID
- authenticated user or tenant context
- current intent
- workflow state
- selected entities
- pending confirmation
- recent messages
- tool results
- escalation status

## State versus memory

Session state is short-lived operational context. Long-term memory should be selective, explicit, and governed by retention rules.

## Failure handling

If state is missing or inconsistent, prefer a safe clarification or restart rather than guessing.
