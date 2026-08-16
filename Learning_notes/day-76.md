# Day 76 / 365 — Force Deterministic Output (Temperature 0 / Seed)

## Objective

Today I learned how to make LLM generation more deterministic and reproducible.

I understood how **temperature** affects randomness during sampling, how **temperature = 0** favours the highest-probability token, and how a **seed** can help reproduce pseudorandom sampling when supported by the model/API.

I also connected deterministic generation with the concepts I learned previously: **logits, probability distributions, logprobs, temperature, top-k, top-p, and sampling**.

---

## Learning

### Deterministic Output

Deterministic output means trying to produce the same result when the same input and generation conditions are used.

For example:

```text
Prompt:
The capital of France is
```

A deterministic generation process may repeatedly produce:

```text
Paris
```

With more randomness in the sampling process, the model can potentially produce different outputs.

```text
Same Prompt
     ↓
Probability Distribution
     ↓
Sampling
     ↓
Possible different outputs
```

Deterministic generation is useful when consistent results are important.

Examples include:

- Classification
- Information extraction
- Structured output
- Data processing
- Testing
- Reproducible experiments
- Evaluation

---

### Temperature

Temperature controls how strongly the model favours high-probability tokens during sampling.

The temperature-adjusted probability distribution can be represented as:

```text
P(xᵢ) = e^(zᵢ/T) / Σⱼ e^(zⱼ/T)
```

Where:

- `zᵢ` = logit for token `i`
- `T` = temperature
- `P(xᵢ)` = probability of token `i`

Conceptually:

```text
Logits
   ↓
Temperature
   ↓
Probability Distribution
   ↓
Sampling
```

Temperature does not change the model's underlying knowledge.

It changes how the model samples from the probability distribution.

---

### Low Temperature

A lower temperature makes the probability distribution more concentrated around high-probability tokens.

For example:

| Token  | Probability |
|--------|-------------|
| Paris  | 90% |
| London | 5% |
| Berlin | 3% |
| Madrid | 2% |

Therefore:

```text
Lower Temperature
       ↓
Less randomness
       ↓
More predictable output
```

---

### High Temperature

A higher temperature generally makes the probability distribution flatter.

For example:

| Token  | Probability |
|--------|-------------|
| Paris  | 50% |
| London | 20% |
| Berlin | 15% |
| Madrid | 15% |

Therefore:

```text
Higher Temperature
       ↓
More randomness
       ↓
More varied output
```

---

### Temperature = 0

Setting:

```text
temperature = 0
```

aims to make generation as deterministic as the model/API allows.

Conceptually, this is closely related to **greedy decoding**.

Greedy decoding means:

```text
Select the highest-probability token.
```

For example:

| Token  | Probability |
|--------|-------------|
| Paris  | 70% |
| London | 15% |
| Berlin | 10% |
| Madrid | 5% |

The highest-probability token is:

```text
Paris
```

So greedy decoding selects:

```text
Paris
```

The simplified process is:

```text
Probability Distribution
          ↓
Highest Probability
          ↓
       Next Token
```

#### Important Limitation

Temperature `0` does not necessarily guarantee that every generation will always be identical.

Differences can still occur because of:

- Model implementation
- Model version
- Backend infrastructure
- Hardware
- Floating-point operations
- Distributed inference
- Provider-specific behaviour

Therefore:

> Temperature 0 aims for deterministic or highly reproducible generation, but absolute reproducibility depends on the complete inference system.

---

### Greedy Decoding

Greedy decoding selects the token with the highest probability at each generation step.

Conceptually:

```text
next_token = argmax(probabilities)
```

For example:

```text
Paris     → 70%
London    → 15%
Berlin    → 10%
Madrid    → 5%
```

The model selects:

```text
Paris
```

Greedy decoding prioritizes the most probable option rather than randomly sampling among possible candidates.

---

### Sampling vs Greedy Decoding

With sampling:

```text
Probability Distribution
          ↓
Sampling
          ↓
Possible Token
```

The output can vary.

With greedy decoding:

```text
Probability Distribution
          ↓
Highest-Probability Token
          ↓
Next Token
```

The output becomes much more predictable.

| Method | Behaviour |
|---|---|
| Sampling | Can select different candidates |
| Greedy decoding | Selects highest-probability candidate |
| Low temperature | Reduces randomness |
| Temperature near 0 | Strongly favours highest-probability candidates |

---

### Seed

A **seed** is a value used to initialize a pseudorandom number generator.

For example:

```text
seed = 42
```

When a generation system supports seed control, using the same seed with the same model, prompt, and generation parameters can help reproduce the same pseudorandom choices.

Conceptually:

```text
Same Prompt
     +
Same Model
     +
Same Parameters
     +
Same Seed
     ↓
More Reproducible Generation
```

A seed does not make the model more intelligent.

It controls the starting point of the pseudorandom process.

Not every model or API supports user-controlled seeds.

---

### Temperature vs Seed

Temperature and seed solve different problems.

| Concept | Purpose |
|---|---|
| Temperature | Controls randomness |
| Seed | Helps reproduce pseudorandom choices |
| Logprob | Represents token likelihood |
| Greedy decoding | Selects the highest-probability token |

A simple way to remember them:

```text
Logprob
"What is likely?"

Temperature
"How much randomness should I allow?"

Seed
"Can I reproduce the random process?"
```

