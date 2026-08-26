# Day 86 — Embed and Insert a Document Set

## Objective

Understand how documents are converted into embeddings, inserted into a vector database, and how a vector index such as **HNSW** makes similarity search more efficient.

---

## 1. Today's Big Picture

```text
Documents
    ↓
Embedding Model
    ↓
Vectors
    ↓
Chroma
    ↓
Vector Index
    ↓
Ready for Similarity Search
```

Remember:

```text
Embedding Model → creates vectors
Chroma          → stores vectors + documents
Vector Index    → organizes vectors for search
HNSW            → one type of vector index
```

---

## 2. What Is a Vector Index?

Imagine we have many vectors:

```text
Vector 1
Vector 2
Vector 3
Vector 4
...
Vector 1,000,000
```

A query needs to find the vectors closest to it.

Without an efficient index, we could compare the query against every vector:

```text
Query
 ↓
Vector 1 → compare
Vector 2 → compare
Vector 3 → compare
...
Vector 1,000,000 → compare
 ↓
Find closest vectors
```

This is **brute-force / exact nearest-neighbour search**.

A vector index creates a search structure that helps find promising nearby vectors without blindly scanning every stored vector.

---

## 3. What Is HNSW?

**HNSW** stands for:

```text
Hierarchical Navigable Small World
```

For today, don't focus on the name.

Think of HNSW as a **network of connections between vectors** that helps the search navigate toward nearby vectors.

```text
Query
  ↓
HNSW Index
  ↓
Promising region
  ↓
Nearby candidates
  ↓
Similar vectors
```

---

## 4. HNSW Does NOT Create the Embeddings

```text
Embedding Model
      ↓
Creates the vector

HNSW
      ↓
Helps search the vectors
```

Therefore:

```text
Embedding ≠ HNSW
```

The embedding model creates the representation.

The index helps retrieve vectors efficiently.

---

## 5. HNSW Does NOT Create Your IDs

You create the document IDs:

```python
ids = [
    "doc1",
    "doc2",
    "doc3"
]
```

Chroma stores them.

```text
You
 ↓
"doc1"
 ↓
Chroma
```

HNSW is not responsible for creating document IDs.

---

## 6. Three Responsibilities

| Component | Job |
|---|---|
| Embedding model | Creates the vector |
| Chroma | Stores document + vector + ID |
| HNSW index | Helps find nearby vectors efficiently |

Memory trick:

```text
Embedding = CREATE
Chroma    = STORE
Index     = FIND
```

---

## 7. Install the Required Packages

```bash
pip install sentence-transformers chromadb
```

---

## 8. Today's Build

Create:

```text
embed_and_insert.py
```

```python
import chromadb
from sentence_transformers import SentenceTransformer


# 1. Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Create persistent Chroma database
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# 3. Create or load a collection
collection = client.get_or_create_collection(
    name="document_set"
)


# 4. Our document set
documents = [
    "Python is a programming language.",
    "Machine learning allows computers to learn from data.",
    "Deep learning uses neural networks.",
    "Pizza is a popular Italian food.",
    "London is the capital of the United Kingdom.",
    "Paris is the capital of France.",
]


# 5. Convert documents into embeddings
embeddings = model.encode(documents)


# 6. Insert documents and embeddings into Chroma
collection.upsert(
    ids=[
        "doc1",
        "doc2",
        "doc3",
        "doc4",
        "doc5",
        "doc6",
    ],
    documents=documents,
    embeddings=embeddings.tolist(),
)


# 7. Check how many records exist
print("Documents stored:", collection.count())


# 8. Show embedding shape
print("Embedding shape:", embeddings.shape)


# 9. Search the collection
query = "I want to learn programming."

results = collection.query(
    query_texts=[query],
    n_results=3
)


print("\nQuery:")
print(query)

print("\nResults:")

for document in results["documents"][0]:
    print("-", document)
```

---

## 9. What Happens at the Embedding Step?

```python
embeddings = model.encode(documents)
```

For six documents:

```text
6 documents
     ↓
all-MiniLM-L6-v2
     ↓
6 × 384 vectors
```

So:

```python
print(embeddings.shape)
```

will produce:

```text
(6, 384)
```

Conceptually:

```text
Document 1 → [384 numbers]
Document 2 → [384 numbers]
Document 3 → [384 numbers]
Document 4 → [384 numbers]
Document 5 → [384 numbers]
Document 6 → [384 numbers]
```

---

## 10. What Does `.tolist()` Do?

The embedding model returns a NumPy array.

```python
embeddings.tolist()
```

converts that NumPy array into regular Python lists.

It does **not** change the embedding meaning or values.

---

## 11. What Does `upsert()` Do?

```python
collection.upsert(
    ids=...,
    documents=...,
    embeddings=...
)
```

tells Chroma to store the records.

Conceptually:

```text
doc1
 │
 ├── Document:
 │   "Python is a programming language."
 │
 └── Vector:
     [384 numbers]
```

The relationship between ID, document and vector is maintained by the database.

---

## 12. What Does the Vector Database Look Like?

Conceptually:

```text
┌─────────────────────────────────────────────┐
│                 CHROMA                      │
│              document_set                   │
├────────┬─────────────────────┬──────────────┤
│ ID     │ Document            │ Embedding    │
├────────┼─────────────────────┼──────────────┤
│ doc1   │ Python...           │ [384 nums]   │
│ doc2   │ Machine learning... │ [384 nums]   │
│ doc3   │ Deep learning...    │ [384 nums]   │
│ doc4   │ Pizza...            │ [384 nums]   │
│ doc5   │ London...           │ [384 nums]   │
│ doc6   │ Paris...            │ [384 nums]   │
└────────┴─────────────────────┴──────────────┘
```

