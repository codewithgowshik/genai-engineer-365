# Day 83 — Annotate a Transformer Diagram in Your Notes

## Objective

Understand the difference between **encoder and decoder Transformer models** and annotate the main stages of a Transformer at a high level.

---

## 1. What Is a Transformer?

A **Transformer** is a neural network architecture designed to process sequences using **attention**.

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
Contextual representations / probabilities
 ↓
Output
```

The important idea is that **attention allows tokens to interact with other tokens and understand their context**.

---

## 2. High-Level Transformer Diagram

```text
                         TRANSFORMER
                              │
                              ↓
                       Input Tokens
                              │
                              ↓
                         Embeddings
                              │
                              ↓
                    Positional Information
                              │
                              ↓
                 ┌────────────────────────┐
                 │   Transformer Layers   │
                 │                        │
                 │  ┌──────────────────┐  │
                 │  │     Attention    │  │
                 │  └────────┬─────────┘  │
                 │           ↓            │
                 │  ┌──────────────────┐  │
                 │  │ Feed-Forward NN  │  │
                 │  └────────┬─────────┘  │
                 │           ↓            │
                 │      Normalization     │
                 │           ↓            │
                 │        Repeat          │
                 └────────────┬───────────┘
                              ↓
                    Contextual Representation
                              │
                              ↓
                         Output Layer
                              │
                              ↓
                       Output / Tokens
```

This is a simplified conceptual diagram. Actual Transformer implementations can differ.

---

## 3. Encoder vs Decoder

The two important Transformer patterns are:

```text
Encoder
   ↓
Understands / represents input


Decoder
   ↓
Generates output
```

| Encoder | Decoder |
|---|---|
| Mainly processes input to create representations | Mainly generates output/token sequences |
| Can use bidirectional self-attention | Uses causal/masked self-attention for generation |
| Useful for understanding and embeddings | Useful for text generation |
| Example: BERT-style models | Example: GPT-style models |

---

## 4. Encoder Model

An encoder reads the input and creates a contextual representation.

```text
Input
  ↓
Tokens
  ↓
Embeddings
  ↓
Self-Attention
  ↓
Feed-Forward Network
  ↓
Output Representation
```

Example:

```text
"The cat is sleeping."
```

The encoder processes the tokens together and creates contextual representations.

Conceptually:

```text
The ←→ cat ←→ is ←→ sleeping
```

The tokens can use information from the surrounding input.

---

## 5. Decoder Model

A decoder is commonly used for **autoregressive text generation**.

Example:

```text
"The cat"
     ↓
Predict next token
     ↓
"sat"
     ↓
Predict next token
     ↓
"on"
     ↓
Predict next token
     ↓
"the"
```

The process is:

```text
Prompt
  ↓
Tokens
  ↓
Embeddings
  ↓
Masked/Causal Self-Attention
  ↓
Feed-Forward Network
  ↓
Output Probabilities
  ↓
Choose next token
  ↓
Add token to sequence
  ↓
Repeat
```

The decoder cannot use future tokens when predicting the current token.

---

## 6. Why Is Decoder Attention Masked?

Suppose the model is generating:

```text
"The cat sat"
```

When predicting:

```text
"sat"
```

the model should only use information available before that position.

Conceptually:

```text
The   cat   sat   on   the
 ↓     ↓
 ✓     ✓     ✗     ✗     ✗
```

The future tokens are hidden.

This is called **causal attention** or **masked self-attention**.

It prevents the model from looking ahead during autoregressive generation.

---

## 7. Self-Attention

Self-attention allows tokens in the same sequence to interact.

Example:

```text
"The animal crossed the road because it was tired."
```

The model needs to understand relationships between:

```text
animal
it
tired
```

Self-attention calculates how much one token should attend to other tokens.

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

## 8. Query, Key and Value

Attention uses three representations:

```text
Query
Key
Value
```

Simple intuition:

### Query

> What information am I looking for?

### Key

> What information does this token contain?

### Value

> What information should be passed forward?

Flow:

```text
Query
  ↓
Compare with Keys
  ↓
Similarity Scores
  ↓
Softmax
  ↓
Attention Weights
  ↓
Weighted Values
  ↓
Attention Output
```

---

## 9. Softmax in Attention

Before softmax:

```text
Raw attention scores

cat      5.0
mat      2.0
dog      1.0
```

Softmax converts these scores into normalized weights.

Conceptually:

```text
cat      0.95
mat      0.04
dog      0.01
```

The weights indicate how strongly the model attends to the different tokens.

Formula:

```text
softmax(xᵢ) = eˣⁱ / Σⱼ eˣʲ
```

Remember:

> **Softmax converts raw scores into normalized weights/probabilities.**

---

## 10. Scaled Dot-Product Attention

The standard formula is:

```text
Attention(Q, K, V)
= softmax((Q × Kᵀ) / √dₖ) × V
```

High-level interpretation:

```text
Q + K
 ↓
Calculate similarity scores
 ↓
Scale scores
 ↓
Softmax
 ↓
Attention weights
 ↓
Weight V
 ↓
Attention output
```

For Day 83, the goal is understanding the flow rather than doing the heavy mathematics manually.

---

## 11. Feed-Forward Network

After attention, the representation passes through a **feed-forward neural network**.

```text
Attention Output
      ↓
Feed-Forward Network
      ↓
Transformed Representation
```

The feed-forward layer applies learned transformations to each token representation.

---

## 12. Residual Connections

Transformers commonly use residual/skip connections.

Conceptually:

```text
Input
  │
  ├───────────────┐
  ↓               │
Attention         │
  ↓               │
Output ───────────┘
        +
        ↓
   Normalization
```

The original input is added back to the transformed output.

This helps information and gradients flow through deep networks.

---

## 13. Normalization

Transformers also use normalization around their sublayers.

Conceptually:

```text
Attention
   ↓
