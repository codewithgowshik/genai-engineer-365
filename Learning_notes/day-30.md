# Day 30: Introduction to Prompt Engineering

## Objective

Learn what prompt engineering is, why prompts matter, and how different prompts produce different responses from the same AI model.

---

# What is Prompt Engineering?

Prompt engineering is the process of designing clear and effective instructions for an AI model to produce accurate, relevant, and useful responses.

A **prompt** is simply the input or instruction you give to an AI.

Example:

```text
What is artificial intelligence?
```

The better the prompt, the better the response.

---

# Why is Prompt Engineering Important?

Large Language Models (LLMs) do not think like humans. They generate responses based on the instructions they receive.

A vague prompt often produces a vague answer.

A detailed prompt usually produces a more accurate and structured answer.

Example:

Poor Prompt:

```text
Explain Python.
```

Better Prompt:

```text
You are a Python instructor.

Explain Python to a beginner in less than 150 words with one simple example.
```

---

# Components of a Good Prompt

A well-written prompt usually contains the following elements:

## 1. Role

Tell the AI who it should act as.

Example:

```text
You are an experienced software engineer.
```

Role prompting changes the perspective of the response.

---

## 2. Task

Clearly describe what the AI should do.

Example:

```text
Explain recursion.
```

The task should be specific and unambiguous.

---

## 3. Context

Provide background information.

Example:

```text
The audience is first-year computer science students.
```

Context helps the AI tailor the response.

---

## 4. Constraints

Limit or guide the output.

Examples:

```text
Maximum 100 words.

Use bullet points.

Do not use technical jargon.
```

Constraints improve consistency.

---

## 5. Output Format

Specify how the answer should be presented.

Examples:

```text
Return the answer as:

- Definition
- Advantages
- Disadvantages
- Example
```

The AI follows the requested structure.

---

# Prompting Techniques

## 1. Zero-Shot Prompting

The AI receives only the task without examples.

Example:

```text
Summarize this article.
```

The model completes the task using its existing knowledge.

---

## 2. Role Prompting

Assign a professional role to the AI.

Example:

```text
You are a cybersecurity expert.

Explain phishing attacks.
```

The AI responds from that perspective.

---

## 3. Context Prompting

Provide additional information before asking the question.

Example:

```text
The reader has no programming experience.

Explain variables in Python.
```

The response becomes more appropriate for the audience.

---

## 4. Constraint Prompting

Limit the response.

Example:

```text
Explain recursion.

Maximum 100 words.

Use simple language.
```

Constraints make responses more predictable.

---

## 5. Structured Prompting

Request information in a specific format.

Example:

```text
Explain climate change.

Include:

- Definition
- Causes
- Effects
- Conclusion
```

The response becomes organized and easier to read.

---

# Comparing Prompts

Using the same task with different prompts produces different results.

Task:

```text
Explain Machine Learning.
```

### Prompt 1

```text
Explain Machine Learning.
```

Result:

General explanation.

---

### Prompt 2

```text
Explain Machine Learning to a 10-year-old.
```

Result:

Simpler language.

---

### Prompt 3

```text
You are a university professor.

Explain Machine Learning.
```

Result:

More technical explanation.

---

### Prompt 4

```text
Explain Machine Learning.

Maximum 100 words.
```

Result:

Short and concise response.

---

### Prompt 5

```text
You are an AI professor.

Explain Machine Learning.

Include:
- Definition
- Applications
- Advantages
- Example

Use bullet points.
```

Result:

Well-structured and detailed response.

---

# Why Different Prompts Produce Different Outputs

The AI model remains the same.

Only the instructions change.

Better instructions lead to better responses.

Prompt engineering is about giving the model enough information to produce the desired output.

---

# Best Practices

* Be specific.
* Clearly define the task.
* Provide relevant context.
* Assign a role when appropriate.
* Specify the desired output format.
* Add constraints if necessary.
* Keep prompts simple and unambiguous.

---

# Common Mistakes

* Asking vague questions.
* Providing insufficient context.
* Giving multiple unrelated tasks in one prompt.
* Omitting the desired output format.
* Using ambiguous language.

---

# Prompt Engineering Workflow

```text
Define Goal
      ↓
Assign Role
      ↓
Provide Context
      ↓
Describe Task
      ↓
Add Constraints
      ↓
Specify Output Format
      ↓
Review Response
      ↓
Improve Prompt
```

Prompt engineering is an iterative process.

Better prompts are created by refining previous prompts.

---

# Key Concepts Learned

* Prompt
* Prompt Engineering
* Role Prompting
* Context Prompting
* Constraint Prompting
* Structured Prompting
* Zero-Shot Prompting
* Output Formatting
* Prompt Refinement
* Prompt Comparison

---

# Key Takeaway

Prompt engineering is the skill of communicating effectively with an AI model. The same model can produce vastly different responses depending on how the prompt is written. By combining clear tasks, relevant context, defined roles, appropriate constraints, and structured output requirements, you can consistently generate higher-quality AI responses. Prompt engineering is one of the most important skills for anyone building applications with Large Language Models.
