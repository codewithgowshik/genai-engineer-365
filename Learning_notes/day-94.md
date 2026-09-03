# Day 94 — Embed Queries and Retrieve Top-K

## Objective

Learn how search queries are converted into embeddings and build a semantic search function that retrieves the top-K most similar results.

## What I Learned

### Query Embedding

Documents are converted into embeddings so they can be stored and searched as vectors.

The search query also needs to be converted into an embedding.

```text
Query
"I want to learn programming."
        ↓
Embedding Model
        ↓
Query Vector
```

The query vector can then be compared with the vectors stored in Chroma.

## Semantic Search Workflow

```text
Documents
    ↓
Document Embeddings
    ↓
Chroma
    ↓
        Query
          ↓
    Query Embedding
          ↓
    Similarity Search
          ↓
       Top-K Results
```

## What Does Top-K Mean?

**K** represents the number of results to retrieve.

For example:

```python
k = 3
```

means:

```text
Return the 3 most similar results.
```

## Today's Build

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

query = "I want to learn programming"

query_embedding = model.encode(query)

k = 3

results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=k
)

print("Query:")
print(query)

print("\nTop", k, "results:")

for i, document in enumerate(results["documents"][0]):
    print(f"\nResult {i + 1}:")
    print(document)
```

## Understanding the Important Parts

### `model.encode(query)`

```python
query_embedding = model.encode(query)
```

This converts the user's text query into a numerical vector.

### `query_embeddings`

```python
query_embeddings=[query_embedding.tolist()]
```

This sends the query vector to Chroma for similarity search.

### `n_results`

```python
n_results=k
```

This tells Chroma how many similar results to return.

## Connection to Previous Days

Day 92 introduced semantic search.

Day 93 introduced chunking and experimenting with chunk sizes.

Day 94 adds query embedding and explicit Top-K retrieval.

```text
Day 92 → Semantic Search
Day 93 → Chunking
Day 94 → Query Embedding + Top-K
```

## Key Concepts

- The search query can be converted into an embedding.
- Query embeddings allow semantic comparison with stored document embeddings.
- Chroma can retrieve the most similar results.
- Top-K means retrieving the K most similar results.
- `n_results` controls how many results Chroma returns.
- Query embedding is an important part of a semantic search pipeline.

## What I Built

A semantic search program using:

- Python
- Sentence Transformers
- `all-MiniLM-L6-v2`
- Query embeddings
- Chroma
- Top-K retrieval

## One-Line Takeaway

**Query embedding converts the user's search into a vector, and Top-K retrieval returns the most similar stored results.**
