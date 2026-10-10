# Multi-Query Retrieval

A simple RAG retrieval experiment that uses **Google Gemini** to generate multiple search queries and **Chroma** to retrieve relevant documents for each query.

The goal is to improve retrieval by searching for the same question in several different ways.

---

## How It Works

Normal semantic search:

```text
User Question
     ↓
Embedding
     ↓
Chroma
     ↓
Relevant Documents
```

Multi-query retrieval:

```text
User Question
     ↓
Google Gemini
     ↓
Multiple Search Queries
     ↓
Search Each Query
     ↓
Chroma
     ↓
Combine Results
     ↓
Remove Duplicates
     ↓
Final Documents
```

### Example

User asks:

```text
How do computers learn?
```

Gemini may generate:

```text
How does machine learning allow computers to learn from data?
How do computers learn patterns from data?
How does machine learning work?
```

Each query is searched separately.

The results are then combined and duplicate documents are removed.

---

# Project Structure

```text
retrieval-argument-generation/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   └── documents.txt
│
├── src/
│   ├── __init__.py
│   ├── ingest.py
│   ├── llm.py
│   ├── retrieval.py
│   └── multi_query.py
│
└── chroma_data/
```

---

# What Each File Does

## `data/documents.txt`

This is our small knowledge base.

It contains the documents that we want to search.

Example:

```text
Machine learning allows computers to learn patterns from data and make predictions.
```

The `ingest.py` file reads these documents and stores them in Chroma.

---

## `src/ingest.py`

This file prepares our documents for searching.

It:

1. Reads `documents.txt`
2. Creates IDs for the documents
3. Converts the documents into embeddings
4. Stores the documents and embeddings in Chroma

Flow:

```text
documents.txt
      ↓
Read documents
      ↓
Create embeddings
      ↓
Store in Chroma
```

Run it with:

```powershell
python -m src.ingest
```

---

## `src/llm.py`

This file connects our project to **Google Gemini**.

Gemini is used to generate multiple versions of the user's search query.

For example:

```text
Original:
How do computers learn?
```

Gemini might generate:

```text
How does machine learning allow computers to learn from data?
How do computers learn patterns from data?
How does machine learning work?
```

Run it with:

```powershell
python -m src.llm
```

This is mainly a test to make sure Gemini is working.

---

## `src/retrieval.py`

This file performs normal semantic search.

It:

1. Takes a search query
2. Converts the query into an embedding
3. Searches Chroma
4. Returns the most similar documents

Example:

```text
Query:
How do computers learn?
```

The system searches the stored embeddings and returns relevant documents.

Run it with:

```powershell
python -m src.retrieval
```

---

## `src/multi_query.py`

This is the main file for today's experiment.

It combines Gemini and semantic retrieval.

It:

1. Takes the original question
2. Asks Gemini to generate multiple queries
3. Searches Chroma using every query
4. Combines all retrieved documents
5. Removes duplicate documents
6. Displays the final results

Flow:

```text
Original Question
       ↓
     Gemini
       ↓
Multiple Queries
       ↓
 ┌─────┼─────┐
 ↓     ↓     ↓
Query1 Query2 Query3
 ↓     ↓     ↓
Chroma Chroma Chroma
 └─────┼─────┘
       ↓
Combine Results
       ↓
Remove Duplicates
       ↓
Final Results
```

Run it with:

```powershell
python -m src.multi_query
```

---

# `requirements.txt`

This contains the Python libraries required by the project.

Main libraries:

```text
chromadb
sentence-transformers
google-genai
python-dotenv
```

Install them with:

```powershell
pip install -r requirements.txt
```

---

# `.env`

This file stores your Gemini API key.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

**Never upload `.env` to GitHub.**

---

# `.gitignore`

This prevents private or unnecessary files from being uploaded to GitHub.

Important entries:

```text
venv/
.env
__pycache__/
chroma_data/
```

---

# How To Run The Project

## 1. Open the project folder

```powershell
cd retrieval-argument-generation
```

---

## 2. Activate your virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

You should see something like:

```text
(venv)
```

at the beginning of your terminal line.

---

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

You only need to do this when the required packages are not installed.

---

## 4. Check Gemini

Run:

```powershell
python -m src.llm
```

This checks whether Gemini can generate multiple queries.

---

## 5. Create the Chroma database

Run:

```powershell
python -m src.ingest
```

This reads:

```text
data/documents.txt
```

and creates the local vector database:

```text
chroma_data/
```

---

## 6. Test normal retrieval

Run:

```powershell
python -m src.retrieval
```

This checks whether semantic search is working.

---

## 7. Run Multi-Query Retrieval

Finally:

```powershell
python -m src.multi_query
```

This is the main experiment for Day 124.

You should see:

```text
Original question:
How do computers learn?

Generated queries:
1. ...
2. ...
3. ...

Combined results:

Result 1:
...

Result 2:
...

TOTAL UNIQUE RESULTS: ...
```

---

# Important Execution Order

Run the files in this order:

```text
1. llm.py
      ↓
2. ingest.py
      ↓
3. retrieval.py
      ↓
4. multi_query.py
```

Or as commands:

```powershell
python -m src.llm
python -m src.ingest
python -m src.retrieval
python -m src.multi_query
```

---

# What I Learned

The main concept of this project is **Multi-Query Retrieval**.

Instead of searching the user's question only once, we generate several different search queries and retrieve documents for each one.

This can improve retrieval coverage because different queries can capture different wording or aspects of the same question.

---

# Multi-Query vs Query Rewriting

### Query Rewriting

One question becomes **one improved query**.

```text
Question
   ↓
LLM
   ↓
One rewritten query
   ↓
Retrieval
```

### Multi-Query Retrieval

One question becomes **multiple queries**.

```text
Question
   ↓
LLM
   ↓
Query 1
Query 2
Query 3
   ↓
Multiple retrievals
   ↓
Combined results
```

---

# Limitations

This is a learning project with a small dataset.

The system may retrieve duplicate or less relevant documents because each generated query performs its own search.

A larger production system would need better ranking, deduplication, evaluation, and retrieval strategies.

---

# Day 124 Goal

The goal of this project is to understand and implement:

* Multi-query retrieval
* LLM-based query generation
* Semantic retrieval
* Combining retrieval results
* Removing duplicate results
* Using Gemini with a vector database

The project is part of my **365 Days of Gen AI learning journey**.
