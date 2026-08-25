# Day 85 — Set Up Chroma Locally

## Objective

Understand **why vector databases are needed** and set up **Chroma locally** so embeddings and documents can be stored and searched instead of keeping everything only in Python memory.

---

## 1. Why Do We Need a Vector Database?

So far, we have done:

```text
Documents
    ↓
Embeddings
    ↓
Python list
    ↓
Compare query with vectors
    ↓
Most similar item
```

This works for small datasets.

But imagine:

```text
10 documents
100 documents
1,000 documents
10 million documents
```

Managing all those vectors manually in Python becomes impractical.

A vector database is designed to store vector representations and support similarity-based retrieval.

---

## 2. What Does a Vector Database Store?

A vector database can organize records containing:

```text
ID
Document
Embedding
Metadata
```

Conceptually:

```text
┌──────────────────────────────────────────┐
│              VECTOR DATABASE             │
├──────┬────────────────────┬──────────────┤
│ ID   │ Document           │ Embedding    │
├──────┼────────────────────┼──────────────┤
│ 001  │ Python...          │ [...]        │
│ 002  │ Pizza...           │ [...]        │
│ 003  │ Travel...          │ [...]        │
└──────┴────────────────────┴──────────────┘
```

The database keeps the vector together with the information it represents.

---

## 3. What Is Chroma?

**Chroma** is a vector database/tool designed for AI applications that work with embeddings.

It can be run locally from Python.

A persistent local Chroma client stores its data on disk.

```text
Python Program
      ↓
    Chroma
      ↓
Local Storage
      ↓
Program closes
      ↓
Program starts again
      ↓
Data still exists
```

---

## 4. Before Chroma vs With Chroma

### Before

```text
Documents
    ↓
Embedding Model
    ↓
Vectors
    ↓
Python Memory
    ↓
Similarity Search
```

### With Chroma

```text
Documents
    ↓
Embedding
    ↓
Chroma Collection
    ↓
Persistent Storage
    ↓
Similarity Search
```

This is an important step toward RAG.

---

## 5. Install Chroma

Inside the virtual environment:

```bash
pip install chromadb
```

Check that it works:

```bash
python -c "import chromadb; print(chromadb.__version__)"
```

---

## 6. Create a Local Chroma Database

Create:

```text
chroma_setup.py
```

Code:

```python
import chromadb


# Create a persistent local Chroma database
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# Create or load a collection
collection = client.get_or_create_collection(
    name="documents"
)


print("Chroma is working!")
print("Collection:", collection.name)
print("Documents:", collection.count())
```

Run:

```bash
python chroma_setup.py
```

Expected output will be similar to:

```text
Chroma is working!
Collection: documents
Documents: 0
```

---

## 7. Understanding `PersistentClient`

This code:

```python
client = chromadb.PersistentClient(
    path="./chroma_data"
)
```

means:

> Create a Chroma database whose data is persisted in the `./chroma_data` directory.

Your project can now look like:

```text
Semantic Search Engine/
│
├── venv/
├── chroma_setup.py
└── chroma_data/
```

---

## 8. What Is a Collection?

A **collection** is a container for related records.

Think of it as a logical group of related documents and embeddings.

```text
Chroma Database
      │
      ├── documents
      ├── products
      └── support_articles
```

For today's project:

```python
collection = client.get_or_create_collection(
    name="documents"
)
```

means:

> Get the `documents` collection if it exists; otherwise create it.

---

## 9. Add Documents

We can add records to the collection:

```python
collection.add(
    ids=[
        "doc1",
        "doc2",
        "doc3"
    ],
    documents=[
        "Python is a programming language.",
        "Pizza is a popular Italian food.",
        "London is the capital of the United Kingdom."
    ]
)
```

Each record needs a unique ID.

Chroma can generate embeddings for documents through its configured embedding function.

---

## 10. Query Chroma

Now we can search the collection:

```python
results = collection.query(
    query_texts=[
        "I want to learn programming"
    ],
    n_results=2
)
```

Conceptually:

```text
User Query
     ↓
Embedding
     ↓
Query Vector
     ↓
Vector Search
     ↓
Nearest Documents
```

---

## 11. Complete Day 85 Build

Create:

```text
chroma_setup.py
```

Use:

