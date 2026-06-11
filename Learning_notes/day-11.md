# Day 011 - Async Programming and Async LLM Calls

## Objective

Learn the fundamentals of asynchronous programming and implement the first asynchronous LLM call using the Gemini API.

---

## Topics Covered

### What is Synchronous Programming?

Synchronous (sync) programming executes tasks one after another.

Example:

```python
response_1 = llm("Python")
response_2 = llm("Java")
response_3 = llm("C++")
```

Flow:

```text
Task 1
↓
Finish
↓
Task 2
↓
Finish
↓
Task 3
↓
Finish
```

The next task starts only after the previous task finishes.

---

### What is Asynchronous Programming?

Asynchronous (async) programming allows tasks to pause while waiting and enables other tasks to run during that time.

Flow:

```text
Task 1 waiting
        ↓
Task 2 running
        ↓
Task 3 running
        ↓
Task 1 resumes
```

This makes waiting time useful and improves overall application throughput.

---

### async Functions

Functions defined using the `async` keyword are asynchronous functions.

Example:

```python
async def llm():
    pass
```

These functions may pause while waiting for external resources such as APIs or databases.

---

### await

The `await` keyword pauses the current async function until the awaited operation finishes.

Example:

```python
response = await client.aio.models.generate_content(
    model=model,
    contents=prompt
)
```

`await` does not block the entire program. It only pauses the current task.

---

### Event Loop

The event loop manages asynchronous tasks.

Responsibilities:

* Start tasks.
* Pause tasks that are waiting.
* Execute other available tasks.
* Resume paused tasks when they are ready.

Flow:

```text
Event Loop
    ↓
Run Task
    ↓
Task waits
    ↓
Run another task
    ↓
Resume previous task
```

---

### asyncio.run()

`asyncio.run()` creates an event loop and executes an asynchronous function.

Example:

```python
asyncio.run(main())
```

Without `asyncio.run()`, async functions are not executed.

---

### asyncio.sleep()

Async code should use:

```python
await asyncio.sleep(2)
```

instead of:

```python
time.sleep(2)
```

#### time.sleep()

Blocks the entire program.

```text
Program
↓
Wait
↓
Continue
```

---

#### asyncio.sleep()

Pauses only the current task.

```text
Current Task
↓
Pause
↓
Other Tasks Can Run
```

---

### Concurrent Execution

Multiple asynchronous tasks can run concurrently.

Example:

```python
await asyncio.gather(
    task_1(),
    task_2(),
    task_3()
)
```

This allows tasks to make progress simultaneously while waiting for external operations.

---

### Async LLM Calls

Gemini asynchronous calls use:

```python
response = await client.aio.models.generate_content(
    model=model,
    contents=prompt
)
```

The request is sent to Gemini and the current task pauses until a response is received.

---

### Retry Logic in Async Code

Retries should use:

```python
await asyncio.sleep(2)
```

instead of:

```python
time.sleep(2)
```

This prevents blocking the event loop.

---

### Why Async Matters for AI Applications

AI applications spend most of their time waiting for:

* API responses
* Database queries
* File operations
* Network requests

Asynchronous programming makes these waiting periods more efficient by allowing other tasks to execute.

---

## Key Takeaways

* Synchronous code executes one task at a time.
* Asynchronous code allows tasks to pause and resume.
* `async` defines asynchronous functions.
* `await` pauses the current task until the result is available.
* The event loop manages asynchronous tasks.
* `asyncio.run()` starts the event loop.
* `asyncio.sleep()` should be used instead of `time.sleep()` in async programs.
* Multiple tasks can run concurrently using `asyncio.gather()`.
* Async programming improves throughput but does not make a single API response faster.
* Async programming is especially useful for APIs and AI applications.

