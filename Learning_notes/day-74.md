# Day 74 / 365 — Temperature, Top-p & Top-k

## Objective

Today I learned about **temperature**, **top-p**, and **top-k** in Large Language Models (LLMs). I also built a top-p sweep experiment using the Gemini API to observe how changing top-p affects model output.

---

## Learning

### Temperature

Temperature is a generation parameter that affects how the model samples the next token from its probability distribution.

In simple terms:

| Setting | Effect |
|---|---|
| Low Temperature | More predictable output |
| High Temperature | More varied output |

> Temperature affects generation **behaviour**, not the model's underlying **knowledge**.

- At a **lower** temperature, the model tends to favour higher-probability tokens more strongly. This generally makes the output more predictable, consistent, and less varied.
- At a **higher** temperature, lower-probability tokens have more opportunity to be selected. This generally makes the output more varied, creative, and less predictable.

Temperature does **not**:

- Train the model
- Add knowledge to the model
- Make the model smarter
- Change its learned parameters

Instead, temperature affects how the model chooses between possible next tokens during generation.

### Top-k

Top-k restricts the model to the `k` most probable tokens.

For example, suppose the model predicts:

| Token | Probability |
|---|---|
| Token A | 40% |
| Token B | 25% |
| Token C | 15% |
| Token D | 10% |
| Token E | 5% |
| Token F | 3% |
| Token G | 2% |

If `top_k = 3`, the model only considers:

- Token A
- Token B
- Token C

The remaining tokens are excluded from the candidate set.

```
Top-k
  ↓
Select the k most probable tokens
  ↓
Sample from those candidates
```

The important point is that top-k uses a **fixed number** of candidate tokens.

```
top_k = 3
→ Always keep 3 candidate tokens
```

### Top-p / Nucleus Sampling

Top-p, also called **nucleus sampling**, restricts the candidate tokens based on their **cumulative probability**.

Instead of specifying a fixed number of tokens, top-p specifies a probability threshold.

For example:

| Token | Probability |
|---|---|
| Token A | 40% |
| Token B | 25% |
| Token C | 15% |
| Token D | 10% |
| Token E | 5% |
| Token F | 3% |
| Token G | 2% |

If `top_p = 0.80`, the model starts with the highest-probability token and adds tokens until the cumulative probability reaches the selected value:

- A = 40%
- A + B = 40% + 25% = 65%
- A + B + C = 40% + 25% + 15% = 80%

Therefore, the candidate set becomes:

- Token A
- Token B
- Token C

> Top-p does **not** mean selecting a percentage of the vocabulary. It means selecting the smallest group of highest-probability tokens whose cumulative probability reaches the chosen `p` value.

The basic process is:

```
Sort tokens by probability
        ↓
Start with the highest-probability token
        ↓
Add probabilities together
        ↓
Reach the top-p threshold
        ↓
Use those tokens as candidates
        ↓
Sample the next token
```

### Top-k vs Top-p

The main difference is:

- **Top-k** → "Give me the top K tokens."
- **Top-p** → "Give me enough of the top tokens to reach probability P."

| Parameter | Candidate count |
|---|---|
| Top-k | Fixed number of candidates |
| Top-p | Dynamic number of candidates |

For example, with `top_p = 0.80`, one prediction might need only **2 candidate tokens**, while another prediction might need **5 candidate tokens**, because the probability distribution changes for every next-token prediction.

### Temperature vs Top-k vs Top-p

| Parameter | What it controls |
|---|---|
| Temperature | How strongly high-probability tokens are favoured |
| Top-k | Number of highest-probability candidate tokens |
| Top-p | Amount of cumulative probability considered |

A simple way to remember them:

- **Temperature** → Changes probability distribution
- **Top-k** → Limits the number of candidates
- **Top-p** → Limits the cumulative probability mass

---

## How Sampling Works

An LLM predicts the next token based on the current context.

For example: `"The cat is"`

The model may assign probabilities to possible next tokens:

| Next Token | Probability |
|---|---|
| sleeping | High |
| hungry | Medium |
| running | Lower |
| flying | Very low |

