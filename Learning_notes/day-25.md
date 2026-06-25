# Day 25: Selectable Personas / Profiles

## Objective

Learn how to change the assistant's behavior using profiles without changing the core system prompt.

---

# What is a Persona?

A persona is a predefined way for the assistant to respond.

Example:

```text
Teacher
↓
Explains simply

Auditor
↓
Focuses on compliance

Consultant
↓
Provides recommendations
```

The AI model stays the same.

Only the instructions change.

---

# System Prompt vs Persona

## System Prompt

Defines the assistant's identity.

Example:

```text
You are an elite Sustainability and ESG Intelligence Assistant.
```

Answers:

```text
What am I?
↓
ESG Assistant
```

---

## Persona

Defines how the assistant behaves.

Example:

```text
Teacher
↓
Simple explanations

Auditor
↓
Compliance-focused answers

Consultant
↓
Practical recommendations
```

Answers:

```text
How should I respond?
```

---

# personas.py

Store all available profiles.

Example:

```python
PERSONAS = {

    "teacher":
    "Explain ESG concepts simply.",

    "auditor":
    "Focus on ESG compliance and evidence.",

    "consultant":
    "Provide practical ESG recommendations."
}
```

Purpose:

```text
Store profile instructions in one place.
```

---

# Current Profile

Variable used to track the selected profile.

Example:

```python
current_profile = None
```

Meaning:

```text
No profile selected.
```

---

# Why Use None?

When the application starts:

```python
current_profile = None
```

The assistant only uses:

```text
SYSTEM_PROMPT
```

No additional profile instructions are applied.

---

# Profile Selection Command

User:

```text
/profile teacher
```

Process:

```text
User Input
      ↓

Extract Profile Name
      ↓

teacher
      ↓

Check PERSONAS
      ↓

Found
      ↓

Update current_profile
```

---

# String Methods Learned

## startswith()

Check whether text begins with a value.

```python
question.startswith("/profile")
```

Example:

```python
"/profile teacher".startswith("/profile")

# True
```

---

## replace()

Replace text.

```python
question.replace(
    "/profile",
    ""
)
```

Result:

```text
teacher
```

---

## strip()

Remove extra spaces.

```python
profile.strip()
```

Example:

```python
" teacher ".strip()

# teacher
```

---

## lower()

Convert text to lowercase.

```python
profile.lower()
```

Example:

```python
"Teacher".lower()

# teacher
```

---

# Why Profile Was Not Found

Example:

```python
profile = " teacher"
```

Dictionary:

```python
PERSONAS = {
    "teacher": "..."
}
```

Comparison:

```python
" teacher" != "teacher"
```

Result:

```text
Profile not found
```

Fix:

```python
profile = (
    question
    .replace("/profile", "")
    .strip()
    .lower()
)
```

---

# Returning Multiple Values

Example:

```python
return (
    True,
    summary,
    current_profile
)
```

Meaning:

```python
handled = True

summary = summary

current_profile = current_profile
```

---

# Understanding the Error

Error:

```text
ValueError:
expected 3, got 2
```

Cause:

```python
handled,
summary,
current_profile
```

expects 3 values.

But:

```python
return False, summary
```

returns only 2.

Fix:

```python
return (
    False,
    summary,
    current_profile
)
```

---

# Prompt Construction

Current Prompt:

```text
SYSTEM_PROMPT
+
Profile
+
Summary
+
History
```

Example:

```text
You are an ESG Assistant.

Explain ESG concepts simply.

Summary:
...

Recent Conversation:
...
```

---

# Architecture

```text
User
 ↓

/profile teacher
 ↓

commands.py
 ↓

PERSONAS
 ↓

current_profile
 ↓

main.py
 ↓

Prompt
 ↓

Gemini
```

---

# Key Concepts Learned

* Persona
* Profile selection
* System Prompt
* startswith()
* replace()
* strip()
* lower()
* Returning multiple values
* Command handling
* Prompt customization

---

# Key Takeaway

The System Prompt defines what the assistant is. The selected profile defines how the assistant responds. Profiles allow the same ESG assistant to act as a teacher, auditor, or consultant without changing its core identity.
