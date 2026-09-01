# Day 92 — Build a Basic Semantic Search Function

## Objective

Understand the difference between keyword search and semantic search, then build a reusable semantic search function using embeddings and Chroma.

## 1. Keyword Search

Keyword search looks for matching words.

```text
User Query
    ↓
Match Words
    ↓
Find Matching Documents
    ↓
Return Results
```

Example:

```text
Query:
"I want to learn programming"

Document:
"Python is a programming language."
```

The word `programming` appears in both.

### Limitation

If the document says:

```text
"Python helps developers write software."
```

the meaning may be related, but the exact keyword `programming` is not present.

---

## 2. Semantic Search

Semantic search focuses on **meaning** rather than only exact words.

```text
Query
  ↓
Embedding Model
  ↓
Query Vector
  ↓
Compare with Document Vectors
  ↓
Similarity Ranking
  ↓
Relevant Documents
```

Example:

```text
Query:
"I want to learn coding."

Document:
"Python is a programming language."
```

The words are not identical, but their meanings are related.

### Simple difference

> **Keyword search asks: "Do the words match?"**

> **Semantic search asks: "Does the meaning match?"**

---

## 3. What Is an Embedding?

An embedding is a numerical representation of information.

```text
"Python is a programming language."
              ↓
       Embedding Model
              ↓
       [384 numbers]
```

In our project we use:

```text
all-MiniLM-L6-v2
```

which produces 384-dimensional embeddings.

---

## 4. Semantic Search Workflow

```text
                 USER QUERY
                     ↓
       "I want to learn programming."
                     ↓
              Embedding Model
                     ↓
                Query Vector
                     ↓
                  Chroma
                     ↓
           Similarity Search
                     ↓
            Similar Documents
```

The stored documents already have their own embeddings.

The query is converted into another embedding.

Then the query vector is compared with the stored vectors.

---

## 5. Query Vector vs Document Vectors

Suppose we have:

```text
Document 1 → Python
Document 2 → Machine learning
Document 3 → Pizza
Document 4 → London
```

Each document has an embedding:

```text
Python           → Vector 1
Machine learning → Vector 2
Pizza            → Vector 3
London           → Vector 4
```

The query becomes another vector:

```text
"I want to learn programming."
             ↓
          Query Vector
```

Then:

```text
Query Vector
     ↓
Compare with stored vectors
     ↓
Similarity ranking
     ↓
Top results
```

---

## 6. Similarity

One common similarity measure is cosine similarity.

Formula:

```text
cosine similarity(A, B)
= (A · B) / (||A|| × ||B||)
```

Dot product:

```text
A · B = Σᵢ(aᵢ × bᵢ)
```

Conceptually:

```text
More similar meaning
       ↓
Higher similarity

Less similar meaning
       ↓
Lower similarity
```

---

## 7. Today's Build

Create:

```text
semantic_search.py
```

```python
import chromadb
from sentence_transformers import SentenceTransformer


# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Connect to Chroma
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# 3. Load existing collection
collection = client.get_collection(
    name="documents"
)


# 4. Semantic search function
def semantic_search(query, n_results=2):

    # Convert query into an embedding
    query_embedding = model.encode(query)

    # Search Chroma
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )

    return results["documents"][0]


# 5. Test the function
query = "I want to learn programming."

results = semantic_search(
    query,
    n_results=2
)


print("Query:")
print(query)

print("\nSemantic search results:")

for i, document in enumerate(results):
    print(f"{i + 1}. {document}")
```

---

## 8. What Does the Function Do?

We create:

```python
def semantic_search(query, n_results=2):
```

The function accepts:

```text
query
```

and:

```text
n_results
```

Then it returns the most relevant documents.

Instead of repeatedly writing the complete search process, we can use:

```python
results = semantic_search(query)
```

---

## 9. Function Workflow

When we call:

```python
semantic_search(
    "I want to learn programming."
)
```

the function performs:

