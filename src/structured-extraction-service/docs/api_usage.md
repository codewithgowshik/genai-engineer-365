# Structured Extraction Service API

## Overview

The Structured Extraction Service is a FastAPI application that extracts structured sustainability information from uploaded PDF documents using Google's Gemini model and Pydantic validation.

---

# Base URL

```
http://127.0.0.1:8000
```

---

# API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# Available Endpoints

## GET /

### Description

Returns the current API status.

### Request

```
GET /
```

### Response

```json
{
    "message": "Structured Extraction Service is running."
}
```

---

## POST /extract

### Description

Uploads a sustainability report in PDF format and extracts structured information.

### Request

```
POST /extract
```

### Request Type

```
multipart/form-data
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| file | PDF File | Yes | Sustainability Report |

---

### Example Request

Upload:

```
Report.pdf
```

---

### Example Response

```json
{
    "company_name": "Future City Initiative",
    "industry": "Smart Infrastructure",
    "country": "United Kingdom",
    "report_year": 2026,
    "revenue": "£2.4 Billion",
    "employees": 8500,
    "carbon_reduction_target": "55% by 2035",
    "net_zero_target": 2045,
    "renewable_energy_percentage": 72.0
}
```

---

# Response Validation

The API validates every response using the `SustainabilityReport` Pydantic model.

This guarantees that every successful response follows the expected schema.

---

# Error Responses

## Missing File

Status Code

```
422 Unprocessable Entity
```

Example

```json
{
    "detail": [
        {
            "msg": "Field required"
        }
    ]
}
```

---

# Current Workflow

```
Client

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

Pydantic

↓

JSON Response
```