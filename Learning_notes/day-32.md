# Day 32: Prompt Anatomy & Reusable Prompt Templates

## Objective

Learn the structure of a good prompt (Prompt Anatomy) and understand why professional AI applications store prompts separately from the source code.

---

# What is a Prompt?

A prompt is the instruction or input given to a Large Language Model (LLM).

It tells the AI:

* What to do
* How to do it
* What kind of output is expected

Example:

```text
Explain Artificial Intelligence.
```

Everything the AI generates depends on the prompt.

---

# What is Prompt Anatomy?

Prompt Anatomy is the structure of a well-designed prompt.

Instead of writing random instructions, professional prompts are built using multiple components.

A complete prompt usually looks like:

```text
Role

↓

Instruction

↓

Context

↓

Constraints

↓

Examples (Optional)

↓

Expected Output
```

---

# 1. Role

The role tells the AI who it should behave as.

Example:

```text
You are a Sustainability Consultant.
```

Other examples:

```text
You are a Python instructor.

You are a Financial Advisor.

You are a Medical Researcher.
```

The role changes the style and expertise of the response.

---

# 2. Instruction

The instruction tells the AI exactly what task to perform.

Example:

```text
Explain ESG.
```

Another example:

```text
Summarize this article.
```

The instruction should always be clear and specific.

---

# 3. Context

Context gives the AI additional background information.

Without context:

```text
Explain Python.
```

With context:

```text
Explain Python to a first-year engineering student who has never programmed before.
```

The AI now understands:

* Audience
* Knowledge level
* Purpose

Context produces more relevant responses.

---

# 4. Constraints

Constraints tell the AI what limitations to follow.

Examples:

```text
Maximum 150 words.

Use bullet points.

Do not use technical jargon.

Only mention three advantages.
```

Constraints improve consistency and control.

---

# 5. Examples (Few-Shot Prompting)

Sometimes showing examples helps the AI understand the desired output.

Example:

```text
Question:
What is ESG?

Answer:
Environmental, Social and Governance.

Question:
What is Carbon Footprint?

Answer:
```

The AI follows the demonstrated pattern.

This technique is called **Few-Shot Prompting**.

---

# 6. Expected Output

Tell the AI how to organize the response.

Example:

```text
Return:

Definition

Advantages

Disadvantages

Conclusion
```

Instead of one long paragraph, the AI produces structured output.

---

# Complete Prompt Example

```text
You are an experienced Sustainability Consultant.

Explain ESG to a small business owner.

Use simple language.

Maximum 200 words.

Include:

- Definition
- Benefits
- Example
- Conclusion
```

Notice how every part of the prompt has a purpose.

---

# Why Prompt Anatomy Matters

A well-structured prompt:

* Produces better answers
* Reduces ambiguity
* Makes responses more consistent
* Improves reliability

Professional AI applications rely on carefully designed prompts.

---

# What is a Prompt Template?

A prompt template is a reusable prompt stored separately from the application code.

Instead of writing prompts directly inside Python:

```python
prompt = """
You are a teacher...

Explain AI...
"""
```

Create a separate file:

```text
teacher_prompt.txt
```

Example:

```text
You are a friendly teacher.

Explain concepts using simple language.

Provide one example.

End with a summary.
```

---

# Why Use Prompt Templates?

Without templates:

```text
Python Code

↓

Large Prompt

↓

Hard to maintain
```

With templates:

```text
Python Code

↓

Load Prompt

↓

Send to LLM
```

The prompt and the code remain separate.

---

# Benefits of Prompt Templates

* Cleaner source code
* Easy to edit prompts
* Reusable
* Easier collaboration
* Better project organization

Prompt engineers can improve prompts without changing Python code.

---

# Typical Project Structure

```text
project/

src/

prompts/

system_prompt.txt

README.md

tests/
```

This structure is common in production AI applications.

---

# Loading a Prompt

Instead of writing long prompts inside Python:

```python
prompt = """
Very long prompt...
"""
```

The application loads the template:

```python
prompt = load_prompt(
    "teacher_prompt.txt"
)
```

The code becomes smaller and easier to maintain.

---

# When to Use Prompt Templates

Prompt templates are useful when:

* The prompt is reused many times.
* The prompt is very long.
* Multiple personas exist.
* Different tasks require different prompts.

---

# Prompt Engineering Workflow

```text
Define Task
      ↓
Design Prompt
      ↓
Store as Template
      ↓
Load Template
      ↓
Send to LLM
      ↓
Evaluate Output
      ↓
Improve Template
```

Prompt engineering is an iterative process.

Templates are updated over time as better prompts are discovered.

---

# Best Practices

* Write one prompt for one purpose.
* Keep prompts reusable.
* Separate prompts from application logic.
* Give prompts meaningful names.
* Store prompts in a dedicated folder.

---

# Key Concepts Learned

* Prompt
* Prompt Anatomy
* Role
* Instruction
* Context
* Constraints
* Examples
* Expected Output
* Few-Shot Prompting
* Prompt Template
* Reusable Prompts
* Prompt Separation
* Prompt Organization

---

# Key Takeaway

A prompt is more than a question—it is a structured set of instructions that guides an AI model. By combining roles, clear instructions, context, constraints, examples, and output requirements, you can produce more accurate and consistent responses. Storing prompts as reusable templates in a dedicated `prompts/` folder keeps AI applications organized, maintainable, and easier to improve over time, which is a standard practice in professional AI development.
