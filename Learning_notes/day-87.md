# Day 87 — Query by Similarity

## Objective

Understand how Chroma and FAISS perform vector similarity search, and build a query that retrieves the most semantically similar documents.

---

## 1. Today's Big Picture

Yesterday:

```text
Documents
    ↓
Embedding
    ↓
Vectors
    ↓
Chroma
    ↓
Store
```

Today:

```text
User Query
    ↓
Embedding
    ↓
Query Vector
    ↓
Vector Search
    ↓
Similar Documents
```

The key idea is:

> The query and stored documents must be converted into vectors in the same embedding space before similarity search can happen.

---

## 2. Why Do We Embed the Query?

Suppose Chroma contains:

```text
doc1 → "Python is a programming language."
doc2 → "Machine learning uses data."
doc3 → "Pizza is an Italian food."
doc4 → "London is the capital of the UK."
```

The user asks:

```text
"I want to learn coding."
```

The query starts as text.

We cannot directly compare:

```text
Text ↔ Vector
```

So we convert the query into a vector:

```text
"I want to learn coding."
          ↓
    Embedding Model
          ↓
      Query Vector
```

Now we can compare:

```text
Query Vector
      ↕
Document Vector
```

---

## 3. Query Workflow

```text
User Query
    ↓
Embedding Model
    ↓
Query Vector
    ↓
Vector Search
    ↓
Similarity / Distance
    ↓
Top K Results
    ↓
Relevant Documents
```

---

## 4. Chroma vs FAISS

### Chroma

Think:

> Vector database + storage + retrieval

```text
Documents
    +
Embeddings
    +
IDs
    +
Metadata
    ↓
Chroma
```

### FAISS

Think:

> Vector similarity search library

```text
Vectors
   ↓
FAISS Index
   ↓
Similarity Search
```

Simple mental model:

```text
Chroma → database-oriented
FAISS  → similarity-search/index-oriented
```

---

## 5. Today's Chroma Build

Create:

```text
query_similarity.py
```

```python
import chromadb
from sentence_transformers import SentenceTransformer


# 1. Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Connect to our existing Chroma database
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# 3. Load the existing collection
collection = client.get_or_create_collection(
    name="document_set"
)


# 4. User query
query = "I want to learn coding."


# 5. Convert query into an embedding
query_embedding = model.encode(query)


# 6. Search Chroma using the query embedding
results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=3
)


# 7. Display results
print("Query:")
print(query)

print("
Most similar documents:")

for i, document in enumerate(results["documents"][0]):
    print(f"{i + 1}. {document}")
```

Run:

```bash
python query_similarity.py
```

---

## 6. What Is Different From Day 86?

### Day 86

```text
Documents
    ↓
Embedding
    ↓
Vectors
    ↓
Chroma
    ↓
Store
```

### Day 87

```text
User Query
    ↓
Embedding
    ↓
Query Vector
    ↓
Chroma
    ↓
Similarity Search
    ↓
Top 3 Documents
```

Day 86 focused on **inserting**.

Day 87 focuses on **retrieving**.

---

## 7. Stored Documents vs Query

### Stored document

```text
"Python is a programming language."
             ↓
       Embedding Model
             ↓
       Document Vector
             ↓
           Chroma
```

### User query

```text
"I want to learn coding."
             ↓
       Embedding Model
             ↓
         Query Vector
```

Then:

```text
Query Vector
      ↕
Document Vectors
      ↓
Similarity Search
```

---

## 8. What Is Actually Being Compared?

Conceptually:

```text
Query Vector
[0.12, -0.43, 0.71, ...]
        ↕
     similarity
        ↕
Document Vector
[0.15, -0.40, 0.68, ...]
```

If their directions are similar, cosine similarity is high.

```text
Similar vector direction
        ↓
Higher similarity
        ↓
Likely related meaning
```

---

## 9. Cosine Similarity

```text
cosine similarity(A, B)
= (A · B) / (||A|| × ||B||)
```

Dot product:

```text
A · B = Σᵢ(aᵢ × bᵢ)
```

The cosine similarity focuses on the angle between vectors.

```text
Same direction
      ↓
High similarity

Different direction
      ↓
Low similarity
```

---

## 10. What Does `n_results=3` Mean?

```python
n_results=3
```

means:

> Return the top 3 results.

Conceptually:

```text
Query
 ↓
Search
 ↓
1. Python programming
2. Machine learning
3. Deep learning
```

---

## 11. Understanding `query_embeddings`

This:

```python
query_embedding = model.encode(query)
```

creates the query vector.

Then:

```python
query_embeddings=[
    query_embedding.tolist()
]
```

passes that vector to Chroma.

So:

```text
Query text
    ↓
SentenceTransformer
    ↓
384-dimensional vector
    ↓
Chroma query
```

---

## 12. Why Must We Use the Same Embedding Model?

If stored documents were embedded using:

```text
all-MiniLM-L6-v2
```

the query should also use:

```text
all-MiniLM-L6-v2
```

Conceptually:

```text
Document
   ↓
Model A
   ↓
Vector Space A

Query
   ↓
Model A
   ↓
Vector Space A
```

Now they can be compared.

Using completely different embedding models generally produces incompatible vector spaces.

---

## 13. HNSW Connection

From Day 86:

```text
Embedding
    ↓
Vector
    ↓
Chroma
    ↓
Vector Index
    ↓
HNSW
```

Today:

```text
Query Vector
      ↓
HNSW / Vector Index
      ↓
Navigate toward promising candidates
      ↓
Similar Vectors
      ↓
Documents
```

