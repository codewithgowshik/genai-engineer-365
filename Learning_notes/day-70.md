# Day 70 / 365 — Shipping Project 2, Reflection, and Planning Phase 3

## 🎯 Objective

Today I completed the final stage of Project 2: the Structured Extraction Service.

The goal was to move the project from a local development project to a **shipped, documented, and portfolio-ready AI service**.

Today focused on:

- Reflecting on what I built.
- Hosting Project 2.
- Adding the project to my portfolio.
- Reviewing what I learned.
- Identifying improvements.
- Planning Phase 3.

---

# 🚀 What Does It Mean to Ship a Project?

A project is not finished simply because the code works on my computer.

Shipping means making the project usable and accessible outside my local development environment.

The progression is:

```text
Local Project
     ↓
Testing
     ↓
Documentation
     ↓
Deployment
     ↓
Live Application
     ↓
Portfolio
```

My Structured Extraction Service has now progressed from a local Python application into a deployable AI backend service.

---

# 🌐 Hosting

Hosting means running my application on a remote server so that other people and applications can access it through the internet.

Previously:

```text
My Computer
     ↓
localhost
     ↓
FastAPI
```

After deployment:

```text
Internet
     ↓
Public API URL
     ↓
FastAPI
     ↓
Extraction Service
```

A deployed API can be accessed by other applications without running the project on my own computer.

---

# 🔗 API and Swagger

My FastAPI application automatically provides interactive API documentation through Swagger.

Locally I used:

```text
http://127.0.0.1:8000/docs
```

After deployment, the same documentation can be available through the public API domain:

```text
https://your-domain/docs
```

This allows users and developers to:

- View API endpoints.
- Upload a PDF.
- Execute requests.
- Inspect responses.
- Understand the API without reading the source code.

---

# 🧩 Project 2 Architecture

The final architecture of my Structured Extraction Service is:

```text
Client
   ↓
FastAPI
   ↓
Request Validation
   ↓
PDF Upload
   ↓
PDF Reader
   ↓
Prompt Builder
   ↓
Gemini
   ↓
Structured Output
   ↓
Pydantic Validation
   ↓
JSON Response
```

Each component has a specific responsibility.

---

# 📄 PDF Processing

The service receives a PDF document from the client.

The PDF reader extracts its text so that the document can be passed to the LLM.

```text
PDF
 ↓
PyMuPDF
 ↓
Extracted Text
```

This converts an unstructured document into text that can be processed by the AI model.

---

# 🧠 Prompt Engineering

The extracted document text is passed into my extraction prompt.

The prompt explains to the LLM:

- What information to extract.
- What fields are required.
- What format the output should follow.

The goal is not simply to ask the LLM:

```text
"Summarize this document."
```

Instead, the model is given a structured extraction task.

---

# 🤖 LLM Integration

Gemini processes the extracted document and produces structured information.

The LLM acts as the reasoning and extraction component of the pipeline.

```text
Document Text
     ↓
Prompt
     ↓
Gemini
     ↓
Structured Information
```

---

# 📦 Structured Output

One of the most important lessons from Project 2 was the difference between raw text output and structured output.

A raw LLM response could look like:

```text
Future City Initiative operates in the smart infrastructure industry...
```

Structured output instead represents the information as fields:

```json
{
    "company_name": "Future City Initiative",
    "industry": "Smart Infrastructure",
    "country": "United Kingdom",
    "report_year": 2026
}
```

This makes the information much easier for software to consume.

---

# 🛡️ Pydantic Validation

Pydantic provides a defined structure for the extracted information.

The model describes what the application expects.

For example:

```text
company_name
industry
country
report_year
revenue
employees
carbon_reduction_target
net_zero_target
renewable_energy_percentage
```

The extracted data can then be validated against this structure.

This prevents my application from blindly trusting arbitrary LLM output.

---

# 🌐 FastAPI

FastAPI exposes the extraction pipeline as an API.

Instead of running:

```bash
python app.py
```

manually, a client can send a request to:

```text
POST /extract
```

The API then processes the document and returns structured JSON.

This makes the extraction system reusable by:

- Websites
- Mobile applications
- Other backend services
- Automation systems
- Future AI applications

---

# 🧪 Testing

Before shipping the project, I added automated tests.

Testing allows me to verify important components without manually checking everything every time.

The project can contain tests for:

```text
Sustainability Model
Prompt Builder
PDF Reader
```

The basic workflow is:

```text
Change Code
    ↓
Run Tests
    ↓
PASSED / FAILED
```

This provides confidence when modifying the project.

---

# ⚠️ Error Handling

I also improved the API's error handling.

Instead of exposing internal Python errors, the API can provide meaningful messages.

For example:

```json
{
    "detail": "Invalid file type. Please upload a PDF file."
}
```

or:

```json
{
    "detail": "Unable to process the PDF. Please try again."
}
```

This makes the API easier to understand and use.

---

# 📚 Documentation

The project also contains documentation explaining:

- What the service does.
- How to install it.
- How to configure it.
- How to run it.
- How to use the API.
- What responses look like.
- What errors can occur.

A project is much more useful when another developer can understand and run it without asking the original developer for help.

---

# 💭 Project Reflection

## What Did I Build?

I built an AI-powered Structured Extraction Service that accepts sustainability reports in PDF format and extracts important information into structured JSON.

The service combines:

```text
Python
+
PyMuPDF
+
Prompt Engineering
+
Gemini
+
Pydantic
+
FastAPI
+
Pytest
```

---

# What Did I Learn?

During Project 2, I learned:

- PDF text extraction.
- Prompt engineering.
- LLM integration.
- Structured outputs.
- Pydantic validation.
- FastAPI.
- API routing.
- File uploads.
- Swagger documentation.
- Request validation.
- Response validation.
- Error handling.
- Automated testing.
- Python virtual environments.
- API documentation.
- Deployment concepts.

---

# Biggest Challenge

One of my biggest challenges was connecting all the individual components into one working application.

Initially, the project consisted of separate pieces:

```text
PDF Reader
LLM
Prompt
Pydantic
```

I gradually connected them:

```text
PDF
 ↓
Reader
 ↓
Prompt
 ↓
LLM
 ↓
Pydantic
```

Then I exposed the pipeline through FastAPI:

```text
Client
 ↓
FastAPI
 ↓
Extraction Pipeline
 ↓
JSON
```

This taught me that building a real application is not only about individual components. The components need to work together as a system.

---

# What Would I Improve?

There are several areas I would improve in a future version:

- Better automated testing.
- LLM mocking.
- OCR support for scanned PDFs.
- Better handling of large documents.
- Authentication.
- Database integration.
- Better logging and observability.
- Docker containerisation.
- More advanced deployment.
- Better LLM evaluation.
- More robust security.

---

# 🔮 Planning Phase 3

Project 2 focused on:

```text
Prompting
+
Structured Output
+
Tools
+
API
```

Phase 3 can focus more heavily on making AI systems **production-ready**.

Potential areas include:

```text
Testing
     ↓
Evaluation
     ↓
Observability
     ↓
Deployment
     ↓
Docker
     ↓
Authentication
     ↓
Databases
     ↓
Production AI Systems
```

The goal is to move from:

> "I can build an AI application."

toward:

> "I can build, test, deploy, monitor, and maintain an AI application."

---

# 🧠 Important Lessons From Project 2

### 1. LLMs are only one part of an AI application.

A useful AI application requires multiple components:

```text
Input
 ↓
Processing
 ↓
Prompt
 ↓
LLM
 ↓
Validation
 ↓
API
 ↓
Output
```

---

### 2. Structured output makes LLMs more useful to software.

Raw text is difficult for software to consume reliably.

Structured data allows other applications to work with the information programmatically.

---

### 3. Validation is important when working with LLMs.

LLMs generate probabilistic outputs.

Validation provides a boundary between the model and the rest of the application.

```text
LLM
 ↓
Pydantic
 ↓
Application
```

---

### 4. APIs make AI functionality reusable.

FastAPI transformed my extraction pipeline into a service that other applications can communicate with.

---

### 5. Testing becomes increasingly important as projects grow.

As the application becomes more complex, automated tests help prevent changes from breaking existing functionality.

---

### 6. Documentation is part of engineering.

A project isn't complete when the code works.

Other developers need to understand:

```text
What?
Why?
How?
Input?
Output?
Errors?
```

---

# 🏆 Project 2 Milestone

Project 2 progressed through:

```text
PDF Reader
     ↓
Prompt Engineering
     ↓
Gemini
     ↓
Structured Output
     ↓
Pydantic
     ↓
FastAPI
     ↓
Validation
     ↓
Swagger
     ↓
Documentation
     ↓
Testing
     ↓
Error Handling
     ↓
Deployment
     ↓
Portfolio
```

This represents the complete journey from an idea to a shipped AI backend service.

---

# 📦 Today's Deliverables

- [x] Reflect on Project 2.
- [x] Review what I learned.
- [x] Identify challenges.
- [x] Identify future improvements.
- [x] Plan Phase 3.
- [x] Prepare the project for deployment.
- [x] Host the project.
- [x] Add the project to my portfolio.
- [x] Update the project README.
- [x] Commit and push the final changes.

---

# 📝 Summary

Today I completed the shipping stage of Project 2. I learned that building an AI application is only one part of the engineering process. A complete project must also be tested, documented, deployed, and presented so that other people can actually use it.

My Structured Extraction Service evolved from a simple PDF extraction experiment into a complete AI backend service using PyMuPDF, prompt engineering, Gemini, Pydantic, FastAPI, automated testing, validation, error handling, and API documentation.

The biggest lesson from Project 2 is that an LLM by itself is not the application. The real engineering work is building the system around the model so that unstructured input can be transformed into reliable, validated, structured data.

Project 2 is now shipped, and Phase 3 will focus on taking these skills further toward production-ready AI engineering.
