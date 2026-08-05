# Day 65 / 365 – Understanding FastAPI Request & Response Validation

## 🎯 Objective

Today I learned how FastAPI validates incoming requests and outgoing responses automatically using Pydantic models. I also documented my API so that other developers can understand how to interact with my Structured Extraction Service.

This marked an important transition from simply building an API to making it reliable, predictable, and easy to use.

---

# Why Request and Response Validation Matters

An API is a contract between a client and a server.

The client promises to send data in a specific format.

The server promises to return data in a specific format.

Validation ensures that both sides follow this contract.

Without validation, incorrect inputs could cause unexpected errors, and inconsistent outputs could make the API difficult to integrate.

---

# Request Validation

Request validation verifies the data sent by the client before it reaches the application's business logic.

In my project, the extraction endpoint requires a PDF file.

```python
file: UploadFile = File(...)
```

This tells FastAPI:

- A file must be included in the request.
- The file parameter is required.
- If the file is missing, automatically return an error response.

Because FastAPI performs this validation automatically, I do not need to manually check whether a file was uploaded.

---

# UploadFile

FastAPI provides the UploadFile class to handle uploaded files efficiently.

When a user uploads a PDF, the file initially exists only in memory.

```
Client

↓

UploadFile

↓

Memory
```

My extraction pipeline expects a file path, so the uploaded file must first be saved to disk before processing begins.

---

# Saving Uploaded Files

To save the uploaded PDF, I used:

```python
shutil.copyfileobj(file.file, buffer)
```

This copies the uploaded file from memory into the uploads directory.

```
Memory

↓

uploads/Report.pdf
```

Once the file has been saved, the existing extraction pipeline can process it without modification.

---

# Response Validation

After Gemini extracts the sustainability information, FastAPI validates the response before sending it back to the client.

This is achieved using:

```python
response_model=SustainabilityReport
```

The response model acts as a contract.

Every successful response must match the SustainabilityReport schema.

If the returned data does not match the schema, FastAPI raises a validation error instead of returning invalid data.

---

# Pydantic Integration

Pydantic defines the structure of the extracted information.

Example fields include:

- company_name
- industry
- country
- report_year
- revenue
- employees
- carbon_reduction_target
- net_zero_target
- renewable_energy_percentage

Instead of working with plain text, my application now works with validated Python objects.

This makes the extraction pipeline much more reliable.

---

# API Routing

Instead of placing every endpoint inside a single file, I organised my API using APIRouter.

```
app.py

↓

FastAPI

↓

API Router

↓

GET /

POST /extract
```

Separating routes from the application entry point improves maintainability and keeps the project organised.

---

# Swagger Documentation

FastAPI automatically generates interactive API documentation.

Running:

```bash
uvicorn app:app --reload
```

provides documentation at:

```
http://127.0.0.1:8000/docs
```

Swagger UI allows me to:

- View available endpoints.
- Upload PDF files.
- Execute requests.
- Inspect JSON responses.
- Test the API without building a frontend.

---

# API Usage Documentation

Today I also learned that writing documentation is an important part of software engineering.

Good API documentation should explain:

- The purpose of the API.
- Available endpoints.
- Required request parameters.
- Expected response format.
- Validation rules.
- Possible error responses.

Documentation makes APIs easier to understand and integrate.

---

# Current Application Flow

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

JSON Response

↓

Client
```

FastAPI acts as the interface between users and my extraction pipeline while Pydantic guarantees the correctness of the returned data.

---

# Skills Learned

Today I learned:

- The purpose of request validation.
- The purpose of response validation.
- How UploadFile works.
- Why uploaded files must be saved before processing.
- How shutil.copyfileobj() copies uploaded files.
- How FastAPI integrates with Pydantic.
- How APIRouter organises API endpoints.
- How Swagger automatically generates API documentation.
- Why API documentation is an essential part of backend development.

---

# Key Takeaways

- FastAPI automatically validates incoming requests.
- Pydantic automatically validates outgoing responses.
- UploadFile temporarily stores uploaded files in memory.
- Uploaded files must be saved before processing.
- APIRouter keeps API endpoints modular.
- Swagger provides interactive documentation with no additional configuration.
- Well-documented APIs improve developer experience and maintainability.
- Building production-ready software includes both implementation and documentation.

---

# Today's Deliverables

- Built API usage documentation.
- Learned request validation using UploadFile.
- Learned response validation using Pydantic.
- Understood how FastAPI automatically validates data.
- Explored Swagger UI for API testing.
- Improved the architecture of the Structured Extraction Service.

---

# Summary

Today I learned how FastAPI uses request validation to ensure that clients send valid data and how response validation guarantees that every API response follows a predefined schema. By integrating Pydantic models with FastAPI, I improved the reliability of my Structured Extraction Service while reducing the amount of manual validation code. I also documented the API so that other developers can easily understand, test, and integrate it. This reinforced the importance of building not only functional APIs but also well-documented and maintainable backend services.
