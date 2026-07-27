# Day 56 / 365 – Tool Calling vs Prompting (Multi-Tool AI Agent)

## 🎯 Objective

Today I explored the difference between **prompting** and **tool calling**, two fundamental concepts in modern AI agents.

The original roadmap for Day 56 recommended building a **Calculator Tool** and a **Weather Tool** to demonstrate how Large Language Models (LLMs) interact with external functions. However, I had already implemented more advanced and practical tools in my AI agent:

- Web Search Tool
- PDF Analysis Tool

Instead of creating temporary demo tools, I adapted the exercise by using these existing tools. Although the implementation differed from the roadmap, the learning objective remained exactly the same.

By replacing the calculator and weather examples with my own production-oriented tools, I was able to understand the same concepts while continuing to improve my main AI project rather than building features that would later be discarded.

This exercise helped me understand how an LLM determines whether it can answer a question directly or whether it needs to invoke an external tool to retrieve additional information.

---

# Why I Swapped the Original Exercise

The roadmap suggested:

- Calculator Tool
- Weather Tool

These tools are commonly used because they are simple examples for learning tool calling.

However, my AI agent had already progressed beyond those examples. It already supports:

- Real-time web search
- PDF document analysis
- Tool argument validation using Pydantic
- Graceful tool error handling

Building another calculator or weather tool would have repeated concepts I had already learned.

Instead, I decided to apply the same learning objectives using my own tools.

This approach allowed me to:

- Continue improving my AI agent.
- Learn the exact same tool-calling concepts.
- Build experience with real-world AI applications instead of isolated demonstrations.

---

# What is Prompting?

Prompting is the simplest interaction with an LLM.

The user provides a prompt, and the model generates a response using only its internal knowledge.

No external resources are accessed.

Example:

```text
User:
What is Artificial Intelligence?
```

Workflow:

```text
User

↓

LLM

↓

Generate Response

↓

Return Answer
```

Everything happens inside the language model.

---

# Characteristics of Prompting

Prompting relies entirely on the knowledge stored within the model during training.

It works well for:

- Definitions
- Explanations
- Brainstorming
- Writing
- Programming help
- General reasoning

However, prompting has limitations.

The model cannot:

- Access today's news
- Read local files
- Query databases
- Call APIs
- Retrieve company documents
- Access private information

---

# What is Tool Calling?

Tool calling extends the capabilities of an LLM by allowing it to interact with external systems.

Instead of immediately generating an answer, the model first determines whether additional information is required.

If so, it generates a structured tool request.

The application executes the requested tool.

The tool returns information.

Finally, the LLM generates a response using both its reasoning ability and the retrieved information.

Workflow:

```text
User

↓

Gemini

↓

Generate Tool Call

↓

Python Executes Tool

↓

Tool Result

↓

Gemini

↓

Final Response
```

---

# Why Tool Calling is Necessary

LLMs are excellent at reasoning, but they are not connected to the outside world by default.

For example:

Question:

```text
What are today's AI news headlines?
```

The model cannot reliably answer this from memory.

Instead, it needs an external source.

Likewise:

```text
Summarise this PDF.
```

The model cannot read files stored on my computer.

A PDF reader tool is required.

Tool calling bridges this gap between reasoning and external information.

---

# Prompting vs Tool Calling

| Prompting | Tool Calling |
|-----------|--------------|
| Uses internal knowledge | Uses external resources |
| No external execution | Executes Python functions |
| Cannot access live data | Retrieves real-time information |
| Cannot read local files | Can analyse uploaded documents |
| No API calls | Can call APIs |
| Fast | Slightly slower |
| Simple workflow | Multi-step workflow |

---

# My AI Agent

Instead of using the calculator and weather examples from the roadmap, I used the tools already integrated into my project.

## Web Search Tool

Purpose:

Retrieve real-time information from the internet.

Example prompts:

- Latest AI news
- Current market trends
- Recent technology updates
- Industry announcements

Whenever Gemini needs information that is constantly changing, it selects the web search tool.

---

## PDF Analysis Tool

Purpose:

Read uploaded PDF documents.

Extract text.

Answer questions based on document contents.

Example prompts:

- Summarise this sustainability report.
- Explain the ESG strategy.
- What are the company's Net Zero targets?
- List all future sustainability goals.

Whenever Gemini needs information from a user-provided document, it selects the PDF tool.

---

# Why My Replacement Makes Sense

Although the roadmap suggested building two demonstration tools, my existing tools already demonstrate the same behaviour.

