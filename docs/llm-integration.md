# LLM Integration

LLM integration should be treated as a replaceable service boundary.

## Provider abstraction

A useful interface can expose:

- model
- messages
- temperature or equivalent generation controls
- timeout
- structured output requirements
- usage metadata
- error classification

## Reliability

Handle provider timeout, rate limit, invalid response, unavailable model, and malformed structured output separately.

## Cost control

Track tokens or provider usage where available. Use smaller models for classification or extraction when they meet the quality requirement.

## Security

Never place API keys in prompts, source code, examples, or logs.
