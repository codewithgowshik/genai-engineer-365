# Day 18 – Summary Memory

## Objective

Learn memory strategies and implement a summary-memory system that preserves important information while preventing the conversation history from growing indefinitely.

---

# Topics Covered

* Sliding window memory
* Summary memory
* Memory compression
* Long-term memory
* Short-term memory
* Internal LLM calls
* Hidden responses

---

# The Problem

Conversation history grows continuously.

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
100 messages
500 messages
1000 messages
```

This increases:

* Token usage
* Cost
* Latency
* Risk of exceeding the context window

---

# Sliding Window Memory

Day 17 introduced:

```python
history[:] = history[-max_messages:]
```

Purpose:

```text
Keep recent messages.
Forget older messages.
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

Using:

```python
history[-4:]
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

# Limitation of Sliding Window

Important information may disappear.

Example:

```text
User: My name is Gowdham.
Assistant: Nice to meet you.

...

100 messages later

User: What is my name?
```

The chatbot may forget because those messages were removed.

---

# Summary Memory

Instead of deleting old messages:

```text
Old Messages
      ↓
Compress
      ↓
Summary
```

Example:

Original conversation:

```text
User: My name is Gowdham.
Assistant: Nice to meet you.

User: I am a computer science student.
Assistant: Great.

User: I want to become an AI engineer.
Assistant: Wonderful.
```

Compressed summary:

```text
The user is Gowdham, a computer science student who wants to become an AI engineer.
```

---

# Types of Memory

## Short-Term Memory

Stored in:

```python
history = []
```

Contains:

```text
Recent conversation
```

---

## Long-Term Memory

Stored in:

```python
summary = ""
```

Contains:

```text
Compressed old conversation
```

---

# Architecture

```text
Summary
      +
Recent History
      ↓
LLM
      ↓
Response
      ↓
Update History
      ↓
Summarize Old Messages
      ↓
Update Summary
```

---

# Summarization Function

```python
async def summarize_memory(
    summary,
    old_messages
)
```

Purpose:

* Compress old messages.
* Preserve important facts.
* Reduce token usage.

---

# Building the Summary Prompt

```python
summary_prompt = f"""
Current summary:

{summary}

New conversation:

{"\n".join(old_messages)}

Update the summary.
Keep only important information.
Be concise.
"""
```

This prompt instructs Gemini to act as a note taker.

---

# Pydantic Request

```python
request = requests(
    prompt=summary_prompt
)
```

Purpose:

Store the summary prompt inside a validated request object.

---

# Sending to Gemini

```python
response = await llm(
    request,
    show_output=False
)
```

Gemini reads:

```text
Current summary
+
Old messages
+
Instructions
```

and generates an updated summary.

---

# Returning the New Summary

```python
return response.answer
```

The generated text becomes the new long-term memory.

---

# Why show_output=False?

Normal conversation:

```python
show_output=True
```

Result:

```text
Answer is printed.
```

Summary generation:

```python
show_output=False
```

Result:

```text
Summary is generated silently.
```

The user does not see internal memory operations.

---

# show_output

Purpose:

Control whether streamed chunks are displayed.

```python
if show_output:

    print(
        chunk.text,
        end="",
        flush=True
    )
```

---

# Streaming Responses

Chunks arrive gradually:

```text
Artificial
Intelligence
is
powerful
```

Collected using:

```python
full_response += chunk.text
```

---

# Important Mistake

Wrong:

```python
if chunk.text:

    full_response = ""

    full_response += chunk.text
```

Problem:

Previous chunks are erased.

---

Correct:

```python
full_response = ""

async for chunk in stream:

    if chunk.text:

        full_response += chunk.text
```

Purpose:

Accumulate all chunks into one response.

---

# Hidden LLM Calls

Two kinds of LLM calls exist:

## User Call

```python
response = await llm(
    request
)
```

Visible to the user.

---

## Memory Call

```python
response = await llm(
    request,
    show_output=False
)
```

Hidden from the user.

---

# Updating Memory

When history becomes too large:

```python
old_messages = history[:-max_messages]
```

Generate a summary:

```python
summary = await summarize_memory(
    summary,
    old_messages
)
```

Then trim:

```python
trim_history(history)
```

---

# Complete Flow

```text
User Question
      ↓

Store User Message
      ↓

Summary + Recent History
      ↓

Gemini
      ↓

Assistant Response
      ↓

Store Response
      ↓

History Too Large?
      ↓

Yes
      ↓

Old Messages
      ↓

summarize_memory()
      ↓

Updated Summary
      ↓

trim_history()
      ↓

Keep Recent Messages
      ↓

Repeat
```

---

# Memory Architecture

```text
Long-Term Memory
(summary)

+
Short-Term Memory
(history)

↓

Context sent to Gemini

↓

Response

↓

Update Memory
```

---

# Key Takeaways

* Sliding window memory forgets old messages.
* Summary memory compresses old messages.
* `history` stores short-term memory.
* `summary` stores long-term memory.
* Gemini itself can generate summaries.
* Internal LLM calls should be hidden from users.
* `show_output` controls visibility.
* `full_response += chunk.text` accumulates streamed chunks.
* Summary memory reduces token usage while preserving important information.

---

# Reflection

Today I learned that deleting old messages is not always desirable because important information may be lost. I implemented a summary-memory mechanism where Gemini acts as its own note-taking system. By combining long-term memory through summaries with short-term memory through recent history, I built a more intelligent conversational architecture similar to those used in production AI systems.
