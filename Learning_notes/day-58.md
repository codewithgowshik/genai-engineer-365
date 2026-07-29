# Day 58 / 365 – Build the Extraction Prompt and Parser

## 🎯 Objective

Today I focused on one of the most important components of a structured extraction system: the **extraction prompt** and the **output parser**.

While previous days focused on reading documents and extracting structured JSON, today's goal was to improve **how the AI is instructed** and **how the application processes the AI's response**.

A well-designed extraction system consists of two equally important parts:

- The extraction prompt
- The output parser

The prompt tells the AI **what information to extract**, while the parser ensures the extracted information can be safely used by the application.

---

# What is an Extraction Prompt?

An extraction prompt is a carefully designed instruction that tells the AI exactly what information should be extracted from a document.

Unlike normal prompts that ask for explanations or summaries, extraction prompts request structured information.

Instead of:

```text
Summarise this report.
```

An extraction prompt might say:

```text
Extract the company name, report year, industry, revenue, and Net Zero target.
Return the result as valid JSON following the provided schema.
```

The quality of the extracted data depends heavily on the quality of the prompt.

---

# Why Prompt Design Matters

Large Language Models can interpret the same document in multiple ways.

Without clear instructions, responses may vary.

Poor prompt:

```text
Tell me about this report.
```

Possible output:

```
Several paragraphs of explanation...
```

Better prompt:

```text
Extract only the requested fields.
If a value is unavailable, return null.
Return valid JSON only.
```

Now the output becomes predictable.

---

# Prompt Engineering for Structured Extraction

A good extraction prompt should include:

- The task
- The target schema
- Formatting instructions
- Missing value rules
- Output constraints

Example structure:

```text
Task

↓

Fields to Extract

↓

JSON Schema

↓

Output Rules

↓

AI Response
```

This helps reduce inconsistent outputs.

---

# What is an Output Parser?

The parser is responsible for processing the AI's response after generation.

Workflow:

```text
LLM Response

↓

Parser

↓

Validate JSON

↓

Application
```

The parser ensures that the response follows the expected format before the data is used elsewhere.

---

# Why Parsing is Important

Even when an AI is instructed to return JSON, responses may still contain:

- Extra explanations
- Incorrect formatting
- Missing fields
- Unexpected values

The parser acts as a safety layer between the LLM and the application.

Without parsing:

```text
LLM

↓

Raw Response

↓

Application
```

With parsing:

```text
LLM

↓

Parser

↓

Validated JSON

↓

Application
```

---

# My Extraction Workflow

My structured extraction pipeline now follows this sequence:

```text
PDF

↓

Extract Text

↓

Gemini

↓

Extraction Prompt

↓

Structured JSON

↓

Parser

↓

Validated Output

↓

Application
```

Each stage has a clear responsibility.

---

# Prompt Responsibilities

The extraction prompt is responsible for:

- Defining the extraction task.
- Specifying which fields to extract.
- Requesting structured output.
- Handling missing information.
- Ensuring consistency.

A well-designed prompt reduces ambiguity and improves extraction quality.

---

# Parser Responsibilities

The parser is responsible for:

- Reading the model output.
- Checking JSON formatting.
- Verifying required fields.
- Detecting missing values.
- Preparing validated data for the application.

The parser does not generate information—it ensures the generated information is usable.

---

# Current Architecture

```text
User

↓

PDF Reader

↓

Extract Text

↓

Gemini

↓

Extraction Prompt

↓

JSON Response

↓

Parser

↓

Validated Structured Data

↓

Application
```

This separation of responsibilities makes the system easier to maintain and extend.

---

# Why Separate Prompt and Parser?

Keeping prompt generation and parsing independent provides several advantages:

- Easier debugging
- Better maintainability
- Reusable prompts
- Reusable parsers
- Cleaner architecture
- Improved reliability

If extraction requirements change, the prompt can be updated without rewriting the parser.

---

# Real-World Applications

Extraction prompts and parsers are used in:

- Document Intelligence Platforms
- Invoice Processing
- Resume Parsing
- Contract Analysis
- Financial Reporting
- ESG Reporting
- Healthcare Systems
- Enterprise Knowledge Management

Most production AI systems separate generation from validation in the same way.

---

# Skills Learned

Today I learned:

- What an extraction prompt is.
- How prompt engineering affects structured output.
- Why prompts should define schemas clearly.
- What an output parser does.
- Why AI-generated JSON should always be validated.
- How prompts and parsers work together in a structured extraction pipeline.
- How to design a more reliable document extraction workflow.

---

# Key Takeaways

- A good extraction prompt leads to more accurate structured data.
- A parser ensures AI-generated output is safe for applications.
- Prompt engineering and parsing are equally important.
- Separating generation from validation improves maintainability.
- Structured extraction systems rely on both well-designed prompts and reliable parsers.

---

# Today's Deliverables

- Improved the extraction prompt for structured output.
- Refined the parser to handle AI responses consistently.
- Reviewed the complete extraction workflow.
- Strengthened the reliability of the structured extraction pipeline.
- Continued developing the Structured Extraction Service for Envora.

---

# Summary

Today I focused on the two core components of a structured extraction system: the extraction prompt and the output parser. I learned how carefully designed prompts guide the AI to produce consistent, schema-compliant responses, while parsers validate and prepare those responses for use within the application. Together, these components form the foundation of reliable AI-powered document extraction systems and are essential for building production-ready document intelligence applications.
