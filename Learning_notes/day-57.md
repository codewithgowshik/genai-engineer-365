# Day 57 / 365 – Project 2: Structured Extraction Service (Repository & Schema Design)

## 🎯 Objective

Today I began **Project 2**, a **Structured Extraction Service**.

The goal of this project is to build an AI system that extracts **structured information** from unstructured documents such as sustainability reports, annual reports, invoices, contracts, and research papers.

Unlike traditional chat applications that generate paragraphs of text, this project focuses on producing **consistent, machine-readable JSON** based on predefined schemas.

Since my main project (**Envora**) already contains PDF analysis and structured JSON extraction, I adapted the roadmap by documenting the architecture, defining the extraction schema, and preparing the project as a standalone module that can be extended into a production-ready document intelligence service.

---

# Why Structured Extraction?

Large Language Models understand documents extremely well.

However, software applications usually need structured information instead of paragraphs.

For example, a sustainability report may contain information such as:

- Company Name
- Industry
- Revenue
- Net Zero Target
- Carbon Emissions
- ESG Score

Instead of asking users to manually search through hundreds of pages, the AI automatically extracts these values into a predefined structure.

---

# Unstructured vs Structured Data

## Unstructured Data

Example:

```text
ABC Ltd plans to reduce carbon emissions by 50% before 2035 while investing heavily in renewable energy.
```

Although humans understand this easily, software cannot directly analyse it.

---

## Structured Data

The same information becomes:

```json
{
    "company_name": "ABC Ltd",
    "carbon_reduction_target": "50%",
    "net_zero_target": 2035,
    "renewable_energy": true
}
```

Structured data is much easier to process, validate, search, store, and analyse.

---

# What is Structured Extraction?

Structured extraction is the process of converting free-form text into predefined fields.

Workflow:

```text
Document

↓

AI Model

↓

Extract Required Information

↓

Populate Schema

↓

Structured JSON
```

Instead of generating another paragraph, the AI fills a schema with relevant information.

---

# Why Schemas are Important

A schema defines:

- What information should be extracted
- Expected data types
- Required fields
- Optional fields
- Validation rules

Without a schema:

```text
Document

↓

LLM

↓

Random Output
```

With a schema:

```text
Document

↓

LLM

↓

Predefined Schema

↓

Consistent JSON
```

Schemas ensure that every document produces predictable output.

---

# Project Goal

The Structured Extraction Service is designed to:

- Read documents
- Understand document contents
- Extract important information
- Return structured JSON

Rather than replacing humans, the system automates repetitive information extraction tasks.

---

# Repository Structure

Today's project structure:

```text
structured-extraction-service/

│
├── README.md
├── extractor.py
├── schemas.py
├── prompts.py
├── sample_documents/
├── outputs/
└── requirements.txt
```

Each file has a dedicated responsibility within the extraction pipeline.

---

# Extraction Workflow

The complete process follows these steps:

```text
User Uploads PDF

↓

PDF Reader

↓

Extract Raw Text

↓

Gemini

↓

Extraction Prompt

↓

Schema

↓

Structured JSON

↓

Application
```

The schema acts as the contract between the AI model and the application.

---

# Example Schema

A simple sustainability report schema:

```json
{
    "company_name": "",
    "industry": "",
    "country": "",
    "report_year": 0,
    "revenue": "",
    "employees": 0,
    "net_zero_target": 0,
    "scope1_emissions": "",
    "scope2_emissions": "",
    "scope3_emissions": "",
    "summary": ""
}
```

Every processed report follows the same format.

---

# Why Consistent JSON Matters

Structured JSON allows applications to:

- Save data into databases
- Generate dashboards
- Search specific fields
- Compare multiple reports
- Build analytics
- Perform compliance checks
- Automate reporting

Without structured output, these tasks become significantly more difficult.

---

# Current Capabilities

At this stage, my AI application already supports:

- Web Search
- PDF Analysis
- Structured JSON Output
- Pydantic Validation
- Graceful Error Handling
- Multi-tool Architecture

Project 2 builds upon these capabilities by focusing specifically on designing a reusable extraction service and defining consistent schemas.

---

# Future Expansion

The extraction service can later support:

- Sustainability Reports
- Annual Reports
- ESG Reports
- Financial Statements
- Research Papers
- Contracts
- Invoices
- Medical Records
- Insurance Documents

Each document type can have its own schema while sharing the same extraction pipeline.

---

# Real-World Applications

Structured extraction is widely used in:

- Enterprise AI Assistants
- Document Intelligence Platforms
- Financial Analysis Systems
- ESG Reporting Tools
- Legal Technology
- Healthcare Systems
- Insurance Platforms
- Procurement Software

Many modern AI products rely on structured extraction instead of free-form text generation.

---

# Skills Learned

Today I learned:

- What structured extraction is
- The difference between structured and unstructured data
- Why schemas are important
- How AI converts documents into machine-readable JSON
- Designing extraction schemas
- Planning a production-ready document extraction service
- Organising an AI project into reusable modules

---

# Key Takeaways

- LLMs can generate both natural language and structured data.
- Schemas provide consistency and predictability.
- Structured JSON is easier to validate, store, and analyse.
- Structured extraction is a core capability of modern document intelligence systems.
- Designing the schema is just as important as building the extraction logic.

---

# Today's Deliverables

- Created the foundation for Project 2.
- Planned the repository structure.
- Defined the initial extraction schema.
- Documented the extraction workflow.
- Prepared the project for future implementation and expansion.

---

# Summary

Today I started **Project 2 – Structured Extraction Service** by focusing on the design rather than implementation. I learned how AI systems convert unstructured documents into structured JSON using predefined schemas. I designed the repository structure, defined the extraction workflow, and created the initial schema that will guide future document extraction. This project lays the foundation for building a scalable document intelligence system capable of processing sustainability reports and other business documents in a consistent and machine-readable format.
