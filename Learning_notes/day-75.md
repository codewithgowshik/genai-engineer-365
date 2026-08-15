# Day 75 / 365 — Sampling, Determinism & Logprobs

## Objective

Today I learned about sampling, determinism, and log probabilities in Large Language Models (LLMs). I understood how a model assigns probabilities to possible next tokens and how logprob can be used to inspect how likely a selected token was.

I also connected logprobs with the concepts I learned previously: temperature, top-k, and top-p.

---

## Learning

### Sampling

An LLM generates text one token at a time.

When the model receives a prompt, it predicts possible tokens that could come next.

For example:

```
The capital of France is
```

The model may internally consider possibilities such as:

- Paris   → High probability
- London  → Lower probability
- Berlin  → Lower probability
- Madrid  → Lower probability

The model then uses a sampling strategy to select the next token.

After selecting the token, it becomes part of the context and the model predicts the next token again.

```
Prompt
   ↓
Predict next token
   ↓
Select token
   ↓
Add token to context
   ↓
Predict next token
   ↓
Repeat
```

### Determinism

Determinism means producing the same result when the same input and generation conditions are used.

A highly deterministic generation process tends to produce the same or very similar output for the same prompt.

For example:

```
Prompt:
The capital of France is

Possible output:
Paris
```

With more randomness in the sampling process, the model can potentially produce different outputs.

```
Same Prompt
     ↓
Probability Distribution
     ↓
Sampling
     ↓
Possible different outputs
```

Determinism is useful when consistent results are important.

Examples include:

- Classification
- Information extraction
- Structured output
- Data processing
- Reproducible experiments

More variation can be useful for:

- Brainstorming
- Creative writing
- Story generation
- Generating multiple ideas

### Logits

Before the model produces probabilities, it produces numerical scores called logits.

Logits are raw scores assigned to possible next tokens.

For example:

| Token  | Logit |
|--------|-------|
| Paris  | 8.5   |
| London | 5.2   |
| Berlin | 4.1   |
| Madrid | 3.0   |

These numbers are not probabilities.

A higher logit generally means the model is assigning a stronger preference to that token compared with the alternatives.

The process is:

```
Model
  ↓
Logits
  ↓
Probability Distribution
```

### Probability Distribution

The logits are converted into probabilities.

A probability distribution represents how likely each possible next token is.

For example:

| Token     | Probability |
|-----------|-------------|
| Paris     | 70%         |
| London    | 15%         |
| Berlin    | 10%         |
| Madrid    | 5%          |
| **Total** | **100%**    |

The probabilities of all possible tokens form a probability distribution.

The model can then use this distribution during sampling.

### Softmax

A common function used to convert logits into probabilities is softmax.

The basic formula is:

```
P(xᵢ) = eᶻⁱ / Σⱼ eᶻʲ
```

Where:

- zᵢ = logit for token i
- e = Euler's number
- P(xᵢ) = probability of token i

Softmax converts the raw logits into values between 0 and 1, and the probabilities add up to 1.

Conceptually:

```
Logits
  ↓
Softmax
  ↓
Probabilities
```

### Log Probability

A log probability, or logprob, is the logarithm of a token's probability.

The formula is:

```
logprob = ln(probability)
```

For example:

```
Probability = 0.70
logprob = ln(0.70)
logprob ≈ -0.357
```

Another example:

```
Probability = 0.10
logprob = ln(0.10)
logprob ≈ -2.303
```

Therefore:

```
Higher probability
       ↓
Logprob closer to 0

Lower probability
       ↓
More negative logprob
```

Example:

| Probability | Logprob                |
|-------------|-------------------------|
| 90%         | approximately -0.105    |
| 70%         | approximately -0.357    |
| 10%         | approximately -2.303    |
| 1%          | approximately -4.605    |

A logprob of 0 would correspond to a probability of 1 or 100%.

### Converting Logprob Back to Probability

If we have a logprob, we can recover the probability using the exponential function.

```
Probability = eˡᵒᵍᵖʳᵒᵇ
```

For example:

```
Logprob = -0.357
e⁻⁰·³⁵⁷ ≈ 0.70
Probability ≈ 70%
```

In Python this can be done using:

```python
import math

probability = math.exp(logprob)
```

This gives the relationship:

```
Probability
     ↓
    ln()
     ↓
Logprob
```

and:

```
Logprob
     ↓
   exp()
     ↓
Probability
```

### Why Logprobs Are Useful

