# Day 91 — Vector Database Notes

## Objective

Understand how to choose a vector database, and document the main concepts learned while building with Chroma.

## 1. What Is a Vector Database?

A vector database is a system designed to store, manage, and search vector embeddings efficiently.

A normal database searches for exact values, for example `WHERE category = "programming"`. A vector database, by contrast, searches for vectors that are semantically similar to a query. The process looks like this:

1. Start with a query vector.
2. Perform a vector search.
3. Retrieve the most similar vectors.
4. Return the documents associated with those vectors.

## 2. Why Do We Need a Vector Database?

Embedding models convert text into vectors. For example, the sentence "Python is a programming language" is passed through an embedding model and turned into a 384-dimensional vector.

When we have many vectors, we need a system that can:

- Store vectors
- Store associated documents
- Store metadata
- Search for similar vectors
- Apply metadata filters
- Persist the data
- Support efficient retrieval

This is where a vector database becomes useful.

## 3. Vector Database Workflow

The general workflow is:

Documents → Embedding Model → Vector Embeddings → Vector Database → Vector Index → Similarity Search → Relevant Documents

For this project specifically, the pipeline was:

Text → all-MiniLM-L6-v2 → 384D embedding → Chroma → Vector search → Relevant documents

## 4. What We Built With Chroma

- **Day 85 — Set Up Chroma:** Established Chroma as a persistent local database.
- **Day 86 — Embed and Insert:** Converted documents into 384-dimensional vectors using an embedding model and inserted them into Chroma.
- **Day 87 — Query by Similarity:** Converted a query into a query embedding, ran a similarity search, and retrieved similar documents.
- **Day 88 — Metadata and Filtering:** Combined a query with a metadata filter to perform a filtered similarity search and return relevant documents.
- **Day 89 — Benchmark Query Latency:** Measured Chroma query latency by starting a timer, running the query, and stopping the timer.
- **Day 90 — Persist and Reload:** Verified that data written to `./chroma_data/` persists after the program closes and that the existing collection loads correctly when the program restarts.

## 5. Choosing a Vector Database

There is no single vector database that is always the best choice. The right choice depends on the application's requirements. Key questions to ask include:

- How many vectors do I need to store?
- How fast must search be?
- Do I need metadata filtering?
- Should this run locally or in the cloud?
- How much infrastructure am I willing to manage?
- What will it cost?
- What integrations do I need?

## 6. Main Selection Factors

### 6.1 Scale

How many vectors will the system need to store? A small project might have around 1,000 vectors, while a production system might need to handle millions. The database and indexing strategy should match the expected scale.

### 6.2 Search Performance

How quickly do results need to come back? This is where vector indexes such as HNSW become important: a query vector is passed through the index to produce an efficient search and a set of results.

### 6.3 Metadata Filtering

Do you need to restrict searches using structured information, such as `category = programming`, `language = Python`, or `level = beginner`? If so, the query and the metadata filter together narrow the set of eligible documents before the similarity search runs.

### 6.4 Persistence

Does the data need to survive application restarts? This project's Chroma setup uses:

```python
client = chromadb.PersistentClient(
    path="./chroma_data"
)
```

This provides persistent local storage.

### 6.5 Deployment

Where should the vector database run — locally, self-hosted, or cloud-managed? A learning project may be well served by a simple local setup, while a production application may need a managed or distributed deployment.

### 6.6 Cost

Total cost includes storage, compute, network, and operational overhead. A powerful solution is not automatically the best one if it is unnecessarily expensive or complex for the task at hand.

### 6.7 Ecosystem and Integration

How easily does the vector database fit into the rest of the application, in a pipeline such as Application → Embedding Model → Vector Database → Retriever → LLM? Good integration simplifies both development and maintenance.

### 6.8 Operational Complexity

How much infrastructure are you willing to manage? A small project can get away with a simple local database and minimal operational work. A large production system, on the other hand, has to account for scalability, reliability, monitoring, backups, security, and availability.

## 7. Chroma — What We Learned

Chroma provided a simple way to understand the complete vector-database workflow. The core setup was:

```python
client = chromadb.PersistentClient(
    path="./chroma_data"
)
```

From there, a collection holds documents, embeddings, and metadata together, and supports querying against all three. Chroma allowed storage and vector retrieval to be combined in one local workflow.

## 8. Vector Database vs. Vector Index

These are related but distinct concepts.

A **vector database** manages documents, embeddings, metadata, IDs, storage, and search as a whole system. A **vector index** is the structure within that system — vectors organized into an index structure to enable efficient nearest-neighbour search. In short, a vector database contains and manages a vector index; the index is the mechanism that makes searching efficient.

## 9. HNSW

HNSW (Hierarchical Navigable Small World) is an approximate nearest-neighbour indexing approach. Conceptually, a query vector is passed through the HNSW index, which identifies promising nearby vectors and returns the top results.

