# Day 010 - Logging and Structured Logging

## Objective

Learn how to monitor and debug applications using Python's logging module and implement structured logging in the Gemini application.

---

## Topics Covered

### What is Logging?

Logging is the process of recording events that occur while an application is running.

Examples:

* Application started
* Sending request to Gemini
* Response received
* Errors and warnings

Logging helps developers understand the flow of the application and diagnose problems.

---

### Why Use Logging?

Using `print()` statements is useful for simple programs, but larger applications require better monitoring.

Benefits of logging:

* Easier debugging
* Better error tracking
* Records application flow
* Provides timestamps for events
* Improves maintainability

---

### Logging Levels

Python logging supports different levels of severity.

#### INFO

Used for normal application events.

Example:

```python
logger.info("Application started")
```

---

#### WARNING

Used for unexpected situations that are not critical.

Example:

```python
logger.warning("API response is slow")
```

---

#### ERROR

Used when something fails.

Example:

```python
logger.error("Failed to connect to Gemini")
```

---

#### DEBUG

Used for detailed information while debugging.

Example:

```python
logger.debug("Response object received")
```

---

### Configuring Logging

The logging module can be configured using:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

---

### Understanding the Format

```python
"%(asctime)s - %(levelname)s - %(message)s"
```

#### %(asctime)s

Displays the date and time.

Example:

```text
2026-06-10 22:41:51
```

---

#### %(levelname)s

Displays the type of log message.

Examples:

* INFO
* WARNING
* ERROR
* DEBUG

---

#### %(message)s

Displays the actual message written by the developer.

Example:

```text
Sending request to Gemini
```

---

### Creating a Logger Object

```python
logger = logging.getLogger(__name__)
```

A logger object is responsible for generating log messages.

`__name__` is automatically replaced with the current module name.

Examples:

```text
main
llm
config
```

---

### Structured Logging

Instead of:

```python
print("Sending request")
```

Use:

```python
logger.info("Sending request to Gemini")
```

Instead of:

```python
print("Request failed")
```

Use:

```python
logger.error("Request failed")
```

Structured logging provides more information and makes debugging easier.

---

### Logging Application Flow

Example:

```text
Application Started
        ↓
Sending Request to Gemini
        ↓
Response Received
        ↓
Application Completed
```

Example output:

```text
2026-06-10 22:41:51 - INFO - Application started
2026-06-10 22:41:53 - INFO - Sending request to Gemini
2026-06-10 22:41:54 - INFO - Response received successfully
```

---

### Retry Logic

When an exception occurs, the application retries the request.

Example:

```python
for attempt in range(3):
```

Benefits:

* Handles temporary failures
* Improves reliability
* Reduces application crashes

---

### Rich Loading Spinner

The Rich library provides a loading animation while Gemini processes the request.

Example:

```python
with console.status("Thinking..."):
```

This improves the user experience and indicates that the application is still running.

---

### Application Structure

```text
main.py
    ↓
llm.py
    ↓
Gemini API
    ↓
Response
```

Logging records events throughout the execution process.