Logprobs allow us to inspect the model's confidence or likelihood for generated tokens.

Instead of only seeing:

```
Paris
```

we can potentially inspect:

```
Token: Paris
Probability: 70%
Logprob: -0.357
```

This gives us more information about the model's token selection.

Logprobs can be useful for:

- Inspecting model confidence
- Comparing candidate tokens
- Debugging generation
- Evaluating outputs
- Understanding sampling behaviour
- Building probability-based applications

### Chosen Token vs Alternative Tokens

Suppose the model receives:

```
The capital of France is
```

It could have a probability distribution like:

| Token  | Probability |
|--------|-------------|
| Paris  | 70%         |
| London | 15%         |
| Berlin | 10%         |
| Madrid | 5%          |

The model may select:

```
Paris
```

The selected token is the chosen candidate.

The other tokens are alternative candidates.

Conceptually:

```
              Next Token
                  ↓
       ┌──────────┼──────────┐
       ↓          ↓          ↓
     Paris      London      Berlin
      70%        15%         10%
       ↑
    Selected
```

Logprob lets us inspect the likelihood of these candidates.

### Top Logprobs

When an API provides top logprobs, it can expose several of the highest-probability candidate tokens at a particular generation step.

For example, Top Candidates:

| Token  | Probability |
|--------|-------------|
| Paris  | 70%         |
| London | 15%         |
| Berlin | 10%         |
| Madrid | 5%          |

This is useful because normally we only see the generated output:

```
Paris
```

With logprob information, we can inspect some of the alternatives the model considered.

### Relationship With Temperature

Temperature changes the shape of the probability distribution used during sampling.

The temperature-adjusted softmax can be represented as:

```
P(xᵢ) = e^(zᵢ/T) / Σⱼ e^(zⱼ/T)
```

Where:

- T = temperature

#### Low Temperature

A lower temperature makes the probability distribution more concentrated around high-probability tokens.

Low Temperature:

| Token  | Probability |
|--------|-------------|
| Paris  | 90%         |
| London | 5%          |
| Berlin | 3%          |
| Other  | 2%          |

The output tends to be more predictable.

#### High Temperature

A higher temperature generally makes the probability distribution flatter.

High Temperature:

| Token  | Probability |
|--------|-------------|
| Paris  | 50%         |
| London | 20%         |
| Berlin | 15%         |
| Other  | 15%         |

The output can become more varied.

Therefore:

```
Temperature
     ↓
Changes probability distribution
     ↓
Changes sampling behaviour
```

### Relationship With Top-k

Top-k is a sampling/filtering method.

Top-k means:

> Keep the k highest-probability candidate tokens.

For example:

| Token  | Probability |
|--------|-------------|
| Paris  | 70%         |
| London | 15%         |
| Berlin | 10%         |
| Madrid | 5%          |

If:

```
k = 2
```

then:

| Token  | Probability | Kept |
|--------|-------------|------|
| Paris  | 70%         | ✓    |
| London | 15%         | ✓    |
| Berlin | 10%         | ✗    |
| Madrid | 5%          | ✗    |

The candidate set becomes:

- Paris
- London

The probabilities can then be renormalized before sampling.

The important idea is:

```
Top-k
  ↓
Fixed number of candidates
```

### Relationship With Top-p

Top-p is also called nucleus sampling.

Instead of selecting a fixed number of tokens, top-p keeps the highest-probability tokens until their cumulative probability reaches the selected threshold.

For example:

| Token  | Probability |
|--------|-------------|
| Paris  | 70%         |
| London | 15%         |
| Berlin | 10%         |
| Madrid | 5%          |

If:

```
top-p = 0.85
```

then:

```
Paris
70%

Paris + London
70% + 15% = 85%
```

Therefore:

- Paris ✓
- London ✓
- Berlin ✗
- Madrid ✗

The important idea is:

```
Top-p
  ↓
Dynamic number of candidates
  ↓
Until cumulative probability reaches P
```

### Top-k vs Top-p

**Top-k**
> "Keep the top K tokens."

**Top-p**
> "Keep enough top tokens to reach probability P."

Example:

| Token | Probability |
|-------|-------------|
| A     | 50%         |
| B     | 20%         |
| C     | 15%         |
| D     | 10%         |
| E     | 5%          |

**Top-k = 3**

- A
- B
- C

Exactly 3 candidates are retained.

**Top-p = 0.85**

```
A + B + C
50% + 20% + 15%
= 85%
```

