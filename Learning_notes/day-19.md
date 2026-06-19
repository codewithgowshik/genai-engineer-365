# Day 19: Save and Reload Conversations as JSON

## Objective

Learn how to persist chatbot memory by saving and loading conversations using JSON files.

---

# Topics Covered

* JSON
* Serialization
* Deserialization
* Persistent memory
* File handling
* Saving conversations
* Loading conversations

---

# The Problem

Until now, the chatbot memory existed only while the program was running.

Example:

```python
history = []
summary = ""
```

These variables live in RAM.

When the program closes:

```text
RAM is cleared
```

and all memory is lost.

---

# Goal

Transform:

```text
Temporary Memory
```

into:

```text
Persistent Memory
```

so that the chatbot remembers previous conversations even after restarting.

---

# JSON

JSON stands for:

```text
JavaScript Object Notation
```

JSON is used to store structured data.

Example:

```json
{
    "history": [
        "User: Hi",
        "Assistant: Hello!"
    ],
    "summary": "The user is Gowshik."
}
```

---

# Components of Memory

## Short-Term Memory

Stored in:

```python
history = []
```

Contains:

```text
Recent conversation
```

Example:

```python
[
    "User: Hi",
    "Assistant: Hello!",
    "User: Explain AI",
    "Assistant: AI stands for Artificial Intelligence."
]
```

---

## Long-Term Memory

Stored in:

```python
summary
```

Contains compressed information.

Example:

```text
The user is Gowshik, a computer science student interested in AI.
```

---

# Saving Memory

Function:

```python
def save_conversation(
    history,
    summary
):
```

Purpose:

Store chatbot memory inside:

```text
conversation.json
```

---

# Creating a Dictionary

```python
data = {
    "history": history,
    "summary": summary
}
```

Example:

```python
{
    "history": [
        "User: Hi",
        "Assistant: Hello!"
    ],
    "summary": "The user is Gowshik."
}
```

---

# Opening a File

```python
with open(
    "conversation.json",
    "w"
) as file:
```

Mode:

```python
"w"
```

means:

```text
Write Mode
```

Purpose:

* Create the file if it does not exist.
* Overwrite previous contents.

---

# Writing JSON

```python
json.dump(
    data,
    file,
    indent=4
)
```

Purpose:

Convert Python objects into JSON and store them inside the file.

---

# indent=4

Without:

```python
indent=4
```

JSON looks like:

```json
{"history":["User: Hi"],"summary":"The user is Gowshik."}
```

Hard to read.

With:

```python
indent=4
```

JSON becomes:

```json
{
    "history": [
        "User: Hi"
    ],
    "summary": "The user is Gowshik."
}
```

which is easier to understand.

---

# Loading Memory

Function:

```python
def load_conversation():
```

Purpose:

Restore previous memory from:

```text
conversation.json
```

---

# Reading Mode

```python
with open(
    "conversation.json",
    "r"
)
```

Mode:

```python
"r"
```

means:

```text
Read Mode
```

---

# Converting JSON to Python

```python
data = json.load(
    file
)
```

Purpose:

Transform:

```json
{
    "history": [...],
    "summary": "..."
}
```

into:

```python
{
    "history": [...],
    "summary": "..."
}
```

Python dictionary.

---

# Returning Multiple Values

```python
return (
    data["history"],
    data["summary"]
)
```

returns two objects:

1. history
2. summary

---

# Unpacking

```python
history, summary = load_conversation()
```

Python automatically assigns:

```python
history = data["history"]

summary = data["summary"]
```

---

# First Run

If:

```text
conversation.json
```

does not exist:

```python
except FileNotFoundError:

    return [], ""
```

returns:

```python
history = []

summary = ""
```

which starts the chatbot with empty memory.

---

# Meaning of

```python
return [], ""
```

Returns:

```python
([], "")
```

which becomes:

```python
history = []

summary = ""
```

Purpose:

Initialize empty memory when no saved conversation exists.

---

# Serialization

Converting:

```python
history
summary
```

into:

```text
JSON
```

using:

```python
json.dump()
```

is called:

```text
Serialization
```

---

# Deserialization

Converting:

```text
JSON
```

back into:

```python
history
summary
```

using:

```python
json.load()
```

is called:

```text
Deserialization
```

---

# Data Flow

Saving:

```text
history + summary
        ↓
save_conversation()
        ↓
Dictionary
        ↓
json.dump()
        ↓
conversation.json
```

---

Loading:

```text
conversation.json
        ↓
json.load()
        ↓
Dictionary
        ↓
return history, summary
        ↓
history, summary = load_conversation()
```

---

# Source of Truth

Day 18:

```python
summary = ""
```

inside memory.py

Memory existed only in RAM.

---

Day 19:

```text
conversation.json
```

becomes the source of truth.

Memory survives application restarts.

---

# Internal Summary Generation

```python
response = await llm(
    request,
    show_output=False
)
```

Purpose:

Generate memory summaries silently.

---

# show_output=False

Meaning:

```text
Generate response
but do not print it.
```

Used for:

* Summary memory
* Internal operations
* Background tasks

---

# Architecture

```text
Program Starts
        ↓
load_conversation()
        ↓
history + summary restored
        ↓
User Question
        ↓
LLM
        ↓
Assistant Response
        ↓
Update History
        ↓
History Too Large?
        ↓
Yes
        ↓
summarize_memory()
        ↓
Update Summary
        ↓
trim_history()
        ↓
save_conversation()
        ↓
conversation.json
```

---

# Folder Structure

```text
project/

main.py

llm.py

memory.py

summary_memory.py

storage.py

conversation.json

models.py

system_prompts.py
```

---

# Key Takeaways

* RAM memory disappears after the program stops.
* JSON provides persistent storage.
* `json.dump()` saves Python objects.
* `json.load()` restores Python objects.
* `history` stores short-term memory.
* `summary` stores long-term memory.
* `history, summary = load_conversation()` performs unpacking.
* `return [], ""` initializes empty memory.
* `show_output=False` hides internal LLM calls.
* `conversation.json` becomes the chatbot's source of truth.

---

# Reflection

Today I learned how to persist chatbot memory using JSON files. Instead of losing all context whenever the program terminates, I implemented a storage layer that saves and restores both short-term and long-term memory. This transformed the chatbot from having temporary memory to maintaining conversations across sessions, an important step toward building more capable AI agents.
