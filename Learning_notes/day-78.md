# Day 78 — Generate Embeddings for Several Sentences

**Date:** Monday, August 17, 2026  
**Week:** 12 — How LLMs Work II: Embeddings & Attention  
**Phase:** 3 — How LLMs Work + Embeddings & Vector Search

---

## 🎯 Objective

Understand what embeddings are and generate embeddings for several sentences using a real embedding model.

### Learning Objectives

- Understand embeddings
- Understand token IDs vs embeddings
- Understand embedding dimensions
- Understand pooling
- Generate embeddings with `all-MiniLM-L6-v2`
- Understand semantic/vector space
- Understand cosine similarity
- Understand how embeddings fit into semantic search and RAG

---

# 1. What Is an Embedding?

An **embedding** is a numerical representation of text.

Example:

```text
"I love programming in Python."
                ↓
        Embedding Model
                ↓
[0.12, -0.43, 0.71, 0.08, ...]
```

The complete vector represents the semantic characteristics of the input text.

Individual dimensions should not normally be interpreted as individual words.

---

# 2. Tokenization vs Embeddings

These are different stages.

### Tokenization

Text is converted into tokens and token IDs:

```text
"I love programming"
        ↓
     Tokenizer
        ↓
[40, 2847, 9182]
```

A token ID is an identifier. It is **not** the final embedding.

### Embedding

The embedding model internally processes the tokenized text and produces a vector:

```text
Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
Neural-network processing
 ↓
Pooling / representation
 ↓
One text embedding
```

So:

> **Token ID ≠ Embedding vector**

---

# 3. What Are Embedding Dimensions?

A dimension is one numerical position in a vector.

For a simple imaginary 4-dimensional vector:

```text
[0.2, 0.8, 0.1, 0.5]
```

there are four dimensions:

```text
D1 = 0.2
D2 = 0.8
D3 = 0.1
D4 = 0.5
```

Your model, `all-MiniLM-L6-v2`, produces:

```text
384 dimensions
```

Therefore:

```text
One text input → one 384-dimensional vector
```

It does **not** mean the sentence is split into 384 pieces.

---

# 4. Example: "hello world"

Conceptually:

```text
"hello world"
      ↓
Tokenization
      ↓
Token IDs
      ↓
Token representations
      ↓
Transformer processing
      ↓
Pooling
      ↓
ONE vector
      ↓
[0.45, 0.61, 0.32, ...]
```

With `all-MiniLM-L6-v2`, that final vector contains 384 values.

Think of the vector as a point in a **384-dimensional semantic/vector space**.

---

# 5. What Is Pooling?

The model produces representations for multiple tokens. Pooling combines token-level representations into one fixed-size representation for the whole text.

For simple mean pooling:

\[
\text{Pooled Vector} = \frac{1}{n}\sum_{i=1}^{n}v_i
\]

Example:

```text
v1 = [0.2, 0.4, 0.6]
v2 = [0.4, 0.2, 0.8]
v3 = [0.6, 0.6, 0.4]
```

Mean pooling:

```text
Dimension 1:
(0.2 + 0.4 + 0.6) / 3 = 0.4

Dimension 2:
(0.4 + 0.2 + 0.6) / 3 = 0.4

Dimension 3:
(0.6 + 0.8 + 0.4) / 3 = 0.6
```

Result:

```text
[0.4, 0.4, 0.6]
```

So:

```text
Multiple token representations
            ↓
         Pooling
            ↓
One fixed-size text representation
```

The exact pooling strategy can vary between embedding models.

---

# 6. Why Do Embedding Values Differ?

Different input text produces different vectors.

Example:

```text
"I love programming in Python."
→ [-0.0576, 0.0042, -0.0281, 0.0252, ...]
```

while:

```text
"I enjoy eating pizza."
→ [-0.0304, 0.0065, 0.0087, 0.1120, ...]
```

The values are produced by the trained neural network.

They are not manually assigned like:

```text
Python → 0.5
Pizza → 0.7
```

The complete vector is the learned representation.

---

# 7. Chunking vs Dimensions

These are completely different concepts.

### Chunking

Chunking determines how much text becomes one input:

```text
Large PDF
   ↓
Chunking
   ↓
Chunk 1
Chunk 2
Chunk 3
...
```

### Embedding dimensions

Dimensions determine how many numerical values represent each chunk:

```text
Chunk 1 → 384 numbers
Chunk 2 → 384 numbers
Chunk 3 → 384 numbers
```

