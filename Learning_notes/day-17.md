# Day 17 - Token Limits and Trimming History

## Objective

Learn how context windows work and how to prevent conversation history from growing indefinitely by trimming old messages.

---

# Topics Covered

* Context window
* Token limits
* History growth
* History trimming
* Negative indexing
* List slicing
* In-place list modification

---

# The Problem

As conversations continue, history keeps growing.

Example:

```python
history = [
    "User: Hi",
    "Assistant: Hello!",
    ...
]
```

Over time:

```text
10 messages
50 messages
100 messages
500 messages
1000 messages
```

Every request sends the entire history to Gemini.

This causes:

* Slow responses.
* Increased costs.
* Larger prompts.
* Context window overflow.

---

# Context Window

The context window is the amount of information an LLM can see at one time.

Think of it as the model's short-term memory.

```text
System Prompt

Message 1
Message 2
Message 3
...
Message N
```

Anything outside the context window becomes invisible to the model.

---

# Token Limits

Models have a maximum number of tokens they can process.

Tokens represent pieces of text.

Example:

```text
Hello world
```

contains multiple tokens.

Long conversations consume more tokens.

Eventually:

```text
History too large
↓
Context limit reached
↓
Old messages cannot fit
```

---

# Solution: Trim History

Instead of keeping everything:

```python
history = [
msg1,
msg2,
msg3,
...
msg1000
]
```

Keep only recent messages:

```python
history[-10:]
```

Purpose:

```text
Keep the last 10 messages.
```

---

# Negative Indexing

Negative indexes count from the end of a list.

Example:

```python
history = [
1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12
]
```

Indexes:

```text
-1 → 12
-2 → 11
-3 → 10
-4 → 9
...
```

---

# Slicing

Example:

```python
history[-5:]
```

Means:

```text
Start from the fifth element from the end
and continue until the end.
```

Result:

```python
[
8,
9,
10,
11,
12
]
```

---

# max_messages

Suppose:

```python
max_messages = 5
```

Then:

```python
history[-max_messages:]
```

becomes:

```python
history[-5:]
```

which returns:

```python
[
8,
9,
10,
11,
12
]
```

Purpose:

Keep only the most recent messages.

---

# Trimming Function

```python
def trim_history(
    history,
    max_messages=10
):

    if len(history) > max_messages:

        history[:] = history[-max_messages:]
```

---

# len()

```python
len(history)
```

returns the number of elements inside the list.

Example:

```python
history = [
1,
2,
3,
4,
5
]
```

Result:

```python
len(history)
```

returns:

```text
5
```

---

# Why Use history[:]?

```python
history[:] = history[-max_messages:]
```

means:

```text
Replace all existing elements
with the last max_messages elements.
```

Example:

Before:

```python
[
1,
2,
3,
4,
5,
6,
7,
8
]
```

After:

```python
history[:] = history[-4:]
```

Result:

```python
[
5,
6,
7,
8
]
```

---

# Difference Between

```python
history = history[-4:]
```

and

```python
history[:] = history[-4:]
```

### history = history[-4:]

Creates a new list.

### history[:] = history[-4:]

Modifies the existing list object.

This preserves references to the same history list.

---

# Mental Model

Think of history as a notebook.

Without trimming:

```text
Page 1
Page 2
Page 3
...
Page 1000
```

Eventually the notebook becomes too large.

Instead of using an infinite notebook:

```text
Remove old pages
Keep recent pages
Continue writing
```

---

# Complete Flow

```text
User Question
        ↓
Store Question
        ↓
Gemini Response
        ↓
Store Response
        ↓
Trim History
        ↓
Keep Recent Messages
        ↓
Repeat
```

---

# Architecture

```text
System Prompt
        +
Trimmed History
        +
Current Question
        ↓
Gemini
        ↓
Response
        ↓
Update History
        ↓
Trim History
        ↓
Repeat
```

---

# Key Takeaways

* Conversation history cannot grow forever.
* LLMs have context windows.
* Long histories consume more tokens.
* Negative indexing counts from the end of a list.
* `history[-max_messages:]` keeps the most recent messages.
* `history[:]` replaces the contents of the existing list.
* Trimming prevents context overflow and improves efficiency.
* Recent messages are usually more valuable than older ones.