This is the main mental model.

---

## 13. Where Does HNSW Fit?

HNSW is **not another document column**.

Think of it as a search structure associated with the stored vectors.

```text
Documents + Vectors
        ↓
      Chroma
        ↓
   Vector Index
        ↓
      HNSW
        ↓
Efficient nearest-neighbour search
```

So:

```text
Data
→ stores the records

Index
→ helps search the vectors
```

---

## 14. Without HNSW

Suppose we have one million vectors.

An exact brute-force search could do:

```text
Query
 ↓
Compare with Vector 1
 ↓
Compare with Vector 2
 ↓
Compare with Vector 3
 ↓
...
 ↓
Compare with Vector 1,000,000
 ↓
Choose closest vectors
```

This checks everything.

---

## 15. With HNSW

HNSW provides a navigation structure:

```text
Query
 ↓
HNSW
 ↓
Navigate through promising connections
 ↓
Nearby candidates
 ↓
Top similar vectors
```

The intuition is:

```text
Brute force
→ Check everything

HNSW
→ Navigate toward promising candidates
```

---

## 16. Exact vs Approximate Search

### Brute-force / exact

```text
Query
 ↓
Check every vector
 ↓
Find exact nearest neighbours
```

### HNSW / approximate nearest neighbour

```text
Query
 ↓
Index
 ↓
Search promising candidates
 ↓
Nearest neighbours
```

HNSW is designed for efficient approximate nearest-neighbour search. This can trade some recall for substantially faster retrieval at scale.

---

## 17. Search Workflow

When the user searches:

```python
query = "I want to learn programming."
```

the query is converted into an embedding:

```text
"I want to learn programming."
            ↓
      Embedding Model
            ↓
       Query Vector
```

Then:

```text
Query Vector
      ↓
Vector Index
      ↓
Nearby vectors
      ↓
Top K results
```

---

## 18. What Does `n_results=3` Mean?

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

## 19. Complete Day 86 Workflow

```text
                 DOCUMENT INGESTION

Documents
    ↓
Embedding Model
    ↓
384D Vectors
    ↓
Chroma
    ↓
Store:
ID + Document + Vector
    ↓
Vector Index
    ↓
Ready for Search
```

Then:

```text
                    SEARCH

User Query
    ↓
Embedding Model
    ↓
Query Vector
    ↓
Vector Index
    ↓
Nearest Neighbours
    ↓
Top K Documents
```

---

## 20. Simple Analogy

Imagine a huge library.

### Embedding

Gives every book a location based on its meaning.

```text
Programming books → Programming area
Cooking books     → Cooking area
Travel books      → Travel area
```

### Chroma

Stores the books and their information.

### HNSW

Provides shortcuts/navigation through the library so you don't have to inspect every book.

```text
Query:
"I want to learn Python"

        ↓

HNSW navigation

        ↓

Programming area

        ↓

Python-related documents
```

---

## 21. Embedding vs Indexing

### Embedding

```text
Text
 ↓
[384 numerical values]
```

Purpose:

> Represent semantic information numerically.

### Index

```text
Many vectors
 ↓
Search structure
 ↓
Efficient nearest-neighbour retrieval
```

Purpose:

> Help find similar vectors efficiently.

Therefore:

```text
Embedding ≠ Index
```

---

## 22. Connection to RAG

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

---

## 23. Day 78 → Day 86

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
Contextual Representations
 ↓
Output
```

### Day 84 — Context + Embeddings

```text
Context
 ↓
Transformer / Attention
 ↓
Contextual Representations
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
 ↓
Vector Search
```

### Day 86 — Vector Index

```text
Embeddings
 ↓
Chroma
 ↓
Vector Index / HNSW
 ↓
Efficient Similarity Search
```

---

## 24. Key Formulas

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

The key mathematical idea remains:

```text
Query Vector
      ↓
Similarity / Distance
      ↓
Find nearby vectors
```

HNSW changes **how efficiently we search**, not how the embedding itself is created.

---

## 25. What I Learned Today

- A document can be converted into an embedding before being inserted into Chroma.
- `all-MiniLM-L6-v2` produces 384-dimensional sentence embeddings.
- `embeddings.shape` shows the number of documents and dimensions.
- `.tolist()` converts the NumPy embedding array into Python lists.
- `upsert()` stores IDs, documents and embeddings in the Chroma collection.
- A vector database stores the document together with its vector representation.
- A vector index is a search structure for finding nearby vectors efficiently.
- HNSW is one type of approximate nearest-neighbour vector index.
- HNSW does not create embeddings.
- HNSW does not create document IDs.
- IDs identify records; embeddings represent meaning; the index helps retrieve nearby vectors.
- Brute-force search compares the query against every stored vector.
- HNSW navigates through promising candidates instead of blindly scanning everything.
- HNSW improves search efficiency at large scale, with an approximate-search trade-off.
- `n_results=3` requests the top 3 search results.
- Vector indexing is an important part of scalable semantic search and RAG.

---

## One-Line Takeaway

> **The embedding model creates the vectors, Chroma stores the documents and vectors, and an index such as HNSW helps find similar vectors efficiently without blindly comparing the query with every stored vector.**