HNSW does not create the vector.

Remember:

```text
Embedding → CREATE
Chroma    → STORE
HNSW      → SEARCH EFFICIENTLY
```

---

## 14. What If HNSW Doesn't Exist?

Vector search can still work.

### Brute-force search

```text
Query Vector
     ↓
Compare with Vector 1
Compare with Vector 2
Compare with Vector 3
...
Compare with every vector
     ↓
Find closest vectors
```

This is exact nearest-neighbour search.

### HNSW

```text
Query Vector
     ↓
HNSW
     ↓
Promising candidates
     ↓
Nearby vectors
     ↓
Top results
```

So:

> Vector search does not require HNSW. HNSW is an indexing approach that makes approximate nearest-neighbour search more efficient at large scale.

---

## 15. FAISS Basic Example

```python
import faiss
import numpy as np


vectors = np.array([
    [1.0, 0.0],
    [0.9, 0.1],
    [0.0, 1.0],
], dtype="float32")


index = faiss.IndexFlatL2(2)

index.add(vectors)


query = np.array([
    [0.95, 0.05]
], dtype="float32")


distances, indices = index.search(query, 2)


print("Distances:")
print(distances)

print("
Indices:")
print(indices)
```

Workflow:

```text
Vectors
   ↓
FAISS Index
   ↓
Query
   ↓
Nearest vectors
```

---

## 16. Chroma vs FAISS — Simple Comparison

| | Chroma | FAISS |
|---|---|---|
| Main purpose | Vector database | Vector similarity search |
| Stores documents | Yes | Not inherently |
| Stores metadata | Yes | Not inherently |
| Persistence workflow | Yes | Index-focused |
| Similarity search | Yes | Yes |
| Indexing | Yes | Yes |
| Useful in RAG | Yes | Often as a search component |

For today's task, you do not need to master every FAISS index type.

Remember:

```text
FAISS = powerful vector search library

Chroma = vector database + search
```

---

## 17. Semantic Search vs Keyword Search

### Keyword search

Looks for matching words.

```text
Query:
"learn coding"

Document:
"Python is a programming language."
```

There may be no exact keyword match for `"coding"`.

### Semantic search

Looks for similar meaning.

```text
"learn coding"
      ↓
Vector representation
      ↓
"Python is a programming language."
      ↓
Similar vector
```

This is why embeddings are useful for semantic search.

---

## 18. Connection to RAG

### Ingestion

```text
Company Documents
       ↓
Chunking
       ↓
Embedding Model
       ↓
Vectors
       ↓
Chroma
       ↓
Vector Index
```

### Retrieval

```text
User Question
       ↓
Query Embedding
       ↓
Vector Search
       ↓
Top K Relevant Chunks
       ↓
LLM
       ↓
Answer
```

The retrieval system finds relevant information before the LLM generates the answer.

---

## 19. Day 78 → Day 87

### Day 78 — Embeddings

```text
Text
 ↓
Embedding
 ↓
384D vector
```

### Day 79 — Similarity

```text
Vector A
 ↕
Cosine Similarity
 ↕
Vector B
```

### Day 80 — Clustering

```text
Many vectors
 ↓
K-Means
 ↓
Clusters
```

### Day 81 — Visualisation

```text
384D
 ↓
PCA
 ↓
2D
 ↓
Visualisation
```

### Day 82 — Semantic Search

```text
Query
 ↓
Embedding
 ↓
Similarity Search
 ↓
Most Similar Item
```

### Day 83 — Transformer

```text
Tokens
 ↓
Attention
 ↓
Context
 ↓
Representation
```

### Day 84 — Context + Embeddings

```text
Context
 ↓
Transformer / Attention
 ↓
Contextual Representation
 ↓
Embedding
```

### Day 85 — Vector Database

```text
Embeddings
 ↓
Chroma
 ↓
Persistent Storage
```

### Day 86 — Vector Index

```text
Vectors
 ↓
Vector Index
 ↓
HNSW
 ↓
Efficient Search
```

### Day 87 — Query by Similarity

```text
Query
 ↓
Query Embedding
 ↓
Vector Search
 ↓
Top Similar Documents
```

---

## 20. Key Formulas

### Cosine Similarity

```text
cosine similarity(A, B)
= (A · B) / (||A|| × ||B||)
```

### Dot Product

```text
A · B = Σᵢ(aᵢ × bᵢ)
```

### Euclidean Distance

```text
d(A,B) = √(Σᵢ(aᵢ - bᵢ)²)
```

The search system uses a similarity or distance measure to determine which vectors are closest to the query.

---

## 21. What I Learned Today

- A query must be converted into a vector before semantic vector search can happen.
- The query and stored documents should use the same embedding model and compatible vector space.
- `model.encode(query)` creates the query embedding.
- `query_embeddings` allows us to explicitly send that embedding to Chroma.
- `n_results=3` requests the top 3 results.
- Chroma can store documents and their embeddings and perform similarity search.
- FAISS is a library focused on efficient vector similarity search and indexing.
- Chroma is more database-oriented, while FAISS is more search/index-oriented.
- HNSW is an indexing approach, not an embedding model.
- Without an index, brute-force search can compare the query with every stored vector.
- HNSW helps navigate toward promising candidates for efficient approximate nearest-neighbour search.
- Semantic search can find related meaning even when exact keywords are different.
- Query-by-similarity is the retrieval mechanism that will later become a core part of RAG.

---

## One-Line Takeaway

> **Convert the user query into the same vector space as the stored documents, search for the closest vectors, and return the documents associated with those vectors.**
