# Day 93 — Experiment with Chunk Sizes

## Objective

Understand how chunk size affects semantic search and experiment with different chunk sizes.

## What I Learned

### What Is Chunking?

Chunking means splitting a long piece of text into smaller pieces called **chunks** before creating embeddings.

Instead of embedding one very large document:

```text
Long Document
      ↓
Embedding
      ↓
Vector Database
```

we split it first:

```text
Long Document
      ↓
Chunks
      ↓
Embeddings
      ↓
Vector Database
```

This makes it easier for semantic search to find specific and relevant information.

## Why Chunk Size Matters

The size of a chunk affects search quality.

### Smaller Chunks

Advantages:

- More specific information
- Less unrelated content
- Can improve precise retrieval

Disadvantage:

- May lose important context

### Larger Chunks

Advantages:

- More context
- Related information can stay together

Disadvantage:

- May contain unrelated information
- Search results can become less precise

There is no single perfect chunk size for every application.

## Today's Experiment

I experimented with different chunk sizes:

```text
50 characters
100 characters
200 characters
```

The goal was to observe:

- Number of chunks created
- How much text each chunk contains
- How changing the chunk size changes the result

## Chunking Function

```python
def chunk_text(text, chunk_size):
    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]
```

## Example

```python
text = """
Python is a programming language.
Python can be used for web development.
Machine learning allows computers to learn from data.
Neural networks are commonly used in deep learning.
Python is also popular for data analysis.
"""

for size in [50, 100, 200]:

    chunks = chunk_text(text, size)

    print(f"\nChunk size: {size}")
    print(f"Number of chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):

        print(f"\nChunk {i + 1}:")
        print(chunk)
```

## What Changes When Chunk Size Changes?

For the same document:

```text
Small chunk size
→ More chunks
→ More specific pieces
→ Less context per chunk
```

```text
Large chunk size
→ Fewer chunks
→ More context
→ Potentially less precise results
```

## Connection to Semantic Search

Chunking happens **before embedding**.

The complete pipeline is:

```text
Long Text
   ↓
Chunking
   ↓
Text Chunks
   ↓
Embeddings
   ↓
Chroma
   ↓
Semantic Search
   ↓
Relevant Chunks
```

This connects directly to the semantic search function I built on Day 92.

## Key Concepts

- Chunking splits long text into smaller pieces.
- Chunk size determines how much text each chunk contains.
- Smaller chunks can provide more precise information.
- Larger chunks can preserve more context.
- Chunk size affects the quality of semantic search.
- Chunking happens before creating embeddings.

## What I Built

A simple chunking experiment that compares:

- 50-character chunks
- 100-character chunks
- 200-character chunks

## One-Line Takeaway

**Chunk size is a trade-off between precise retrieval and preserving context.**