```text
Query
 ↓
Embedding Model
 ↓
Query Embedding
 ↓
Chroma
 ↓
Similarity Search
 ↓
Top Results
 ↓
Return Documents
```

---

## 10. Why Make a Function?

Without a function:

```text
Query 1
 ↓
Write search code

Query 2
 ↓
Write search code

Query 3
 ↓
Write search code
```

With a function:

```text
semantic_search(query)
```

we can reuse the same logic:

```python
semantic_search("I want to learn Python.")

semantic_search("What is machine learning?")

semantic_search("Tell me about programming.")
```

This makes the code easier to reuse and maintain.

---

## 11. Example

### Query

```text
"I want to learn coding."
```

### Documents

```text
1. Python is a programming language.
2. Machine learning allows computers to learn from data.
3. Pizza is a popular Italian food.
4. London is the capital of the United Kingdom.
```

Conceptually:

```text
Query
"I want to learn coding."
        ↓
     Query Vector
        ↓
Compare with document vectors
        ↓
Python              ← highly related
Machine learning    ← related
Pizza               ← less related
London              ← less related
```

The exact ranking depends on the embeddings and similarity calculation.

---

## 12. Connection to Previous Days

### Day 85

```text
Chroma
 ↓
Vector Database
```

### Day 86

```text
Embeddings
 ↓
Vector Database
 ↓
Vector Index
```

### Day 87

```text
Query
 ↓
Similarity Search
 ↓
Similar Documents
```

### Day 88

```text
Metadata
 ↓
Filtering
 ↓
Controlled Search
```

### Day 89

```text
Query
 ↓
Benchmark
 ↓
Latency
```

### Day 90

```text
Persistent Chroma
 ↓
Close Program
 ↓
Reload Database
```

### Day 91

```text
Vector Database Concepts
 ↓
Choose Based on Requirements
```

### Day 92

```text
Semantic Search
 ↓
Reusable Search Function
```

---

## 13. Important Distinction

```text
Embedding
→ Converts text into a vector

Vector Database
→ Stores and retrieves vectors and associated data

Similarity Search
→ Finds vectors similar to the query vector

Semantic Search
→ Searches based on meaning using representations such as embeddings
```

---

## 14. Semantic Search Mental Model

```text
                 TEXT
                  ↓
            EMBEDDING MODEL
                  ↓
                VECTOR
                  ↓
          VECTOR DATABASE
                  ↓
          SIMILARITY SEARCH
                  ↓
          RELEVANT DOCUMENTS
```

For a query:

```text
"I want to learn programming."
```

the process is:

```text
Query
 ↓
Query Embedding
 ↓
Query Vector
 ↓
Compare with stored vectors
 ↓
Rank by similarity
 ↓
Return relevant documents
```

---

## 15. Key Concepts

### Keyword Search

> Searches primarily by matching words or terms.

### Semantic Search

> Searches based on semantic meaning using representations such as embeddings.

### Embedding

> A numerical representation of information, such as the meaning of text.

### Query Embedding

> The vector representation of the user's search query.

### Similarity Search

> Finding stored vectors that are most similar to a query vector.

### Vector Database

> A database designed to store and retrieve vector representations efficiently.

### Search Function

> A reusable piece of code that performs the semantic-search workflow.

---

## 16. What I Learned Today

- Keyword search focuses mainly on matching words.
- Semantic search focuses on meaning.
- Embeddings allow text meaning to be represented numerically.
- A query can be converted into an embedding before searching.
- The query vector can be compared with stored document vectors.
- Similarity measures help rank candidate documents.
- Cosine similarity is one common way to compare vectors.
- A semantic search function can package the embedding and search process into reusable code.
- `n_results` controls how many results we request from Chroma.
- Semantic search can find related concepts even when the exact words differ.
- Chroma can act as the retrieval layer for our semantic search system.

## One-Line Takeaway

> **Semantic search converts a query into an embedding and uses vector similarity to find documents with related meaning rather than relying only on exact keyword matches.**
