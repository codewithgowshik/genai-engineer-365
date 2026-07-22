# Day 51 / 365 – Function (Tool) Calling with Gemini

## 🎯 Objective

Today I learned how Large Language Models (LLMs) interact with external tools. Instead of relying only on their internal knowledge, they can decide when to use external functions such as web search, databases, APIs, or calculators.

---

# What is Function (Tool) Calling?

Function calling allows an LLM to request the execution of external code whenever it needs information or capabilities that it does not possess.

The model **does not execute Python code itself.**

Instead, it tells the application:

> "Please execute this function for me."

The application runs the function and returns the result back to the model.

---

# Overall Architecture

```text
                User
                  │
                  ▼
              Gemini LLM
                  │
      ┌───────────┴───────────┐
      │                       │
Need Tool?               No Tool Needed
      │                       │
      ▼                       ▼
Python Function         Generate Answer
(search_web)
      │
      ▼
Tavily API
      │
      ▼
Search Results
      │
      ▼
Gemini LLM
      │
      ▼
Final Response
```

---

# Automatic Function Calling

The Google GenAI SDK provides automatic function calling.

Example:

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        tools=[search_web]
    )
)
```

Here:

- Gemini receives the available tools.
- Gemini decides whether it needs one.
- The SDK automatically executes the Python function.
- The SDK automatically sends the function result back to Gemini.
- Gemini generates the final response.

As developers, we only receive:

```python
response.text
```

---

# How Automatic Function Calling Works

```text
User
 │
 ▼
Gemini
 │
 ▼
Needs Tool?
 │
 ▼
SDK automatically executes search_web()
 │
 ▼
Tavily Search
 │
 ▼
SDK sends result back
 │
 ▼
Gemini
 │
 ▼
Final Answer
```

---

# Limitation of Automatic Function Calling

Automatic tool execution is simple but hides the internal workflow.

The application never knows:

- When Gemini requested the tool
- Which tool Gemini requested
- When the tool starts
- When the tool finishes

Because of this, it is difficult to build professional UI transitions.

Example:

```text
Thinking...
Searching the Web...
Reading Sources...
Generating Answer...
```

The SDK handles those steps internally.

---

# Manual Function Calling

Manual function calling gives the developer complete control.

Instead of allowing the SDK to execute functions automatically:

1. Gemini returns a function call.
2. Python executes the function.
3. Python sends the result back.
4. Gemini generates the final answer.

---

# Manual Workflow

```text
User
 │
 ▼
Gemini
 │
 ▼
Function Call?
 │
 ├── No
 │      │
 │      ▼
 │   Final Answer
 │
 └── Yes
        │
        ▼
Execute Python Function
        │
        ▼
External API
        │
        ▼
Return Result
        │
        ▼
Gemini
        │
        ▼
Final Response
```

---

# Why Manual Function Calling?

Manual execution allows the application to know exactly what is happening.

Benefits:

- Show **Thinking...**
- Show **Searching the Web...**
- Show **Reading Sources...**
- Show **Generating Answer...**
- Log every tool call
- Retry failed tools
- Handle errors
- Add custom business logic
- Support multiple tools

---

# Production Architecture

Current architecture:

```text
User
 │
 ▼
Gemini
 │
 ▼
Automatic Tool Execution
 │
 ▼
Answer
```

Production architecture:

```text
User
 │
 ▼
🤔 Thinking...
 │
 ▼
Gemini
 │
 ▼
Tool Requested?
 │
 ├── No
 │      │
 │      ▼
 │   Final Answer
 │
 └── Yes
        │
        ▼
🌐 Searching the Web...
        │
        ▼
search_web()
        │
        ▼
📄 Reading Sources...
        │
        ▼
🧠 Analysing...
        │
        ▼
Gemini
        │
        ▼
✍️ Generating Response...
        │
        ▼
Answer
```

---

# Why This Matters for Envora

Envora will eventually use multiple tools such as:

- `search_web()`
- `analyze_pdf()`
- `calculate_carbon()`
- `generate_esg_report()`
- `search_company()`
- `extract_tables()`
- `vector_search()`

Manual function calling allows Envora to decide which tool to use while providing users with a transparent, professional workflow.

---

# Today's Key Learnings

- LLMs cannot execute Python code directly.
- Function calling allows an LLM to request external code execution.
- Automatic function calling is easy to implement but hides the execution process.
- Manual function calling provides full control over tool execution and user experience.
- Manual function calling is essential for building production-grade AI agents.

---

# Tomorrow's Plan (Day 52)

## Learn

- Function Declarations
- `response.function_calls`
- `types.FunctionDeclaration`
- `types.Part.from_function_response`
- Multi-turn tool calling
- Manual agent execution loop

## Build

- Replace automatic tool calling with manual execution.
- Build a complete production tool-calling loop.
- Add dynamic agent states:
  - 🤔 Thinking...
  - 🌐 Searching the Web...
  - 📄 Reading Sources...
  - 🧠 Analysing...
  - ✍️ Generating Response...

---

# Summary

Today I moved beyond basic LLM prompting and learned how AI models interact with external tools. While automatic function calling offers convenience, manual function calling provides complete control over execution, user experience, and scalability. This forms the foundation for building production-grade AI agents capable of orchestrating multiple tools, APIs, and reasoning steps. Tomorrow, I will implement the complete manual function-calling workflow for Envora.
