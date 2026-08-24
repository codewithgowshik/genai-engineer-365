# Day 84 — Embeddings Explainer Note

## Objective

Understand **why context matters** and how embeddings represent the meaning of text as numerical vectors.

---

## 1. What Is an Embedding?

An embedding is a numerical representation of information.

```text
Sentence
   ↓
Embedding Model
   ↓
Vector
```

Example:

```text
"I love Python programming."
        ↓
[0.12, -0.43, 0.71, 0.08, ...]
```

With the model used in this project:

```text
Sentence
   ↓
all-MiniLM-L6-v2
   ↓
384-dimensional vector
```

---

## 2. Why Do We Need Embeddings?

Computers cannot directly calculate semantic similarity between raw sentences.

For example:

```text
"I love Python."
```

and:

```text
"Python is my favourite programming language."
```

use different wording but have similar meaning.

Embeddings represent both as vectors so their positions in vector space can be compared.

```text
Text A
  ↓
Vector A

Text B
  ↓
Vector B

Vector A ↔ Vector B
       ↓
Similarity
```

---

## 3. Embedding Space

An embedding vector can be thought of as a position in a high-dimensional **vector space**.

For a simple 2D illustration:

```text
                 Y
                 ↑

       ● Python programming

                 ● Python language


                            ● Pizza


    ● Travel
                 └────────────────→ X
```

In the real model there are many more dimensions.

For `all-MiniLM-L6-v2`:

```text
384 dimensions
```

We cannot directly visualise all 384 dimensions, but the vector still exists mathematically in that high-dimensional space.

---

## 4. What Does a Dimension Mean?

A common misunderstanding is:

> "Dimension 1 = programming, dimension 2 = food, dimension 3 = travel."

Usually, it does **not** work that simply.

A dimension is one numerical component of the learned representation.

```text
[
    0.12,
   -0.43,
    0.71,
    0.08,
    ...
]
```

The meaning of the sentence is distributed across many dimensions.

Think of the **complete vector** as the representation rather than assigning one simple human-readable meaning to each individual dimension.

---

## 5. How Text Becomes an Embedding

A simplified pipeline is:

```text
Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
Token Embeddings
 ↓
Transformer
 ↓
Contextual Token Representations
 ↓
Pooling
 ↓
Sentence Embedding
```

The embedding model is not simply creating 384 random numbers.

A trained neural network produces the representation based on patterns learned during training.

---

## 6. Tokens vs Embeddings

These are different concepts.

### Tokens

Tokens are pieces of text used by the model.

```text
"Python programming"
        ↓
Tokens
        ↓
Token IDs
```

### Embeddings

Embeddings are numerical vectors representing information.

```text
Token / sentence
       ↓
Vector
```

Therefore:

```text
Tokenization → breaks text into model-readable pieces

Embedding → represents information numerically
```

---

## 7. Why Context Matters

This is today's main topic.

Consider:

```text
"I went to the bank."
```

What does **bank** mean?

It could mean:

```text
Bank → financial institution
```

or:

```text
Bank → side of a river
```

The surrounding context determines the meaning.

Compare:

```text
"I deposited money at the bank."
```

with:

```text
"I sat on the bank of the river."
```

The word **bank** is the same, but the context is different.

---

## 8. Context Changes Representation

A Transformer can use surrounding tokens to understand contextual meaning.

```text
"I deposited money at the bank."
                    ↓
             financial context


"I sat on the bank of the river."
                    ↓
                river context
```

This is one reason **attention** is important.

```text
Word
 ↓
Look at surrounding tokens
 ↓
Understand relationships
 ↓
Contextual representation
```

---

## 9. Static vs Contextual Representations

### Static representation

A static representation gives the same representation to a word regardless of the sentence.

```text
bank
 ↓
same vector
```

### Contextual representation

A contextual representation depends on surrounding information.

```text
"bank" + financial context
        ↓
Representation A


"bank" + river context
        ↓
Representation B
```

This is a major idea behind modern Transformer-based language models.

---

## 10. How Attention Helps Context

Consider:

```text
"The animal didn't cross the road because it was tired."
```

When processing:

```text
"it"
```

the model can use attention to examine other tokens.

Conceptually:

```text
it
 ↓
animal       █████████
road         ███
cross        ██
tired        ████
```

High-level flow:

```text
Tokens
 ↓
Queries, Keys, Values
 ↓
Attention Scores
 ↓
Softmax
 ↓
Attention Weights
 ↓
Weighted Values
 ↓
Contextual Representation
```

---

## 11. Embeddings and Context

### Before contextual processing

```text
Token
 ↓
Token embedding
```

### After Transformer processing

```text
Token
 ↓
Attention + Transformer layers
 ↓
Contextual representation
```

### Sentence embedding

An embedding model can combine contextual token representations into one sentence-level vector.

```text
Contextual token representations
              ↓
           Pooling
              ↓
       Sentence embedding
              ↓
          384 values
```

---

## 12. What Is Pooling?

A sentence contains multiple token representations.

