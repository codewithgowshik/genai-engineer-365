# Day 50 — Function (Tool) Calling with Tavily Web Search

## Objective

Today's goal is to understand what **tool (function) calling** is and prepare Envora to use external tools.

Instead of only generating text, an LLM can decide to use a function to retrieve real-world information.

---

# What is Tool Calling?

A Large Language Model (LLM) is excellent at reasoning and generating text, but it has limitations.

For example, it cannot:

- Search today's news
- Access live ESG regulations
- Read files from your computer
- Query a database
- Perform calculations using external systems

To overcome these limitations, we give the LLM access to **tools**.

A tool is simply a Python function that performs a specific task.

Example:

```python
def search_web(query: str):
    ...
```

The LLM can request this function whenever it needs information from the internet.

---

# Why Do We Need Tools?

Without tools, the LLM only answers using its training knowledge.

Example:

User:
> What are the latest UK sustainability reporting regulations?

Without a tool:

- The model may provide outdated information.

With a web search tool:

- The model searches the web.
- Reads the latest information.
- Produces an accurate response.

---

# Our First Tool

Today's tool is:

```python
search_web(query)
```

Purpose:

- Search the internet
- Return search results
- Allow Gemini to access current information

---

# Project Structure

```
src/
│
├── config.py
├── web_search.py
├── main.py
└── .env
```

---

# Storing API Keys

API keys should never be hardcoded inside Python files.

Instead, create a `.env` file.

Example:

```env
API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Python loads these values securely.

---

# Loading Environment Variables

```python
from dotenv import load_dotenv

load_dotenv()
```

Purpose:

Reads the `.env` file and makes the variables available to Python.

Without this line:

```python
os.getenv("TAVILY_API_KEY")
```

would return:

```python
None
```

---

# Reading Environment Variables

```python
os.getenv("TAVILY_API_KEY")
```

Purpose:

Retrieve the API key stored inside the environment.

Example:

```env
TAVILY_API_KEY=tvly-xxxxxxxx
```

returns

```python
"tvly-xxxxxxxx"
```

---

# Creating the Tavily Client

```python
from tavily import TavilyClient

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)
```

Purpose:

Create a connection between our application and Tavily's search service.

Just like:

```python
client = genai.Client(...)
```

creates a connection to Gemini.

---

# Building the Tool

```python
def search_web(query: str):

    response = tavily_client.search(
        query=query,
        search_depth="advanced",
        max_results=5,
    )

    return response
```

This function:

1. Receives a search query.
2. Sends it to Tavily.
3. Receives the search results.
4. Returns the response.

---

# Understanding Each Parameter

## query

```python
query=query
```

The search phrase.

Example:

```python
search_web(
    "Latest CSRD regulations"
)
```

---

## search_depth

```python
search_depth="advanced"
```

Performs a deeper, more comprehensive search instead of a quick lookup.

---

## max_results

```python
max_results=5
```

Limits the search results to five items.

---

# Testing the Tool

Before connecting the tool to Gemini, test it independently.

Example:

```python
result = search_web(
    "Latest CSRD sustainability reporting requirements"
)

print(result)
```

Expected output:

```python
{
    "results": [
        {
            "title": "...",
            "url": "...",
            "content": "..."
        }
    ]
}
```

Testing independently ensures:

- API key is correct.
- Tavily is working.
- Internet connection is working.
- The function behaves correctly.

---

# Current Architecture

Today we built this:

```
User
 │
 ▼
search_web()
 │
 ▼
Tavily API
 │
 ▼
Search Results
```

This is **API integration**.

---

# What We Have NOT Built Yet

We have **not** implemented tool calling.

Currently:

```python
result = search_web(...)
```

We manually call the function.

---

# Actual Tool Calling

The complete tool-calling workflow will be:

```
User
 │
 ▼
Gemini
 │
 ▼
Gemini decides:
"I need search_web()"
 │
 ▼
Python executes search_web()
 │
 ▼
Tavily API
 │
 ▼
Search Results
 │
 ▼
Gemini
 │
 ▼
Final Response
```

Notice the difference:

Today:

- The developer calls the function.

Tool Calling:

- Gemini decides when to call the function.

---

# Difference Between API Integration and Tool Calling

## API Integration

```
Python
 │
 ▼
search_web()
 │
 ▼
Tavily
```

The developer chooses when to execute the function.

---

## Tool Calling

```
User
 │
 ▼
Gemini
 │
 ▼
Function Request
 │
 ▼
Python executes function
 │
 ▼
Tool Result
 │
 ▼
Gemini
 │
 ▼
Answer
```

The LLM decides whether a tool is required.

---

# Key Concepts Learned Today

- What a tool (function) is.
- Why LLMs need external tools.
- API integration with Tavily.
- Using `.env` to store API keys securely.
- Loading environment variables.
- Creating reusable clients in `config.py`.
- Building a reusable `search_web()` function.
- Testing tools independently before integrating with an LLM.
- The difference between API integration and tool calling.

---

# Key Takeaways

- A tool is simply a Python function.
- Tavily provides live internet search capability.
- `config.py` should initialize reusable clients.
- `.env` keeps API keys secure.
- Always verify a tool works before connecting it to an LLM.
- Today's work prepares Envora for real tool calling.
- In the next step, Gemini will decide when to call `search_web()` automatically.

---

# Summary

Today we built Envora's first external tool:

**`search_web()`**

This tool enables live internet searches using Tavily.

Although Gemini is **not yet** calling the function automatically, we now have a working, reusable tool that is ready to be integrated into Gemini's function-calling system in the next lesson.