Calculator Tool demonstrates:

- External function execution.

My Web Search Tool demonstrates:

- External function execution.

Weather Tool demonstrates:

- Accessing external information.

My PDF Tool demonstrates:

- Accessing external information from local documents.

Both approaches teach the same underlying architecture.

The only difference is that my implementation solves real-world problems rather than simple demonstrations.

---

# My Current Architecture

```text
                    User
                      │
                      ▼
                   Gemini
                      │
          Does Gemini Need a Tool?
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
Direct Response              Tool Request
                                      │
                       ┌──────────────┴──────────────┐
                       │                             │
                       ▼                             ▼
                 search_web()             extract_pdf_text()
                       │                             │
                       └──────────────┬──────────────┘
                                      ▼
                               Tool Result
                                      │
                                      ▼
                                   Gemini
                                      │
                                      ▼
                               Final Response
```

---

# How Gemini Chooses a Tool

The decision process is based on the user's request.

Example:

User:

```text
Explain Machine Learning.
```

Gemini already knows the answer.

Result:

```text
No Tool Needed
```

---

User:

```text
Latest AI news.
```

Gemini requires real-time information.

Result:

```text
search_web()
```

---

User:

```text
Summarise this sustainability report.
```

Gemini needs to read a document.

Result:

```text
extract_pdf_text()
```

---

# Complete Tool Calling Lifecycle

My AI agent now follows this workflow:

```text
User Prompt

↓

Gemini

↓

Analyse User Intent

↓

Does a Tool Need to be Called?

↓

Yes

↓

Generate Tool Call

↓

Validate Arguments

↓

Execute Tool

↓

Receive Tool Result

↓

Gemini Generates Final Response

↓

Return Response
```

If no tool is required:

```text
User Prompt

↓

Gemini

↓

Generate Response

↓

Return Response
```

---

# Benefits of Multiple Tools

Supporting multiple tools makes the AI agent significantly more capable.

Instead of relying only on language generation, it can combine:

- Internal reasoning
- Live web information
- Local document understanding

This architecture can easily be extended with additional tools in the future.

---

# Possible Future Tools

The same architecture could support:

- SQL Database Search
- Vector Database (RAG)
- Email Sender
- Calendar Integration
- File Manager
- Image Analysis
- Code Execution
- CRM Integration

Each new capability follows the same tool-calling workflow.

---

# Real-World Applications

Modern AI assistants use tool calling extensively.

Examples include:

- ChatGPT
- Claude
- Google Gemini
- GitHub Copilot
- Cursor
- LangChain Agents
- LangGraph
- Enterprise AI Assistants

The architecture I implemented follows the same general design principles used by these systems.

---

# Skills Learned

Today I learned:

- The difference between prompting and tool calling.
- Why LLMs require external tools.
- How Gemini decides whether to call a tool.
- Multi-tool AI agent architecture.
- Tool selection based on user intent.
- End-to-end tool execution workflow.
- How to adapt generic learning exercises to real-world projects.
- Why building production-oriented tools provides greater long-term value than isolated demonstrations.

---

# Key Takeaways

- Prompting uses only the LLM's internal knowledge.
- Tool calling extends the capabilities of an LLM.
- The model decides when external information is required.
- Python executes the requested tool.
- The tool result is returned to the model before the final response is generated.
- The calculator and weather examples from the roadmap taught the same concepts as my Web Search Tool and PDF Analysis Tool.
- Adapting the exercise allowed me to reinforce my own AI project while achieving the same learning outcomes.

---

# Today's Deliverables

- Completed the learning objective for tool calling vs prompting.
- Replaced the roadmap's Calculator Tool with my existing Web Search Tool.
- Replaced the roadmap's Weather Tool with my existing PDF Analysis Tool.
- Demonstrated direct LLM responses.
- Demonstrated web search tool execution.
- Demonstrated PDF analysis tool execution.
- Validated the complete multi-tool workflow.
- Strengthened the architecture of my AI agent instead of creating temporary demo tools.

---

# Summary

Today I studied the difference between prompting and tool calling by applying the concepts to my own AI agent. Although the original roadmap recommended implementing a Calculator Tool and a Weather Tool, I adapted the exercise by replacing them with my already implemented Web Search Tool and PDF Analysis Tool. These tools demonstrate the same principles of external function execution while providing practical value for my project. Through this exercise, I strengthened my understanding of tool selection, multi-tool workflows, and the architecture used by modern AI agents, while continuing to build features that directly contribute to my long-term project.