Pooling combines them into a single vector.

A simple example is mean pooling:

```text
Token 1 → v₁
Token 2 → v₂
Token 3 → v₃
```

Mean pooling:

```text
Sentence Vector = (v₁ + v₂ + v₃) / 3
```

General formula:

```text
Pooled Vector = (1/n) × Σᵢ vᵢ
```

This is the simple intuition. Specific embedding models can use different pooling implementations and attention-mask handling.

---

## 13. Why Similar Sentences Have Similar Vectors

Suppose:

```text
Sentence A:
"I love programming in Python."

Sentence B:
"Python is my favourite programming language."
```

Their meanings are related.

The embedding model can place their vectors relatively close in embedding space.

```text
             Programming

          ● A
             ● B


                        ● Pizza
```

This allows similarity methods such as cosine similarity to compare them.

---

## 14. Cosine Similarity

Cosine similarity compares two vectors.

```text
cosine similarity(A, B)
= (A · B) / (||A|| × ||B||)
```

Conceptually:

```text
Similar meaning
      ↓
Similar vector direction
      ↓
Higher cosine similarity
```

---

## 15. Embeddings in Semantic Search

This connects directly to Day 82.

```text
Stored Documents
      ↓
Embedding Model
      ↓
Stored Vectors
      ↓
Vector Database
```

Then:

```text
User Query
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Relevant Vectors
      ↓
Original Documents
```

The query and documents are represented in the same vector space so their semantic relationship can be measured.

---

## 16. Embeddings in RAG

```text
             DOCUMENT SIDE

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
             QUERY SIDE

User Question
      ↓
Query Embedding
      ↓
Vector Search
      ↓
Top Relevant Chunks
      ↓
LLM / Transformer
      ↓
Answer
```

This allows a chatbot to retrieve information from private or external documents.

---

## 17. Embedding Is Not the LLM's Final Answer

An embedding is not:

```text
"Here is the answer to your question..."
```

Instead:

```text
Text
 ↓
Embedding
 ↓
Vector
```

The vector can be used for:

- Similarity search
- Semantic search
- Clustering
- Recommendation
- Retrieval
- Classification
- RAG

---

## 18. Context vs Embedding

These concepts are related but different.

### Context

Context is surrounding information that helps determine meaning.

```text
"The bank approved my loan."
```

versus:

```text
"I sat beside the river bank."
```

### Embedding

An embedding is the numerical representation produced by a model.

```text
Text
 ↓
Model
 ↓
Vector
```

Therefore:

```text
Context → helps determine meaning

Embedding → represents information numerically
```

---

## 19. Complete Mental Model

```text
Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
Token Embeddings
 ↓
Transformer
 ↓
Attention
 ↓
Contextual Token Representations
 ↓
Pooling
 ↓
Sentence Embedding
 ↓
Vector Space
 ↓
Similarity / Search / Clustering
```

---

## 20. Connection to Everything Learned So Far

### Day 76 — Deterministic Output

```text
Temperature / Seed
 ↓
Control generation randomness
```

### Day 77 — Hallucination

```text
LLM
 ↓
Can generate unsupported information
 ↓
Mitigation / grounding
```

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
Groups
```

### Day 81 — Visualisation

```text
384D
 ↓
PCA
 ↓
2D
 ↓
Visualise
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
Contextual representations
 ↓
Output
```

### Day 84 — Context + Embeddings

```text
Context
 ↓
Transformer / Attention
 ↓
Contextual representations
 ↓
Embedding
 ↓
Vector Space
 ↓
Search / Similarity / RAG
```

---

## 21. Key Formulas

### Mean Pooling

```text
Pooled Vector = (1/n) × Σᵢ vᵢ
```

### Cosine Similarity

```text
cosine similarity(A, B)
= (A · B) / (||A|| × ||B||)
```

### Dot Product

```text
A · B = Σᵢ(aᵢ × bᵢ)
```

### Scaled Dot-Product Attention

```text
Attention(Q, K, V)
= softmax((Q × Kᵀ) / √dₖ) × V
```

---

## 22. What I Learned Today

- Context is essential for understanding the meaning of language.
- The same word can have different meanings depending on surrounding words.
- Transformers use attention to model relationships between tokens.
- Token representations can become contextual representations after Transformer processing.
- Embeddings are numerical representations of information.
- A sentence embedding represents a sentence as a vector.
- `all-MiniLM-L6-v2` produces 384-dimensional sentence embeddings.
- Meaning is distributed across the dimensions of an embedding rather than one dimension representing one simple concept.
- Pooling combines token-level representations into a sentence-level representation.
- Similar meanings can produce vectors that are close in embedding space.
- Cosine similarity can compare those vectors.
- Semantic search uses embeddings to retrieve information based on meaning.
- RAG uses embeddings and vector search to retrieve relevant external information before an LLM generates an answer.

---

## One-Line Takeaway

> **Context helps the Transformer understand meaning; the resulting contextual information can be converted into an embedding vector, allowing us to compare, search, cluster, and retrieve information by semantic meaning.**
