# Production RAG App

## Overview
An AI application that answers questions using information retrieved from a collection of documents.

## Planned Features
- Document ingestion and chunking
- Text embeddings
- Vector storage with ChromaDB
- Semantic retrieval
- LLM-based answer generation
- Source references
- Evaluation and testing

## Architecture
Documents -> Ingestion -> Chunking -> Embeddings -> ChromaDB
User Question -> Retrieval -> Relevant Context -> LLM -> Answer

## Technology Stack
- Python
- ChromaDB
- Sentence Transformers
- FastAPI
- LLM provider integration

## Project Structure
- src/ingestion.py: Document ingestion
- src/retrieval.py: Relevant document retrieval
- src/generation.py: Answer generation
- src/main.py: Application entry point
- tests/: Automated tests
- data/: Local document data

## Status
Initial project setup. Features will be implemented incrementally.
