# Semantic Search Engine

Project 3 of my 365 Gen AI learning journey.

A semantic search engine that retrieves relevant information based on meaning rather than only exact keyword matches.

## Goal

Build a search system that can:

- Process documents
- Split documents into chunks
- Create embeddings
- Store and search vectors
- Embed user queries
- Retrieve top-K results
- Combine keyword and vector search
- Rank results
- Evaluate search quality

## Search Pipeline

```text
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Query Embedding
    ↓
Search
    ↓
Ranking
    ↓
Top-K Results
```

## Project Structure

- `data/` — project documents and data
- `src/` — application implementation
- `tests/` — search quality and application tests

## Project Status

Project 3 — foundation and design phase.