```python
import chromadb


# 1. Create a persistent local Chroma database
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# 2. Create or load a collection
collection = client.get_or_create_collection(
    name="documents"
)


# 3. Add or update documents
collection.upsert(
    ids=[
        "doc1",
        "doc2",
        "doc3",
        "doc4"
    ],
    documents=[
        "Python is a programming language.",
        "Machine learning allows computers to learn from data.",
        "Pizza is a popular Italian food.",
        "London is the capital of the United Kingdom."
    ]
)


# 4. Show number of stored documents
print("Documents stored:", collection.count())


# 5. Search the collection
query = "I want to learn about programming."

results = collection.query(
    query_texts=[query],
    n_results=2
)


# 6. Display results
print("\nQuery:")
print(query)

print("\nMost relevant documents:")

for document in results["documents"][0]:
    print("-", document)
```

---

## 12. Code Workflow

```text
                 chromadb
                    ↓
             PersistentClient
                    ↓
             Local Database
                    ↓
                Collection
                    ↓
              Add Documents
                    ↓
          Embedding + Indexing
                    ↓
               User Query
                    ↓
          Query Embedding
                    ↓
             Vector Search
                    ↓
          Relevant Documents
```

---

## 13. `add()` vs `upsert()`

### `add()`

Adds new records.

If the same IDs are already present, adding them again can cause duplicate-ID errors.

### `upsert()`

Means approximately:

```text
If ID doesn't exist
    ↓
Insert

If ID already exists
    ↓
Update
```

For repeated testing, `upsert()` is convenient because the script can be run multiple times using the same IDs.

---

## 14. Why Is This Better Than Day 82?

### Day 82

```text
items = [...]

        ↓

Encode items
        ↓
Calculate similarity
        ↓
argmax()
```

Everything was handled directly inside Python.

### Day 85

```text
Documents
     ↓
Chroma Collection
     ↓
Persistent Storage
     ↓
Query
     ↓
Vector Search
     ↓
Relevant Documents
```

The database now manages the storage and retrieval layer.

---

## 15. Important Mental Model

Don't think:

> "A vector database is just a database that stores vectors."

A better mental model is:

> **A vector database stores vector representations together with the data they represent and provides similarity-based retrieval.**

A record can conceptually contain:

```text
ID:
doc42

Document:
"Python is a programming language."

Embedding:
[0.12, -0.43, 0.71, ... 384 values]

Metadata:
{
    "topic": "programming",
    "source": "notes"
}
```

Then we can ask:

```text
"What documents are most similar to this query?"
```

---

## 16. Why Vector Databases Matter for RAG

### Document ingestion

```text
Company Documents
       ↓
Chunking
       ↓
Embeddings
       ↓
Vector Database
```

### User query

```text
"What is our refund policy?"
             ↓
       Query Embedding
             ↓
        Vector Search
             ↓
      Relevant Chunks
             ↓
             LLM
             ↓
           Answer
```

This is the foundation of the retrieval stage in RAG.

---

## 17. Chroma and Embedding Models

Chroma can handle document embedding through its configured embedding function.

You can also provide your own embedding function/model when you need explicit control over which embedding model is used.

Conceptually:

```text
Option A

Document
   ↓
Chroma embedding function
   ↓
Vector
   ↓
Chroma
```

or:

```text
Option B

Document
   ↓
Your embedding model
   ↓
Vector
   ↓
Chroma
```

This distinction becomes important when building a controlled RAG system.

---

## 18. Day 78 → Day 85

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
384D vectors
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
Query Embedding
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
 ↓
Vector Space
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
 ↓
Relevant Documents
```

---

## 19. Key Formulas

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

The important point today is that a vector database uses a similarity/distance mechanism to find vectors that are close to a query vector.

---

## 20. What I Learned Today

- A vector database is designed for storing and retrieving vector representations.
- Storing vectors in a database is more practical than keeping everything in Python memory.
- Chroma can be run locally.
- `PersistentClient` allows Chroma data to persist on disk.
- A Chroma collection groups related records.
- Records can contain IDs, documents, embeddings, and metadata.
- `add()` is used to add new records.
- `upsert()` can insert new records or update existing records with the same IDs.
- Chroma can handle document embedding through its configured embedding function.
- You can also provide your own embedding model/function when you need control.
- Vector search compares a query representation against stored representations.
- Vector databases are an important component of RAG systems.
- Day 85 connects the embedding work from Days 78–84 to persistent vector storage and retrieval.

---

## One-Line Takeaway

> **A vector database such as Chroma stores embeddings alongside their source data and makes similarity-based retrieval practical, forming an important foundation for RAG.**