Residual Connection
   ↓
Normalization
   ↓
Feed-Forward
   ↓
Residual Connection
   ↓
Normalization
```

The exact placement can vary between Transformer implementations.

---

## 14. Transformer Layer

A simplified Transformer layer can be remembered as:

```text
Input
  ↓
Self-Attention
  ↓
Residual + Normalization
  ↓
Feed-Forward Network
  ↓
Residual + Normalization
  ↓
Output
```

Many Transformer layers are stacked together:

```text
Input
  ↓
Layer 1
  ↓
Layer 2
  ↓
Layer 3
  ↓
...
  ↓
Layer N
```

---

## 15. Encoder Transformer

```text
Input Tokens
     ↓
Embeddings
     ↓
Positional Information
     ↓
┌─────────────────────────┐
│ Transformer Encoder     │
│                         │
│ Self-Attention          │
│       ↓                 │
│ Residual + Norm         │
│       ↓                 │
│ Feed-Forward            │
│       ↓                 │
│ Residual + Norm         │
└───────────┬─────────────┘
            ↓
Contextual Representations
```

The encoder is useful when the goal is to **understand or represent the input**.

---

## 16. Decoder Transformer

```text
Previous Tokens
      ↓
Embeddings
      ↓
Positional Information
      ↓
┌─────────────────────────┐
│ Transformer Decoder     │
│                         │
│ Causal Self-Attention   │
│       ↓                 │
│ Residual + Norm         │
│       ↓                 │
│ Feed-Forward            │
│       ↓                 │
│ Residual + Norm         │
└───────────┬─────────────┘
            ↓
      Output Logits
            ↓
          Softmax
            ↓
   Next Token Probability
            ↓
       Next Token
```

The decoder is commonly used to **generate text one token at a time**.

---

## 17. Encoder-Only vs Decoder-Only

### Encoder-only

```text
Text
 ↓
Encoder
 ↓
Representation
```

Useful for:

- Text embeddings
- Classification
- Semantic similarity
- Understanding input

### Decoder-only

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

Useful for:

- Text generation
- Chat
- Code generation
- Autoregressive completion

---

## 18. What About Encoder-Decoder?

There is also a third important architecture:

**Encoder-Decoder**

```text
Input
  ↓
Encoder
  ↓
Representation
  ↓
Decoder
  ↓
Output
```

This is useful for sequence-to-sequence tasks.

Example:

```text
English sentence
       ↓
    Encoder
       ↓
Meaning representation
       ↓
    Decoder
       ↓
French sentence
```

Remember:

```text
Encoder-only
→ Understand / represent

Decoder-only
→ Generate

Encoder-decoder
→ Transform one sequence into another
```

---

## 19. Transformer vs Embedding Model

Do not confuse these concepts.

### Embedding model

```text
Text
 ↓
Embedding model
 ↓
Vector
```

Purpose:

> Produce a numerical representation of text.

### Transformer

```text
Tokens
 ↓
Attention + neural network layers
 ↓
Contextual representations
 ↓
Output
```

A Transformer architecture can be used inside models that produce embeddings.

For example, `all-MiniLM-L6-v2` uses a Transformer-based architecture to create sentence embeddings.

---

## 20. Transformer vs RAG

They solve different parts of an AI system.

### Transformer

```text
Tokens
 ↓
Transformer
 ↓
Contextual representations
 ↓
Model output
```

### RAG

```text
Documents
 ↓
Chunks
 ↓
Embeddings
 ↓
Vector Database

User Query
 ↓
Query Embedding
 ↓
Similarity Search
 ↓
Relevant Chunks
 ↓
LLM / Transformer
 ↓
Answer
```

RAG can therefore use a Transformer-based model to process the retrieved context.

---

## 21. Day 78 → Day 83

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
Cosine Similarity
 ↓
Highest Score
 ↓
Most Similar Item
```

### Day 83 — Transformer

```text
Tokens
 ↓
Embeddings
 ↓
Transformer Layers
 ↓
Attention
 ↓
Contextual Representations
 ↓
Output
```

---

## 22. Key Formulas

### Cosine Similarity

```text
cosine similarity(A, B)
= (A · B) / (||A|| × ||B||)
```

### Dot Product

```text
A · B = Σᵢ(aᵢ × bᵢ)
```

### Softmax

```text
softmax(xᵢ) = eˣⁱ / Σⱼ eˣʲ
```

### Scaled Dot-Product Attention

```text
Attention(Q, K, V)
= softmax((Q × Kᵀ) / √dₖ) × V
```

### Mean / Centroid

```text
C = (1/n) × Σᵢ vᵢ
```

### Euclidean Distance

```text
d(A,B) = √(Σᵢ(aᵢ - bᵢ)²)
```

---

## 23. What I Learned Today

- A Transformer is a neural network architecture based heavily on attention.
- Transformers process token representations through multiple layers.
- Self-attention allows tokens to interact with other tokens.
- Query, Key and Value are used in attention.
- Softmax converts attention scores into normalized weights.
- Feed-forward networks transform the representations after attention.
- Residual connections help information and gradients flow through the network.
- Normalization is used around Transformer sublayers.
- Encoder models are mainly used to create contextual representations of input.
- Decoder models are commonly used for autoregressive text generation.
- Decoder self-attention uses causal masking so the model cannot look at future tokens during generation.
- Encoder-decoder models can transform one sequence into another.
- Transformer architecture and embedding models are related but are not the same thing.
- RAG uses retrieval to provide external context to an LLM.

---

## One-Line Takeaway

> **A Transformer processes token representations through repeated attention and feed-forward layers; encoder models focus on understanding input, while decoder models commonly generate text one token at a time.**
