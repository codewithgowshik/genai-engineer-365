# Day 34: Prompt Iteration & Continuous Integration (CI)

## Objective

Learn how to improve prompts through iteration and understand the basics of Continuous Integration (CI) by automatically checking your code with linting and tests.

---

# What is Prompt Iteration?

Prompt iteration is the process of gradually improving a prompt until it produces the desired response.

Rarely does the first prompt give the perfect answer.

Instead, prompt engineering follows an iterative cycle.

```text
Write Prompt
      ↓
Generate Response
      ↓
Evaluate Response
      ↓
Improve Prompt
      ↓
Generate Again
      ↓
Repeat Until Satisfied
```

Professional AI engineers spend significant time refining prompts rather than rewriting entire applications.

---

# Why Iterate on Prompts?

A prompt may produce responses that are:

* Too short
* Too long
* Too technical
* Missing important information
* Poorly structured

Instead of changing the AI model, improve the prompt.

---

# Example

### First Prompt

```text
Explain ESG.
```

Result:

A general explanation.

---

### Second Prompt

```text
Explain ESG to a university student.
```

Result:

Better because the audience is defined.

---

### Third Prompt

```text
You are an ESG consultant.

Explain ESG to a university student.

Use simple language.
```

Result:

More professional and easier to understand.

---

### Fourth Prompt

```text
You are an ESG consultant.

Explain ESG to a university student.

Use simple language.

Include:

- Definition
- Importance
- Benefits
- Example

Maximum 200 words.
```

Result:

Clear, structured and consistent.

---

# The Prompt Iteration Process

Instead of trying to write the perfect prompt immediately, improve one part at a time.

```text
Original Prompt
       ↓
Improve Role
       ↓
Improve Context
       ↓
Improve Constraints
       ↓
Improve Output Format
       ↓
Final Prompt
```

Small improvements often lead to much better responses.

---

# Evaluating a Prompt

After receiving an AI response, ask:

* Is it accurate?
* Is it complete?
* Is it easy to understand?
* Is it relevant?
* Is it well structured?

If the answer is "No" to any question, improve the prompt.

---

# Prompt Refinement Tips

Instead of making the prompt longer, make it clearer.

Good improvements include:

* Defining the audience
* Assigning a role
* Adding context
* Limiting the response length
* Specifying the output format

---

# What is Continuous Integration (CI)?

Continuous Integration (CI) is a software development practice where code is automatically checked whenever changes are made.

Instead of manually testing everything, CI automatically runs checks.

Typical CI workflow:

```text
Developer Writes Code
          ↓
Push to GitHub
          ↓
CI Starts
          ↓
Run Tests
          ↓
Run Linter
          ↓
Report Success or Failure
```

---

# Why Use CI?

CI helps:

* Detect bugs early
* Prevent broken code from being merged
* Maintain code quality
* Save debugging time

Most professional software projects use CI.

---

# What is a Linter?

A linter checks your source code for:

* Formatting issues
* Style problems
* Unused imports
* Common programming mistakes

A linter improves code quality without changing program behavior.

Popular Python linters include:

* Ruff
* Flake8
* Pylint

---

# What are Automated Tests?

Automated tests verify that your functions behave correctly.

Example:

```python
assert clean_prompt("  hello  ") == "hello"
```

Every time the tests run, Python checks whether the function still works.

---

# Simple CI Pipeline

```text
Write Code
     ↓
Run Tests
     ↓
Run Linter
     ↓
Fix Issues
     ↓
Commit
     ↓
Push
```

This process ensures only working code is committed.

---

# GitHub Actions

GitHub Actions is GitHub's built-in CI system.

It automatically runs workflows stored inside:

```text
.github/

workflows/
```

Example tasks:

* Run pytest
* Run Ruff
* Build project

No manual action is required after pushing.

---

# Why CI Matters

Without CI:

```text
Write Code

↓

Push

↓

Hope Everything Works
```

With CI:

```text
Write Code

↓

Push

↓

Automatic Checks

↓

Receive Feedback
```

CI provides confidence that your project still works.

---

# Best Practices

* Improve prompts gradually.
* Test prompts with multiple examples.
* Keep prompts clear and focused.
* Run tests before committing.
* Use linting to maintain clean code.
* Automate repetitive checks whenever possible.

---

# Key Concepts Learned

* Prompt Iteration
* Prompt Refinement
* Prompt Evaluation
* Continuous Integration (CI)
* Automated Testing
* Linting
* Ruff
* Flake8
* GitHub Actions
* Code Quality

---

# Key Takeaway

Prompt engineering is an iterative process. Instead of expecting the perfect response from the first prompt, evaluate the output and refine the prompt step by step. In software engineering, Continuous Integration follows the same philosophy—automatically checking code quality through tests and linting after every change. Both practices focus on continuous improvement, helping you build more reliable AI applications and higher-quality software.
