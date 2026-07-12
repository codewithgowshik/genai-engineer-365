# Day 42: Prompt Templates and Variables

## Objective

Learn how prompt templates work, understand the role of variables in prompt generation, and build reusable prompts that can be dynamically customized for different tasks.

---

# What is a Prompt Template?

A prompt template is a reusable prompt with placeholders (variables) that can be replaced with different values at runtime.

Instead of writing a new prompt every time, you create one template and fill in the required information.

Example:

```text
You are a {role}.

Explain {topic} to a {audience}.

Use {tone}.
```

The words inside `{}` are variables.

---

# Why Use Prompt Templates?

Without templates:

```text
Prompt 1:
You are a Python teacher...

Prompt 2:
You are a Java teacher...

Prompt 3:
You are a JavaScript teacher...
```

This creates duplicate prompts.

With a template:

```text
You are a {language} teacher.

Explain {topic}.
```

Only the variable changes.

---

# Benefits of Prompt Templates

* Reusable
* Easy to maintain
* Reduces duplicate prompts
* Easier to update
* Works well with APIs
* Scales to many use cases

Most AI applications use prompt templates.

---

# What are Variables?

Variables are placeholders that receive values when the prompt is generated.

Example template:

```text
You are a {profession}.
```

Example values:

```text
profession = Doctor
```

Generated prompt:

```text
You are a Doctor.
```

---

# Common Prompt Variables

Examples include:

* role
* audience
* topic
* tone
* language
* context
* company
* format
* constraints

Variables allow one template to support many scenarios.

---

# Example

Template:

```text
You are a {role}.

Explain {topic}.

Audience:
{audience}

Tone:
{tone}
```

Input:

```text
role = Sustainability Consultant

topic = Carbon Footprint

audience = Small Business Owners

tone = Professional
```

Generated prompt:

```text
You are a Sustainability Consultant.

Explain Carbon Footprint.

Audience:
Small Business Owners

Tone:
Professional
```

---

# Why Templates Matter

Imagine writing prompts for:

* 100 users
* 50 different roles
* 20 languages

Without templates you would create hundreds of prompts.

Templates reduce everything to:

```text
One Template

+

Variables
```

---

# Prompt Template Workflow

```text
Template
      ↓
Insert Variables
      ↓
Generate Prompt
      ↓
Send to LLM
      ↓
Receive Response
```

This is the workflow used in many AI frameworks.

---

# Prompt Templates in Software

Many AI applications keep prompt templates separate from the application logic.

Example structure:

```text
project/

src/

prompts/

summarizer.txt

teacher.txt

consultant.txt
```

The application loads a template and replaces variables before sending it to the model.

---

# Good Template Design

A good prompt template should:

* Have one clear purpose.
* Use meaningful variable names.
* Avoid unnecessary repetition.
* Include output requirements.
* Be easy to reuse.

---

# Common Mistakes

* Hardcoding values.
* Using too many variables.
* Choosing unclear variable names.
* Mixing multiple tasks into one template.
* Forgetting required variables.

---

# Best Practices

* Keep templates focused.
* Use descriptive variable names.
* Separate templates from code.
* Reuse templates whenever possible.
* Test templates with different values.

---

# Real-World Applications

Prompt templates are widely used in:

* Chatbots
* Customer support systems
* AI writing assistants
* AI coding assistants
* Report generators
* Enterprise AI platforms
* AI agents

Templates allow one application to support many different users and tasks.

---

# Key Concepts Learned

* Prompt Template
* Variables
* Placeholder
* Dynamic Prompt
* Prompt Generation
* Reusability
* Parameterization
* Template Design
* Prompt Engineering
* Automation

---

# Key Takeaway

Prompt templates allow developers to create reusable prompts by replacing fixed values with variables. Instead of writing a separate prompt for every situation, a single template can generate many prompts dynamically. This approach reduces duplication, improves maintainability, and is widely used in production AI systems where prompts need to adapt to different users, tasks, and contexts.
