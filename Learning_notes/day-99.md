# Day 99 — Create Project 3 Repo and Design It

## Objective

Define the product and create the foundation for **Project 3: Semantic Search Engine**.

Today is about deciding what the product should do, why it is useful, and how the project will be organised before building the implementation.

## What I Learned

### 1. Defining the Product

Before building a project, I need to clearly understand the problem the product is solving.

For Project 3, the problem is:

> Users should be able to search documents based on meaning, rather than relying only on exact keyword matches.

The product goal is to build a search engine that can find relevant information from documents using semantic similarity.

## 2. What the Semantic Search Engine Should Do

The project will eventually be able to:

- Process documents
- Split documents into chunks
- Create embeddings
- Store and search vectors
- Convert user queries into embeddings
- Retrieve top-K results
- Combine keyword and vector search
- Rank search results
- Evaluate search quality

These capabilities are based on the search concepts learned before starting Project 3.

## 3. Search Pipeline

The overall product can be represented as:

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

### What each stage means

**Documents**

The information that the search engine needs to search.

**Chunking**

Breaking larger documents into smaller pieces.

**Embeddings**

Representing text as numerical vectors.

**Vector Database**

Storing and searching the vectors.

**Query Embedding**

Converting the user's search query into a vector.

**Search**

Finding documents or chunks that are similar to the query.

**Ranking**

Ordering results by relevance.

**Top-K**

Returning the best K results.

## 4. Project Architecture

The project is organised into separate areas:

```text
semantic-search-engine/
│
├── README.md
│
├── data/
│
├── src/
│
└── tests/
```

### `README.md`

Documents what the project is, its goal, and how the system is structured.

### `data/`

Contains the documents and data that the search engine will work with.

### `src/`

Contains the implementation of the search engine.

The implementation will be built incrementally rather than all at once.

### `tests/`

Contains tests used to check whether the search system works correctly and whether search quality is improving.

## 5. Project Structure

The planned structure is:

```text
semantic-search-engine/
├── README.md
├── data/
│   └── documents.txt
├── src/
│   ├── chunking.py
│   ├── embeddings.py
│   ├── search.py
│   └── hybrid_search.py
└── tests/
    └── test_search.py
```

The files are organised according to their future responsibilities.

## 6. Connection to Previous Learning

Project 3 brings together the concepts learned during the Semantic Search Foundations section.

```text
Semantic Search
      ↓
Chunking
      ↓
Query Embedding
      ↓
Top-K Retrieval
      ↓
Keyword Search
      ↓
Hybrid Search
      ↓
Search Evaluation
      ↓
Project 3
```

The project is therefore not starting from zero.

It is taking the individual concepts learned earlier and turning them into one complete system.

## 7. Product vs Implementation

An important lesson today is that **defining the product comes before building the implementation**.

The product answers:

> What are we building and what problem does it solve?

The implementation answers:

> How are we going to build it?

For Day 99, the focus is primarily on the first question and on creating a clean project structure.

## What I Built Today

I created the foundation for **Project 3 — Semantic Search Engine**:

- Created the project repository
- Defined the product goal
- Designed the search pipeline
- Planned the project architecture
- Created the initial folder and file structure
- Prepared the project for incremental implementation

## Key Concepts

- Product definition identifies the problem and goal of a project.
- A clear product goal helps guide implementation decisions.
- Project architecture separates responsibilities into organised components.
- Semantic search uses meaning rather than only exact keyword matching.
- Project 3 combines the semantic-search concepts learned in previous days.
- The implementation will be developed incrementally.

## One-Line Takeaway

**Day 99 turns the semantic-search concepts I learned into a clearly defined Project 3 with a planned product and project architecture.**