Therefore:

```text
1000 chunks
    ↓
1000 embeddings
    ↓
1000 × 384
```

Not:

```text
1000 chunks → 384 chunks
```

---

# 8. Day 78 Build — Sentence Embeddings

## Install

```bash
pip install sentence-transformers scikit-learn
```

## Python

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I love programming in Python.",
    "Python is my favourite programming language.",
    "I enjoy building software.",
    "I enjoy eating pizza.",
    "Pizza is one of my favourite foods.",
    "I love travelling around Europe.",
]

embeddings = model.encode(sentences)

print("Number of sentences:", len(sentences))
print("Embedding shape:", embeddings.shape)

for sentence, embedding in zip(sentences, embeddings):
    print("\nSentence:", sentence)
    print("First 10 values:", embedding[:10])
```

---

# 9. Understanding `(6, 384)`

The experiment produced:

```text
Number of sentences: 6
Embedding shape: (6, 384)
```

This means:

```text
6    = number of text inputs
384  = dimensions per embedding
```

Therefore:

```text
Sentence 1 → 384 numbers
Sentence 2 → 384 numbers
Sentence 3 → 384 numbers
Sentence 4 → 384 numbers
Sentence 5 → 384 numbers
Sentence 6 → 384 numbers
```

So:

> **6 vectors, each containing 384 dimensions.**

---

# 10. Cosine Similarity

Once text has been converted into vectors, we can compare them.

A common measure is cosine similarity:

\[
\text{cosine similarity}(A,B)
=
\frac{A\cdot B}{\|A\|\|B\|}
\]

Dot product:

\[
A\cdot B = \sum_i a_i b_i
\]

Cosine similarity measures how similarly two vectors are oriented.

Conceptually:

```text
Similar meaning
      ↓
Vectors tend to point in similar directions
      ↓
Higher cosine similarity
```

Code:

```python
from sklearn.metrics.pairwise import cosine_similarity

similarities = cosine_similarity(embeddings)

print("Similarity Matrix:")
print(similarities)
```

---

# 11. Semantic Search

Embeddings enable semantic/vector search.

```text
Documents
    ↓
Chunking
    ↓
Embedding Model
    ↓
Vectors
    ↓
Vector Database
```

Then:

```text
User Query
    ↓
Embedding Model
    ↓
Query Vector
    ↓
Similarity Search
    ↓
Most relevant vectors
    ↓
Original text chunks
```

---

# 12. Embeddings in RAG

A basic RAG architecture:

```text
                 COMPANY DOCUMENTS
                         ↓
                    Extract Text
                         ↓
                      Chunking
                         ↓
                  Embedding Model
                         ↓
                       Vectors
                         ↓
                  Vector Database
                         │
                         │
                    User Question
                         ↓
                  Query Embedding
                         ↓
                  Similarity Search
                         ↓
                Relevant Text Chunks
                         ↓
                         LLM
                         ↓
                       Answer
```

The embedding layer helps **retrieve relevant information**.

The LLM uses the retrieved information to **generate the answer**.

---

# 13. Key Formulas

### Token embedding lookup concept

\[
\mathbf{e}_i = E[i]
\]

A token ID acts as an index into a learned embedding matrix.

### Mean pooling

\[
\boxed{
\text{Pooled Vector} =
\frac{1}{n}\sum_{i=1}^{n}v_i
}
\]

### Dot product

\[
\boxed{
A\cdot B=\sum_i a_i b_i
}
\]

### Cosine similarity

\[
\boxed{
\text{cosine similarity}(A,B)
=
\frac{A\cdot B}{\|A\|\|B\|}
}
\]

### Euclidean distance

\[
\boxed{
d(A,B)=\sqrt{\sum_i(a_i-b_i)^2}
}
\]

---

# 14. What I Learned Today

- Embeddings are numerical representations of text.
- Token IDs and embeddings are different.
- An embedding model internally tokenizes and processes text.
- `all-MiniLM-L6-v2` produces 384-dimensional sentence embeddings.
- `(6, 384)` means six vectors, each containing 384 dimensions.
- 384 dimensions do not mean 384 chunks or 384 words.
- Pooling combines token-level representations into a fixed-size text representation.
- Chunking and embedding dimensions are separate concepts.
- Cosine similarity can compare embedding vectors.
- Embeddings are heavily used for semantic search and RAG.
- In RAG, document chunks are embedded and stored, then the user query is embedded and compared against them.
- Retrieved text is supplied to the LLM as context.

---

