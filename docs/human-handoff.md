# Human Handoff

A chatbot should have a clear escalation path when automation is uncertain or inappropriate.

## Escalation triggers

- low confidence
- repeated failed attempts
- sensitive account issue
- payment dispute
- security concern
- user explicitly requests an agent
- action requires human approval

## Handoff data

Pass only the context required for the human agent to continue the conversation.

## Recovery

Record the handoff state so the chatbot does not continue conflicting automated actions while a human is handling the case.
