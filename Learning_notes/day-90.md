# Day 90 — Persist and Reload the Index

## Objective

Understand metadata and filtering, then prove that a persistent Chroma database can be closed and loaded again without recreating the stored data.

## 1. Today's Big Picture

```text
Documents / Vectors
        ↓
      Chroma
        ↓
 ./chroma_data/
        ↓
   Stored on disk
        ↓
Program closes
        ↓
Data remains
        ↓
Program starts again
        ↓
Existing collection loads
```

## 2. What Is Persistence?

Persistence means **saving database data so it remains available after the Python process stops**.

```python
client = chromadb.PersistentClient(
    path="./chroma_data"
)
```

The path `./chroma_data/` is where the local Chroma database is persisted.

### Simple memory trick

> **Persist = save it. Reload = use it again later.**

## 3. Why Persistence Matters

```text
Run program
    ↓
Store data
    ↓
Close program
    ↓
Data remains
    ↓
Start program again
    ↓
Connect to the same database
    ↓
Use existing data
```

We do not need to recreate and insert the entire dataset every time the application starts.

## 4. Metadata and Filtering Review

Metadata is additional structured information about a document.

Example:

```text
Document:
"Python is a programming language."

Metadata:
category = programming
```

A filter can use this metadata:

```python
where={"category": "programming"}
```

This means:

> Only consider documents whose metadata category is `programming`.

Conceptually:

```text
All documents
      ↓
Metadata filter
      ↓
Eligible documents
      ↓
Similarity search
      ↓
Results
```

## 5. Today's Build

Create:

```text
persist_reload.py
```

```python
import chromadb


# 1. Connect to the persistent Chroma database
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# 2. Load the existing collection
collection = client.get_collection(
    name="documents"
)


# 3. Check how many documents survived
print("Collection:", collection.name)
print("Documents stored:", collection.count())


# 4. Read the stored documents
data = collection.get(
    include=["documents"]
)


print("\nStored documents:")

for id, document in zip(
    data["ids"],
    data["documents"]
):
    print(f"{id} → {document}")


# 5. Run a query
query = "I want to learn programming."

results = collection.query(
    query_texts=[query],
    n_results=2
)


# 6. Display search results
print("\nQuery:")
print(query)

print("\nMost similar documents:")

for document in results["documents"][0]:
    print("-", document)
```

Run:

```bash
python persist_reload.py
```

## 6. What Does `zip()` Mean?

In:

```python
for id, document in zip(
    data["ids"],
    data["documents"]
):
```

`zip()` pairs corresponding items from two lists.

Example:

```python
ids = ["doc1", "doc2", "doc3"]

documents = [
    "Python",
    "Machine learning",
    "Pizza"
]
```

`zip()` pairs them:

```text
doc1 → Python
doc2 → Machine learning
doc3 → Pizza
```

So:

```python
zip(ids, documents)
```

means:

> Pair the first ID with the first document, the second ID with the second document, and so on.

## 7. What Does `include=` Mean?

In:

```python
data = collection.get(
    include=["documents"]
)
```

`include` tells Chroma which information we want returned.

Here:

```python
include=["documents"]
```

means:

> Return the documents.

Conceptually, a record can contain:

```text
ID
Document
Embedding
Metadata
```

`include` controls which supported fields are returned by the operation.

It does not add anything to the database.

## 8. What Are We Proving Today?

### Step 1

Run the program that already inserted your documents.

```text
Documents
   ↓
Chroma
   ↓
./chroma_data/
```

### Step 2

Stop the Python program.

### Step 3

Run:

```bash
python persist_reload.py
```

### Step 4

Check:

```text
Documents stored: 4
```

If your four existing documents are still available, persistence is working.

Your current dataset is:

```text
doc1 → Python is a programming language.
doc2 → Machine learning allows computers to learn from data.
doc3 → Pizza is a popular Italian food.
doc4 → London is the capital of the United Kingdom.
```

## 9. Important: Use the Correct Collection

For this project, continue using your actual:

```text
documents
```

collection.

Today's persistence test should use:

```python
collection = client.get_collection(
    name="documents"
)
```

This avoids accidentally switching between different collections.

## 10. Persist vs Reload

### Persist

```text
Memory
  ↓
Chroma
  ↓
Disk
  ↓
./chroma_data/
```

### Reload

```text
./chroma_data/
  ↓
PersistentClient
  ↓
Existing Chroma database
  ↓
Existing collection
```

