# Day 71 / 365 — Tokens \& Tokenization

# 🎯 Objective

Today I learned how Large Language Models process text using tokens.

I learned:

* What a token is.
* What tokenization means.
* What a tokenizer does.
* What a token ID is.
* Why token IDs are not random.
* What a tokenizer vocabulary is.
* What `cl100k\_base` is.
* Why one word can become multiple tokens.
* How token IDs are used before the model processes text.
* How an LLM predicts the next token.
* Why token count matters in Generative AI.

# 📚 Learning

# What is a Token?

A **token** is a piece of text that a language model processes.

A token can be:

* A complete word.
* Part of a word.
* Punctuation.
* A space combined with a word.
* A symbol.

The exact tokens depend on the tokenizer.

# Word Count vs Token Count

One word does not always equal one token.

I entered:

```text
gowshik
```

The tokenizer returned:

```text
Token IDs:
\[37286, 939, 1609]

Token count:
3

Word count:
1
```

So:

```text
1 word → 3 tokens
```

This shows that:

> \*\*Word count and token count are different.\*\*

A tokenizer can split one word into multiple pieces.

# What is a Tokenizer?

A **tokenizer** converts human-readable text into tokens and token IDs.

The basic process is:

```text
Text
 ↓
Tokenizer
 ↓
Tokens
 ↓
Token IDs
```

For example:

```text
"gowshik"
    ↓
Tokenizer
    ↓
\[37286, 939, 1609]
```

The tokenizer uses its vocabulary and encoding rules to decide how the text is split.

# What is a Token ID?

A **token ID** is a numerical identifier assigned to a token in the tokenizer's vocabulary.

Conceptually:

```text
"hello" → 15339
"world" → 1917
```

For my example:

```text
"gow" → 37286
"sh"  → 939
"ik"  → 1609
```

The number itself does not contain the meaning of the token.

It is simply an identifier.

# Are Token IDs Random?

No.

Token IDs are assigned as part of the tokenizer's vocabulary.

They can be thought of like indexes:

```text
ID 0 → Token A
ID 1 → Token B
ID 2 → Token C
...
```

The ID is used to identify a particular token.

Token IDs are also **tokenizer-specific**.

Different tokenizers can assign different IDs to the same text.

# What is a Vocabulary?

A tokenizer has a **vocabulary** containing many possible tokens.

Conceptually:

```text
Vocabulary
├── hello
├── world
├── ing
├── tion
├── !
├── ,
└── many other tokens
```

Each token has an associated ID.

The vocabulary allows the tokenizer to convert text into numerical IDs.

# What is `cl100k\_base`?

I used `tiktoken` with:

```python
encoding = tiktoken.get\_encoding("cl100k\_base")
```

`cl100k\_base` is a **pre-built tokenizer encoding**.

It contains the vocabulary and rules required to convert text into token IDs.

For example:

```python
encoding.encode("gowshik")
```

returned:

```text
\[37286, 939, 1609]
```

So:

```text
"gowshik"
    ↓
cl100k\_base
    ↓
\[37286, 939, 1609]
```

Important:

> \*\*`cl100k\_base` is a tokenizer encoding, not the language model itself.\*\*

# Tokenizer vs Language Model

The tokenizer and the language model have different jobs.

The tokenizer prepares the text:

```text
Text
 ↓
Tokens
 ↓
Token IDs
```

The language model processes those representations:

```text
Token IDs
 ↓
Embeddings
 ↓
Transformer
 ↓
Probabilities
 ↓
Next Token
```

Therefore:

> \*\*Tokenizer ≠ LLM\*\*

# How Does the Model Use Token IDs?

The model does not treat:

```text
37286
```

as the mathematical meaning of the number 37,286.

Instead, the token ID is used to retrieve a learned representation called an **embedding**.

Conceptually:

```text
Token ID
   ↓
Embedding Lookup
   ↓
Embedding Vector
   ↓
Transformer
```

