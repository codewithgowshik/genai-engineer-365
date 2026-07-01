# Day 31: Improving Weak Prompts

## Objective

Learn how to identify weak prompts, improve them, and understand why small changes can significantly improve AI responses.

---

# What is a Weak Prompt?

A weak prompt is a prompt that gives the AI very little information.

Weak prompts are usually:

* Too short
* Too vague
* Missing context
* Missing a clear objective
* Missing the desired output format

Example:

```text
Explain AI.
```

This prompt is valid, but it doesn't tell the AI:

* Who the audience is
* How detailed the explanation should be
* What format to use
* What topics to include

As a result, the response is very generic.

---

# Characteristics of a Good Prompt

A good prompt clearly communicates what you want.

It usually includes:

* Role
* Task
* Context
* Constraints
* Output Format

Example:

```text
You are an AI instructor.

Explain Artificial Intelligence to a beginner.

Use simple language.

Include:
- Definition
- Real-world examples
- Advantages
- Limitations

Maximum 200 words.
```

The AI now has clear instructions.

---

# Prompt Improvement Process

Improving prompts is an iterative process.

```text
Weak Prompt
      ↓
Identify Missing Information
      ↓
Add Context
      ↓
Assign a Role
      ↓
Add Constraints
      ↓
Specify Output Format
      ↓
Review the Result
```

The goal is not to write longer prompts.

The goal is to write clearer prompts.

---

# Example 1

Weak Prompt:

```text
Write about Python.
```

Problems:

* No audience
* No objective
* No structure
* No length requirement

Improved Prompt:

```text
You are a Python instructor.

Explain Python to a beginner.

Include:
- What Python is
- Why it is popular
- One practical example

Use simple English.

Maximum 150 words.
```

---

# Example 2

Weak Prompt:

```text
Write an email.
```

Improved Prompt:

```text
You are a professional business consultant.

Write a polite email to a client explaining that the project deadline has been extended by three days.

Keep the tone professional and under 150 words.
```

---

# Example 3

Weak Prompt:

```text
Summarize this article.
```

Improved Prompt:

```text
Summarize the article for a high-school student.

Focus only on the main ideas.

Use bullet points.

Keep the summary under 100 words.
```

---

# Why Prompt Improvement Works

The AI generates responses based on the information it receives.

More useful instructions produce more useful responses.

The model has not changed.

Only the prompt has changed.

---

# Common Problems in Weak Prompts

* Vague instructions
* Missing audience
* Missing context
* Too many unrelated requests
* No desired output format
* No length limit

---

# Prompt Refinement

Prompt engineering is rarely perfect on the first attempt.

A common workflow is:

```text
Write Prompt
      ↓
Generate Response
      ↓
Evaluate Response
      ↓
Improve Prompt
      ↓
Generate Again
```

This process is called **prompt refinement**.

---

# Before vs After

Weak Prompt:

```text
Explain climate change.
```

Improved Prompt:

```text
You are an environmental science teacher.

Explain climate change to a 15-year-old student.

Include:
- Definition
- Main causes
- Effects
- One real-world example

Use simple language.

Maximum 200 words.
```

The improved version produces a more focused and useful response.

---

# Best Practices

* Clearly define the task.
* Identify the target audience.
* Provide enough context.
* Assign a role when appropriate.
* Specify the desired output format.
* Add reasonable constraints.
* Review and refine the prompt if necessary.

---

# Key Concepts Learned

* Weak Prompt
* Prompt Refinement
* Prompt Improvement
* Role Prompting
* Context
* Constraints
* Output Formatting
* Prompt Evaluation
* Iterative Prompting

---

# Key Takeaway

A good prompt is not necessarily a long prompt—it is a clear prompt. Prompt engineering is an iterative process where you continuously refine your instructions until the AI produces the response you need. Small improvements such as adding context, defining the audience, assigning a role, or specifying an output format can dramatically improve the quality of the AI's responses.
