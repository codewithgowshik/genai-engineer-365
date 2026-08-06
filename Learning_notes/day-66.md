# Day 66 / 365 – Improving My AI Service and Understanding API Documentation

## 🎯 Objective

Today I focused on improving my Structured Extraction Service by understanding how production APIs are documented, validated, and presented to other developers. Instead of building new AI functionality, I learned how to make my API easier to understand, easier to use, and more professional.

I also explored how FastAPI automatically generates interactive API documentation using Swagger UI and why documentation is an important part of backend software development.

---

# Why Documentation Matters

Writing code is only one part of software engineering.

If another developer cannot understand how to install, run, or use the application, the project becomes difficult to maintain and collaborate on.

Documentation explains:

- What the project does.
- How to install it.
- How to configure it.
- How to run it.
- How to use the available API endpoints.
- What responses and errors to expect.

A good README is often the first thing another developer reads before looking at the source code.

---

# Backend Services Need Documentation

Unlike desktop applications, backend services usually have no graphical interface.

Developers interact with APIs using HTTP requests.

Because of this, backend projects must clearly document:

- Available endpoints.
- Supported request methods.
- Required parameters.
- Response format.
- Validation rules.
- Error responses.

Good documentation reduces confusion and improves developer experience.

---

# Swagger UI

One of FastAPI's most useful features is its automatic documentation system.

When the application runs:

```bash
uvicorn app:app --reload
```

Swagger UI becomes available at:

```
http://127.0.0.1:8000/docs
```

Swagger automatically generates interactive API documentation directly from the FastAPI application.

It allows developers to:

- Explore available endpoints.
- Upload PDF files.
- Execute requests.
- View JSON responses.
- Test the API without writing frontend code.

This significantly speeds up API development and debugging.

---

# Request Validation

FastAPI automatically validates incoming requests before executing the endpoint.

For my extraction endpoint, the uploaded PDF is defined as:

```python
file: UploadFile = File(...)
```

This means:

- A file must be uploaded.
- The file parameter is required.
- Missing input automatically returns a validation error.

This removes the need for manual validation logic.

---

# Response Validation

FastAPI also validates outgoing responses.

Using:

```python
response_model=SustainabilityReport
```

ensures every successful response follows the SustainabilityReport schema.

This guarantees consistent API responses and prevents accidental mistakes from reaching the client.

---

# UploadFile

UploadFile is FastAPI's representation of an uploaded file.

Initially, the uploaded PDF exists only in memory.

```
Client

↓

UploadFile

↓

Memory
```

Since my extraction pipeline requires a file path, the uploaded file must first be saved into the uploads directory before processing.

---

# Saving Uploaded Files

The uploaded PDF is stored using:

```python
shutil.copyfileobj(file.file, buffer)
```

This copies the uploaded file from memory into a physical file.

```
Memory

↓

uploads/Report.pdf
```

Once saved, my existing extraction pipeline can process the document without modification.

---

# Modular API Architecture

One of the biggest improvements in my project is maintaining a clean architecture.

Instead of placing everything inside one file, responsibilities are separated.

```
app.py

↓

FastAPI Application

↓

API Router

↓

Extractor

↓

PDF Reader

↓

Prompt Builder

↓

Gemini

↓

Pydantic

↓

Structured JSON
```

Each component performs one responsibility, making the application easier to understand and maintain.

---

# API Documentation

Today I also learned how to document an API for other developers.

A good API document should explain:

- Project overview
- Installation
- Environment variables
- Running the server
- Available endpoints
- Request examples
- Response examples
- Validation behaviour
- Error responses

Documentation is an essential part of professional software development.

---

# Current Project Workflow

```
Client

↓

HTTP Request

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

↓

Client
```

The extraction service is now exposed as a reusable backend API that other applications can integrate with.

---

# Skills Learned

Today I learned:

- Why backend services require documentation.
- How to structure a professional README.
- The purpose of Swagger UI.
- How FastAPI generates automatic API documentation.
- Why request validation improves API reliability.
- Why response validation ensures consistent output.
- How UploadFile manages uploaded files.
- Why modular architecture improves maintainability.
- The importance of documenting APIs for other developers.

---

# Key Takeaways

- Documentation is part of software engineering, not an optional task.
- A good README helps other developers understand and use the project.
- Swagger automatically creates interactive API documentation.
- FastAPI validates both incoming requests and outgoing responses.
- UploadFile stores uploaded files temporarily in memory.
- Uploaded files must be saved before processing.
- Modular architecture makes APIs easier to maintain and document.
- Production-ready software combines good code with good documentation.

---

# Today's Deliverables

- Improved project documentation.
- Documented API usage.
- Understood Swagger UI.
- Learned request and response validation.
- Improved understanding of backend service architecture.
- Prepared the Structured Extraction Service for future deployment.

---

# Summary

Today I focused on making my Structured Extraction Service more professional by learning how backend APIs are documented and presented to other developers. I explored FastAPI's automatic Swagger documentation, reinforced my understanding of request and response validation, and recognised that writing clear documentation is as important as writing reliable code. This milestone improved not only the functionality of my project but also its usability and maintainability, bringing it closer to production-ready standards.