For example:

```text
37286
  ↓
\[0.21, -0.73, 0.44, 0.12, ...]
```

The actual embedding contains many dimensions.

# How Does an LLM Predict?

An LLM predicts the **next token**.

For example:

```text
"The cat is"
```

The model considers many possible next tokens:

```text
sleeping
hungry
running
cute
...
```

Each possible token receives a probability.

Conceptually:

```text
sleeping → 42%
hungry   → 18%
cute     → 11%
running  → 8%
...
```

The model then selects a next token according to its decoding or sampling strategy.

For example:

```text
"The cat is"
      ↓
" sleeping"
```

Then the model predicts another token.

# Autoregressive Generation

LLMs generate text one token at a time.

For example:

```text
"The cat is"
      ↓
" sleeping"
```

Now the context becomes:

```text
"The cat is sleeping"
```

The model predicts again:

```text
"The cat is sleeping"
            ↓
            "."
```

The process continues:

```text
Input
 ↓
Next Token
 ↓
Next Token
 ↓
Next Token
 ↓
...
```

This is called **autoregressive generation**.

# Complete LLM Pipeline

The main pipeline I learned is:

```text
Human Text
    ↓
Tokenizer
    ↓
Tokens
    ↓
Token IDs
    ↓
Embeddings
    ↓
Transformer
    ↓
Probabilities
    ↓
Next Token
    ↓
More Context
    ↓
Next Token
```

The important idea is:

> \*\*An LLM repeatedly predicts the next token to generate text.\*\*

# Why Token Count Matters

Token count is important in Generative AI because it affects:

* Context window.
* Processing requirements.
* API usage.
* API cost.

More tokens generally mean more information for the model to process.

Understanding token usage is therefore important when building real-world AI applications.

# 🧪 My Experiment

I tested:

```text
gowshik
```

The result was:

```text
Token IDs:
\[37286, 939, 1609]

Token count:
3

Word count:
1
```

This demonstrated:

```text
1 word
   ↓
3 tokens
   ↓
3 token IDs
```

I learned that the tokenizer does not simply split text based on spaces.

# 🔑 Key Takeaways

* LLMs process **tokens**, not directly words.
* A token is a piece of text.
* One word can contain multiple tokens.
* Word count and token count are different.
* A tokenizer converts text into token IDs.
* A token ID is an identifier for a token.
* Token IDs are not random semantic numbers.
* Token IDs depend on the tokenizer.
* A tokenizer has a vocabulary of tokens.
* `cl100k\_base` is a pre-built tokenizer encoding.
* The tokenizer and the language model are separate components.
* Token IDs are used to retrieve learned embeddings.
* The Transformer processes those representations.
* The LLM predicts the next token.
* Text is generated one token at a time.
* Token count matters for context, performance, and cost.

# 💭 Reflection

Today I understood how text is converted into a format that an LLM can process.

I initially wondered whether token IDs such as:

```text
37286
939
1609
```

were random numbers.

I learned that they are identifiers assigned to tokens in the tokenizer vocabulary.

My experiment with:

```text
gowshik
```

was useful because one word became three tokens:

```text
gowshik
   ↓
\[37286, 939, 1609]
```

I also learned that the model does not directly understand these numbers as mathematical values. The IDs are used to retrieve learned embeddings, which are then processed by the Transformer.

The most important concept I learned today is:

```text
Text
 ↓
Tokenizer
 ↓
Token IDs
 ↓
Embeddings
 ↓
Transformer
 ↓
Probabilities
 ↓
Next Token
```

# 📝 Summary

Today I learned the basics of tokens and tokenization.

A tokenizer converts text into tokens and token IDs. The token IDs are used to retrieve learned embeddings, which are then processed by the Transformer.

The model produces probabilities for possible next tokens and generates text one token at a time.

The main concept I learned is:

> \*\*An LLM predicts the next token, not directly the next word.\*\*

# 