---

### Reproducibility

Reproducibility means being able to repeat an experiment and obtain the same or highly similar result under the same conditions.

For example:

```text
Prompt:
List 5 benefits of artificial intelligence.
```

A more reproducible configuration might be:

```text
temperature = 0
seed = 42
```

When supported, repeated runs may produce:

```text
Run 1 → Same / highly similar output
Run 2 → Same / highly similar output
Run 3 → Same / highly similar output
Run 4 → Same / highly similar output
```

This is useful when developing and testing AI applications.

---

### Why Deterministic Output Is Useful

Deterministic generation can be useful for:

- Testing
- Debugging
- Evaluation
- Classification
- Information extraction
- Structured JSON generation
- Data processing
- Reproducible experiments

For example:

```text
Input
  ↓
AI Model
  ↓
Expected Output
```

If the model behaves consistently, it becomes easier to test and debug the application.

---

### Practical Experiment

Use the same prompt for all experiments:

```text
List exactly 5 benefits of artificial intelligence.
Number them from 1 to 5.
```

#### Experiment 1 — Temperature 1

```text
temperature = 1
```

Run the prompt multiple times.

Record the outputs:

```text
Run 1:
...

Run 2:
...

Run 3:
...

Run 4:
...

Run 5:
...
```

Look for differences in:

- Word choice
- Ordering
- Sentence structure
- Formatting

---

#### Experiment 2 — Temperature 0

Run the same prompt:

```text
temperature = 0
```

Run it multiple times.

Compare the results with Experiment 1.

Expected observation:

```text
Temperature 1
      ↓
More variation

Temperature 0
      ↓
More predictable output
```

---

#### Experiment 3 — Temperature 0 + Seed

If the API/model supports seeds:

```text
temperature = 0
seed = 42
```

Run the prompt multiple times.

Compare:

```text
Experiment A
temperature = 1

Experiment B
temperature = 0

Experiment C
temperature = 0
seed = 42
```

The goal is to observe how controlling randomness affects reproducibility.

---

### Experiment Results

| Experiment | Temperature | Seed | Expected Behaviour |
|---|---:|---:|---|
| A | 1.0 | — | More variation |
| B | 0 | — | More predictable |
| C | 0 | 42 | Greater reproducibility when supported |

The actual results depend on the model and API implementation.

---

### Relationship With Logprobs

Today's topic connects directly to logprobs.

Suppose the model predicts:

| Token  | Probability | Logprob |
|--------|-------------|---------|
| Paris  | 70% | -0.357 |
| London | 15% | -1.897 |
| Berlin | 10% | -2.303 |
| Madrid | 5% | -2.996 |

The model has a probability distribution over possible next tokens.

Temperature changes how this distribution is used during sampling.

The generation process then selects the next token.

```text
Logits
  ↓
Probability Distribution
  ↓
Temperature
  ↓
Sampling / Greedy Decoding
  ↓
Selected Token
  ↓
Logprob
```

---

### Complete Generation Process

The concepts from the previous days can now be connected into one pipeline:

```text
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
Probability Distribution
     ↓
Temperature
     ↓
Top-k / Top-p
     ↓
Sampling / Greedy Decoding
     ↓
Selected Next Token
     ↓
Logprob Inspection
     ↓
Add Token to Context
     ↓
Predict Next Token
     ↓
Repeat
```

The important distinction is:

- **Logits** → Raw scores for possible tokens
- **Probability distribution** → Likelihood of candidate tokens
- **Temperature** → Controls randomness
- **Top-k** → Keeps a fixed number of top candidates
- **Top-p** → Keeps candidates based on cumulative probability
- **Sampling** → Selects the next token
- **Logprob** → Represents token likelihood
- **Seed** → Helps reproduce pseudorandom choices
- **Greedy decoding** → Selects the highest-probability token

---

### My Mental Model

The easiest way for me to remember today's concept is:

```text
MODEL
  ↓
"What could come next?"
  ↓
LOGITS
  ↓
"How strong is each possibility?"
  ↓
PROBABILITIES
  ↓
"How likely is each possibility?"
  ↓
TEMPERATURE
  ↓
"How random should generation be?"
  ↓
TOP-K / TOP-P
  ↓
"Which candidates should remain?"
  ↓
SAMPLING / GREEDY
  ↓
"Which token gets selected?"
  ↓
SEED
  ↓
"Can the generation process be reproduced?"
  ↓
NEXT TOKEN
  ↓
Repeat
```

---

### Formula Summary

**Temperature-adjusted softmax**

```text
P(xᵢ) = e^(zᵢ/T) / Σⱼ e^(zⱼ/T)
```

**Greedy decoding**

```text
next_token = argmax(probabilities)
```

**Log probability**

```text
logprob = ln(P)
```

**Probability from logprob**

```text
P = e^(logprob)
```

---

## Reflection

Today I understood that LLM output is not inherently deterministic because token generation involves probability distributions and sampling.

I learned that reducing temperature makes the model's output more predictable, while temperature `0` strongly favours the highest-probability token.

I also learned that a seed can help reproduce pseudorandom generation when supported by the model/API.

Most importantly, I connected **temperature, greedy decoding, seed, and reproducibility** with my previous understanding of **logits, probabilities, sampling, and logprobs**.
