# Chatbot Architecture

A production chatbot is a system of cooperating components rather than a single prompt.

## Reference architecture

```
Channel
  -> API / Gateway
  -> Authentication
  -> Conversation Session
  -> Router
  -> Retrieval / Memory / Tools
  -> Response Generator
  -> Guardrails
  -> Channel
```

## Design boundaries

Keep channel handling separate from conversation logic. Keep external tools behind explicit interfaces. Keep model providers replaceable where practical.

## Reliability

Define timeouts, retry policies, fallback responses, idempotency for write actions, and structured logs.

## Safety

Use least privilege for tools. Require approval for destructive or externally visible actions when appropriate.

## Testing

Use synthetic conversations, mocked providers, deterministic fixtures, and integration environments. Never use production customer conversations in public tests.
