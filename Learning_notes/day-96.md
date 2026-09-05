# Day 96 — Combine Keyword and Vector Scores

## Objective

Learn hybrid search and build a simple system that combines keyword and vector search scores.

## What I Learned

### What Is Hybrid Search?

Hybrid search combines two search methods:

- **Keyword search** — looks for matching words.
- **Vector search** — looks for similar meaning using embeddings.

```text
                 Query
                   ↓
          ┌────────┴────────┐
          ↓                 ↓
    Keyword Search    Vector Search
          ↓                 ↓
   Keyword Score      Vector Score
          └────────┬────────┘
                   ↓
           Combined Score
                   ↓
             Final Ranking
```

## Why Combine Them?

Keyword search is useful when exact words matter.

Vector search is useful when the meaning is similar even when the exact words are different.

Combining them allows both signals to influence the final ranking.

## Today's Scoring Formula

```text
Combined Score =
    (Keyword Score × 0.3)
    +
    (Vector Score × 0.7)
```

This means:

- Keyword score has 30% weight.
- Vector score has 70% weight.

### Example

```text
Keyword Score = 0.8
Vector Score  = 0.9

Combined Score =
(0.8 × 0.3) + (0.9 × 0.7)

= 0.24 + 0.63

= 0.87
```

A higher combined score means a higher position in the final ranking.

## Today's Build

I created a simple hybrid search function.

```python
import chromadb
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path="./chroma_data"
)

collection = client.get_collection(
    name="documents"
)


def keyword_score(query, document):

    query_words = query.lower().split()
    document_words = document.lower()

    matches = 0

    for word in query_words:

        if word in document_words:
            matches += 1

    if len(query_words) == 0:
        return 0

    return matches / len(query_words)


def hybrid_search(query, k=3):

    data = collection.get(
        include=["documents"]
    )

    documents = data["documents"]

    query_embedding = model.encode(query)

    vector_results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=len(documents),
        include=["documents", "distances"]
    )

    vector_documents = vector_results["documents"][0]
    distances = vector_results["distances"][0]

    results = []

    for document, distance in zip(
        vector_documents,
        distances
    ):

        vector_score = 1 / (1 + distance)

        keyword = keyword_score(
            query,
            document
        )

        combined_score = (
            keyword * 0.3
            +
            vector_score * 0.7
        )

        results.append(
            (combined_score, document)
        )

    results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return results[:k]


query = "Python programming"

results = hybrid_search(
    query,
    k=3
)

print("Query:", query)

print("\nHybrid search results:")

for i, (score, document) in enumerate(results):

    print(f"\nResult {i + 1}")
    print("Score:", round(score, 4))
    print("Document:", document)
```

## Important Parts

### Keyword Score

```python
keyword = keyword_score(query, document)
```

This calculates how many query words appear in the document.

### Vector Score

```python
vector_score = 1 / (1 + distance)
```

This converts the returned vector distance into a simple similarity-style score for this experiment.

### Combined Score

```python
combined_score = (
    keyword * 0.3
    +
    vector_score * 0.7
)
```

This combines the two signals.

### Ranking

```python
results.sort(
    key=lambda x: x[0],
    reverse=True
)
```

This sorts the results from the highest combined score to the lowest.

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
      ↓
Day 96
Hybrid Search
```

Day 95 used keyword search as a backup.

Day 96 goes one step further: **keyword and vector scores are combined and both influence the ranking.**

## Key Concepts

- Hybrid search combines keyword and vector search.
- Keyword search captures exact word matches.
- Vector search captures semantic similarity.
- Scores can be combined using weights.
- The combined score can be used to rank results.
- `0.3` gives keyword matching 30% weight.
- `0.7` gives vector similarity 70% weight.
- Higher combined scores are ranked first.

## What I Built

A simple hybrid search system using:

- Python
- Chroma
- Sentence Transformers
- Keyword scoring
- Vector similarity
- Weighted score combination
- Result ranking
- Top-K retrieval

## One-Line Takeaway

**Hybrid search combines keyword matching and vector similarity so both exact terms and semantic meaning can influence the final ranking.**
