# Day 88 — Add Metadata and Filter on It

## Objective

Understand metadata, why it is useful for vector search, and how to filter Chroma results using metadata.

## 1. Today's Big Picture

```text
Documents
    ↓
Embedding Model
    ↓
Vectors
    ↓
Chroma
    ├── ID
    ├── Document
    ├── Vector
    └── Metadata
             ↓
      Metadata Filter
             ↓
      Similarity Search
             ↓
      Relevant Documents
```

## 2. What Is Metadata?

**Metadata is additional structured information about a document.**

Example:

```text
Document:
"Python is a programming language."

Metadata:
category = programming
level = beginner
```

Think:

```text
Document + Metadata
```

Metadata describes the document but is separate from its embedding.

## 3. Embedding vs Metadata

### Embedding

```text
"Python is a programming language."
              ↓
       Embedding Model
              ↓
        [384 numbers]
```

The embedding represents semantic information.

### Metadata

```text
category = programming
level = beginner
```

Metadata provides structured attributes.

```text
Embedding → represents meaning
Metadata  → provides structured information
```

## 4. Is Metadata Automatic?

In our code, **no**.

We provide it ourselves:

```python
metadatas = [
    {"category": "programming"},
    {"category": "machine-learning"},
    {"category": "food"},
    {"category": "geography"}
]
```

Chroma stores the metadata we provide.

An LLM or classifier could generate metadata automatically, but that would be a separate system.

## 5. Our Four Documents

```text
doc1 → Python is a programming language.
doc2 → Machine learning allows computers to learn from data.
doc3 → Pizza is a popular Italian food.
doc4 → London is the capital of the United Kingdom.
```

Categories:

```text
doc1 → programming
doc2 → machine-learning
doc3 → food
doc4 → geography
```

## 6. What the Database Contains

Conceptually:

```text
┌────────┬──────────────────────────┬────────────────────┐
│ ID     │ Document                 │ Metadata           │
├────────┼──────────────────────────┼────────────────────┤
│ doc1   │ Python...                │ category=program.  │
│ doc2   │ Machine learning...      │ category=ML        │
│ doc3   │ Pizza...                 │ category=food      │
│ doc4   │ London...                │ category=geography │
└────────┴──────────────────────────┴────────────────────┘
```

Each document also has its embedding.

Conceptually:

```text
ID + Document + Embedding + Metadata
```

## 7. Adding Metadata in Chroma

```python
collection.upsert(
    ids=[
        "doc1",
        "doc2",
        "doc3",
        "doc4"
    ],
    documents=documents,
    embeddings=embeddings.tolist(),
    metadatas=[
        {"category": "programming"},
        {"category": "machine-learning"},
        {"category": "food"},
        {"category": "geography"}
    ]
)
```

## 8. What Is Filtering?

Filtering restricts which records are eligible for the search.

```python
where={"category": "programming"}
```

means:

> Only consider documents whose category is `programming`.

Conceptually:

```text
4 documents
     ↓
Metadata filter
category = programming
     ↓
Eligible documents
     ↓
Similarity search
```

## 9. Filtering + Similarity Search

A vector search asks:

> Which documents are semantically similar?

A metadata filter asks:

> Which documents are allowed to participate in the search?

Together:

```text
User Query
     +
Metadata Filter
     ↓
Eligible Documents
     ↓
Similarity Search
     ↓
Top K Results
```

## 10. Today's Build

Create:

```text
metadata_filter.py
```

```python
import chromadb
from sentence_transformers import SentenceTransformer


# 1. Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Connect to the existing Chroma database
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# 3. Create a separate collection for today's exercise
collection = client.get_or_create_collection(
    name="metadata_demo"
)


# 4. Our four documents
documents = [
    "Python is a programming language.",
    "Machine learning allows computers to learn from data.",
    "Pizza is a popular Italian food.",
    "London is the capital of the United Kingdom."
]


# 5. Metadata for each document
metadatas = [
    {"category": "programming"},
    {"category": "machine-learning"},
    {"category": "food"},
    {"category": "geography"}
]


# 6. Create embeddings
embeddings = model.encode(documents)


# 7. Store documents, embeddings and metadata
collection.upsert(
    ids=[
        "doc1",
        "doc2",
        "doc3",
        "doc4"
    ],
    documents=documents,
    embeddings=embeddings.tolist(),
    metadatas=metadatas
)


# 8. Check the number of documents
print("Documents stored:", collection.count())


# 9. User query
query = "I want to learn programming."


# 10. Convert query into an embedding
query_embedding = model.encode(query)


# 11. Search only programming documents
results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    where={"category": "programming"},
    n_results=2
)


# 12. Display results
print("\nQuery:")
print(query)

print("\nFiltered results:")

for i, document in enumerate(results["documents"][0]):
    print(f"{i + 1}. {document}")
```

