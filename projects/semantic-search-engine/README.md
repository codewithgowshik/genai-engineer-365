# Semantic Search Engine

A semantic search application that retrieves documents based on **meaning**, rather than relying only on exact keyword matches.

The project uses embeddings and vector search to understand the relationship between a user's query and stored documents.

---

## Project Overview

Traditional keyword search looks for exact words in a document.

Semantic search works differently.

It converts text into **embeddings** — numerical representations of meaning — and compares the query embedding with stored document embeddings.

The basic pipeline is:

```text
Documents
    ↓
Ingestion
    ↓
Chunking
    ↓
Embeddings
    ↓
Chroma Vector Database
    ↓
Similarity Search
    ↓
Ranking
    ↓
Top-K Results
    ↓
Streamlit UI
```

---

## Features

* Document ingestion
* Text chunking
* Sentence-based chunking experiments
* Embedding generation
* Chroma vector database
* Semantic similarity search
* Query embeddings
* Top-K retrieval
* Keyword + vector hybrid ranking
* Result-count filtering
* Streamlit user interface
* Search relevance evaluation
* Hit Rate measurement
* Search latency measurement
* Embedding model caching
* Persistent vector storage

---

## How It Works

### 1. Document Ingestion

Raw documents are read from the data directory.

```text
Raw Documents
      ↓
Read
      ↓
Prepare Text
      ↓
Create Embeddings
      ↓
Store in Chroma
```

---

### 2. Chunking

Long text can be divided into smaller pieces called **chunks**.

Chunking helps create searchable units of text.

The project experimented with different chunk sizes and later explored sentence-based chunking.

---

### 3. Embeddings

The project uses:

```text
all-MiniLM-L6-v2
```

to convert text into numerical vectors.

For example:

```text
Text
 ↓
Embedding Model
 ↓
Vector
```

The same process is applied to a user's search query.

---

### 4. Vector Search

When the user enters a query:

```text
User Query
     ↓
Query Embedding
     ↓
Vector Similarity Search
     ↓
Most Similar Documents
```

The query vector is compared with stored document vectors.

---

### 5. Top-K Retrieval

The search system returns the top `K` results.

For example:

```text
k = 3
```

means:

```text
Return the top 3 results
```

The Streamlit interface allows the user to choose the number of results.

---

### 6. Hybrid Ranking

The project also experiments with combining keyword and vector scores.

The experimental formula is:

```text
Combined Score =
(Keyword Score × Keyword Weight)
+
(Vector Score × Vector Weight)
```

Example:

```text
30% Keyword
70% Vector
```

Different weights can be tested to observe how they affect search results.

---

## Architecture

The high-level architecture is:

```text
                    USER
                      │
                      ▼
              ┌──────────────┐
              │  Streamlit   │
              │      UI      │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │    Search    │
              │   Backend    │
              └──────┬───────┘
                     │
                     ▼
              Query Embedding
                     │
                     ▼
              ┌──────────────┐
              │    Chroma    │
              │ Vector Store │
              └──────┬───────┘
                     │
                     ▼
              Similarity Search
                     │
                     ▼
                  Ranking
                     │
                     ▼
                Top-K Results
                     │
                     ▼
              Streamlit Display
```

For a more detailed explanation, see:

```text
ARCHITECTURE.md
```

---

## Tech Stack

### Language

* Python

### Vector Database

* Chroma

### Embeddings

* Sentence Transformers
* `all-MiniLM-L6-v2`

### User Interface

* Streamlit

### Development

* Git
* GitHub

---

## Project Structure

```text
semantic-search-engine/
│
├── app.py
├── README.md
├── ARCHITECTURE.md
│
├── data/
│   └── documents.txt
│
├── src/
│   ├── ingest.py
│   ├── search.py
│   ├── hybrid_search.py
│   ├── chunking.py
│   └── embeddings.py
│
└── tests/
    ├── test_search.py
    └── evaluate_search.py
```

> The exact files in the repository may change as the project is developed.

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd semantic-search-engine
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

---

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local Streamlit address shown in the terminal.

---

## Using the Search Engine

1. Open the Streamlit application.
2. Enter a search query.
3. Select the number of results.
4. Click **Search**.
5. Review the retrieved documents.

Example query:

```text
I want to learn programming
```

---

## Evaluation

The project includes a small relevance test set.

Each test contains:

```text
Query
+
Expected Relevant Document ID
```

The search system retrieves documents and compares them with the expected results.

### Hit Rate

The project uses a simple Hit Rate measurement:

```text
Hit Rate =
Successful Queries / Total Queries
```

A query is considered successful when an expected relevant document appears in the retrieved results.

---

## Performance

Search latency is also measured.

```text
Latency =
End Time - Start Time
```

Average latency can be calculated as:

```text
Average Latency =
Total Latency / Number of Queries
```

This provides a basic measurement of search performance.

---

## Caching

The Streamlit application uses caching for expensive resources such as the embedding model.

Streamlit's:

```python
@st.cache_resource
```

can cache a resource so it can be reused during application reruns.

The goal is to avoid unnecessary repeated loading of the embedding model.

---

## Development Process

The project was developed incrementally:

```text
Project Design
     ↓
Data Ingestion
     ↓
Search Backend
     ↓
Streamlit UI
     ↓
Filters & Result Display
     ↓
Search Evaluation
     ↓
Chunking & Ranking Experiments
     ↓
Caching
     ↓
Documentation
```

Each stage builds on the previous stage.

---

## Project Goal

The goal of this project is to build a practical semantic search system that demonstrates how:

* text can be converted into embeddings
* vector databases can store and retrieve embeddings
* semantic similarity can be used for search
* keyword and vector signals can be combined
* search quality can be evaluated
* search performance can be measured
* a Python search backend can be connected to a user interface

---

