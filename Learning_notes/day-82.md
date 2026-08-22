# Day 82 — Find the Most Similar Item to a Query

## Objective

Understand the Transformer at a high level and build a simple semantic search system that finds the most similar item to a user's query using embeddings and cosine similarity.

---

## 1. What Are We Building?

Today we move from comparing two texts to comparing a query against many stored items.

```text
User Query
    ↓
Convert query to embedding
    ↓
Compare with stored embeddings
    ↓
Calculate similarity scores
    ↓
Find highest score
    ↓
Return most similar item
```

Example:

```text
Query:
"I want to learn Python"

Items:
"I love programming in Python."
"I enjoy eating pizza."
"I travelled around Europe."
"Python is my favourite programming language."
```

The system should return a Python-related item because its meaning is closest to the query.

---

## 2. Basic Pipeline

```text
                 STORED ITEMS
                     ↓
               Embedding Model
                     ↓
              Stored Embeddings
                     ↓
                  Vector Space


User Query
     ↓
Embedding Model
     ↓
Query Vector
     ↓
Compare with stored vectors
     ↓
Cosine Similarity
     ↓
Highest similarity
     ↓
Most Similar Item
```

This is the foundation of semantic/vector search.

---

## 3. Why Do We Embed the Query?

The stored items have already been converted into vectors.

The user's query must also be converted into a vector so both sides exist in the same embedding space.

```text
Stored item → Vector
User query  → Vector
```

Then they can be compared mathematically.

---

## 4. Query vs Stored Items

Imagine:

```text
Item A → Python programming
Item B → Pizza
Item C → Travelling
Item D → Python language
```

After calculating similarity:

```text
Query ↔ Item A → 0.91
Query ↔ Item B → 0.12
Query ↔ Item C → 0.08
Query ↔ Item D → 0.95
```

The highest score is:

```text
0.95
```

Therefore:

```text
Item D → Most Similar
```

---

## 5. Cosine Similarity

Today's build uses cosine similarity.

```text
cosine similarity(A, B)
= (A · B) / (||A|| × ||B||)
```

Cosine similarity compares the direction of two vectors.

```text
Higher similarity → more similar
Lower similarity  → less similar
```

The exact score interpretation depends on the embedding model and data.

---

## 6. Main Idea of Today's Build

We calculate:

```text
Query ↔ Item 1
Query ↔ Item 2
Query ↔ Item 3
Query ↔ Item 4
...
```

Then:

```text
Find the maximum similarity score
```

In Python:

```python
best_index = similarities.argmax()
```

This gives the position of the most similar item.

---

## 7. Build — Semantic Search

Install:

```bash
pip install sentence-transformers scikit-learn
```

Create:

```text
semantic_search.py
```

Code:

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Items we want to search
items = [
    "I love programming in Python.",
    "Python is my favourite programming language.",
    "I enjoy building software.",
    "I enjoy eating pizza.",
    "Pizza is one of my favourite foods.",
    "I love travelling around Europe.",
    "I want to visit France and Italy.",
]


# 3. Create embeddings for the items
item_embeddings = model.encode(items)


# 4. User query
query = "I want to learn Python programming."


# 5. Create embedding for the query
query_embedding = model.encode([query])


# 6. Calculate similarity
similarities = cosine_similarity(
    query_embedding,
    item_embeddings
)[0]


# 7. Find the most similar item
best_index = similarities.argmax()


# 8. Display result
print("Query:", query)

print("\nMost similar item:")
print(items[best_index])

print("\nSimilarity score:")
print(similarities[best_index])
```

---

## 8. How the Code Works

### Step 1 — Load the embedding model

```python
model = SentenceTransformer("all-MiniLM-L6-v2")
```

The model is ready to convert text into embeddings.

For this model, each sentence is represented by a 384-dimensional vector.

### Step 2 — Create stored items

```python
items = [
    "I love programming in Python.",
    "Python is my favourite programming language.",
    "I enjoy building software.",
    "I enjoy eating pizza.",
    "Pizza is one of my favourite foods.",
    "I love travelling around Europe.",
    "I want to visit France and Italy.",
]
```

Think of these as a small database.

### Step 3 — Convert stored items into embeddings

```python
item_embeddings = model.encode(items)
```

The flow is:

```text
7 sentences
     ↓
Embedding model
     ↓
7 × 384 vectors
```

Shape:

```text
(7, 384)
```

### Step 4 — Create the query

```python
query = "I want to learn Python programming."
```

This is what the user wants to search for.

### Step 5 — Convert the query into an embedding

```python
query_embedding = model.encode([query])
```

The flow is:

```text
User Query
    ↓
Embedding Model
    ↓
Query Vector
    ↓
1 × 384
```

The square brackets mean the query is one sentence inside a collection:

```python
[query]
```

---

## 9. Compare the Query with Every Item

```python
similarities = cosine_similarity(
    query_embedding,
    item_embeddings
)[0]
```

Conceptually:

```text
                    Query
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
       Item 0       Item 1      Item 2
          ↓           ↓           ↓
       Compare      Compare     Compare
          │           │           │
          └───────────┼───────────┘
                      ↓
               Similarity Scores
