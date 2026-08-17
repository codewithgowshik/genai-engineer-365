# Day 77 / 365 — Hallucinations & Mitigation

**Date:** Sunday, August 16, 2026  
**Week:** 11 — How LLMs Work I: Tokens & Sampling  
**Phase:** 3 — How LLMs Work + Embeddings & Vector Search  
**Topic:** Why Models Hallucinate  
**Build:** Document a hallucination and a mitigation

---

## Objective

Today I learned why Large Language Models can **hallucinate** — generate information that sounds convincing but is incorrect, unsupported, or fabricated.

I understood that an LLM is fundamentally generating likely token sequences rather than directly querying a database of verified facts.

I also learned how to identify a hallucination and apply a practical mitigation strategy.

---

# Learning

## What Is an LLM Hallucination?

An **LLM hallucination** occurs when a model generates information that is presented as factual but is incorrect, unsupported, or fabricated.

For example:

```text
User:
Who invented the Python programming language?

Model:
Python was invented by James Gosling in 1991.
```

This is incorrect. Python was created by **Guido van Rossum**.

The response can still sound convincing because the model can produce fluent language even when the underlying claim is wrong.

The important distinction is:

```text
Fluent answer ≠ Correct answer
```

---

## Why Do LLMs Hallucinate?

An LLM is fundamentally a **next-token prediction system**.

It learns statistical patterns from its training data and uses those patterns to generate a sequence of tokens.

```text
Prompt
  ↓
Context
  ↓
Predict next token
  ↓
Predict next token
  ↓
Predict next token
  ↓
Complete response
```

The model is not automatically performing a database lookup for every factual statement.

Therefore:

> An LLM can generate a highly plausible statement without having reliable evidence that the statement is true.

---

## Next-Token Prediction

Suppose the model receives:

```text
The first person to walk on the Moon was
```

The model has learned strong associations between this context and:

```text
Neil Armstrong
```

It predicts the next token based on learned patterns.

```text
Context
   ↓
Probability Distribution
   ↓
Most likely next token
   ↓
New context
   ↓
Repeat
```

This mechanism is powerful, but it does not inherently provide a **truth verification mechanism**.

---

## Plausibility vs Truth

One of the most important concepts today is:

```text
Plausible ≠ True
```

An LLM can generate:

```text
"This sounds correct."
```

without necessarily having:

```text
"Evidence that this is correct."
```

Therefore, a confident tone should not automatically be interpreted as evidence of correctness.

---

## Common Types of Hallucinations

### 1. Factual Hallucination

The model gives an incorrect fact.

```text
The Eiffel Tower is located in Berlin.
```

The statement is fluent but factually incorrect.

### 2. Fabricated Sources

The model invents a paper, website, book, or citation.

```text
According to the 2024 study "AI and Human Cognition"
published by the Oxford Institute of Artificial Intelligence...
```

If the study does not actually exist, the citation is fabricated.

### 3. Fabricated People or Events

The model can create plausible-sounding people, organisations, events, or historical details.

```text
Professor David Wilson founded the Institute of Neural Computing in 1987.
```

If there is no such professor or institute, this is a hallucination.

### 4. Incorrect Calculations

LLMs can sometimes produce incorrect arithmetic or reasoning.

```text
37 × 24 = 788
```

The answer may look reasonable but is incorrect.

This is one reason external calculators or programmatic computation are useful for numerical tasks.

### 5. Misinterpreting the User's Context

A model may assume information that the user never provided.

```text
User:
Write a summary of my company.

Model:
Your company has 50 employees and operates in London.
```

If the user never provided those facts, the model has invented information.

---

## Why Does Confidence Not Equal Accuracy?

An LLM can produce language that sounds confident because its objective is to generate a likely sequence of tokens.

It does not inherently have a built-in truth meter.

Therefore:

```text
Confidence of wording
        ≠
Factual accuracy
```

A model might say:

```text
"Absolutely. The answer is..."
```

even when the answer is wrong.

---

# Hallucination Example

Consider:

```text
User:
Who was the first person to receive the Nobel Prize
in Artificial Intelligence in 1955?
```

There is a problem with the premise: there was no Nobel Prize category for Artificial Intelligence in 1955.

A hallucinating model might invent an answer such as:

```text
The first Nobel Prize in Artificial Intelligence was awarded
to Alan Turing in 1955.
```

This contains fabricated information.

A safer response would be:

```text
There was no Nobel Prize category for Artificial Intelligence
in 1955, so the premise of the question is incorrect.
```

This demonstrates an important mitigation:

> **The model should be willing to reject a false premise instead of trying to complete it.**

---

# Hallucination Mitigation

Hallucination cannot simply be solved by telling a model:

```text
"Don't hallucinate."
```

We need techniques that provide the model with better information or constrain its behaviour.

Common mitigation strategies include:

- Grounding
- Retrieval-Augmented Generation (RAG)
- Asking the model to cite sources
- Structured outputs
- Tool use
- External verification
- Restricting the model to provided context
- Human review

---

## Mitigation 1 — Grounding

**Grounding** means providing the model with trusted information that it should use to generate its answer.

Instead of:

```text
Question
   ↓
LLM
   ↓
Answer
```

we can use:

```text
Trusted Information
        ↓
      LLM
        ↓
      Answer
```

For example:

```text
Context:
Python was created by Guido van Rossum.

Question:
Who created Python?
```

The model can answer using the supplied context:

```text
Guido van Rossum.
```

---

## Mitigation 2 — Retrieval-Augmented Generation

RAG combines retrieval with generation.

```text
User Question
      ↓
Retrieve Relevant Documents
      ↓
Relevant Context
      ↓
LLM
      ↓
Grounded Answer
```

Instead of expecting the model to remember everything from training, we retrieve relevant information at query time.

RAG is useful for:

- Company knowledge bases
- Documentation
- University information
- Legal documents
- Internal policies
- Product documentation
- Frequently changing information

---

## Mitigation 3 — Source-Based Prompting

We can explicitly instruct the model to use only the provided information.

```text
Answer the question using only the information provided below.

If the answer cannot be found in the context,
say "I don't have enough information."

Context:
...
```

This creates a constraint:

```text
Available Context
      ↓
LLM
      ↓
Answer only from context
```

This can reduce unsupported claims.

---

## Mitigation 4 — Ask for Evidence

Another strategy is asking the model to provide evidence for its answer.

```text
Answer the question and provide the source
from the supplied documents that supports your answer.
```

The source should be independently verifiable rather than blindly trusting a citation generated by the model.

---

## Mitigation 5 — Tool Use

For tasks where external tools are more reliable than the model itself, use a tool.

```text
Mathematics
   ↓
Calculator

Current information
   ↓
Search / Database

Company data
   ↓
Database

Weather
   ↓
Weather API
```

Instead of asking the LLM to calculate:

```text
123456 × 789
```

we can use a calculator and let the LLM interpret the result.

---

# Build — Document a Hallucination and a Mitigation

## Build Goal

Today's build is:

> **Document one hallucination and one mitigation.**

The goal is not to build a complete RAG system yet.

Instead, create a small experiment:

```text
Hallucination
      ↓
Identify the problem
      ↓
Apply mitigation
      ↓
Compare results
```

---

## Step 1 — Create a Hallucination

Use a prompt that encourages the model to answer something it may not know.

```text
Who was the first Nobel Prize winner in Artificial Intelligence?
```

Record the model's response.

```text
Prompt:
Who was the first Nobel Prize winner in Artificial Intelligence?

Response:
...
```

Then verify whether the claim is actually true.

---

## Step 2 — Identify the Hallucination

Document:

```text
Claim:
...

Why it appears plausible:
...

Why it is incorrect:
...

Correct information:
...
```

The important distinction is:

```text
Model output
      ↓
Verification
      ↓
Truth
```

---

## Step 3 — Apply a Mitigation

Use a grounded prompt:

```text
Answer only using the provided context.

If the answer is not supported by the context,
say "I don't have enough information."

Context:
[trusted information]

Question:
[question]
```