The model first produces numerical scores called **logits**:

```
Token A → Score
Token B → Score
Token C → Score
Token D → Score
```

These scores are converted into probabilities. For example:

| Token | Probability |
|---|---|
| Token A | 70% |
| Token B | 20% |
| Token C | 7% |
| Token D | 3% |

Temperature, top-k, and top-p can then influence the sampling process. After selecting a token, that token becomes part of the context, and the model predicts the next token. This process continues repeatedly:

```
Context
  ↓
Predict next token
  ↓
Apply sampling
  ↓
Select token
  ↓
Add token to context
  ↓
Predict next token
  ↓
Repeat...
```

---

## Experiment: Top-p Sweep (Gemini API)

A **top-p sweep** means testing the same prompt with multiple top-p values. The important rule is to keep the prompt, model, temperature, and other settings the same while changing only top-p.

For this experiment, I tested:

- 0.1
- 0.3
- 0.5
- 0.7
- 0.9
- 1.0

The experiment structure was:

```
Same Prompt
      ↓
Same Model
      ↓
Same Temperature
      ↓
Different Top-p
      ↓
Compare Outputs
```

The temperature was kept fixed at `temperature = 0.5`.

### Experiment Prompt

```
Write the beginning of a story about a young explorer.
```

### Results

| Top-p | Output |
|---|---|
| 0.1 | Experiment output |
| 0.3 | Experiment output |
| 0.5 | Experiment output |
| 0.7 | Experiment output |
| 0.9 | Experiment output |
| 1.0 | Experiment output |

> The exact output can change because the model uses sampling during generation.

### Observations

A lower top-p gives the model a more restricted candidate pool:

```
Lower Top-p
  ↓
Smaller probability mass considered
  ↓
Fewer possible candidate tokens
  ↓
More restricted sampling
```

A higher top-p allows more of the probability distribution to be considered:

```
Higher Top-p
  ↓
More probability mass considered
  ↓
More possible candidate tokens
  ↓
More variation can be possible
```

The exact behaviour depends on the model, prompt, temperature, and other generation settings.

---

## Important Understanding

The most important thing I learned today is that top-k and top-p do **not** work the same way.

- **Top-k** → Fixed number of possible tokens
- **Top-p** → Variable number of possible tokens based on cumulative probability

For example:

- `Top-k = 3` → Keep 3 tokens
- `Top-p = 0.80` → Keep enough highest-probability tokens to reach 80% cumulative probability

---

## Connecting the Dots

This connects with the previous days of learning:

- **Day 71** introduced tokens and token IDs.
- **Day 72** introduced BPE tokenization and token boundaries.
- **Day 73** introduced context windows and temperature.
- **Day 74** introduced top-k and top-p sampling.

The complete LLM generation flow can be understood as:

```
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
Temperature
  ↓
Top-k / Top-p Filtering
  ↓
Sampling
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

## Practical Applications

Different sampling settings can be useful for different applications.

**Lower randomness / more restricted sampling** is useful for:

- Structured responses
- Classification
- Information extraction
- Consistent formatting
- Predictable workflows

**More variation** is useful for:

- Brainstorming
- Creative writing
- Story ideas
- Marketing ideas
- Generating multiple alternatives

> The correct configuration depends on the model and application.

---

## Reflection

Today I understood that top-k restricts the model to a fixed number of the most probable tokens, while top-p dynamically selects tokens based on cumulative probability.

I also learned how temperature, top-k, and top-p work together to control the sampling process, and compared different top-p settings using the Gemini API.

---

## Summary

Today I learned three important sampling concepts:

- **Temperature** → Controls how probability is distributed.
- **Top-k** → Keeps a fixed number of highest-probability tokens.
- **Top-p** → Keeps the smallest group of tokens whose cumulative probability reaches P.

The main sampling flow is:

```
Prompt
  ↓
Tokens
  ↓
Model
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
```

**The biggest lesson from today:** Top-k controls *how many* candidate tokens are considered, while top-p controls *how much cumulative probability* is considered.
