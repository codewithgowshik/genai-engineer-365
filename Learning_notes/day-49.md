# Day 49 – Google GenAI SDK Structured Output

## 🎯 Objective

Learn how to use the Google GenAI SDK's **Structured Output** feature to automatically convert an AI response into a Python object using a Pydantic model.

---

# Why Structured Output?

Before today, Gemini returned text (or JSON as a string). We had to manually convert that text into Python objects.

### Previous Workflow

```text
Prompt
    ↓
Gemini
    ↓
JSON String
    ↓
json.loads()
    ↓
Dictionary
    ↓
Pydantic Validation
    ↓
Python Object
```

This required extra code for:

- Cleaning the response
- Parsing JSON
- Validating the data
- Creating the Python object

---

# Today's Workflow

Instead of manually parsing JSON, we provide our Pydantic model directly to the SDK.

```text
Prompt
    ↓
Gemini SDK
    ↓
response_schema
    ↓
Validated Python Object
```

The SDK automatically performs:

- JSON generation
- JSON parsing
- Pydantic validation
- Python object creation

---

# Pydantic Schema

We already created a schema.

```python
from pydantic import BaseModel

class SustainabilityAnalysis(BaseModel):
    topic: str
    summary: str
    recommendations: list[str]
```

This schema tells Gemini exactly what format the response should follow.

---

# GenerateContentConfig

```python
config=types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=SustainabilityAnalysis
)
```

This configuration controls how Gemini generates the response.

---

# response_mime_type

```python
response_mime_type="application/json"
```

## Purpose

This tells Gemini:

> "Return JSON instead of plain text."

Without it, Gemini may respond like:

```text
Carbon neutrality means balancing carbon emissions...
```

With it, Gemini responds in JSON format.

```json
{
  "topic": "Carbon Neutrality",
  "summary": "Balancing emissions.",
  "recommendations": [
    "Use renewable energy",
    "Recycle",
    "Reduce waste"
  ]
}
```

---

# response_schema

```python
response_schema=SustainabilityAnalysis
```

## Purpose

This tells the SDK:

> "The response must match this Pydantic model."

The SDK sends the schema to Gemini.

Gemini generates JSON matching that schema.

---

# What Happens Internally?

Suppose Gemini generates:

```json
{
  "topic": "Carbon Neutrality",
  "summary": "Balancing emissions.",
  "recommendations": [
    "Use renewable energy",
    "Recycle",
    "Reduce waste"
  ]
}
```

The SDK automatically performs something similar to:

```python
data = json.loads(response_text)

analysis = SustainabilityAnalysis(**data)
```

You never have to write this code.

---

# response.parsed

```python
analysis = response.parsed
```

This is the most important line of today's lesson.

The SDK has already:

1. Parsed the JSON.
2. Validated the JSON.
3. Created the Pydantic object.

`response.parsed` simply returns that object.

Equivalent manual code:

```python
data = json.loads(response.answer)

analysis = SustainabilityAnalysis(**data)
```

Today, all of that becomes:

```python
analysis = response.parsed
```

---

# What is Stored Inside `analysis`?

`analysis` is **not** a dictionary.

It is an instance of the `SustainabilityAnalysis` class.

Equivalent to writing:

```python
analysis = SustainabilityAnalysis(
    topic="Carbon Neutrality",
    summary="Balancing emissions.",
    recommendations=[
        "Use renewable energy",
        "Recycle",
        "Reduce waste"
    ]
)
```

---

# Accessing the Data

Since `analysis` is already a Python object:

```python
print(analysis.topic)
```

```python
print(analysis.summary)
```

```python
print(analysis.recommendations)
```

You can also iterate over lists.

```python
for recommendation in analysis.recommendations:
    print(recommendation)
```

---

# Comparison

## Previous Approach

```text
Prompt
    ↓
Gemini
    ↓
JSON String
    ↓
json.loads()
    ↓
Dictionary
    ↓
Pydantic Validation
    ↓
Python Object
```

---

## Structured Output

```text
Prompt
    ↓
Gemini SDK
    ↓
response_schema
    ↓
Pydantic Object
```

---

# Benefits

- ✅ Less code
- ✅ No manual JSON parsing
- ✅ Automatic validation
- ✅ Cleaner implementation
- ✅ Type-safe responses
- ✅ Easier to maintain
- ✅ Better developer experience

---

# Real-World Use Cases

Structured Output is ideal for applications requiring predictable AI responses.

Examples:

- AI Chatbots
- Customer Support Systems
- Medical Report Analysis
- Financial Report Generation
- Sustainability Reporting
- Resume Parsing
- Invoice Extraction
- Product Recommendation Systems
- AI APIs
- Document Analysis

---

# Key Concepts Learned

- Pydantic models define the expected response structure.
- `response_mime_type="application/json"` instructs Gemini to return JSON.
- `response_schema` tells the SDK which Pydantic model to use.
- The SDK automatically parses and validates the response.
- `response.parsed` returns a ready-to-use Pydantic object.
- Manual `json.loads()` is no longer required.
- Manual Pydantic validation is no longer required.

---

# Summary

## Before Day 49

```python
response = llm(...)

data = json.loads(response.answer)

analysis = SustainabilityAnalysis(**data)
```

---

## After Day 49

```python
response = client.aio.models.generate_content(
    ...,
    config=types.GenerateContentConfig(
        response_schema=SustainabilityAnalysis,
        response_mime_type="application/json"
    )
)

analysis = response.parsed
```

The SDK automatically converts Gemini's response into a validated Pydantic object.

---

# Key Takeaway

> **Google GenAI Structured Output allows you to provide a Pydantic schema directly to the SDK. The SDK ensures Gemini returns data matching that schema, automatically parses the JSON, validates it, and returns a ready-to-use Python object through `response.parsed`. This eliminates manual JSON parsing, reduces boilerplate code, and improves reliability.**
