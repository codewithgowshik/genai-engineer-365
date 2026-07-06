# Day 36: Zero-Shot vs Few-Shot Prompting

## Objective

Learn the difference between Zero-Shot and Few-Shot Prompting, understand when to use each technique, and compare their outputs using the same task.

---

# What is Prompting?

Prompting is the process of providing instructions to a Large Language Model (LLM) so that it can perform a specific task.

Different prompting techniques help improve the quality, consistency, and accuracy of AI-generated responses.

Two of the most common techniques are:

* Zero-Shot Prompting
* Few-Shot Prompting

---

# What is Zero-Shot Prompting?

Zero-shot prompting means asking the AI to perform a task **without giving any examples**.

The model relies entirely on its pre-trained knowledge and your instructions.

Example:

```text
Translate the following sentence into French:

Good morning.
```

The model has never been shown an example within the prompt.

---

# Characteristics of Zero-Shot Prompting

* No examples are provided.
* Faster to write.
* Simpler prompts.
* Relies on the model's existing knowledge.
* Works well for common tasks.

---

# Example

Prompt:

```text
Summarize this article.
```

The AI generates a summary without seeing any example summaries.

---

# Advantages of Zero-Shot Prompting

* Simple to write.
* Requires fewer tokens.
* Faster execution.
* Suitable for general-purpose tasks.

---

# Limitations of Zero-Shot Prompting

* Output style may vary.
* Less consistent.
* Can misunderstand formatting requirements.
* Performance may decrease for specialized tasks.

---

# What is Few-Shot Prompting?

Few-shot prompting provides the AI with a small number of examples before asking it to complete a similar task.

Instead of only giving instructions, you also demonstrate the expected pattern.

---

# Example

```text
English: Hello
French: Bonjour

English: Thank you
French: Merci

English: Good night
French:
```

The AI follows the same pattern to complete the translation.

---

# Characteristics of Few-Shot Prompting

* Includes examples.
* Demonstrates the desired output.
* Produces more consistent responses.
* Helps with formatting.
* Useful for specialized tasks.

---

# Advantages of Few-Shot Prompting

* More reliable outputs.
* Better consistency.
* Improved formatting.
* Better performance on custom tasks.

---

# Limitations of Few-Shot Prompting

* Uses more tokens.
* Longer prompts.
* More preparation required.
* Context window fills more quickly.

---

# Zero-Shot vs Few-Shot

| Zero-Shot             | Few-Shot                             |
| --------------------- | ------------------------------------ |
| No examples           | Includes examples                    |
| Short prompts         | Longer prompts                       |
| Faster                | Slightly slower                      |
| Less consistent       | More consistent                      |
| Lower token usage     | Higher token usage                   |
| Best for simple tasks | Best for complex or repetitive tasks |

---

# When to Use Zero-Shot

Use Zero-Shot when:

* The task is simple.
* The model already understands the task.
* Speed is important.
* You don't need a specific output format.

Examples:

* Explain a concept.
* Translate text.
* Answer factual questions.
* Summarize an article.

---

# When to Use Few-Shot

Use Few-Shot when:

* You need consistent formatting.
* The task is domain-specific.
* You want a particular writing style.
* The model struggles with zero-shot prompts.

Examples:

* Product classification
* Custom email writing
* Sentiment analysis
* Structured extraction
* Specialized document generation

---

# Example Comparison

## Zero-Shot

```text
Classify the sentiment:

"I love this product."
```

Possible response:

```text
Positive
```

---

## Few-Shot

```text
Sentence:
"I hate waiting."

Sentiment:
Negative

Sentence:
"This is amazing."

Sentiment:
Positive

Sentence:
"I love this product."

Sentiment:
```

Response:

```text
Positive
```

The few-shot prompt teaches the model the expected pattern before asking it to complete the task.

---

# Workflow

```text
Choose Task
      ↓
Write Zero-Shot Prompt
      ↓
Evaluate Response
      ↓
Create Few-Shot Prompt
      ↓
Compare Responses
      ↓
Identify Improvements
```

Prompt engineering is an experimental process.

---

# Best Practices

* Use Zero-Shot for simple, well-known tasks.
* Use Few-Shot when consistency matters.
* Keep examples relevant.
* Use high-quality examples.
* Avoid giving contradictory examples.
* Keep the number of examples small but representative.

---

# Key Concepts Learned

* Prompting
* Zero-Shot Prompting
* Few-Shot Prompting
* Examples
* Pattern Learning
* Prompt Consistency
* Prompt Evaluation
* Prompt Comparison
* Context Window
* Token Usage

---

# Key Takeaway

Zero-shot prompting relies entirely on the model's existing knowledge and requires no examples, making it fast and simple for common tasks. Few-shot prompting teaches the model the desired pattern by providing a small number of examples before the actual task. Although few-shot prompts consume more tokens, they often produce more consistent, accurate, and well-formatted responses, especially for specialized or repetitive tasks. Choosing the right technique depends on the complexity of the task and the level of control required over the output.
