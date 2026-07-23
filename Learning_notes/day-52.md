# Day 52 / 365 – Manual Function Calling & Complete Tool-Calling Loop

## 🎯 Objective

Today I learned how to implement the complete manual tool-calling loop using the Google Gemini API. Instead of allowing the SDK to automatically execute tools, I manually controlled the entire execution flow, enabling a production-ready AI agent architecture.

---

# Why Manual Function Calling?

Large Language Models (LLMs) cannot directly execute Python code. They can only decide **when** a tool is needed and request the application to execute it.

The application is responsible for:

1. Executing the requested function.
2. Returning the result to the LLM.
3. Receiving the final response from the LLM.

This process is called the **Tool-Calling Loop**.

---

# Automatic vs Manual Function Calling

## Automatic Function Calling

```text
User
 │
 ▼
Gemini
 │
 ▼
SDK executes tool automatically
 │
 ▼
Tool
 │
 ▼
Gemini
 │
 ▼
Answer
```

### Advantages

- Very simple to implement.
- Minimal code.
- Suitable for prototypes.

### Disadvantages

- No control over execution.
- Cannot display custom UI states.
- Difficult to debug.
- Limited flexibility.
- Not ideal for production systems.

---

## Manual Function Calling

```text
User
 │
 ▼
Gemini
 │
 ▼
Returns Function Call
 │
 ▼
Python executes Tool
 │
 ▼
Tool Result
 │
 ▼
Gemini
 │
 ▼
Final Response
```

### Advantages

- Complete control over execution.
- Better debugging.
- Custom UI updates.
- Logging and monitoring.
- Retry failed tools.
- Validate tool arguments.
- Production-ready architecture.

---

# Complete Tool-Calling Loop

## Step 1 — User Prompt

The user sends a request.

```text
What are today's AI news headlines?
```

---

## Step 2 — Send Request to Gemini

The application sends:

- System Prompt
- User Prompt
- Available Tool Definitions

Gemini decides whether a tool is required.

---

## Step 3 — Gemini Requests a Tool

Instead of answering immediately, Gemini returns:

```text
Function:
search_web

Arguments:
query = "Today's AI news"
```

Gemini does **not** execute the tool.

---

## Step 4 — Detect the Function Call

The application checks whether Gemini requested a tool.

```python
if response.function_calls:
```

If no tool is requested:

```text
Return the response immediately.
```

Otherwise:

Continue with tool execution.

---

## Step 5 — Execute the Tool

Extract the function arguments.

Example:

```text
query = "Today's AI news"
```

Execute:

```python
search_web(query)
```

This performs the Tavily search.

---

## Step 6 — Receive Tool Result

The external API returns:

```text
Search Results
```

Example:

- Latest AI announcements
- OpenAI updates
- Google Gemini news

---

## Step 7 — Return Tool Result to Gemini

Convert the Python output into a Function Response.

```text
Function Response

↓

Gemini
```

Now Gemini has:

- Original Question
- Function Call
- Tool Output

---

## Step 8 — Generate Final Response

Gemini analyses the returned data and generates a complete answer for the user.

---

# Full Workflow

```text
                User
                  │
                  ▼
            User Prompt
                  │
                  ▼
               Gemini
                  │
        Needs External Tool?
          │              │
          │              │
         No             Yes
          │              │
          ▼              ▼
     Final Answer    Function Call
                           │
                           ▼
                  Execute Python Function
                           │
                           ▼
                     Tavily Search
                           │
                           ▼
                     Search Results
                           │
                           ▼
                Return Function Response
                           │
                           ▼
                         Gemini
                           │
                           ▼
                    Final Response
```

---

# Production UI Workflow

One of the biggest advantages of manual tool calling is complete UI control.

```text
🤔 Thinking...

↓

🌐 Searching the Web...

↓

📄 Reading Sources...

↓

🧠 Analysing Results...

↓

✍️ Generating Response...

↓

✅ Final Answer
```

This creates a much more transparent and professional user experience.

---

# Why This Matters

Manual function calling enables:

- Full control over tool execution.
- Better debugging.
- Improved observability.
- Error handling.
- Retry mechanisms.
- Logging.
- Analytics.
- Dynamic user interfaces.
- Multi-tool orchestration.

These capabilities are essential for building production-grade AI agents.

---

# Applications in Envora

The same execution loop can be reused for every future tool.

Examples:

- search_web()
- analyze_pdf()
- vector_search()
- search_company()
- calculate_carbon()
- generate_esg_report()
- database_search()
- retrieve_documents()

Each tool follows exactly the same lifecycle.

---

# Key Concepts Learned

- Function Calling
- Tool Declaration
- Function Arguments
- Function Execution
- Function Response
- Conversation History
- Multi-turn Tool Calling
- Agent Loop
- Tool Orchestration
- Manual Execution

---

# Files Modified

## Primary File

```
llm.py
```

Major changes:

- Replaced automatic tool calling.
- Added manual tool detection.
- Executed Python functions manually.
- Returned tool responses to Gemini.
- Preserved retry logic.
- Preserved metrics.
- Preserved logging.
- Preserved response models.

---

## Supporting Files

```
tools/web_search.py
```

Used to execute Tavily searches.

```
config.py
```

Provides Gemini and Tavily clients.

```
logger_config.py
```

Logs tool execution.

```
metrics.py
```

Tracks token usage and cost.

---

# Today's Deliverables

- Understood the complete tool-calling lifecycle.
- Learned how Gemini requests external tools.
- Learned how Python executes requested functions.
- Learned how tool results are returned to Gemini.
- Built the foundation for production AI agents.
- Prepared Envora for multiple integrated tools.

---

# Summary

Today I learned one of the most important concepts in agentic AI: the manual tool-calling loop. Rather than relying on automatic SDK behaviour, I now understand how to control every stage of tool execution—from receiving a function request, executing Python code, returning results to the LLM, and generating the final response. This architecture provides the flexibility, observability, and scalability required to build production-grade AI systems capable of orchestrating multiple tools, APIs, and reasoning workflows.
