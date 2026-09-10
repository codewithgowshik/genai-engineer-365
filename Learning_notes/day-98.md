# Day 98 — Measure Precision@k

## 📚 Learn (30 min): Search UX

**Topic:** Evaluating the quality of semantic search results

---

## 1. What is Search UX?

Search UX means the experience a user has when they search for something and receive results.

For a semantic search system, good Search UX is not simply about returning results quickly.

The results should be:

- Relevant
- Useful
- Related to the user's intent
- Ranked appropriately
- Free from unnecessary results

For example, if a user searches:

> "How do I reset my password?"

A good semantic search system should return documents about **password resets**, not merely documents containing words such as "password" or "account".

---

## 2. The Semantic Search Pipeline

```text
User Query
    ↓
Embedding
    ↓
Query Vector
    ↓
Vector Database
    ↓
Similarity Search
    ↓
Top-k Results
    ↓
Relevance Evaluation
    ↓
Precision@k
```

The important question today is:

> **How do we know whether the retrieved results are actually relevant?**

This is where evaluation metrics become important.

---

## 3. Similarity Does Not Equal Relevance

Our vector database calculates how similar the query vector is to stored document vectors.

For example:

```text
Query:
"What is the company's carbon reduction target?"

Retrieved results:

1. Carbon reduction target       → 0.91
2. Renewable energy usage        → 0.87
3. Employee benefits             → 0.62
4. Office locations              → 0.55
```

The similarity score tells us that result #1 is close to the query.

But the similarity score itself does **not** tell us whether the result is actually useful to the user.

Therefore we need a **relevance test set**.

---

## 4. Relevance Test Set

A relevance test set contains queries and the results that we consider relevant.

Example:

```python
test_cases = [
    {
        "query": "What is the carbon reduction target?",
        "relevant": [
            "carbon reduction target",
            "emissions reduction goals"
        ]
    },
    {
        "query": "How much renewable energy does the company use?",
        "relevant": [
            "renewable energy percentage"
        ]
    }
]
```

The test set gives us something against which we can evaluate our search system.

---

## 5. What is Precision@k?

**Precision@k** measures how many of the first `k` retrieved results are relevant.

```text
Precision@k = Number of relevant results in top k / k
```

For example:

```text
Top 5 results:

1. Relevant      ✓
2. Relevant      ✓
3. Not relevant  ✗
4. Relevant      ✓
5. Not relevant  ✗
```

There are **3 relevant results** in the top 5.

Therefore:

```text
Precision@5 = 3 / 5
            = 0.60
```

So the search system has a **60% Precision@5** for this query.

---

## 6. Why `k` Matters

`k` represents the number of top results we are evaluating.

Examples:

```text
Precision@1
Precision@3
Precision@5
Precision@10
```

### Precision@1

> Is the first result relevant?

### Precision@3

> How useful are the first three results?

### Precision@5

> How useful are the first five results?

For a search interface that displays the first 5 results, **Precision@5** can be particularly useful.

---

## 7. Implementing Precision@k

A simple Python implementation is:

```python
def precision_at_k(retrieved, relevant, k):
    top_k = retrieved[:k]

    relevant_count = sum(
        1 for item in top_k
        if item in relevant
    )

    return relevant_count / k
```

Example:

```python
retrieved = [
    "carbon reduction target",
    "renewable energy",
    "employee benefits",
    "emissions reduction goals",
    "office locations"
]

relevant = {
    "carbon reduction target",
    "emissions reduction goals"
}

score = precision_at_k(
    retrieved,
    relevant,
    5
)

print(score)
```

Output:

```text
0.4
```

Because:

```text
Relevant results = 2
k = 5

Precision@5 = 2 / 5
            = 0.4
```

---

## 8. Testing Multiple Queries

One query is not enough to evaluate a search system.

We should test several queries.

Example:

```python
test_cases = [
    {
        "query": "What is the carbon reduction target?",
        "retrieved": [
            "carbon reduction target",
            "renewable energy",
            "employee benefits",
            "emissions reduction goals",
            "office locations"
        ],
        "relevant": {
            "carbon reduction target",
            "emissions reduction goals"
        }
    },
    {
        "query": "What percentage of energy is renewable?",
        "retrieved": [
            "renewable energy",
            "carbon reduction target",
            "employee benefits",
            "office locations",
            "company history"
        ],
        "relevant": {
            "renewable energy"
        }
    }
]
```

Then calculate Precision@5 for each query.

---

## 9. Average Precision@k

After evaluating multiple queries, we can calculate the average.

Example:

```text
Query 1 → Precision@5 = 0.80
Query 2 → Precision@5 = 0.60
Query 3 → Precision@5 = 1.00
```

Average:

```text
(0.80 + 0.60 + 1.00) / 3
= 0.80
```

So:

```text
Average Precision@5 = 0.80
```

This gives us a better picture of the search system than evaluating only one query.

---

## 10. Precision vs Recall

Precision and recall measure different things.

### Precision

> Of the results we retrieved, how many were relevant?

```text
Precision = Relevant Retrieved / Retrieved
```

### Recall

> Of all the relevant results available, how many did we retrieve?

```text
Recall = Relevant Retrieved / Total Relevant
```

For Day 98, our focus is **Precision@k**.

We are asking:

> **Are the results near the top actually useful?**

---

## 11. Why Precision@k Is Useful for Semantic Search

Imagine our system returns:

```text
Top 5:

1. Relevant
2. Relevant
3. Relevant
4. Irrelevant
5. Irrelevant
```

Then:

```text
Precision@5 = 3 / 5 = 0.60
```

If we improve the embedding model, chunking strategy, metadata filtering, or retrieval configuration and get:

```text
Top 5:

1. Relevant
2. Relevant
3. Relevant
4. Relevant
5. Relevant
```

Then:

```text
Precision@5 = 5 / 5 = 1.00
```

We now have a measurable way to determine whether our search system improved.

---

## 12. Precision@k and Search UX

Search UX is strongly affected by the quality of the first few results.

Users usually care most about:

```text
Result #1
Result #2
Result #3
...
```

They don't want to inspect hundreds of irrelevant documents.

Therefore, improving **top-k precision** can directly improve the usefulness of a semantic search system.

A useful mental model is:

```text
Better Retrieval
      ↓
More Relevant Top-k Results
      ↓
Higher Precision@k
      ↓
Better Search UX
```

---

## 13. What We Are NOT Building Today

Do **not** jump to a full RAG system today.

Today's focus is:

```text
Query
 ↓
Embedding
 ↓
Vector Search
 ↓
Top-k Results
 ↓
Evaluate Results
 ↓
Precision@k
```

We are evaluating the **retrieval layer first**.

Only after retrieval works reliably should we add an LLM that generates an answer from the retrieved context.

---

## 14. Practical Evaluation Workflow

```text
1. Use the relevance test set from Day 97
        ↓
2. Run each query through semantic search
        ↓
3. Retrieve top-k results
        ↓
4. Compare retrieved results with relevant results
        ↓
5. Calculate Precision@k
        ↓
6. Repeat for multiple queries
        ↓
7. Calculate average Precision@k
        ↓
8. Identify weak queries
```

---

# 🛠️ BUILD — Measure Precision@k

Create a small evaluation script/function.

The core function should look like:

```python
def precision_at_k(retrieved, relevant, k):
    top_k = retrieved[:k]

    relevant_count = sum(
        1 for item in top_k
        if item in relevant
    )

    return relevant_count / k
```

Then test it using the relevance test set you created on **Day 97**.

Evaluate several queries rather than only one.

---

## 🧪 Example Evaluation

```text
Query 1
Precision@5 → 0.80

Query 2
Precision@5 → 0.60

Query 3
Precision@5 → 1.00
```

Then:

```text
Average Precision@5 → 0.80
```

Record the results so we can compare them against future improvements.

---

# 🧠 Key Concepts to Remember

### Semantic Search

Search based on **meaning**, rather than only exact keyword matches.

### Embedding

A numerical representation of the meaning of text.

### Vector Search

Finds stored vectors that are mathematically similar to the query vector.

### Top-k

The first `k` results returned by the search system.

### Relevance

Whether a retrieved result is actually useful for the query.

### Precision@k

Measures how many of the top `k` retrieved results are relevant.

```text
Precision@k = Relevant results in top-k / k
```

### Search UX

The quality and usefulness of the user's search experience, especially the relevance of the highest-ranked results.

---

# 🎯 Day 98 Takeaway

The important lesson is:

> **A search system is not good simply because it returns results. We need to measure whether those results are relevant.**

The progression is:

```text
Embedding
    ↓
Vector Search
    ↓
Top-k Retrieval
    ↓
Relevance Test Set
    ↓
Precision@k
    ↓
Measure Search Quality
    ↓
Improve Retrieval
```

**Day 97** gave us the relevance test set.

**Day 98** uses that test set to measure retrieval quality.

**Next:** use these measurements to improve the search system rather than blindly assuming that higher similarity scores mean better results.
