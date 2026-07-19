# Day 48: Constrain Output to an Enum of Categories

## Objective

Learn how to constrain a Large Language Model's output to a predefined set of categories using Python Enums and Pydantic validation. This improves the consistency, reliability, and predictability of structured AI outputs.

---

# What is an Enum?

An **Enum (Enumeration)** is a special Python data type that defines a fixed set of allowed values.

Instead of accepting any string, an Enum restricts a value to one of the predefined options.

Example:

```python
from enum import Enum

class Category(str, Enum):
    ENVIRONMENT = "ENVIRONMENT"
    SOCIAL = "SOCIAL"
    GOVERNANCE = "GOVERNANCE"
```

Only these three values are considered valid.

---

# Why Use Enums?

Large Language Models generate text probabilistically. Without constraints, the same concept can be represented in multiple ways.

Example outputs:

```
Environment
```

```
Environmental
```

```
Climate
```

```
Green Initiative
```

Although they refer to similar concepts, they are different strings and make software harder to build.

Using an Enum forces the model to return a single standardized value.

Example:

```
ENVIRONMENT
```

---

# Benefits of Enum-Based Outputs

- Produces consistent responses.
- Reduces ambiguity.
- Simplifies validation.
- Makes downstream processing easier.
- Improves production reliability.

---

# Enum Validation with Pydantic

Pydantic can validate Enum values automatically.

Example:

```python
from pydantic import BaseModel

class ESGClassification(BaseModel):
    category: Category
```

Valid response:

```json
{
    "category": "SOCIAL"
}
```

Invalid response:

```json
{
    "category": "Community"
}
```

The second example fails validation because `"Community"` is not part of the Enum.

---

# Prompt Engineering

The prompt should explicitly instruct the model to choose only from the allowed categories.

Example:

```text
Classify the following statement.

Choose ONLY ONE category.

Allowed Categories:

ENVIRONMENT
SOCIAL
GOVERNANCE

Return ONLY valid JSON.

{
    "category": ""
}
```

Providing clear constraints significantly improves response consistency.

---

# Workflow

```text
User Input
      │
      ▼
Prompt
      │
      ▼
Gemini
      │
      ▼
JSON Response
      │
      ▼
json.loads()
      │
      ▼
Pydantic Validation
      │
      ▼
Enum Validation
      │
      ▼
Python Object
```

---

# Example

### Input

```text
The company installed solar panels to reduce carbon emissions.
```

### LLM Response

```json
{
    "category": "ENVIRONMENT"
}
```

### Validation

```python
classification = ESGClassification(**data)
```

Output:

```
Category.ENVIRONMENT
```

or

```python
classification.category.value
```

Output:

```
ENVIRONMENT
```

---

# Real-World Applications

Enums are widely used in AI systems to classify information into predefined categories.

Examples include:

### Email Classification

- Spam
- Personal
- Promotion

### Customer Support

- Bug
- Feature Request
- Question

### Medical Diagnosis

- Low Risk
- Medium Risk
- High Risk

### Document Classification

- Invoice
- Receipt
- Contract

### Sustainability (ESG)

- Environment
- Social
- Governance

---

# Best Practices

- Keep the number of categories small.
- Use meaningful category names.
- Clearly list all allowed values in the prompt.
- Validate responses using Pydantic.
- Reject invalid categories instead of guessing.

---

# Key Concepts Learned

- Enum (Enumeration)
- Constrained Output
- Controlled Vocabulary
- Classification
- Prompt Constraints
- Pydantic Enum Validation
- Structured Outputs
- Reliable AI Systems

---

# Key Takeaway

Large Language Models can generate many different words for the same concept, making responses inconsistent. Enums solve this problem by restricting the model to a predefined set of valid values. Combined with Pydantic validation, enums ensure AI responses are predictable, consistent, and reliable for production applications.
