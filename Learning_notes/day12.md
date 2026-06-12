# Day 012 - Streaming Responses from an LLM

## Objective

Learn how to stream responses from Gemini and display them chunk-by-chunk in the terminal.

---

## Topics Covered

### What is Streaming?

Streaming allows an LLM to send its response gradually instead of waiting for the entire response to finish.

Normal response:

```text
User Question
      ↓
Wait...
      ↓
Wait...
      ↓
Entire Response
      ↓
Print
```

Streaming response:

```text
User Question
      ↓
Chunk 1
      ↓
Print
      ↓
Chunk 2
      ↓
Print
      ↓
Chunk 3
      ↓
Print
```

---

## Why Use Streaming?

Benefits:

* Better user experience.
* Faster perceived speed.
* Similar behavior to ChatGPT.
* User sees the answer immediately.
* Useful for chatbots and AI applications.

---

## Normal Response

Day 11 used:

```python
response = await client.aio.models.generate_content(
    model=model,
    contents=prompt
)
```

This waits until Gemini generates the entire response.

Flow:

```text
Request
↓
Wait
↓
Whole Response Arrives
↓
Print
```

---

## Streaming Response

Day 12 uses:

```python
stream = await client.aio.models.generate_content_stream(
    model=model,
    contents=prompt
)
```

The stream returns chunks of text as they become available.

Flow:

```text
Request
↓
Chunk Arrives
↓
Print
↓
Chunk Arrives
↓
Print
↓
Response Complete
```

---

## Processing Chunks

Chunks are received using:

```python
async for chunk in stream:
```

The loop continues until all chunks are received.

Example:

```python
async for chunk in stream:

    if chunk.text:

        print(
            chunk.text,
            end="",
            flush=True
        )
```

---

## What is a Chunk?

A chunk is a small part of the response.

Example:

Full response:

```text
Python is a programming language.
```

Possible chunks:

```python
chunk1.text = "Python "
chunk2.text = "is a "
chunk3.text = "programming language."
```

Streaming prints each chunk immediately.

---

## async for

`async for` is used to iterate over asynchronous streams.

Example:

```python
async for chunk in stream:
```

This waits for new chunks to arrive and processes them one by one.

---

## flush=True

```python
print(
    chunk.text,
    end="",
    flush=True
)
```

Purpose:

* Forces Python to display output immediately.
* Prevents text from remaining in the output buffer.

Without:

```python
flush=False
```

Python may wait and display multiple chunks together.

With:

```python
flush=True
```

Chunks appear instantly.

---

## end=""

Normally:

```python
print("Hello")
```

adds a newline.

Equivalent to:

```python
print("Hello", end="\n")
```

Using:

```python
end=""
```

prevents new lines and allows chunks to appear continuously.

Example:

```python
print("Python ", end="")
print("is ", end="")
print("awesome")
```

Output:

```text
Python is awesome
```

---

## Retry Logic

Errors are handled using:

```python
for attempt in range(3):
```

If an exception occurs:

```python
await asyncio.sleep(2)
```

waits two seconds before retrying.

---

## Keeping the Chat Running

Using:

```python
while True:
```

allows the chatbot to continuously ask questions.

Example:

```python
while True:

    question = input("Ask anything: ")

    if question.lower() == "exit":
        break

    await llm(question)
```

