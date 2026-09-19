# Tool Calling

Tools give a chatbot controlled access to external capabilities.

## Tool contract

A tool should define:

- name
- purpose
- input schema
- authorization requirements
- timeout
- expected output
- error behavior
- whether human approval is required

## Execution flow

```
LLM decision
 -> validate tool arguments
 -> authorize
 -> optional approval
 -> execute
 -> validate result
 -> return bounded result
```

The model should never receive unrestricted shell, database, or administrative access.
