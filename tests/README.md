# Testing Structure

The repository should grow toward real automated tests as implementations mature.

## Suggested tests

### Python
- intent classification
- empty/invalid input
- session state and recent-message limits

### JavaScript
- request payload construction
- HTTP error handling
- malformed API responses

### PHP
- message normalization
- validation
- request construction

### Integration
Use mocked LLM providers and synthetic APIs. Keep provider-specific tests separate from deterministic unit tests.

### Security
Test unauthorized tool calls, prompt-injection cases, malformed tool arguments, rate limits, and accidental secret exposure.

Public CI must never call a customer's live chatbot or expose production credentials.
