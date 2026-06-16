# Day 16 - System Prompts and Roles

## Objective

Learn how system prompts work and how to configure the behavior of an LLM by providing instructions before the conversation starts.

---

# Topics Covered

* System prompts
* Roles
* Personality
* Behavior
* Configurable prompts
* Combining system prompts with conversation history

---

# What is a System Prompt?

A system prompt is a set of instructions given to the model before the conversation begins.

It tells the model:

* Who it is.
* How it should behave.
* How it should format responses.
* What rules it should follow.

Think of it as:

```text
Identity + Rules + Personality
```

---

# Why Use System Prompts?

System prompts help control:

### Personality

Examples:

```text
Helpful
Professional
Teacher
Friendly
Funny
```

---

### Response Style

Examples:

```text
Short answers
Detailed explanations
Bullet points
Examples
```

---

### Restrictions

Examples:

```text
Never write code.
Always explain simply.
Limit responses to 100 words.
```

---

# Example

System Prompt:

```text
You are a Python teacher.

Explain concepts simply.

Use examples whenever possible.
```

User:

```text
What is Python?
```

Gemini:

```text
Python is a beginner-friendly programming language.

Example:

print("Hello World")
```

---

# Roles in LLMs

LLMs generally use three roles.

---

## System Role

Controls behavior.

Example:

```text
You are a professional software engineer.

Always explain clearly.
```

---

## User Role

Represents the user's message.

Example:

```text
How do loops work?
```

---

## Assistant Role

Represents previous responses.

Example:

```text
Loops are used to repeat code.
```

---

# Conversation Structure

```text
System
 ↓
User
 ↓
Assistant
 ↓
User
 ↓
Assistant
```

---

# System Prompt File

Create:

```text
system_prompt.py
```

Example:

```python
SYSTEM_PROMPT = """
You are a helpful AI assistant.

Explain concepts simply.

Use examples whenever possible.
"""
```

Purpose:

Separate configuration from application logic.

---

# Memory and System Prompt

Memory answers:

```text
What has happened?
```

System Prompt answers:

```text
Who are you?
How should you behave?
```

These are different.

---

# Conversation History

Example:

```python
history = [
    "User: Hi",
    "Assistant: Hello!",
    "User: What is Python?"
]
```

---

# join()

Using:

```python
"\n".join(history)
```

Produces:

```text
User: Hi
Assistant: Hello!
User: What is Python?
```

---

# Combining System Prompt and History

Suppose:

System Prompt:

```text
You are a Python tutor.

Explain concepts simply.
```

History:

```text
User: Hi
Assistant: Hello!

User: What is Python?
```

Combining them:

```python
full_prompt = f"""
{SYSTEM_PROMPT}

{request.prompt}
"""
```

Result:

```text
You are a Python tutor.

Explain concepts simply.

User: Hi
Assistant: Hello!

User: What is Python?
```

---

# Why Combine Them?

Because Gemini needs:

1. Instructions.
2. Previous conversation.
3. Current question.

to generate better responses.

---

# Architecture

```text
system_prompt.py
        ↓

SYSTEM_PROMPT
        ↓

memory.py
        ↓

history
        ↓

main.py
        ↓

request.prompt
        ↓

llm.py
        ↓

full_prompt

=
SYSTEM_PROMPT
+
CONVERSATION HISTORY

        ↓

Gemini
        ↓

Response
```

---

# Mental Model

Think of the system prompt as a job description.

Example:

```text
You are a math teacher.

Explain slowly.

Provide examples.
```

Gemini behaves according to these instructions.

---

# Difference Between System Prompt and Memory

### System Prompt

Defines:

```text
Who are you?
How should you behave?
```

Examples:

```text
Teacher
Programmer
Friendly assistant
```

---

### Memory

Defines:

```text
What has happened so far?
```

Examples:

```text
User: Hi
Assistant: Hello!

User: My name is Gowdham.
Assistant: Nice to meet you.
```

---

# Complete Flow

```text
System Prompt
        ↓

Conversation History
        ↓

Current Question
        ↓

Combined Prompt
        ↓

Gemini
        ↓

Response
        ↓

Save Response
        ↓

Repeat
```
