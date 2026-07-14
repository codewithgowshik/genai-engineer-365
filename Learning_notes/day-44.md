# Day 44: Validating JSON Against a Schema

## Objective

Learn why AI-generated JSON should be validated, understand what a JSON schema is, and verify that LLM responses match an expected structure before using them in an application.

---

# Why Validation Matters

Large Language Models usually follow instructions, but they are **not guaranteed** to return perfectly formatted JSON every time.

For example, you might ask for:

```json
{
  "name": "",
  "age": 0
}
```

Sometimes the model returns:

```json
{
  "name": "Alice",
  "age": 25
}
```

Perfect.

But sometimes it may return:

```text
Sure! Here's the JSON:

{
  "name": "Alice",
  "age": 25
}
```

Or even:

```json
{
  "name": "Alice"
}
```

The JSON is now invalid for your application because the required field is missing.

---

# What is Validation?

Validation is the process of checking whether data follows an expected structure.

Instead of trusting the AI blindly, the application verifies the response before using it.

Validation checks:

* Required fields
* Data types
* Missing values
* Invalid values
* Overall structure

---

# What is a Schema?

A schema is a blueprint describing what data should look like.

Example:

```text
Person

↓

name → string

age → integer

city → string
```

If the JSON matches the blueprint, it is considered valid.

---

# JSON Schema Example

Expected structure:

```json
{
  "topic": "",
  "summary": "",
  "recommendations": []
}
```

Valid response:

```json
{
  "topic": "Carbon Neutrality",
  "summary": "Reducing net carbon emissions.",
  "recommendations": [
    "Use renewable energy",
    "Improve energy efficiency"
  ]
}
```

---

# Invalid Response

```json
{
  "topic": "Carbon Neutrality"
}
```

Problems:

* Missing `summary`
* Missing `recommendations`

The application should reject or handle this response.

---

# Types of Validation

Validation can check:

### Required Fields

```text
summary

recommendations
```

---

### Data Types

Correct:

```json
{
  "score": 90
}
```

Incorrect:

```json
{
  "score": "ninety"
}
```

---

### Lists

Correct:

```json
{
  "recommendations": [
    "Solar",
    "Wind"
  ]
}
```

Incorrect:

```json
{
  "recommendations": "Solar"
}
```

---

### Nested Objects

Example:

```json
{
  "company": {
    "name": "Envora",
    "country": "UK"
  }
}
```

Validation ensures the nested structure is correct.

---

# Why AI Engineers Validate JSON

Without validation:

```text
LLM

↓

Application

↓

Crash
```

With validation:

```text
LLM

↓

Validation

↓

Valid

↓

Application
```

or

```text
LLM

↓

Validation

↓

Invalid

↓

Retry or Error Handling
```

Validation prevents unexpected failures.

---

# Validation Workflow

```text
User Prompt
      ↓
LLM Response
      ↓
Parse JSON
      ↓
Validate Schema
      ↓
Use Data
```

Every production AI system follows a similar workflow.

---

# Python and JSON Validation

Python first converts the text into a dictionary.

```python
import json

data = json.loads(response)
```

Then the application validates it.

Modern AI applications often use libraries such as:

* Pydantic
* jsonschema

These libraries automatically verify that the data matches the expected schema.

---

# Example Schema

Imagine a sustainability assistant returning:

```json
{
  "company": "",
  "overall_score": 0,
  "strengths": [],
  "weaknesses": [],
  "recommendations": []
}
```

Validation ensures:

* `company` is a string.
* `overall_score` is a number.
* `strengths` is a list.
* `weaknesses` is a list.
* `recommendations` is a list.

---

# Common Validation Errors

* Missing fields
* Wrong data types
* Invalid JSON syntax
* Unexpected fields
* Incorrect nesting

Applications should detect these problems before processing the response.

---

# Best Practices

* Always request valid JSON.
* Parse the response before using it.
* Validate required fields.
* Validate data types.
* Handle validation failures gracefully.
* Never assume AI output is always correct.

---

# Real-World Applications

JSON validation is used in:

* AI APIs
* AI Agents
* Function Calling
* Customer Support Systems
* Report Generation
* Workflow Automation
* Enterprise AI Platforms

Reliable AI software depends on validated structured data.

---

# Key Concepts Learned

* JSON
* JSON Validation
* Schema
* Required Fields
* Data Types
* Parsing
* Validation Workflow
* Error Handling
* Structured Output
* Data Integrity

---

# Key Takeaway

Generating structured JSON is only the first step. Before AI-generated data is used by an application, it should always be validated against a predefined schema. Validation ensures that required fields exist, data types are correct, and the overall structure matches expectations. This process makes AI applications more reliable, predictable, and suitable for production environments.
