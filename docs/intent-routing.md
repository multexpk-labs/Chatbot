# Intent Routing

Intent routing maps a user message to a known capability.

## Common strategies

1. Keyword or rule matching
2. Classical classifier
3. Embedding similarity
4. LLM classification
5. Hybrid routing

## Recommended pattern

Use confidence thresholds and an explicit fallback intent such as `unknown` or `needs_clarification`.

Do not allow low-confidence classification to trigger sensitive actions automatically.

## Example

```text
message
  -> normalize
  -> classify
  -> confidence check
  -> route
  -> validate action
```
