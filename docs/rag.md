# Retrieval-Augmented Generation

RAG combines retrieval with generation so a chatbot can answer from a controlled knowledge source.

## Pipeline

```
Question
 -> Query preparation
 -> Retrieval
 -> Filtering / ranking
 -> Context construction
 -> Generation
 -> Citation or source metadata
 -> Validation
```

## Evaluation

Measure retrieval quality separately from answer quality. Test missing information and conflicting documents.

## Safety

Treat retrieved documents as untrusted input. Retrieved text must not automatically gain permission to invoke tools or override system instructions.
