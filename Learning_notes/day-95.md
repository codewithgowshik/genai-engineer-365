# Day 95 — Add a Keyword Fallback

## Objective

Learn how search results can be ranked and build a simple keyword fallback for semantic search.

## What I Learned

### Ranking Results

Search can return multiple possible results.

Ranking means putting the most relevant results first.

```text
Search
  ↓
Results
  ↓
Rank by relevance
  ↓
Best results first
```

Semantic search ranks results using vector similarity.

## Keyword Search

Keyword search looks for words that actually appear in the document.

Example:

```text
Query:
Python programming

Document:
Python is a programming language.
```

The document contains words related to the query, so keyword search can identify it.

## What Is a Fallback?

A fallback means using another method when the first method does not provide a useful result.

For this project:

```text
User Query
    ↓
Semantic Search
    ↓
Useful results?
   ↙       ↘
 YES       NO
  ↓         ↓
Return   Keyword Search
results       ↓
           Return results
```

The important idea is:

**Semantic search first. Keyword search as a backup.**

## Why Use a Keyword Fallback?

Semantic search is good at understanding meaning.

Keyword search is useful when exact words matter.

For example, a user might search for a specific identifier or term that does not have much semantic meaning.

Using both methods makes the search system more robust.

## Today's Build

I added a simple keyword search function.

```python
def keyword_search(query):

    data = collection.get(
        include=["documents"]
    )

    matches = []

    for document in data["documents"]:

        if query.lower() in document.lower():

            matches.append(document)

    return matches
```

Then I added it as a fallback:

```python
def search(query):

    results = semantic_search(query)

    if results:
        return results

    return keyword_search(query)
```

## Understanding the Fallback

This part:

```python
if results:
    return results
```

means:

> If semantic search returned results, use those results.

This part:

```python
return keyword_search(query)
```

means:

> If semantic search did not return results, try keyword search.

## Connection to Previous Days

```text
Day 92
Semantic Search
      ↓
Day 93
Chunking
      ↓
Day 94
Query Embedding + Top-K
      ↓
Day 95
Keyword Fallback
```

## Key Concepts

- Ranking means ordering results by relevance.
- Semantic search uses meaning and vector similarity.
- Keyword search looks for matching words.
- A fallback is a backup search method.
- Semantic search can be used first.
- Keyword search can be used when semantic search does not provide a useful result.
- Combining retrieval methods can make search more robust.

## What I Built

A simple search system containing:

- Semantic search
- Keyword search
- Keyword fallback
- Basic result ranking

## One-Line Takeaway

**Use semantic search first for meaning, and use keyword search as a backup when exact terms are important or semantic search does not provide a useful result.**