Run:

```bash
python metadata_filter.py
```

Expected result:

```text
Documents stored: 4

Query:
I want to learn programming.

Filtered results:
1. Python is a programming language.
```

## 11. Understanding `where`

```python
where={"category": "programming"}
```

means:

```text
Look at metadata
       ↓
category
       ↓
must equal
       ↓
programming
```

The embedding model does not determine the category here. We already provided it.

## 12. Why Metadata Is Useful

Imagine thousands of documents with fields such as:

```text
category
author
language
department
year
difficulty
document_type
```

Metadata lets you narrow retrieval using structured attributes.

For example:

```python
where={"category": "programming"}
```

or:

```python
where={"language": "Python"}
```

## 13. Multiple Metadata Fields

You can store several fields:

```python
metadatas=[
    {
        "category": "programming",
        "level": "beginner",
        "language": "Python"
    },
    {
        "category": "machine-learning",
        "level": "beginner",
        "language": "Python"
    },
    {
        "category": "food",
        "level": "beginner",
        "language": "Italian"
    },
    {
        "category": "geography",
        "level": "general",
        "language": "English"
    }
]
```

## 14. Metadata Is Not Part of the 384 Dimensions

This is important.

```text
Document
   ↓
Embedding Model
   ↓
384-dimensional vector
```

Metadata is stored separately:

```text
Document
   ├── Embedding → [384 numbers]
   │
   └── Metadata
          └── category = programming
```

It is **not** dimension 385.

## 15. Similarity Search Without a Filter

```text
Query
 ↓
Similarity Search
 ↓
Potentially consider all documents
 ↓
Top K
```

## 16. Similarity Search With a Filter

```text
Query
 ↓
Metadata Filter
 ↓
Eligible documents
 ↓
Similarity Search
 ↓
Top K
```

The filter gives you additional control over retrieval.

## 17. Real-World Analogy

Imagine an online shopping website.

Search:

```text
"running shoes"
```

This is similar to semantic search.

Then filter:

```text
Brand = Nike
Size = 10
Price < £100
```

These are structured filters.

Similarly:

```text
Semantic query
       +
Metadata filters
       ↓
More controlled results
```

## 18. Connection to RAG

Metadata filtering is useful in RAG.

Imagine a company has:

```text
HR documents
Finance documents
Engineering documents
Legal documents
```

A user asks:

```text
"What is our holiday policy?"
```

You might restrict retrieval to:

```text
department = HR
```

Then:

```text
User Question
      ↓
Query Embedding
      ↓
Metadata Filter
      ↓
Vector Similarity Search
      ↓
Relevant Chunks
      ↓
LLM
      ↓
Answer
```

## 19. Day 85 → Day 88

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

## 20. Key Concepts

### Embedding

> Numerical representation of semantic information.

```text
Text
 ↓
Embedding
 ↓
384 numbers
```

### Metadata

> Additional structured information about a record.

```text
category = programming
level = beginner
```

### Filter

> Restricts which records can participate in retrieval.

```text
category = programming
```

### Similarity Search

> Finds vectors that are close to the query vector.

```text
Query Vector
     ↓
Similarity
     ↓
Closest vectors
```

## 21. Key Formulas

Metadata filtering itself does not require a new mathematical formula.

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

The metadata filter is a **structured condition**, not a vector dimension.

## 22. What I Learned Today

- Metadata is additional structured information about a document.
- Metadata is separate from the embedding.
- Metadata does not become another embedding dimension.
- In our example, metadata is manually provided.
- Chroma stores metadata together with the document record.
- `metadatas=[...]` attaches metadata to records.
- `where={...}` applies a metadata filter during querying.
- Similarity search finds semantically similar vectors.
- Metadata filtering restricts which records are eligible for retrieval.
- Metadata and similarity search can be combined.
- Chroma does not automatically decide the category or level in our example.
- An LLM or classifier could generate metadata automatically, but that is a separate process.
- Metadata is useful for controlling and narrowing retrieval in larger systems.
- Metadata filtering is especially useful in RAG systems.

## One-Line Takeaway

> **Embedding represents what the document means, metadata provides structured information about the document, and metadata filtering lets us control which documents participate in similarity search.**
