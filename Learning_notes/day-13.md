# Day 013 - Pydantic Models for Request and Response

## Objective

Learn how to use Pydantic for data validation and define request and response models for the application.

---

## Topics Covered

### What is Pydantic?

Pydantic is a Python library used to define and validate data.

It ensures that incoming data follows the structure and data types we expect.

---

## Why Use Pydantic?

Benefits:

* Data validation
* Type checking
* Cleaner code
* Fewer bugs
* Easier maintenance
* Structured data

---

## BaseModel

All Pydantic models inherit from:

```python
from pydantic import BaseModel
```

`BaseModel` provides automatic validation and useful methods for working with data.

---

## Creating a Request Model

```python
from pydantic import BaseModel


class Request(BaseModel):

    # User question
    prompt: str
```

Example:

```python
request = Request(
    prompt="What is AI?"
)
```

Accessing the field:

```python
print(request.prompt)
```

Output:

```text
What is AI?
```

---

## Creating a Response Model

```python
from pydantic import BaseModel


class Response(BaseModel):

    # Gemini answer
    answer: str
```

Example:

```python
response = Response(
    answer="Artificial Intelligence is..."
)
```

Accessing the field:

```python
print(response.answer)
```

Output:

```text
Artificial Intelligence is...
```

---

## Validation

Pydantic validates the data automatically.

Correct:

```python
Request(
    prompt="Hello"
)
```

Incorrect:

```python
Request(
    prompt=123
)
```

Pydantic raises a validation error because `prompt` should be a string.

---

## Type Hints

```python
prompt: str
answer: str
```

These specify the expected data types.

Common types:

```python
str
int
float
bool
list
dict
```

---

## Request and Response Flow

```text
User
 ↓

Request Model
(prompt)

 ↓

Gemini

 ↓

Response Model
(answer)

 ↓

User
```

---

## Streaming Response

Gemini sends data in chunks.

Example:

```text
Chunk 1 → "Artificial "
Chunk 2 → "Intelligence "
Chunk 3 → "is..."
```

To create a response model, chunks are collected:

```python
full_response = ""
```

Inside the loop:

```python
full_response += chunk.text
```

After streaming completes:

```python
return Response(
    answer=full_response
)
```

---

## Why Collect the Response?

Streaming only gives small pieces of text.

Example:

```text
"Artificial "
"Intelligence "
"is..."
```

Combining them produces:

```text
"Artificial Intelligence is..."
```

This complete string can then be validated using the Response model.

---

## Printing While Streaming

```python
print(
    chunk.text,
    end="",
    flush=True
)
```

Purpose:

* Shows text immediately.
* Creates a ChatGPT-like experience.
* Does not affect the stored response.

---

## Validator Analogy

Think of a validator as a security guard.

```text
Incoming Data
       ↓
Validator
       ↓
Approved Data
```

The validator checks:

* Required fields
* Correct data types
* Valid values

Invalid data is rejected before entering the application.

---

## Why Use Models Instead of Raw Strings?

Before:

```python
str
 ↓
llm()
 ↓
str
```

After:

```text
Request Model
 ↓
llm()
 ↓
Response Model
```

Advantages:

* Safer code
* Structured data
* Easier debugging
* Better scalability


Today I learned how to use Pydantic to create structured request and response models. I understood how data validation works and why collecting streamed chunks into a complete response is necessary. Using Pydantic makes applications cleaner, safer, and easier to maintain.
