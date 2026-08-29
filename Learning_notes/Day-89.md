# Day 89 — Persistence and Benchmark Query Latency

## Objective

Understand how Chroma persistence keeps the vector database available between program runs and benchmark the latency of a similarity query.

## 1. Today's Big Picture

```text
Persistence:

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
Existing data can be loaded
```

Benchmarking:

```text
Query Vector
      ↓
START TIMER
      ↓
Chroma similarity search
      ↓
STOP TIMER
      ↓
Query latency
```

## 2. What Is Persistence?

Persistence means **saving the vector database so that the data survives after the Python program stops**.

```python
client = chromadb.PersistentClient(
    path="./chroma_data"
)
```

The important part is:

```text
./chroma_data/
```

Chroma uses this location for persistent local storage.

## 3. Why Persistence Matters

With persistence:

```text
Run program
    ↓
Store documents + vectors
    ↓
Close program
    ↓
Start program again
    ↓
Connect to same database
    ↓
Existing collection/data is available
```

We don't need to recreate and reinsert all documents every time the application starts.

## 4. What Is Query Latency?

**Latency = how long an operation takes.**

```text
Start
  ↓
Similarity Search
  ↓
End
```

Formula:

```text
Latency = End Time - Start Time
```

Example:

```text
Start = 10.000 seconds
End   = 10.015 seconds

Latency = 0.015 seconds
        = 15 milliseconds
```

## 5. Why Benchmark Query Latency?

A vector database may contain only a few documents today, but eventually it could contain:

```text
10,000
100,000
1,000,000
10,000,000+
```

Benchmarking gives us a measurement of retrieval performance.

## 6. Important Benchmarking Detail

Today's benchmark measures **Chroma query/search latency**, not embedding-model latency.

```text
Query text
    ↓
Embedding Model
    ↓
Query Vector
    ↓
START TIMER
    ↓
Chroma Search
    ↓
STOP TIMER
```

The timer starts **after**:

```python
query_embedding = model.encode(query)
```

This isolates the database/search operation.

## 7. Today's Build

Create:

```text
benchmark_query.py
```

```python
import time
import chromadb
from sentence_transformers import SentenceTransformer


# 1. Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Connect to the persistent Chroma database
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# 3. Load the existing collection
collection = client.get_collection(
    name="documents"
)


# 4. Query
query = "I want to learn programming."


# 5. Convert the query into an embedding
query_embedding = model.encode(query)


# 6. Start timer
start_time = time.perf_counter()


# 7. Run similarity search
results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=2
)


# 8. Stop timer
end_time = time.perf_counter()


# 9. Calculate latency
latency = end_time - start_time


# 10. Display results
print("Query:")
print(query)

print("\nResults:")

for document in results["documents"][0]:
    print("-", document)

print("\nQuery latency:")
print(f"{latency:.6f} seconds")
```

Run:

```bash
python benchmark_query.py
```

## 8. Expected Output

Your exact timing depends on your computer and environment.

```text
Query:
I want to learn programming.

Results:
- Python is a programming language.
- Machine learning allows computers to learn from data.

Query latency:
0.004321 seconds
```

The important thing is the measurement, not a specific expected number.

## 9. Why Use `time.perf_counter()`?

```python
time.perf_counter()
```

is suitable for measuring elapsed time.

Basic pattern:

```python
start = time.perf_counter()

# operation

end = time.perf_counter()
elapsed = end - start
```

## 10. Benchmark Multiple Queries

A single measurement can vary. A small multi-query benchmark is more useful.

```python
queries = [
    "I want to learn programming.",
    "What is machine learning?",
    "Tell me about pizza.",
    "What is the capital of the UK?",
    "I want to learn Python."
]
```

Measure each query and calculate:

```text
Average Latency
= Sum of Latencies / Number of Queries
```

Example:

```text
Query 1 → 0.0041 s
Query 2 → 0.0038 s
Query 3 → 0.0045 s
Query 4 → 0.0039 s
Query 5 → 0.0040 s
```

## 11. Persistence vs Latency

These are different concepts.

### Persistence

```text
Chroma
 ↓
Disk
 ↓
Data survives
```

### Latency

```text
Query
 ↓
Search
 ↓
Time measurement
```

Remember:

```text
Persistence → DATA LIFETIME
Latency     → OPERATION SPEED
```

## 12. Connection to HNSW

```text
Stored vectors
      ↓
Vector index
      ↓
HNSW
      ↓
Efficient similarity search
```

Today we measure how long the search operation takes.

We are not implementing HNSW ourselves; Chroma manages the underlying search/indexing system.

## 13. Day 85 → Day 89

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
Query
      +
Metadata Filter
      ↓
Filtered Similarity Search
      ↓
Relevant Documents
```

```text
Day 89
Persistent Chroma
      +
Query
      ↓
Measure Search Latency
```

## 14. Key Concepts

### Persistence

> Keeping database data available across program runs.

### Query latency

> The elapsed time required for the measured query operation.

### Benchmark

> A controlled measurement used to evaluate performance.

### `time.perf_counter()`

> A Python timer suitable for measuring elapsed time.

### HNSW

> An approximate nearest-neighbour indexing approach that helps make vector search efficient.

## 15. Key Formulas

### Latency

```text
Latency = End Time - Start Time
```

### Average Latency

```text
Average Latency
= Sum of Latencies / Number of Queries
```

## 16. What I Learned Today

- Persistence allows Chroma data to survive after the Python program closes.
- `PersistentClient(path="./chroma_data")` connects to a persistent local database.
- The same database path can be opened again in a later program run.
- Query latency measures how long a query operation takes.
- `time.perf_counter()` can be used to measure elapsed time.
- Starting the timer after query embedding lets us measure Chroma search latency separately from embedding latency.
- Running multiple queries gives a more useful small benchmark than measuring only one query.
- Average latency can summarize multiple measurements.
- Persistence and latency are different concepts: persistence concerns data lifetime, while latency concerns operation speed.
- HNSW helps make vector search efficient; benchmarking lets us measure search performance.

## One-Line Takeaway

> **Persistence keeps your vector database available across program runs, while benchmarking measures how quickly the vector database performs a query.**