Run the same or related question again.

---

## Step 4 — Compare

| Test | Approach | Result |
|---|---|---|
| A | Normal LLM prompt | Hallucinated / unsupported answer |
| B | Grounded prompt | Refuses or answers using provided evidence |

The objective is to demonstrate that **constraining the model with trusted context can reduce unsupported generation**.

---

# Example Experiment

## Without Grounding

```text
Prompt:
Who invented the XYZ technology in 1982?
```

The model may attempt to provide:

```text
The technology was invented by Dr. John Smith in 1982.
```

If there is no evidence that Dr. John Smith existed or invented the technology, this is a hallucination.

---

## With Grounding

```text
Answer only using the context below.

If the answer is not present in the context,
say "I don't have enough information."

Context:

XYZ technology was first documented in 1994.

Question:

Who invented XYZ technology in 1982?
```

A safer answer would be:

```text
I don't have enough information to identify an inventor
from the provided context.
```

The model is prevented from filling missing information with an invented answer.

---

# Hallucination Documentation Template

```text
Hallucination

Prompt:
...

Model Response:
...

Claim Being Made:
...

Verification:
...

Why It Is Incorrect / Unsupported:
...

Mitigation:
...

Mitigated Prompt:
...

New Response:
...

Result:
...
```

This gives me a reproducible record of the experiment.

---

# Key Mental Model

```text
LLM
 ↓
Predicts likely tokens
 ↓
Produces plausible language
 ↓
Plausible ≠ necessarily true
```

Therefore:

```text
LLM
 ↓
Potential Hallucination
 ↓
Grounding / Retrieval / Tools
 ↓
Verification
 ↓
More Reliable Answer
```

---

# Connection to Previous Days

Earlier I learned:

```text
Prompt
 ↓
Tokens
 ↓
Transformer
 ↓
Logits
 ↓
Probabilities
 ↓
Sampling
 ↓
Next Token
```

Today I learned an important consequence of that process.

The model is optimising for generating likely token sequences, not directly for guaranteeing factual truth.

Therefore:

```text
High probability
        ≠
High factual accuracy
```

This is one of the fundamental limitations of LLMs.

---

## RAG Connection

Today's hallucination lesson prepares me for the next stage of the roadmap:

```text
Documents
   ↓
Embeddings
   ↓
Vector Database
   ↓
Similarity Search
   ↓
Relevant Context
   ↓
LLM
   ↓
Grounded Answer
```

This is the foundation of **Retrieval-Augmented Generation (RAG)**.

Instead of relying entirely on what the model learned during training, we can provide relevant external knowledge at inference time.

---

# Key Takeaways

1. **Hallucination** is when an LLM generates incorrect, fabricated, or unsupported information.
2. LLMs generate likely token sequences; they do not inherently verify every factual claim.
3. **Fluent language does not guarantee factual accuracy.**
4. A confident response can still be completely wrong.
5. Hallucinations can include false facts, fake citations, fake people, fake events, incorrect calculations, and unsupported assumptions.
6. **Grounding** can reduce hallucinations by providing trusted context.
7. **RAG** retrieves relevant information and provides it to the model before generation.
8. **Tools** are useful when the task requires reliable calculations, current data, or database information.
9. Models should be allowed to say:

```text
"I don't have enough information."
```

rather than inventing an answer.

10. The goal is not simply to make the model sound confident.

> **The goal is to make the answer grounded, verifiable, and reliable.**

---

# Reflection

Today I learned that one of the biggest limitations of LLMs is that they can produce highly convincing answers without those answers necessarily being true.

I understood why this happens: the model is fundamentally generating probable token sequences based on learned patterns rather than automatically verifying every statement against a trusted source.

I also learned that hallucinations can be mitigated using **grounding, RAG, external tools, source-based prompting, and verification**.

The most important lesson for me is:

> **An LLM should not be treated as a source of truth by default. It should be treated as a reasoning and generation system that needs reliable context or verification when factual accuracy matters.**
