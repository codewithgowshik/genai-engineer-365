# Day 81 — Visualise Embeddings in 2D

## Objective

Understand the basic intuition behind **attention** and learn how to visualise high-dimensional sentence embeddings in **2D**.

---

## 1. What Are Embeddings?

An embedding converts text into a numerical vector.

```text
"I love Python"
      ↓
Embedding Model
      ↓
[0.12, -0.43, 0.71, ...]
      ↓
384-dimensional vector
```

Each sentence is represented by a point in a high-dimensional vector space.

---

## 2. Why Visualise Embeddings?

Our embedding model produces **384 dimensions**, which humans cannot easily visualise.

```text
384 dimensions
      ↓
Dimensionality Reduction
      ↓
2 dimensions
      ↓
X and Y coordinates
```

---

## 3. Dimensionality Reduction

We cannot directly display 384 dimensions on a normal graph, so we can use **PCA (Principal Component Analysis)**.

```text
384D
 ↓
PCA
 ↓
2D
```

PCA creates a lower-dimensional representation that tries to preserve important patterns in the original data.

---

## 4. PCA — Simple Intuition

PCA looks for directions in the data that contain the most variation.

```text
Original 384D data
        ↓
Find important directions
        ↓
Principal Component 1
Principal Component 2
        ↓
Plot using X and Y
```

For our visualisation:

```text
X-axis → Principal Component 1
Y-axis → Principal Component 2
```

---

## 5. Important Warning

A 2D plot is only a **visual approximation**.

Original embeddings:

```text
384 dimensions
```

After PCA:

```text
2 dimensions
```

Some information is therefore lost.

---

# 6. Attention — Intuition

Attention is a mechanism that allows a model to determine:

> **Which parts of the input are important to each other?**

For example:

```text
"The cat sat on the mat because it was tired."
```

When processing **"it"**, the model needs to understand which earlier words are relevant.

Attention helps the model determine relationships between tokens.

---

## 7. Simple Attention Example

Conceptually:

```text
it
 ↓
cat      ██████████
mat      ███
sat      ██
the      █
```

The bars represent attention weights conceptually.

---

## 8. Attention Is Not the Same as Embeddings

### Embedding

```text
Text
 ↓
Vector
```

Purpose:

> Represent information numerically.

### Attention

```text
Tokens
 ↓
Relationships / importance
 ↓
Context-aware representations
```

Purpose:

> Help the model understand which tokens are relevant to each other.

---

## 9. Query, Key and Value

Attention is commonly explained using:

```text
Query
Key
Value
```

Simple intuition:

- **Query:** What am I looking for?
- **Key:** What information does each token represent?
- **Value:** What information should I retrieve?

Flow:

```text
Query
  ↓
Compare with Keys
  ↓
Attention Scores
  ↓
Softmax
  ↓
Attention Weights
  ↓
Weighted Values
  ↓
Output
```

---

## 10. Attention Formula

The standard scaled dot-product attention formula is:

```text
Attention(Q, K, V)
= softmax((Q × Kᵀ) / √dₖ) × V
```

For today, understand the flow rather than memorising the heavy mathematics.

---

# 11. Build — Visualise Embeddings

Install:

```bash
pip install sentence-transformers scikit-learn matplotlib
```

Create:

```text
embedding_visualization.py
```

Code:

```python
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Sentences
sentences = [
    # Programming
    "I love programming in Python.",
    "Python is my favourite programming language.",
    "I enjoy building software.",

    # Food
    "I enjoy eating pizza.",
    "Pizza is one of my favourite foods.",
    "I love cooking delicious meals.",

    # Travel
    "I love travelling around Europe.",
    "I want to visit France and Italy.",
    "Travelling is one of my favourite hobbies.",
]


# 3. Generate embeddings
embeddings = model.encode(sentences)

print("Original embedding shape:", embeddings.shape)


# 4. Reduce 384 dimensions to 2 dimensions
pca = PCA(n_components=2)

embeddings_2d = pca.fit_transform(embeddings)

print("2D embedding shape:", embeddings_2d.shape)


# 5. Plot the embeddings
plt.figure(figsize=(10, 7))

plt.scatter(
    embeddings_2d[:, 0],
    embeddings_2d[:, 1]
)


# 6. Add sentence labels
for i, sentence in enumerate(sentences):
    plt.annotate(
        sentence,
        (
            embeddings_2d[i, 0],
            embeddings_2d[i, 1]
        )
    )


plt.title("Sentence Embeddings Visualised in 2D")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.tight_layout()
plt.show()
```

