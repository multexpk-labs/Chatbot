# Chatbot Testing

Testing should cover deterministic components separately from model-dependent behavior.

## Unit tests

Test:

- intent routing
- state transitions
- input validation
- tool schemas
- authorization
- response parsing

## Integration tests

Mock LLM and external APIs for repeatability. Add selected provider integration tests in controlled environments.

## Conversation tests

Use fixture conversations covering normal paths, ambiguity, missing information, tool failures, escalation, and recovery.

## Security tests

Include prompt-injection attempts, unauthorized tool requests, malformed inputs, rate-limit behavior, and secret-leak checks.
