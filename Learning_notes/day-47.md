# Day 47: Extracting Structured Data from Unstructured Text

## Objective

Learn how to use an LLM to extract structured information from natural language, understand why information extraction is important, and represent multiple extracted items as validated Pydantic models.

---

# What is Information Extraction?

Information extraction is the process of identifying useful pieces of information from unstructured text and converting them into a structured format.

Humans naturally identify names, dates, places, products, and events while reading.

AI models can perform the same task and return the information in a structured form.

---

# Structured vs Unstructured Data

## Unstructured Text

```text
John bought a Tesla Model 3 on 12 July 2026 for £32,000.
```

This sentence is easy for humans to read but difficult for software to process directly.

---

## Structured Output

```json
{
  "customer": "John",
  "product": "Tesla Model 3",
  "date": "2026-07-12",
  "price": 32000
}
```

The same information is now machine-readable.

---

# Why Extract Structured Data?

Many AI applications receive documents, emails, reports, invoices, or meeting notes.

Before software can use that information, it must first extract the important fields.

Examples include:

* Customer details
* Product names
* Dates
* Prices
* Locations
* Email addresses

---

# Extracting Multiple Items

Sometimes one document contains several objects.

Example:

```text
Apple released the iPhone.

Google announced Gemini.

Microsoft introduced Copilot.
```

Instead of one object, we need a list.

---

# Expected JSON

```json
[
  {
    "company": "Apple",
    "product": "iPhone"
  },
  {
    "company": "Google",
    "product": "Gemini"
  },
  {
    "company": "Microsoft",
    "product": "Copilot"
  }
]
```

---

# Using Pydantic

A model describes one item.

```python
class Product(BaseModel):
    company: str
    product: str
```

The final result becomes a list of Product objects.

---

# Workflow

```text
Unstructured Text
        ↓
LLM
        ↓
JSON List
        ↓
json.loads()
        ↓
Validate Each Item
        ↓
List of Pydantic Objects
```

---

# Why Use a List?

Many real-world documents contain multiple records.

Examples:

* Shopping receipts
* Meeting attendees
* Job applicants
* Products
* Orders
* Transactions

Lists allow software to process each record individually.

---

# Validation

Each extracted object should still be validated.

Example:

```json
{
    "company": "Apple"
}
```

This should fail if the schema also requires a product field.

Validation guarantees that every extracted item has the expected structure.

---

# Real-World Applications

Information extraction is used in:

* Invoice processing
* Resume parsing
* Healthcare records
* Legal documents
* Customer support
* CRM systems
* AI Agents
* Enterprise search

Many AI-powered business applications rely on structured extraction.

---

# Best Practices

* Clearly define the required schema.
* Return only JSON.
* Validate every extracted item.
* Handle missing values carefully.
* Keep each object focused on one entity.

---

# Key Concepts Learned

* Information Extraction
* Structured Data
* Unstructured Data
* JSON Arrays
* Lists
* Pydantic Models
* Validation
* Entity Extraction
* Data Processing
* Reliable AI Outputs

---

# Key Takeaway

Large Language Models can transform unstructured text into structured data by extracting important information and returning it in a predefined format. When multiple records exist, they should be represented as a JSON array and validated individually using Pydantic models. This technique is widely used in production AI systems for document processing, automation, and business intelligence.
