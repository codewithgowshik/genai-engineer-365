# Day 63 / 365 – Building the End-to-End Extraction Pipeline

## 🎯 Objective

Today I connected all the individual components of my Structured Extraction Service into a complete end-to-end extraction pipeline.

Previously, I had built each module independently:

- PDF Reader
- Prompt Builder
- Gemini Integration

Today, I introduced an **Extractor** that orchestrates these components into a single workflow.

Instead of manually calling each module, the extraction pipeline now coordinates the complete document processing process automatically.

---

# Why an Extraction Pipeline?

Building individual modules is useful, but production AI systems require a central component that coordinates the workflow.

Without an extraction pipeline, the application would need to manually call every component.

Example:

```python
text = read_pdf(file_path)

prompt = build_extraction_prompt(text)

response = await generate(prompt)
```

As the project grows, this approach becomes difficult to maintain.

Instead, a single extraction function manages the complete workflow.

---

# What is an Extractor?

The extractor is the orchestration layer of the application.

It does not perform the individual tasks itself.

Instead, it coordinates the different modules in the correct order.

Its responsibilities include:

- Reading the PDF
- Building the extraction prompt
- Sending the prompt to Gemini
- Returning the generated response

Each specialised module continues to handle only its own responsibility.

---

# Extraction Workflow

The application now follows this complete workflow.

```text
PDF

↓

PDF Reader

↓

Extracted Text

↓

Prompt Builder

↓

Gemini

↓

Response

↓

Return Result
```

Instead of writing this workflow repeatedly, the extractor performs it automatically.

---

# Separation of Responsibilities

Each module has a single responsibility.

## PDF Reader

Responsibility:

```text
PDF

↓

Extract Text
```

---

## Prompt Builder

Responsibility:

```text
Extracted Text

↓

Build Prompt
```

---

## LLM Module

Responsibility:

```text
Prompt

↓

Gemini

↓

Response
```

---

## Extractor

Responsibility:

```text
Coordinate every module

↓

Return the final response
```

The extractor does not contain PDF logic, prompt engineering, or Gemini implementation details.

Its only purpose is orchestration.

---

# Why This Architecture Matters

Separating responsibilities makes the project:

- Easier to understand
- Easier to test
- Easier to maintain
- Easier to extend
- More reusable

Each module can evolve independently without affecting the rest of the application.

---

# End-to-End Pipeline

The extraction service now behaves like a production AI workflow.

```text
User

↓

Upload PDF

↓

Read PDF

↓

Extract Text

↓

Generate Prompt

↓

Send to Gemini

↓

Receive Response

↓

Return Result
```

The entire pipeline is executed through a single extraction function.

---

# Logging the Workflow

To understand how the application behaves, I added simple execution logs during each stage.

The extraction process reports:

- Reading PDF
- Building Prompt
- Sending request to Gemini
- Receiving response
- Extraction complete

These logs make debugging and future improvements much easier.

---

# Benefits of an Orchestrator

Using an extractor provides several advantages.

- Removes duplicate code
- Simplifies the application entry point
- Keeps modules independent
- Improves readability
- Supports future expansion

Future additions such as:

- JSON parsing
- Pydantic validation
- Logging
- Metrics
- Retry logic

can all be added inside the extraction pipeline without changing the application interface.

---

# Current Architecture

```text
app.py

↓

extractor.py

↓

pdf_reader.py

↓

extraction_prompt.py

↓

llm.py

↓

Gemini

↓

Response
```

The application is now organised into clear, reusable layers.

---

# Skills Learned

Today I learned:

- How to design an orchestration layer.
- Why AI applications need an extraction pipeline.
- The importance of separation of concerns.
- Coordinating multiple modules together.
- Building an end-to-end AI workflow.
- Creating modular and reusable software architecture.

---

# Key Takeaways

- Individual modules should perform one responsibility only.
- The extractor coordinates the complete workflow.
- Modular architecture improves maintainability.
- AI systems should be designed as reusable pipelines rather than single scripts.
- Orchestration is a fundamental software engineering concept for AI applications.

---

# Today's Deliverables

- Built the extraction pipeline.
- Connected the PDF Reader, Prompt Builder, and LLM.
- Created a reusable extractor module.
- Added basic execution logging.
- Completed the first end-to-end document extraction workflow.

---

# Summary

Today I transformed my Structured Extraction Service from a collection of independent modules into a complete end-to-end AI application. By introducing an extraction pipeline, I connected the PDF Reader, Prompt Builder, and Gemini integration into a single reusable workflow. This orchestration layer simplifies the application architecture, promotes separation of concerns, and provides a scalable foundation for future features such as structured output validation, logging, metrics, and FastAPI integration. This marks the transition from building isolated components to engineering a modular AI system.
