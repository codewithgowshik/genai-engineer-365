# Day 46: Repair Loop for Invalid JSON

## Objective

Learn how to recover from invalid AI-generated JSON by implementing a repair loop that requests a corrected response instead of immediately failing.

---

# Why Do We Need a Repair Loop?

Large Language Models are good at following instructions, but they are not perfect.

Even when asked to return JSON, they may produce:

* Missing fields
* Incorrect data types
* Extra explanations
* Markdown code blocks
* Invalid JSON syntax

Instead of stopping with an error, many AI applications automatically ask the model to fix its previous response.

---

# What is a Repair Loop?

A repair loop is a retry mechanism.

If validation fails, the application sends another prompt asking the model to correct the previous output.

The corrected response is then parsed and validated again.

---

# Basic Workflow

```text
User Request
      ↓
LLM Response
      ↓
Parse JSON
      ↓
Validate
      ↓
 ┌───────────────┐
 │               │
Valid         Invalid
 │               │
 ▼               ▼
Use Data     Ask LLM to Repair
                  │
                  ▼
            Corrected JSON
                  │
                  ▼
             Validate Again
```

---

# Example

Prompt:

```text
Return ONLY valid JSON.
```

The model returns:

```text
Sure! Here's the JSON:

{
    "topic":"Carbon Neutrality"
}
```

Problems:

* Markdown/text before JSON.
* Missing required fields.

Instead of crashing, the application asks:

```text
Your previous response was invalid.

Return ONLY valid JSON that matches this schema:

{
    "topic":"",
    "summary":"",
    "recommendations":[]
}
```

The model usually fixes its output.

---

# Benefits

Repair loops:

* Improve reliability.
* Reduce manual retries.
* Recover from formatting mistakes.
* Make AI applications more robust.
* Improve user experience.

---

# Retry Limits

Never retry forever.

Typical production systems allow:

* 1 retry
* 2 retries
* 3 retries

If the model still fails, the application reports an error.

---

# Best Practices

* Explain why validation failed.
* Include the required schema.
* Ask for ONLY corrected JSON.
* Limit the number of retries.
* Log failures for debugging.

---

# Common Mistakes

* Infinite retry loops.
* Not validating repaired responses.
* Sending vague repair instructions.
* Ignoring validation errors.

---

# Real-World Applications

Repair loops are commonly used in:

* AI Agents
* Function Calling
* Document Extraction
* Data Pipelines
* Enterprise AI Systems
* Workflow Automation

Reliable AI systems rarely trust the first response without validation.

---

# Key Concepts Learned

* Repair Loop
* Retry Logic
* Validation
* Error Recovery
* Robust AI Systems
* JSON Parsing
* Schema Validation
* Reliability
* Structured Output
* Fault Tolerance

---

# Key Takeaway

A repair loop makes AI applications more reliable by automatically requesting corrected output when validation fails. Instead of stopping at the first error, the application retries with clear instructions and validates the repaired response before using it. This pattern is widely used in production AI systems where reliability is essential.
