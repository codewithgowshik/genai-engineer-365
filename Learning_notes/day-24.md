# Day 24: Add Commands Like /reset, /save and /system

## Objective

Learn how to add commands to a CLI assistant and manage conversation state.

---

# Topics Covered

* Command handling
* Assistant controls
* Saving conversations
* Resetting memory
* Configuration
* Personas
* Command routing

---

# What is a Command?

A command is a special input that performs an action instead of sending a question to the LLM.

Example:

```text
/help
/save
/reset
/usage
/exit
```

---

# Normal Question vs Command

Normal Question:

```text
What is ESG?
```

Flow:

```text
User
 ↓
Gemini
 ↓
Response
```

---

Command:

```text
/save
```

Flow:

```text
User
 ↓
Command Handler
 ↓
Execute Action
```

No Gemini call is required.

---

# /help

Purpose:

Display available commands.

Example:

```text
/help
```

Output:

```text
Available Commands

/help
/usage
/save
/reset
/exit
```

---

# /usage

Purpose:

Display token usage and cost.

Example:

```text
Input Tokens
Output Tokens
Total Tokens
Total Cost
```

---

# /save

Purpose:

Store current conversation memory.

Code:

```python
save_conversation(
    history,
    summary
)
```

Flow:

```text
history
summary
 ↓
conversation.json
```

---

# /reset

Purpose:

Clear memory.

Code:

```python
history.clear()

summary = ""
```

Before:

```text
User: My name is Gowshik
```

After:

```text
history = []
summary = ""
```

Memory is erased.

---

# Summary vs History

## History

Stores recent messages.

Example:

```python
history = [
    "User: Hi",
    "Assistant: Hello"
]
```

---

## Summary

Stores compressed memory.

Example:

```python
summary = """
User is interested in ESG.
"""
```

---

# How Memory Works

Prompt sent to Gemini:

```python
prompt=f"""
Summary:

{summary}

Recent Conversation:

{"\n".join(history)}
"""
```

This means:

```text
Summary
 +
Recent Messages
 ↓
Gemini
```

The assistant remembers previous chats because both are included in the prompt.

---

# Why the Name Test Failed

The conversation history was likely being sent correctly.

However the system prompt instructed Gemini:

```text
Do not store personal information
```

Therefore Gemini ignored the name even though it was present in memory.

---

# Command Handler

Instead of putting all command logic in main.py:

```python
if question == "/save":
...
if question == "/reset":
...
if question == "/usage":
...
```

Create:

```text
commands.py
```

Purpose:

```text
Handle all commands
```

---

# Architecture

```text
User Input
      ↓

commands.py

      ↓

Command?
      ↓

Yes
 ↓
Execute

No
 ↓
Gemini
```

---

# Separation of Concerns

main.py

```text
Chat Flow
```

commands.py

```text
Command Logic
```

storage.py

```text
Save / Load
```

memory.py

```text
Conversation Memory
```

---

# Project Structure

```text
project-1-llm-cli-assistant/

src/

main.py

commands.py

llm.py

memory.py

storage.py

summary_memory.py

metrics.py
```

---

# Key Concepts Learned

## Commands

Special actions that do not require an LLM call.

---

## Save

Stores conversation state in JSON.

---

## Reset

Clears conversation memory.

---

## History

Recent messages.

---

## Summary

Compressed long-term memory.

---

## Command Handler

A dedicated file that manages assistant commands.

---

# Key Takeaways

* Commands improve assistant usability.
* `/save` stores memory.
* `/reset` clears memory.
* History stores recent messages.
* Summary stores compressed memory.
* Commands should be separated from chat logic.
* Memory is injected into prompts through history and summary.

---

# Reflection

Today I learned how commands work in a CLI assistant. I understood the difference between normal questions and commands, how conversation memory is saved and reset, and how history and summary are injected into prompts to give the assistant memory. I also learned why command logic should be separated into its own file for better project organization.