---

# 12. Understanding the Code

### Generate embeddings

```python
embeddings = model.encode(sentences)
```

Produces:

```text
9 sentences × 384 dimensions
```

So:

```text
(9, 384)
```

### PCA

```python
pca = PCA(n_components=2)
```

means:

> Reduce the 384-dimensional vectors to 2 dimensions.

Then:

```python
embeddings_2d = pca.fit_transform(embeddings)
```

produces:

```text
(9, 2)
```

Each sentence now has:

```text
[X, Y]
```

coordinates.

---

# 13. Understanding `[:, 0]` and `[:, 1]`

After PCA, `embeddings_2d` might look like:

```text
[
    [1.2,  3.5],
    [0.8,  2.9],
    [-1.4, 0.5],
    [2.1, -0.7]
]
```

Think of it as:

```text
          Column 0    Column 1
Row 0       1.2         3.5
Row 1       0.8         2.9
Row 2      -1.4         0.5
Row 3       2.1        -0.7
```

### `[:, 0]`

```python
embeddings_2d[:, 0]
```

means:

```text
: → every row
0 → first column
```

Result:

```text
[1.2, 0.8, -1.4, 2.1]
```

These are the **X coordinates**.

### `[:, 1]`

```python
embeddings_2d[:, 1]
```

means:

```text
: → every row
1 → second column
```

Result:

```text
[3.5, 2.9, 0.5, -0.7]
```

These are the **Y coordinates**.

Python uses zero-based indexing:

```text
0 = first column
1 = second column
```

Therefore:

```python
plt.scatter(
    embeddings_2d[:, 0],  # X
    embeddings_2d[:, 1]   # Y
)
```

means:

> Plot every sentence's first PCA coordinate on X and second PCA coordinate on Y.

---

# 14. What the Plot Represents

Original data:

```text
Sentence 1 → [384 numbers]
Sentence 2 → [384 numbers]
Sentence 3 → [384 numbers]
...
```

After PCA:

```text
Sentence 1 → [X₁, Y₁]
Sentence 2 → [X₂, Y₂]
Sentence 3 → [X₃, Y₃]
...
```

These can be plotted:

```text
             Y
             ↑

        ● ●
       Programming


                         ● ●
                          Food


    ● ●
     Travel

             └────────────────→ X
```

---

# 15. Day 78 → Day 81

### Day 78 — Embeddings

```text
Text
 ↓
384-dimensional vector
```

Question:

> How can I represent text numerically?

### Day 79 — Similarity

```text
Vector A
   ↕
Cosine Similarity
   ↕
Vector B
```

Question:

> How similar are these two texts?

### Day 80 — Clustering

```text
Many vectors
     ↓
K-Means
     ↓
Groups
```

Question:

> Which texts naturally belong together?

### Day 81 — Visualisation

```text
384D vectors
     ↓
PCA
     ↓
2D coordinates
     ↓
Graph
```

Question:

> Can I visually see the structure of my embeddings?

---

# 16. Key Formulas

### Centroid

```text
C = (1/n) × Σᵢ vᵢ
```

### Euclidean Distance

```text
d(A,B) = √(Σᵢ(aᵢ - bᵢ)²)
```

### Cosine Similarity

```text
cosine similarity(A, B)
= (A · B) / (||A|| × ||B||)
```

### Scaled Dot-Product Attention

```text
Attention(Q, K, V)
= softmax((Q × Kᵀ) / √dₖ) × V
```

---

# 17. What I Learned Today

- Embeddings represent sentences as numerical vectors.
- Our model produces 384-dimensional embeddings.
- Humans cannot directly visualise 384 dimensions.
- PCA can reduce the embeddings to 2 dimensions.
- The resulting 2D coordinates can be plotted.
- `[:, 0]` selects every row from the first column.
- `[:, 1]` selects every row from the second column.
- PCA is a visual approximation and loses some information.
- Similar sentences can appear close together in embedding space.
- Attention helps an LLM understand relationships between tokens.
- Attention determines how much focus different tokens should receive.
- Query, Key and Value are the basic components of attention.
- Attention and embeddings are different concepts.
- Embeddings represent information numerically; attention helps process contextual relationships.

---

## One-Line Takeaway

> **We use PCA to compress 384-dimensional embeddings into 2D coordinates for visualisation, while attention helps LLMs determine which tokens are important to each other in context.**
