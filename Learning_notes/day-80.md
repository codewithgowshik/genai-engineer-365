# Day 80 — Cluster a Handful of Sentences by Similarity

## Objective

Understand how embeddings can be used to group semantically similar sentences into clusters using K-Means.

## 1. What Is Clustering?

**Clustering = automatically putting similar things into groups.**

Example:

```text
"I love Python programming."
"Python is my favourite language."
"I enjoy building software."

"I love eating pizza."
"Pizza is my favourite food."
"I enjoy cooking meals."

"I love travelling around Europe."
"I want to visit France."
"Travelling is my favourite hobby."
```

A clustering algorithm can discover:

```text
Cluster 1 → Programming
Cluster 2 → Food
Cluster 3 → Travel
```

The algorithm does not need the topic names beforehand.

## 2. Embeddings Before Clustering

A computer needs numerical data to perform clustering.

```text
Sentence
   ↓
Embedding model
   ↓
384-dimensional vector
   ↓
K-Means
   ↓
Cluster
```

The embedding represents the sentence as a point in a high-dimensional vector space.

## 3. What Is K-Means?

**K-Means is a clustering algorithm.**

- **K** = number of clusters.
- **Means** = average/mean position used to calculate cluster centres.

For example:

```python
n_clusters=3
```

means:

> Create 3 clusters.

The cluster centres are called **centroids**.

## 4. What Is a Centroid?

A **centroid** is the centre of a cluster.

```text
      ●
   ●  ★  ●
      ●
```

`★` represents the centroid.

The centroid is calculated from the average position of the vectors assigned to that cluster.

## 5. How K-Means Works

```text
Choose K
   ↓
Choose initial centroids
   ↓
Assign each vector to its nearest centroid
   ↓
Calculate the mean of each cluster
   ↓
Move each centroid to the new mean
   ↓
Repeat
   ↓
Clusters become stable
```

The key cycle is:

> **Assign → Calculate Mean → Move Centroid → Repeat**

## 6. How Vectors Are Assigned

Each sentence has an embedding:

```text
Sentence
   ↓
[384 numerical values]
```

K-Means compares the vector's position with the centroid positions and assigns the vector to the closest centroid.

```text
Vector A → Centroid 1
Vector B → Centroid 1
Vector C → Centroid 2
Vector D → Centroid 3
```

## 7. Mathematical Idea

K-Means uses distance to determine how close a vector is to a centroid.

A common distance measure is Euclidean distance:

```text
d(A,B) = √( Σᵢ (aᵢ - bᵢ)² )
```

For Day 80, this idea is applied across all 384 dimensions.

## 8. Centroid / Mean Formula

For vectors:

```text
v₁, v₂, ..., vₙ
```

the centroid is:

$$
\boxed{C=\frac{1}{n}\sum_{i=1}^{n}v_i}
$$

Example:

```text
A = [2, 4]
B = [4, 6]
C = [6, 8]
```

Mean:

```text
x = (2 + 4 + 6) / 3 = 4
y = (4 + 6 + 8) / 3 = 6
```

Therefore:

```text
Centroid = [4, 6]
```

This is why it is called **K-Means**.

## 9. Random State / Seed

```python
random_state=42
```

`42` is **not a coordinate** and does not become a centroid.

It is a **seed value** used to make the random initialization reproducible.

```text
Seed
 ↓
Pseudo-random generator
 ↓
Random initialization
 ↓
Initial centroids
```

You can also use:

```python
random_state=10
```

or:

```python
random_state=17
```

Different seeds can produce different initial starting positions.

However, the final clustering can still be identical when the dataset is easy to separate.

## 10. Why Changing the Seed May Not Change the Output

For a simple dataset such as:

```text
Programming
Food
Travel
```

the groups are clearly separated in the embedding space.

Therefore:

```text
random_state=42
```

and:

```text
random_state=17
```

can produce the same final clusters.

The starting points may differ, but the algorithm can converge to the same stable grouping.

## 11. What Is `n_init`?

```python
n_init=10
```

K-Means can be sensitive to its initial centroid positions.

`n_init=10` tells the algorithm to try multiple initializations and select the better clustering result according to its objective.

```text
Initialization 1 → result
Initialization 2 → result
...
Initialization 10 → result
          ↓
     Best solution
```