Without an index, a brute-force approach would have to compare the query against every stored vector one by one to find the closest match. HNSW avoids this by making large-scale search far more efficient.

## 10. Similarity Search

A query is first converted into a vector — for example, "I want to learn programming" becomes a query vector via the embedding model. That query vector is then compared against the stored vectors, and the resulting similarity or distance scores determine the closest vectors and, in turn, the documents associated with them.

## 11. Cosine Similarity

One common similarity measure is cosine similarity:

```
cosine similarity(A, B) = (A · B) / (||A|| × ||B||)
```

where the dot product is `A · B = Σᵢ(aᵢ × bᵢ)`. The idea is to compare the direction of two vectors: vectors pointing in a similar direction have higher similarity, while vectors pointing in different directions have lower similarity.

## 12. Metadata

Metadata is additional structured information attached to a record. For example, the document "Python is a programming language" might have the metadata `category = programming`. Metadata is stored separately from the embedding — a document has its embedding (a set of 384 numbers) and, alongside it, its metadata (such as `category = programming`). Metadata does not become an extra dimension of the embedding itself.

## 13. Metadata Filtering

A metadata filter restricts which records are eligible for retrieval. For example, `where={"category": "programming"}` narrows the full set of documents down to programming-related documents before the similarity search runs, producing the final results.

To summarize the relationship:

- **Embedding** represents meaning.
- **Metadata** provides structured attributes.
- **Filter** restricts which records are eligible.

## 14. Persistence

Persistence allows data to survive after the Python process closes. Documents stored in Chroma are written to `./chroma_data/`, and that data remains even after the program closes. When the program starts again, the `PersistentClient` loads the existing collection from `./chroma_data/` so it can be queried immediately.

Persistence is distinct from latency: persistence concerns how long data lives, while latency concerns how fast an operation runs.

## 15. Query Latency

Latency measures how long an operation takes:

```
Latency = End Time - Start Time
```

For example, if a query starts at 10.000 seconds and ends at 10.015 seconds, the latency is 0.015 seconds, or 15 milliseconds.

To benchmark Chroma's search performance separately from the embedding step, the process is: embed the query to get a query vector, start the timer, run the Chroma search, stop the timer, and record the latency.

## 16. What Makes a Good Vector Database?

The right choice depends on the application. Useful evaluation criteria include:

- Scale
- Search performance
- Metadata filtering
- Persistence
- Deployment model
- Cost
- Reliability
- Ecosystem and integrations
- Operational complexity

There is no universal winner — the correct choice is the one that best fits the application's requirements.

## 17. Vector Databases in RAG

Vector databases are commonly used in the retrieval part of a RAG (Retrieval-Augmented Generation) system.

**Ingestion:** Documents are chunked, passed through an embedding model to produce vectors, and stored in the vector database.

**Retrieval:** A user's question is converted into a query embedding, which drives a vector search. Metadata filtering narrows the results to relevant chunks, which are then passed to the LLM to produce an answer.

The vector database provides the retrieval layer that supplies relevant information to the LLM.

## 18. Complete Mental Model

Documents are chunked and prepared, then passed through an embedding model to produce 384-dimensional vectors. These vectors, along with their documents, metadata, and IDs, are stored in the vector database, which builds a vector index (such as HNSW) on top of them for efficient search.

On the query side, a user's question is converted into a query embedding, narrowed by a metadata filter, and compared against the index via similarity search. The resulting relevant chunks are passed to the LLM, which produces the final answer.

## 19. Day 85 → Day 91

| Day | Focus | Outcome |
|-----|-------|---------|
| 85 | Set up Chroma | Vector database |
| 86 | Insert embeddings | Vector index / HNSW |
| 87 | Query by similarity | Semantic retrieval |
| 88 | Metadata and filtering | Controlled retrieval |
| 89 | Benchmark latency | Performance measurement |
| 90 | Persist and reload | Durable vector storage |
| 91 | Choose a vector database | Understand trade-offs; document the complete workflow |

## 20. What I Learned This Week

- Vector databases are designed to store and retrieve embeddings efficiently.
- Embeddings represent semantic information as vectors.
- Vector indexes help make nearest-neighbour search more efficient.
- HNSW is an approximate nearest-neighbour indexing approach.
- Similarity search retrieves vectors close to a query vector.
- Metadata provides structured information about records.
- Metadata filtering restricts which records participate in retrieval.
- Persistence allows vector data to survive application restarts.
- Query latency measures retrieval performance.
- Chroma provided a practical local environment for learning these concepts.
- Choosing a vector database depends on scale, performance, filtering, persistence, deployment, cost, integrations, and operational requirements.
- Vector databases form an important part of the retrieval layer in RAG systems.

### One-Line Takeaway

A vector database stores embeddings and associated data, indexes them for efficient similarity search, supports structured filtering and persistence, and provides the retrieval layer needed by systems such as RAG.