## 11. What Is Being Persisted?

Conceptually, the persistent Chroma database maintains the information needed for the collection, including stored records and vector-search data.

```text
              ./chroma_data/

        ┌───────────────────────┐
        │ Chroma Database       │
        │                       │
        │ IDs                   │
        │ Documents             │
        │ Embeddings            │
        │ Metadata              │
        │ Search/index data     │
        └───────────────────────┘
```

When the application starts again:

```text
PersistentClient
       ↓
./chroma_data/
       ↓
Existing database
       ↓
Existing collection
       ↓
Existing data
```

## 12. Persistence Does Not Mean Re-Embedding

If the documents have already been embedded and stored, restarting the program does not mean we must recreate the entire collection from scratch.

Instead:

```text
./chroma_data/
   ↓
Existing stored data
   ↓
Load collection
   ↓
Query
```

## 13. Query After Reloading

After loading the existing collection:

```python
query = "I want to learn programming."

results = collection.query(
    query_texts=[query],
    n_results=2
)
```

Workflow:

```text
Existing Chroma database
        ↓
Load collection
        ↓
User query
        ↓
Query embedding
        ↓
Similarity search
        ↓
Top 2 results
```

## 14. Persistence vs Latency

These are different concepts.

### Persistence

> Does my data survive after the program stops?

```text
Chroma
 ↓
Disk
 ↓
Data remains
```

### Latency

> How long does my query take?

```text
Query
 ↓
Search
 ↓
Measure time
```

Remember:

```text
Persistence → DATA LIFETIME

Latency → OPERATION SPEED
```

## 15. Connection to HNSW

Earlier we learned:

```text
Stored vectors
      ↓
Vector index
      ↓
HNSW
      ↓
Efficient search
```

Persistence allows the database and its stored search information to be available across program runs.

Today's focus is not implementing HNSW. It is understanding that the database can be reopened instead of rebuilding the entire collection.

## 16. Connection to RAG

A real RAG application needs persistent storage.

### Ingestion

```text
Documents
    ↓
Chunking
    ↓
Embedding
    ↓
Vectors
    ↓
Chroma
    ↓
Persistent Storage
```

### Later

```text
User Question
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

The vector database can remain available between application restarts.

## 17. Day 85 → Day 90

```text
Day 85
Vector Database
      ↓
Chroma
      ↓
Store vectors
```

```text
Day 86
Vector Index
      ↓
HNSW
      ↓
Efficient search
```

```text
Day 87
Query
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Similar Documents
```

```text
Day 88
Metadata
      +
Filter
      ↓
Controlled Similarity Search
```

```text
Day 89
Persistence
      +
Query
      ↓
Benchmark Latency
```

```text
Day 90
Persistent Database
      ↓
Close Program
      ↓
Open Program Again
      ↓
Reload Existing Collection
      ↓
Query Existing Data
```

## 18. Key Concepts

### Persistence

> Keeping database data available across program runs.

### Reload

> Opening the previously persisted database and accessing the existing collection again.

### Metadata

> Additional structured information about a record.

### Filter

> A condition that restricts which records are eligible for retrieval.

### `zip()`

> Pairs corresponding items from multiple iterables.

### `include=`

> Specifies which supported fields should be returned by a Chroma operation.

## 19. Key Formula

Persistence itself does not require a mathematical formula.

The performance formula from Day 89 remains:

```text
Latency = End Time - Start Time
```

Metadata filtering is a structured condition, not a vector dimension.

## 20. What I Learned Today

- Persistence saves Chroma data beyond the lifetime of a Python process.
- `PersistentClient(path="./chroma_data")` connects to the persistent local database.
- A program can close and later reconnect to the same database.
- Reloading does not mean recreating all documents from scratch.
- The existing `documents` collection can be loaded after restarting the program.
- Metadata provides structured information about stored records.
- `where={...}` can restrict retrieval using metadata.
- `zip()` pairs corresponding IDs and documents.
- `include=["documents"]` tells Chroma which returned field we want from the `get()` operation.
- Persistence and query latency are different concepts.
- Persistent vector databases are important for real-world retrieval and RAG systems.
- HNSW is related to efficient vector search, while persistence concerns keeping the database available across runs.

## One-Line Takeaway

> **Persistence saves your vector database so you can close the program, reopen it later, reload the existing collection, and query the data without rebuilding it from scratch.**
