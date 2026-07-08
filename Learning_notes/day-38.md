# Day 38: Delimiters and Prompt Structure

## Objective

Learn how delimiters improve prompt clarity, understand why they are used in professional AI applications, and use them to separate different sections of a prompt.

---

# What are Delimiters?

A delimiter is a symbol or marker used to clearly separate different parts of a prompt.

Instead of writing one long block of text, delimiters organize the prompt into logical sections.

Delimiters help both humans and AI understand where one section ends and another begins.

---

# Why Use Delimiters?

Without delimiters, a prompt may become confusing because instructions, context, and user input are mixed together.

Example:

```text
Explain the following article. The article is about climate change. The audience is a school student. Here is the article...
```

The model must infer which parts are instructions and which parts are content.

With delimiters:

```text
### Instruction

Explain the article.

### Audience

School student

### Article

...
```

The structure becomes much clearer.

---

# Benefits of Delimiters

Using delimiters provides several advantages:

* Improves prompt readability.
* Separates instructions from data.
* Reduces ambiguity.
* Makes prompts easier to maintain.
* Produces more consistent responses.

Professional AI applications almost always use structured prompts.

---

# Common Delimiters

There is no single correct delimiter.

Common choices include:

Using triple hashes:

```text
###
```

Using triple dashes:

```text
---
```

Using XML-style tags:

```text
<instruction>

<context>

<input>
```

Using triple quotes:

```text
"""
```

The important point is consistency.

---

# Prompt Without Delimiters

```text
Summarize this article for a beginner. The article discusses renewable energy technologies and their impact on reducing carbon emissions...
```

Everything is mixed together.

---

# Prompt With Delimiters

```text
### Role

You are a sustainability educator.

### Instruction

Summarize the article.

### Audience

Beginner

### Context

The article discusses renewable energy technologies.

### Output

Use bullet points.
```

Each section has a clear purpose.

---

# Structuring a Prompt

A professional prompt often follows this order:

```text
Role
    ↓
Instruction
    ↓
Context
    ↓
Examples (Optional)
    ↓
User Input
    ↓
Output Requirements
```

This makes prompts easier to read and modify.

---

# Example

Without structure:

```text
Explain ESG for a beginner in simple English with examples and end with recommendations.
```

Structured version:

```text
### Role

You are an ESG consultant.

### Audience

Beginner.

### Instruction

Explain ESG.

### Requirements

- Use simple English.
- Give one practical example.
- Finish with three recommendations.
```

The structured version is easier to understand and maintain.

---

# Delimiters in Real AI Systems

Many AI systems use delimiters to separate:

* System prompts
* User prompts
* Retrieved documents
* Tool outputs
* Conversation history

This prevents different types of information from becoming mixed together.

---

# Delimiters for Retrieved Context

When using Retrieval-Augmented Generation (RAG), retrieved documents are usually separated from the user's question.

Example:

```text
### Retrieved Context

...

### User Question

...
```

This makes it clear which text is reference material and which text is the user's request.

---

# Delimiters for Examples

Few-shot prompting often separates examples using delimiters.

Example:

```text
### Example 1

Question:
...

Answer:
...

### Example 2

Question:
...

Answer:
...
```

The model can easily identify the pattern.

---

# Best Practices

* Keep one purpose per section.
* Use consistent delimiters.
* Clearly label each section.
* Separate instructions from context.
* Avoid mixing unrelated information.

---

# Common Mistakes

* Mixing instructions and context together.
* Using inconsistent delimiters.
* Creating overly complex prompt structures.
* Forgetting to label sections.
* Repeating information across multiple sections.

---

# Prompt Design Workflow

```text
Define Role
      ↓
Write Instruction
      ↓
Add Context
      ↓
Separate Using Delimiters
      ↓
Specify Output Format
      ↓
Review Prompt
```

Organized prompts are easier to maintain and reuse.

---

# Key Concepts Learned

* Delimiters
* Prompt Structure
* Prompt Organization
* Context Separation
* Prompt Readability
* Structured Prompting
* Prompt Design
* Prompt Clarity
* Context Management
* Prompt Maintenance

---

# Key Takeaway

Delimiters are simple markers that organize prompts into clear sections such as role, instruction, context, examples, and output requirements. They improve readability, reduce ambiguity, and help AI models distinguish between different types of information. As prompts become larger and more complex, using delimiters becomes an essential prompt engineering practice for building reliable and maintainable AI applications.