Three candidates happen to be retained.

However, the number can change depending on the probability distribution.

### Complete Next-Token Generation Process

The concepts from Days 71–75 connect together into one pipeline:

```
Human Prompt
     ↓
Tokenizer
     ↓
Token IDs
     ↓
Transformer Model
     ↓
Logits
     ↓
Temperature
     ↓
Probability Distribution
     ↓
Top-k / Top-p Filtering
     ↓
Sampling
     ↓
Selected Next Token
     ↓
Logprob Inspection
     ↓
Add Token To Context
     ↓
Predict Next Token
     ↓
Repeat
```

The important distinction is:

- **Temperature** → Shapes the probability distribution
- **Top-k** → Filters by number of candidates
- **Top-p** → Filters by cumulative probability
- **Sampling** → Selects the next token
- **Logprob** → Lets us inspect how likely a token was

### My Mental Model

The easiest way for me to remember the process is:

```
MODEL
  ↓
"What could come next?"
  ↓
LOGITS
  ↓
"How strong is each possibility?"
  ↓
PROBABILITY DISTRIBUTION
  ↓
"How likely is each possibility?"
  ↓
TEMPERATURE
  ↓
"How concentrated should the distribution be?"
  ↓
TOP-K / TOP-P
  ↓
"Which candidates should remain?"
  ↓
SAMPLING
  ↓
"Which token gets selected?"
  ↓
LOGPROB
  ↓
"How likely was that token?"
```

### Practical Experiment

For today's experiment, the intended goal was to inspect token log probabilities from a model response.

The Gemini model I was using returned:

```
400 INVALID_ARGUMENT
Logprobs is not enabled for models/gemini-2.5-flash
```

This showed an important practical lesson:

> An API may expose a feature in its general API schema, but the specific model being used may not support that feature.

Therefore, I did not treat the failed Gemini request as a successful logprob experiment.

The learning objective was still completed conceptually by understanding:

```
Token
↓
Probability
↓
Logprob
↓
Candidate comparison
↓
Sampling
```

### Formula Summary

**Softmax**

```
P(xᵢ) = eᶻⁱ / Σⱼ eᶻʲ
```

Converts logits into probabilities.

**Temperature Softmax**

```
P(xᵢ) = e^(zᵢ/T) / Σⱼ e^(zⱼ/T)
```

Temperature changes the probability distribution.

**Log Probability**

```
logprob = ln(P)
```

Converts probability into log probability.

**Probability From Logprob**

```
P = e^(logprob)
```

Converts log probability back into probability.

**Top-k**
> Keep the k highest-probability tokens.

**Top-p**
> Find the smallest k such that:
>
> Σ P(token) ≥ p
>
> Then sample from the resulting candidate set.

### Connection to Previous Days

#### Day 71 — Tokens

I learned that LLMs process text as tokens and represent tokens using token IDs.

```
Text
 ↓
Tokenizer
 ↓
Tokens
 ↓
Token IDs
```

#### Day 72 — Tokenization

I learned how text is split into token pieces using tokenization techniques such as BPE.

```
Text
 ↓
Token Pieces
 ↓
Token IDs
```

#### Day 73 — Temperature

I learned how temperature changes the model's probability distribution and affects output variability.

```
Logits
 ↓
Temperature
 ↓
Probability Distribution
```

#### Day 74 — Top-k and Top-p

I learned how top-k and top-p filter the candidate tokens before sampling.

```
Probability Distribution
 ↓
Top-k / Top-p
 ↓
Candidate Tokens
```

#### Day 75 — Logprobs

I learned how log probabilities allow us to inspect the likelihood assigned to generated tokens.

```
Token
 ↓
Probability
 ↓
Logprob
```

### Final Understanding

An LLM does not simply choose a complete word from a list.

It repeatedly predicts the probability of possible next tokens.

The process can be simplified as:

```
Input Tokens
     ↓
Transformer
     ↓
Logits
     ↓
Probability Distribution
     ↓
Temperature
     ↓
Top-k / Top-p
     ↓
Sampling
     ↓
Next Token
     ↓
Logprob
     ↓
Next Generation Step
```

The model repeats this process token by token until the response is complete.

## Reflection

Today I understood that logprobs do not predict the next token by themselves; they allow me to inspect how likely the model considered a token.

I also connected logits, probability distributions, temperature, top-k, top-p, sampling, and logprobs into one complete next-token generation process.
