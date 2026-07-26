# Day 55 / 365 – Handle Tool Errors Gracefully

## 🎯 Objective

Today I improved my AI agent by implementing **graceful error handling** for tool execution.

Instead of allowing the application to crash when a tool fails, my agent now catches errors, provides meaningful feedback, and continues operating whenever possible.

Reliable AI systems should expect tools to fail and recover gracefully.

---

# Why Tool Errors Happen

AI tools often depend on external resources such as:

- Internet APIs
- Local files
- Databases
- Cloud services

These resources are not always available.

Common failures include:

- Missing files
- Invalid file paths
- Network issues
- API failures
- Permission errors
- Unexpected exceptions

Without proper error handling, a single tool failure can terminate the entire application.

---

# Previous Workflow

Previously, if a tool encountered an error, the application stopped executing.

```text
User

↓

Gemini

↓

Tool Call

↓

Tool Error

↓

Application Crashes
```

This creates a poor user experience.

---

# Improved Workflow

After implementing graceful error handling:

```text
User

↓

Gemini

↓

Tool Call

↓

Execute Tool

↓

Did an Error Occur?

├── No
│      ↓
│  Return Result
│
└── Yes
       ↓
Catch Exception

↓

Create Friendly Error Message

↓

Gemini

↓

Respond to User
```

The AI continues running even if one tool fails.

---

# What is Exception Handling?

Python provides **exceptions** to represent runtime errors.

Instead of allowing exceptions to terminate the application, they can be handled safely.

Example structure:

```python
try:
    # Execute tool
except Exception:
    # Handle error
```

This allows the program to recover instead of crashing.

---

# How Tool Error Handling Works

When Gemini requests a tool:

```text
Gemini

↓

Tool

↓

Success?
```

If successful:

```text
Tool Result

↓

Gemini

↓

Final Response
```

If unsuccessful:

```text
Tool Error

↓

Catch Exception

↓

Return Error Information

↓

Gemini

↓

Helpful Response
```

---

# Example: Missing PDF

Suppose the user requests:

```text
Summarise report.pdf
```

But the file does not exist.

Instead of:

```text
FileNotFoundError

Application Stops
```

The application should return:

```text
Unable to open the requested PDF file.

Please check that the file exists and try again.
```

The agent continues running normally.

---

# Example: Web Search Failure

Possible causes:

- Internet unavailable
- API timeout
- Invalid API key

Instead of exposing internal errors, the application can return:

```text
The web search service is currently unavailable.

Please try again later.
```

---

# Why Graceful Errors Matter

Good AI systems should:

- Never crash because of one tool
- Inform the user clearly
- Continue processing future requests
- Hide unnecessary technical details
- Make debugging easier

---

# Error Handling Workflow

```text
Execute Tool

↓

Exception?

↓

No

↓

Return Result

↓

Gemini

↓

Answer
```

or

```text
Execute Tool

↓

Exception

↓

Catch Error

↓

Generate Friendly Message

↓

Gemini

↓

Answer User
```

---

# Types of Tool Errors

Some common exceptions include:

## File Errors

- FileNotFoundError
- PermissionError

---

## Network Errors

- ConnectionError
- TimeoutError

---

## Validation Errors

- Invalid input
- Missing arguments

---

## Unexpected Errors

- RuntimeError
- ValueError
- TypeError

Even unexpected exceptions should be handled safely.

---

# Error Recovery

A production AI agent should recover whenever possible.

Example:

```text
Web Search Failed

↓

Notify User

↓

Application Continues

↓

Next Prompt Works Normally
```

The agent remains available instead of terminating.

---

# Good Error Messages

Avoid exposing raw Python exceptions.

Poor example:

```text
Traceback...
FileNotFoundError...
```

Better example:

```text
Unable to locate the requested file.

Please verify the file path and try again.
```

Users should receive actionable information rather than technical stack traces.

---

# Where Error Handling Happens

The execution flow now becomes:

```text
User

↓

Gemini

↓

Tool Request

↓

Execute Tool

↓

Try

↓

Success?

├── Return Result
│
└── Catch Exception

↓

Friendly Error

↓

Gemini

↓

Final Response
```

---

# Files Updated

```
llm.py
```

Updated to safely execute tools and handle exceptions.

---

```
tools/search.py
```

Improved handling for web search failures.

---

```
tools/pdf_reader.py
```

Improved handling for missing or invalid PDF files.

---

# Real-World Importance

Graceful error handling is used in:

- AI Agents
- Backend APIs
- FastAPI applications
- LangChain
- LangGraph
- Enterprise software
- Cloud services
- Production automation systems

Reliable software assumes failures will occur and is designed to recover from them.

---

# Skills Learned

Today I learned:

- Python exception handling
- try / except blocks
- Tool error recovery
- Creating user-friendly error messages
- Preventing application crashes
- Building resilient AI agents
- Improving user experience
- Defensive programming

---

# Key Takeaways

- External tools can fail unexpectedly.
- Never assume a tool will always succeed.
- Catch exceptions before they crash the application.
- Return meaningful messages instead of raw errors.
- Graceful recovery makes AI systems more reliable and production-ready.

---

# Today's Deliverables

- Added exception handling around tool execution.
- Prevented the AI agent from crashing when a tool fails.
- Returned clear, user-friendly error messages.
- Tested successful and failed tool executions.
- Improved the resilience of the AI agent.

---

# Summary

Today I enhanced my AI agent by implementing graceful error handling for tool execution. Instead of allowing exceptions from web searches or PDF processing to terminate the application, the agent now catches errors, generates meaningful feedback, and continues operating normally. This makes the system more robust, user-friendly, and aligned with production-quality software engineering practices, where failures are anticipated and handled safely.