```

Example:

```text
Item 0 → 0.91
Item 1 → 0.95
Item 2 → 0.82
Item 3 → 0.12
Item 4 → 0.08
Item 5 → 0.10
Item 6 → 0.07
```

The exact values depend on the model and data.

---

## 10. What Does `[0]` Mean?

The similarity calculation returns a matrix:

```text
[
    [0.91, 0.95, 0.82, 0.12, 0.08, 0.10, 0.07]
]
```

Using:

```python
[0]
```

selects the first row:

```text
[
    0.91,
    0.95,
    0.82,
    0.12,
    0.08,
    0.10,
    0.07
]
```

Now there is one similarity score for each item.

---

## 11. What Does `argmax()` Do?

```python
best_index = similarities.argmax()
```

`argmax()` means:

> Find the position of the largest value.

Example:

```text
Index:       0     1     2     3
Similarity: 0.72  0.95  0.31  0.45
```

Largest value:

```text
0.95
```

Its index:

```text
1
```

Therefore:

```python
best_index = 1
```

---

## 12. Retrieve the Original Item

```python
items[best_index]
```

becomes:

```python
items[1]
```

and returns:

```text
"Python is my favourite programming language."
```

The connection is:

```text
Similarity score
      ↓
Index
      ↓
Original item
```

---

## 13. Complete Workflow

```text
                 STORED ITEMS
                     │
                     ↓
              Embedding Model
                     │
                     ↓
             Stored Vectors
                     │
                     │
USER QUERY          │
    │               │
    ↓               │
Embedding Model     │
    │               │
    ↓               │
Query Vector        │
    │               │
    └───────┬───────┘
            ↓
    Cosine Similarity
            ↓
   Compare with EVERY
       stored vector
            ↓
     Similarity Scores
            ↓
        argmax()
            ↓
   Highest similarity
            ↓
    Most Similar Item
```

---

## 14. Semantic Search

Traditional keyword search looks for matching words.

Semantic search looks at meaning.

### Keyword Search

```text
Query
 ↓
Find matching words
 ↓
Results
```

### Semantic Search

```text
Query
 ↓
Embedding
 ↓
Vector
 ↓
Similarity
 ↓
Meaning-based results
```

Example:

```text
Query:
"I want to learn Python."
```

can match:

```text
"Python is my favourite programming language."
```

Remember:

```text
Keyword search → WORD MATCHING
Semantic search → MEANING MATCHING
```

---

## 15. Connection to RAG

Today's system is very close to the retrieval stage of RAG.

```text
User Query
     ↓
Query Embedding
     ↓
Similarity Search
     ↓
Relevant Documents
     ↓
LLM
     ↓
Answer
```

A real RAG system usually retrieves multiple relevant chunks rather than only one.

```text
Query
 ↓
Embedding
 ↓
Vector Search
 ↓
Top 5 relevant chunks
 ↓
LLM
 ↓
Final answer
```

Today we are starting with:

```text
Top 1 result
```

---

## 16. Transformer — High-Level Intuition

A Transformer is an architecture used by modern language models and many other AI systems.

At a high level:

```text
Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
Embeddings
 ↓
Transformer
 ↓
Contextual representations
 ↓
Output probabilities
 ↓
Next token
```

The Transformer uses attention to understand relationships between tokens.

---

## 17. Transformer and Attention

Consider:

```text
"The dog chased the ball because it was fast."
```

The model needs to understand relationships between words such as:

```text
dog
ball
it
fast
```

Attention allows tokens to interact with one another.

```text
Token
 ↓
Attention
 ↓
Look at relevant tokens
 ↓
Context-aware representation
```

The Transformer processes this contextual information through multiple layers.

---

## 18. Encoder and Decoder Intuition

Transformers can be used in different architectures.

### Encoder-style models

Useful for understanding and producing representations.

```text
Text
 ↓
Encoder
 ↓
Representation
```

### Decoder-style models

Commonly used for generating text.

```text
Prompt
 ↓
Decoder
 ↓
Next-token probabilities
 ↓
Next token
 ↓
Repeat
```

This is a high-level distinction.

---

## 19. Day 78 → Day 82

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
Many stored vectors
       ↑
       │
Query → Embedding
       ↓
Cosine Similarity
       ↓
Highest score
       ↓
Most similar item
```

---

## 20. What I Learned Today

- A query can also be converted into an embedding.
- Stored items and queries should be represented in the same embedding space.
- Cosine similarity can compare a query vector with many item vectors.
- `argmax()` finds the position of the highest similarity score.
- `items[best_index]` retrieves the original item at that position.
- `[0]` selects the first row of the similarity matrix.
- Semantic search retrieves information based on meaning rather than exact keyword matching.
- Embeddings are the foundation of vector search.
- The Transformer uses attention to model relationships between tokens.
- Transformers process contextual information through multiple layers.
- The retrieval stage of RAG follows a similar query-embedding → similarity-search pipeline.
- Real RAG systems usually retrieve multiple relevant chunks before passing them to an LLM.

---

## Key Formulas

### Cosine Similarity

```text
cosine similarity(A, B)
= (A · B) / (||A|| × ||B||)
```

### Dot Product

```text
A · B = Σᵢ(aᵢ × bᵢ)
```

---

## One-Line Takeaway

> **Convert the user's query into a vector, compare it with stored vectors using cosine similarity, find the highest score with `argmax()`, and return the original item at that index.**
