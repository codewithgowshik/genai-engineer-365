# Day 64 / 365 – Building My First AI API with FastAPI

## 🎯 Objective

Today I transformed my Structured Extraction Service from a command-line application into a web API using FastAPI.

Previously, my extraction pipeline could only be executed manually by running:

```bash
python app.py
```

Today, I exposed the same pipeline through an HTTP endpoint, allowing external applications to upload PDF files and receive structured JSON responses.

---

# Why FastAPI?

My extraction pipeline was already working.

```
PDF

↓

PDF Reader

↓

Prompt Builder

↓

Gemini

↓

Pydantic

↓

Structured Output
```

However, only I could execute it from my local machine.

If another application, such as a website or mobile app, wanted to use my extraction service, it would not be able to execute my Python script directly.

Instead, it needs an API.

FastAPI provides that interface.

---

# What is an API?

An API (Application Programming Interface) allows different software applications to communicate with each other.

Instead of running Python files manually, clients send HTTP requests.

Example:

```
Client

↓

POST /extract

↓

FastAPI

↓

Extractor

↓

JSON Response
```

The API acts as the communication layer between users and my extraction pipeline.

---

# FastAPI Application Structure

Instead of placing every endpoint inside a single file, I organised my project using routers.

Project structure:

```
structured-extraction-service/

app.py

src/

    routes/
        api.py

    extractor/
        extractor.py

    prompts/
        extraction_prompt.py

    schemas/
        sustainability.py

    tools/
        pdf_reader.py

    llm.py
```

Each module continues to have a single responsibility.

---

# app.py

The responsibility of app.py is only to start the FastAPI application.

It creates the FastAPI instance and registers all API routes.

```
Create FastAPI Application

↓

Register Routes

↓

Start Server
```

No extraction logic exists inside app.py.

---

# APIRouter

Instead of writing every endpoint inside app.py, FastAPI provides APIRouter.

A router groups related endpoints together.

Example:

```
Routes

↓

GET /

POST /extract

GET /health
```

This keeps the project modular and scalable.

---

# Request Validation

FastAPI automatically validates incoming requests.

For the extraction endpoint, the uploaded PDF is defined as:

```python
file: UploadFile = File(...)
```

This tells FastAPI:

- The request must contain a file.
- The file parameter is required.
- If the file is missing, FastAPI automatically returns an error response.

No manual validation code is required.

---

# UploadFile

UploadFile represents the uploaded document.

Initially, the uploaded PDF exists only in memory.

```
Browser

↓

Memory (UploadFile)
```

Since my extraction pipeline expects a file path, I save the uploaded file into the uploads directory before processing it.

---

# shutil.copyfileobj()

To save the uploaded file, I used:

```python
shutil.copyfileobj(file.file, buffer)
```

This copies the uploaded file from memory into a physical file on disk.

```
UploadFile

↓

Memory

↓

uploads/Report.pdf
```

Once the file is stored, my existing extraction pipeline can process it without modification.

---

# Integrating the Existing Pipeline

One important lesson today was that I did not rewrite my extraction logic.

Instead, FastAPI simply calls my existing extractor.

Workflow:

```
Browser

↓

Upload PDF

↓

FastAPI

↓

Extractor

↓

PDF Reader

↓

Prompt Builder

↓

Gemini

↓

SustainabilityReport

↓

JSON
```

This demonstrates the benefit of modular software architecture.

---

# Response Validation

FastAPI integrates directly with Pydantic.

Using:

```python
response_model=SustainabilityReport
```

FastAPI validates every successful response before sending it back to the client.

This guarantees that the API always returns the expected structure.

If the returned object does not match the schema, FastAPI raises a validation error automatically.

---

# Swagger UI

FastAPI automatically generates interactive API documentation.

Running:

```bash
uvicorn app:app --reload
```

provides documentation at:

```
http://127.0.0.1:8000/docs
```

Swagger allows me to:

- Upload files
- Execute API requests
- View JSON responses
- Test endpoints without writing frontend code

---

# Current System Architecture

```
Client

↓

POST /extract

↓

FastAPI

↓

API Route

↓

Extractor

↓

PDF Reader

↓

Prompt Builder

↓

Gemini

↓

Pydantic Validation

↓

Structured JSON Response
```

My extraction service is now accessible through an HTTP API.

---

# Skills Learned

Today I learned:

- What an API is.
- Why FastAPI is used.
- How FastAPI applications are structured.
- The purpose of APIRouter.
- How UploadFile works.
- Why uploaded files must be saved before processing.
- How shutil.copyfileobj() copies uploaded files.
- How FastAPI performs automatic request validation.
- How Pydantic provides automatic response validation.
- How Swagger UI simplifies API testing.

---

# Key Takeaways

- FastAPI exposes Python applications through HTTP endpoints.
- APIRouter keeps API routes organised.
- UploadFile stores uploaded files temporarily in memory.
- shutil.copyfileobj() saves uploaded files to disk.
- Request validation prevents invalid inputs from reaching the application.
- Response validation ensures every API response matches the expected schema.
- Swagger automatically generates interactive API documentation.
- A modular architecture allows the API layer to reuse the existing extraction pipeline without changing its internal implementation.

---

# Today's Deliverables

- Built the FastAPI application.
- Created API routing using APIRouter.
- Integrated the extraction pipeline with FastAPI.
- Added request validation using UploadFile.
- Added response validation using Pydantic.
- Enabled automatic Swagger documentation.
- Successfully exposed the Structured Extraction Service through an HTTP API.

---

# Summary

Today I transformed my Structured Extraction Service into a production-style web API using FastAPI. Instead of running the extraction pipeline manually, external applications can now upload PDF files through an HTTP endpoint and receive validated JSON responses. By combining FastAPI with Pydantic, I implemented automatic request and response validation while maintaining a clean, modular architecture. This milestone marks the transition from a standalone AI application to an API service that can be integrated into web applications, mobile apps, or other backend systems.
