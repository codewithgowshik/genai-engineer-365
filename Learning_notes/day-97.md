# Day 97 — Create a Small Relevance Test Set

## Objective

Learn how to evaluate search quality and create a small test set containing queries with known relevant documents.

## What I Learned

### Evaluating Search Quality

I have now built several parts of a search system:

```text
Day 92 → Semantic Search
Day 93 → Chunking
Day 94 → Query Embedding + Top-K
Day 95 → Keyword Fallback
Day 96 → Hybrid Search
```

The next question is:

> How do I know whether my search system is actually returning useful results?

To answer this, I need a small **relevance test set**.

## What Is a Relevance Test Set?

A relevance test set is a collection of:

```text
Query + Expected Relevant Documents
```

For example:

```text
Query:
"What is a programming language?"

Relevant:
doc1
```

The expected relevant document is decided before testing the search system.

## My Current Documents

My Chroma collection contains:

```text
doc1 → Python is a programming language.
doc2 → Machine learning allows computers to learn from data.
doc3 → Pizza is a popular Italian food.
doc4 → London is the capital of the United Kingdom.
```

Based on these documents, I can create test queries and define which document should be relevant.

## Today's Build

I created a small relevance test set:

```python
test_set = [
    {
        "query": "What is a programming language?",
        "relevant_ids": ["doc1"]
    },
    {
        "query": "How do computers learn from data?",
        "relevant_ids": ["doc2"]
    },
    {
        "query": "What is a popular Italian food?",
        "relevant_ids": ["doc3"]
    },
    {
        "query": "What is the capital of the United Kingdom?",
        "relevant_ids": ["doc4"]
    }
]


for test in test_set:

    print("Query:", test["query"])
    print("Relevant documents:", test["relevant_ids"])
    print()
```

## Understanding the Test Set

Each test contains two important pieces of information:

### Query

The question that will be given to the search system.

Example:

```python
"query": "What is a programming language?"
```

### Relevant IDs

The document IDs that I expect to be relevant.

Example:

```python
"relevant_ids": ["doc1"]
```

This means:

> For this query, `doc1` should be considered relevant.

## How the Test Set Will Be Used

The test set gives me a reference for evaluating my search system.

```text
Test Query
    ↓
Run Search
    ↓
Actual Results
    ↓
Compare With
    ↓
Expected Relevant Documents
```

For example:

```text
Expected:
doc1

Search returns:
doc1, doc3, doc2
```

The relevant document `doc1` appeared in the results.

## What Is Relevance?

Relevance means whether a retrieved document is useful for answering the query.

Example:

```text
Query:
"What is Python?"

Python document → Relevant
Pizza document  → Not relevant
```

The test set records these expected relevant results so they can be checked consistently.

## Connection to Previous Days

The search pipeline is now developing into an evaluation workflow:

```text
Documents
    ↓
Embeddings
    ↓
Semantic / Hybrid Search
    ↓
Top-K Results
    ↓
Relevance Test Set
    ↓
Evaluate Search Quality
```

## Key Concepts

- Search quality needs to be evaluated.
- A relevance test set contains test queries and expected relevant document IDs.
- Relevance means whether a result is useful for the query.
- Expected results provide a reference for testing.
- Actual search results can be compared with expected results.
- A small test set is enough to begin evaluating a search system.

## What I Built

A small relevance test set containing:

- Search queries
- Expected relevant document IDs
- A simple script to display the test cases

## One-Line Takeaway

**A relevance test set gives a search system known queries and expected relevant documents so its results can be evaluated consistently.**
