# Day 15 - Multi-turn Conversations and Message History

## Objective

Learn how to maintain conversation history and build a multi-turn chatbot that remembers previous messages.

---

# Topics Covered

* Multi-turn conversations
* Message history
* Context
* Memory
* `join()`
* Storing user messages
* Storing assistant responses

---

# Single-turn Conversation

Until now, every question was independent.

Flow:

```text
User
 ↓
Question
 ↓
Gemini
 ↓
Answer
```

After generating the answer, Gemini forgets everything.

Example:

```text
User: My name is Gowdham.
AI: Nice to meet you.

User: What is my name?
AI: I don't know.
```

---

# Multi-turn Conversation

In a multi-turn conversation, previous messages are preserved.

Example:

```text
User: My name is Gowdham.
Assistant: Nice to meet you.

User: What is my name?
Assistant: Your name is Gowdham.
```

---

# Memory

Memory is simply storing previous messages and sending them again with every request.

Memory is not magic.

Our application remembers by maintaining a conversation history.

---

# Message History

History is stored inside a list.

```python
history = []
```

This list acts like a notebook.

Example:

```python
history = [
    "User: Hi",
    "Assistant: Hello!"
]
```

---

# Adding User Messages

Function:

```python
def add_to_history(
    history,
    question
):

    history.append(
        f"User: {question}"
    )
```

Purpose:

Store user questions in the history list.

Example:

```python
history = []

add_to_history(
    history,
    "Hi"
)
```

History becomes:

```python
[
    "User: Hi"
]
```

---

# Why History Is Declared Once

Correct:

```python
history = []

while True:
```

Wrong:

```python
while True:

    history = []
```

Declaring history inside the loop destroys previous messages.

---

# Storing Assistant Responses

Function:

```python
def add_assistant_response(
    history,
    answer
):

    history.append(
        f"Assistant: {answer}"
    )
```

Purpose:

Store Gemini's responses.

Example:

```python
add_assistant_response(
    history,
    "Hello!"
)
```

History becomes:

```python
[
    "User: Hi",
    "Assistant: Hello!"
]
```

---

# Complete History Example

```python
[
    "User: Hi",
    "Assistant: Hello!",

    "User: What is AI?",
    "Assistant: Artificial Intelligence is..."
]
```

---

# join()

History is a list.

Example:

```python
history = [
    "User: Hi",
    "Assistant: Hello!",
    "User: What is AI?"
]
```

Using:

```python
"\n".join(history)
```

produces:

```text
User: Hi
Assistant: Hello!
User: What is AI?
```

---

# Why Use join()?

Gemini expects a string.

Wrong:

```python
contents = history
```

Correct:

```python
contents = "\n".join(history)
```

`join()` converts the list into one large string.

---

# Request Model

```python
request = Request(
    prompt="\n".join(history)
)
```

Purpose:

Send the entire conversation to Gemini.

---

# How Gemini Remembers

Without history:

```text
User: My name is Gowdham.
Assistant: Nice to meet you.

User: What is my name?
Assistant: I don't know.
```

With history:

Gemini receives:

```text
User: My name is Gowdham.
Assistant: Nice to meet you.

User: What is my name?
```

Therefore it can answer:

```text
Your name is Gowdham.
```

---

# Response Object

Our `llm()` function returns:

```python
return Response(
    answer=full_response
)
```

Example:

```python
Response(
    answer="Hello!"
)
```

---

# response.answer

If:

```python
response = await llm(request)
```

then:

```python
response.answer
```

returns:

```python
"Hello!"
```

because `answer` is a field inside the Response model.

---

# Storing Gemini Responses

```python
response = await llm(request)

add_assistant_response(
    history,
    response.answer
)
```

History becomes:

```python
[
    "User: Hi",
    "Assistant: Hello!"
]
```

---

# Complete Flow

```text
User enters question
        ↓
add_to_history()
        ↓
History grows
        ↓
join(history)
        ↓
Create request
        ↓
llm()
        ↓
Gemini generates answer
        ↓
response.answer
        ↓
add_assistant_response()
        ↓
History grows again
        ↓
Repeat
```

---

# Mental Model

Think of history as a notebook.

```text
Question
↓
Write into notebook

Answer
↓
Write into notebook

Next Question
↓
Read entire notebook

Answer
↓
Write into notebook
```

The notebook keeps growing throughout the conversation.
