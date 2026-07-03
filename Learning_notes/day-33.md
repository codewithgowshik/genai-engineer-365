# Day 33: Common Prompt Failure Modes

## Objective

Learn why AI sometimes produces incorrect or low-quality responses and understand how to identify and fix common prompt failure modes.

---

# What is a Prompt Failure?

A prompt failure occurs when the AI's response does not meet the user's expectations.

This may happen because:

* The prompt is unclear.
* The prompt lacks context.
* The instructions are ambiguous.
* The task is too broad.
* The output format is not specified.

Prompt failures are usually caused by the prompt rather than the AI model itself.

---

# Common Prompt Failure Modes

## 1. Ambiguous Instructions

An ambiguous prompt does not clearly describe the task.

Example:

```text
Explain Python.
```

Problem:

The AI does not know:

* Who the audience is.
* What level of detail is required.
* Which aspect of Python to explain.

Improved Prompt:

```text
Explain Python to a beginner who has never programmed before.

Use simple language and one practical example.
```

---

## 2. Missing Context

Without context, the AI must make assumptions.

Example:

```text
Write a report.
```

Questions the AI may have:

* What kind of report?
* Who will read it?
* What should it include?

Improved Prompt:

```text
Write a one-page sustainability report for a small manufacturing company.

The audience is senior management.
```

---

## 3. Too Broad

Large tasks often produce incomplete answers.

Example:

```text
Teach me Artificial Intelligence.
```

This covers too many topics.

Improved Prompt:

```text
Explain what Artificial Intelligence is.

Then explain Machine Learning with one simple example.
```

Breaking a large task into smaller tasks improves the response.

---

## 4. Missing Output Format

If no format is specified, responses may become difficult to read.

Example:

```text
Explain ESG.
```

Improved Prompt:

```text
Explain ESG.

Use this format:

- Definition
- Importance
- Benefits
- Example
```

The output becomes organized and consistent.

---

## 5. No Constraints

Without constraints, responses may become too long or too technical.

Example:

```text
Explain Climate Change.
```

Improved Prompt:

```text
Explain Climate Change.

Maximum 150 words.

Use simple English.

Avoid technical terms.
```

Constraints improve consistency.

---

## 6. Multiple Tasks in One Prompt

Example:

```text
Explain Python.

Write code.

Compare Java.

Explain AI.

Summarize everything.
```

The AI may produce a confusing response.

Better approach:

Break the work into separate prompts.

One prompt should focus on one primary task.

---

## 7. Unrealistic Requests

Example:

```text
Predict the stock market for the next year.
```

The AI cannot reliably predict future events.

Instead:

```text
Explain the factors that influence stock market movements.
```

Always ask questions that the model can reasonably answer.

---

## 8. Conflicting Instructions

Example:

```text
Explain Artificial Intelligence in one sentence.

Include five examples.
```

The instructions conflict.

A prompt should have consistent requirements.

---

# How to Fix Prompt Failures

A simple workflow:

```text
Write Prompt
      ↓
Generate Response
      ↓
Identify Problems
      ↓
Improve Prompt
      ↓
Generate Again
```

Prompt engineering is an iterative process.

---

# Prompt Improvement Checklist

Before sending a prompt, ask yourself:

* Is the task clear?
* Is enough context provided?
* Is the audience defined?
* Are there reasonable constraints?
* Is the output format specified?
* Does the prompt focus on one task?

If the answer is "Yes" to all, the prompt is likely to produce a better response.

---

# Example

Weak Prompt:

```text
Explain Machine Learning.
```

Problems:

* No audience.
* No format.
* No constraints.

Improved Prompt:

```text
You are a university lecturer.

Explain Machine Learning to a first-year engineering student.

Use simple language.

Include:

- Definition
- Real-world example
- Advantages
- Limitations

Maximum 200 words.
```

This prompt provides clear guidance to the AI.

---

# Prompt Evaluation

After receiving a response, evaluate it based on:

* Accuracy
* Clarity
* Completeness
* Relevance
* Structure

If any area is weak, refine the prompt instead of immediately changing the model.

---

# README Polish

Documentation is often the first thing users see.

A professional README should include:

* Project title
* Description
* Features
* Installation
* Usage
* Commands
* Screenshots
* Technologies used
* Future improvements

Screenshots help readers quickly understand the project without running it.

Recommended screenshots:

* Home screen or terminal interface
* Main application workflow
* Command examples
* Project structure (optional)

---

# Best Practices

* Give clear instructions.
* Provide sufficient context.
* Keep one prompt focused on one task.
* Specify the desired output format.
* Add reasonable constraints.
* Review and refine prompts based on results.

---

# Key Concepts Learned

* Prompt Failure
* Ambiguity
* Context
* Constraints
* Output Formatting
* Prompt Refinement
* Prompt Evaluation
* README Documentation
* Documentation Quality

---

# Key Takeaway

Not every poor AI response is caused by the model. In many cases, the prompt is the real issue. Learning to recognize common prompt failure modes—such as ambiguity, missing context, conflicting instructions, and lack of structure—helps you design prompts that produce more accurate and reliable results. Alongside good prompts, clear documentation with polished screenshots makes your projects easier to understand, use, and share.
