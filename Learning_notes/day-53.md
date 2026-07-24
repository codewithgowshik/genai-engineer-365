# Day 53 / 365 – Building a PDF Reader Tool for an AI Agent

## 🎯 Objective

Today I implemented a second tool for my AI agent: **PDF Text Extraction**.

Instead of relying only on web search, my AI agent can now read PDF documents, extract their content, and use that information to answer questions or generate summaries.

This introduces a completely new capability and demonstrates how an LLM can choose between different tools depending on the user's request.

---

# Why a PDF Tool?

Many real-world applications require understanding documents rather than searching the web.

Examples include:

- Sustainability Reports
- ESG Reports
- Annual Reports
- Research Papers
- Contracts
- Technical Documentation
- Company Policies

A PDF reader enables the AI to access information that is not available through internet searches.

---

# Previous Architecture

My AI agent only had one capability.

```text
User
 │
 ▼
Gemini
 │
 ▼
search_web()
 │
 ▼
Internet
 │
 ▼
Answer
```

This meant every request depended on web search.

---

# New Architecture

My AI agent now has multiple capabilities.

```text
                    User
                      │
                      ▼
                   Gemini
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
   search_web()         extract_pdf_text()
          │                       │
          ▼                       ▼
      Tavily API             PDF Document
          │                       │
          └───────────┬───────────┘
                      ▼
                Final Response
```

Gemini can decide which tool is appropriate based on the user's request.

---

# What is PDF Text Extraction?

A PDF file contains pages that may include text, images, tables, and graphics.

Text extraction is the process of reading each page and collecting its textual content so it can be processed by the LLM.

Workflow:

```text
PDF File

↓

Open PDF

↓

Read Every Page

↓

Extract Text

↓

Combine Text

↓

Return to Gemini
```

---

# PDF Processing Workflow

The complete workflow is:

```text
User uploads PDF

↓

extract_pdf_text()

↓

PyMuPDF

↓

Extract Text

↓

Return Text

↓

Gemini

↓

Summary / Answer
```

---

# PyMuPDF

I used **PyMuPDF** (`fitz`) for PDF processing.

Advantages:

- Fast
- Lightweight
- Supports large PDFs
- Extracts text efficiently
- Widely used in production AI applications

Installation:

```bash
pip install pymupdf
```

Import:

```python
import fitz
```

---

# How the Tool Works

## Step 1

Open the PDF.

```text
report.pdf

↓

fitz.open()
```

---

## Step 2

Loop through every page.

```text
Page 1

↓

Page 2

↓

Page 3

↓

...

↓

Last Page
```

---

## Step 3

Extract text from each page.

```text
Page Text

↓

Append

↓

Complete Document
```

---

## Step 4

Return the extracted text.

```text
{
    "text": "Entire PDF Content"
}
```

This allows Gemini to understand the document.

---

# Tool Selection

My AI agent now decides between two different capabilities.

## Web Search

Example:

```text
Latest AI news
```

↓

```text
search_web()
```

---

## PDF Reader

Example:

```text
Summarise this sustainability report.
```

↓

```text
extract_pdf_text()
```

The model automatically selects the appropriate tool.

---

# Example Workflow

```text
User:
Summarise this sustainability report.

↓

Gemini

↓

extract_pdf_text()

↓

PDF Reader

↓

Extracted Text

↓

Gemini

↓

Summary
```

---

# Example Questions

My PDF tool can now answer questions such as:

- Summarise this report.
- What are the Net Zero targets?
- What are the Scope 1 emissions?
- List all sustainability goals.
- What are the company's KPIs?
- What renewable energy initiatives are mentioned?
- Explain the governance section.
- What are the future objectives?

---

# Advantages

The PDF reader provides several benefits:

- Reads offline documents.
- Supports company reports.
- Enables document summarisation.
- Allows question answering over uploaded files.
- Works with ESG and sustainability reports.
- Forms the foundation for Retrieval-Augmented Generation (RAG).

---

# Current Limitation

Currently, the tool extracts the entire document and sends all extracted text to Gemini.

```text
PDF

↓

Entire Text

↓

Gemini
```

This works well for smaller documents but becomes inefficient for very large reports.

---

# Future Improvement

The next step is to implement Retrieval-Augmented Generation (RAG).

Future workflow:

```text
PDF

↓

Extract Text

↓

Split into Chunks

↓

Generate Embeddings

↓

Store in Vector Database

↓

Retrieve Relevant Chunks

↓

Gemini

↓

Answer
```

This approach scales to thousands of documents while reducing token usage.

---

# Real-World Applications

This capability is commonly used in:

- ESG platforms
- Sustainability reporting tools
- Financial analysis systems
- Legal document assistants
- Research assistants
- Enterprise knowledge bases
- Compliance platforms

---

# Files Added

## New Tool

```
tools/pdf_reader.py
```

Responsibilities:

- Open PDF files
- Extract text
- Return extracted content

---

## Existing Files

```
llm.py
```

Updated to register the new PDF tool and allow Gemini to choose between multiple tools.

---

# Skills Learned

Today I learned:

- PDF text extraction
- Using PyMuPDF
- Building a second AI tool
- Multi-tool AI agents
- Dynamic tool selection
- Document processing
- AI document understanding
- Tool orchestration

---

# Today's Deliverables

- Implemented a PDF text extraction tool.
- Integrated the tool into the AI agent.
- Enabled Gemini to choose between web search and PDF reading.
- Successfully extracted text from uploaded sustainability reports.
- Built the foundation for future RAG and document intelligence features.

---

# Summary

Today I expanded my AI agent beyond web search by implementing a PDF text extraction tool using PyMuPDF. My agent can now process uploaded documents, extract their textual content, and use that information to answer questions or generate summaries. This marks an important step towards building production-grade AI systems capable of working with both external information and user-provided documents. It also establishes the foundation for future enhancements such as document chunking, embeddings, vector databases, and Retrieval-Augmented Generation (RAG).
