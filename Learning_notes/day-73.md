# Day 73 / 365 — Context Windows & Temperature

## Objective

Today I learned about context windows and temperature in Large Language Models (LLMs). I also built a temperature sweep experiment using the Gemini API to observe how changing temperature affects model output.

---

## Learning

### Context Windows

A **context window** is the maximum amount of tokenized information that an LLM can process and consider during a generation request. Context is measured in **tokens**, not simply words.

A context can contain user input, previous conversation, system instructions, other information provided to the model, and generated output — depending on the model.

```text
Context Window
├── Input Tokens
├── Previous Context
└── Output Tokens
```

LLMs do not have unlimited context. When the amount of information becomes larger than the model's supported context window, the application needs to manage the context.

Context windows are especially important when working with:

- Long conversations
- Large documents
- RAG systems
- Chat applications
- Long prompts
- Large amounts of retrieved information

The basic relationship is:

```text
Human Text
   ↓
Tokenizer
   ↓
Tokens
   ↓
Context Window
```

A longer piece of text generally requires more tokens, although the exact number depends on the tokenizer.

### Temperature

Temperature is a generation parameter that affects how the model samples the next token from its probability distribution.

In simple terms:

```text
Low Temperature   → More predictable output
High Temperature  → More varied output
```

> Temperature affects generation **behaviour**, not the model's underlying **knowledge**.

- At a **lower** temperature, the model tends to favour higher-probability tokens more strongly. This generally makes the output more predictable, consistent, and less varied.
- At a **higher** temperature, lower-probability tokens have more opportunity to be selected. This generally makes the output more varied, creative, and less predictable.

Higher temperature does not automatically mean better output. Too much randomness can sometimes make responses less coherent.

Temperature does **not**:
- Train the model
- Add knowledge to the model
- Make the model smarter
- Change its learned parameters

Instead, temperature affects how the model chooses between possible next tokens during generation.

### How Sampling Works

An LLM predicts the next token based on the current context.

For example, given the prompt:

> "The cat is"

The model may assign different probabilities to possible next tokens:

| Next Token | Probability Level |
|---|---|
| sleeping | High |
| hungry | Medium |
| running | Lower |
| flying | Very low |

The model then uses its sampling configuration to select a token. After selecting a token, that token becomes part of the context, and the model predicts another token. This process continues until generation stops.

The model produces numerical scores called **logits** for possible next tokens:

```text
Token A → Score
Token B → Score
Token C → Score
Token D → Score
```

These scores are converted into probabilities, for example:

| Token | Probability |
|---|---|
| Token A | 70% |
| Token B | 20% |
| Token C | 7% |
| Token D | 3% |

Temperature changes how concentrated or spread out this probability distribution becomes during sampling.

**Low Temperature:**
```text
Low Temperature
   ↓
More concentrated probability distribution
   ↓
High-probability tokens are strongly favoured
   ↓
More predictable output
```

**High Temperature:**
```text
High Temperature
   ↓
Flatter probability distribution
   ↓
Lower-probability tokens have more opportunity
   ↓
More varied output
```

---

## Experiment: Temperature Sweep (Gemini API)

A **temperature sweep** means testing the same prompt at multiple temperature values. The important rule is to keep the prompt, model, and other settings the same while changing only the temperature.

For this experiment, I tested:

- 0.0
- 0.25
- 0.5
- 0.75
- 1.0

The experiment kept the prompt and model the same while changing only the temperature.

### Results

| Temperature | Output |
|---|---|
| 0.0 | Elara Vance, a |
| 0.25 | Elara Vance, a history major |
| 0.5 | Elara Vance considered herself a cartographer |
| 0.75 | Elara was a creature of habit |
| 1.0 | Elara considered herself a connoisseur of |

### Comparison

| Temperature | Output | Observation |
|---|---|---|
| 0.0 | Elara Vance, a | More conservative |
| 0.25 | Elara Vance, a history major | Slightly more specific |
| 0.5 | Elara Vance considered herself a cartographer | More varied |
| 0.75 | Elara was a creature of habit | Different direction |
| 1.0 | Elara considered herself a connoisseur of | More varied |

### Observations

The prompt remained the same, but the output changed as the temperature changed.

- At **0.0**, the output was more conservative and predictable.
- At **0.25**, the output became slightly more varied.
- At **0.5**, the model produced a different and more creative continuation.
- At **0.75**, it produced another distinct direction.
- At **1.0**, it produced another varied continuation.

This experiment demonstrated that temperature influences the model's sampling behaviour.

> The experiment does **not** mean that higher temperature always produces better or more creative writing. It means that changing temperature changes the probability distribution used during sampling, which can lead to different outputs.

The exact behaviour depends on the model, prompt, temperature, other generation settings, and sampling process.

At lower temperatures, outputs generally become more predictable. At higher temperatures, outputs generally become more variable.

```text
0.0 ───── 0.25 ───── 0.5 ───── 0.75 ───── 1.0
Predictable                          More varied
```

---

## When to Use Which Temperature

| Use Case | Recommended Temperature |
|---|---|
| Structured responses | Lower |
| Classification | Lower |
| Information extraction | Lower |
| Consistent formatting | Lower |
| Predictable workflows | Lower |
| Brainstorming | Higher |
| Creative writing | Higher |
| Story ideas | Higher |
| Marketing ideas | Higher |
| Generating multiple alternatives | Higher |

> The appropriate temperature depends on the model and application.

---

## Context Window vs. Temperature

Context window and temperature are two different concepts.

| Concept | Answers |
|---|---|
| **Context Window** | How much tokenized information can the model consider? |
| **Temperature** | How does the model sample among possible next tokens? |

```text
Context Window → Controls the available context
Temperature    → Controls sampling behaviour
```

---

## Connecting the Dots

This connects with the previous days of learning:

- **Day 71** introduced tokens and token IDs.
- **Day 72** introduced BPE tokenization and token boundaries.
- **Day 73** connects these ideas to LLM generation.

The complete LLM generation flow can be understood as:

```text
Human Text
   ↓
Tokenizer
   ↓
Token Pieces
   ↓
Token IDs
   ↓
Embeddings
   ↓
Transformer
   ↓
Logits
   ↓
Probability Distribution
   ↓
Temperature / Sampling
   ↓
Next Token
   ↓
Updated Context
   ↓
Next Token
   ↓
Repeat...
```

The model continues this process until it reaches a stopping condition.

---

## Reflection

Today I understood how context windows determine how much tokenized information an LLM can consider and why token management matters.

I also observed through my Gemini experiment that changing temperature changes the variability of next-token generation.

---

## Summary

Today I learned two important LLM concepts: **context windows** and **temperature**.

A context window determines how much tokenized information the model can consider, while temperature influences how the model samples the next token.

My Gemini experiment showed that using the same prompt with different temperatures can produce different outputs.

The main generation flow is:

```text
Prompt
   ↓
Tokens
   ↓
Model
   ↓
Logits
   ↓
Temperature
   ↓
Probability Distribution
   ↓
Sampling
   ↓
Next Token
```

**The biggest lesson from today:**

> Context determines how much information the model can work with, while temperature influences how it chooses the next token.
