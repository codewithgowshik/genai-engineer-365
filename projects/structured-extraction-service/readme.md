# Envora Structured Extraction Engine

## Overview

The Envora Structured Extraction Engine is an AI-powered document processing module that extracts structured information from unstructured documents such as sustainability reports, annual reports, and ESG reports.

Instead of generating free-form text, the system converts documents into structured JSON based on predefined schemas.

---

## Features

- PDF document processing
- AI-powered structured extraction
- JSON output
- Schema-based extraction
- Pydantic validation
- Graceful error handling
- Gemini-powered extraction

---

## Architecture

User

↓

Upload PDF

↓

PDF Reader

↓

Extract Text

↓

Gemini

↓

Structured Schema

↓

JSON Output

---

## Example Schema

{
    "company_name": "",
    "industry": "",
    "report_year": 0,
    "net_zero_target": 0,
    "summary": ""
}

---

## Technologies

- Python
- Google Gemini
- Pydantic
- PyMuPDF
- JSON

---

## Future Improvements

- Multi-document extraction
- Vector Database
- RAG
- Batch processing
- Database integration