Remember:

```text
random_state → controls reproducible randomness
n_init → number of initializations tried
```

## 12. Cosine Similarity vs Clustering

### Cosine similarity

Answers:

> How similar are these two vectors?

$$
\text{cosine similarity}(A,B)
=
\frac{A\cdot B}{\|A\|\|B\|}
$$

### Clustering

Answers:

> Which vectors should belong to the same group?

```text
Many vectors
     ↓
K-Means
     ↓
Clusters
```

Remember:

```text
Cosine similarity → COMPARE
Clustering → GROUP
K-Means → ONE METHOD FOR GROUPING
```

## 13. Day 78 → Day 79 → Day 80

### Day 78 — Embeddings

```text
Text
 ↓
Embedding
 ↓
384-dimensional vector
```

Question:

> How can I represent text numerically?

### Day 79 — Similarity

```text
Vector A
   ↕
Cosine similarity
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

## 14. Python Code

```python
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans


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

print("Embedding shape:", embeddings.shape)


# 4. Choose number of clusters
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)


# 5. Cluster the embeddings
labels = kmeans.fit_predict(embeddings)


# 6. Display results
for i, sentence in enumerate(sentences):
    print(f"Cluster {labels[i]}: {sentence}")
```

## 15. Understanding `fit_predict()`

```python
labels = kmeans.fit_predict(embeddings)
```

does two things:

**fit** → learns the cluster structure and centroids.

**predict** → assigns each embedding to a cluster.

```text
fit_predict()
     ↓
Learn + Assign
```

## 16. Understanding `enumerate()`

`enumerate()` gives both the **index** and the **value**.

```python
for i, sentence in enumerate(sentences):
    print(i, sentence)
```

Output:

```text
0 I love Python
1 I love pizza
2 I love travelling
```

In the clustering code, the index connects each sentence to its cluster label:

```python
for i, sentence in enumerate(sentences):
    print(f"Cluster {labels[i]}: {sentence}")
```

The cluster numbers are arbitrary. `Cluster 0` does not inherently mean Food or Programming.

## 17. Real-World Applications

### Document organization

```text
Documents
 ↓
Embeddings
 ↓
Clustering
 ↓
Finance / Legal / HR / Marketing / Engineering
```

### Customer feedback

```text
Customer feedback
 ↓
Embeddings
 ↓
Clusters
 ↓
Pricing / Delivery / Product / Features
```

### Support tickets

```text
Support tickets
 ↓
Embeddings
 ↓
Clusters
 ↓
Login / Payment / Account / Technical
```

## 18. Clustering vs RAG

### Clustering

Used to organize or discover groups:

```text
Documents
 ↓
Embeddings
 ↓
Clustering
 ↓
Groups
```

### RAG

Used to retrieve relevant information for a query:

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
LLM
```

## 19. Key Formulas

### Mean / Centroid

$$
\boxed{C=\frac{1}{n}\sum_{i=1}^{n}v_i}
$$

### Euclidean Distance

$$
\boxed{d(A,B)=\sqrt{\sum_i(a_i-b_i)^2}}
$$

### Cosine Similarity

$$
\boxed{
\text{cosine similarity}(A,B)
=
\frac{A\cdot B}{\|A\|\|B\|}
}
$$

## 20. What I Learned Today

- Clustering automatically groups similar data points.
- K-Means is a clustering algorithm.
- `K` represents the number of clusters.
- A centroid represents the centre of a cluster.
- Embeddings convert sentences into numerical vectors.
- K-Means works with these numerical vectors.
- Each vector is assigned to its nearest centroid.
- Centroids are recalculated using the mean of their assigned vectors.
- K-Means repeats the assignment and centroid-update process until the result stabilizes.
- `random_state` is a seed used for reproducible randomness.
- `n_init` controls how many initializations K-Means tries.
- `enumerate()` provides both an index and a value in Python.
- Cosine similarity compares vectors; clustering groups vectors.
- Cluster labels such as `0`, `1`, and `2` are arbitrary identifiers.

## One-Line Takeaway

> **Embeddings turn sentences into vectors; K-Means uses those vectors to find groups by repeatedly assigning vectors to nearby centroids and moving the centroids to the mean of their groups.**
