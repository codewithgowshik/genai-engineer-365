# Day 26: Unit Testing & README

## Objective

Learn how to write unit tests for small functions and understand why testing is an important part of software development.

---

# What is Unit Testing?

A unit test checks whether a single function works correctly.

Instead of manually testing every feature, we write code that automatically verifies the output.

Example:

```python
def add(a, b):
    return a + b
```

Test:

```python
def test_add():

    assert add(2, 3) == 5
```

If the result is correct, the test passes.

---

# Why Do We Write Tests?

* Detect bugs early.
* Ensure existing code still works after changes.
* Save time by automating repetitive checks.
* Increase confidence when adding new features.

---

# The Unit Test Workflow

Every unit test follows the same pattern.

```
Prepare Input
      ↓
Call Function
      ↓
Get Result
      ↓
Compare Result using assert
```

---

# Understanding assert

`assert` verifies that a condition is true.

Example:

```python
assert 5 == 5
```

Output:

```
✅ Test Passed
```

Example:

```python
assert 5 == 10
```

Output:

```
❌ AssertionError
```

Meaning the expected value and actual value are different.

---

# Core Functions Tested

## 1. clean_prompt()

Purpose:

* Removes unwanted spaces.

Test:

```python
assert clean_prompt("  hello  ") == "hello"
```

---

## 2. add_to_history()

Purpose:

* Stores the user's message.

Expected:

```python
history = [
    "User: Hello"
]
```

---

## 3. add_assistant_response()

Purpose:

* Stores the AI response.

Expected:

```python
history = [
    "Assistant: Hello"
]
```

---

## 4. trim_history()

Purpose:

* Keeps only the most recent messages.
* Prevents unlimited conversation growth.

Example:

Before:

```
1
2
3
4
5
6
7
```

After:

```
3
4
5
6
7
```

---

## 5. estimate_tokens()

Purpose:

* Estimates the number of tokens in a prompt.

Example:

```python
tokens = estimate_tokens("HelloWorld")

assert tokens == 2
```

---

## 6. calculate_cost()

Purpose:

* Calculates API cost based on input and output tokens.

Example:

```python
cost = calculate_cost(
    1000,
    1000
)

assert cost == 0.0005
```

---

## 7. update_metrics()

Purpose:

* Updates the session statistics.

Updates:

* Total Input Tokens
* Total Output Tokens
* Total Cost

Example:

```python
previous_input = metrics.total_input_tokens

metrics.update_metrics(
    100,
    50,
    25
)

assert metrics.total_input_tokens == previous_input + 100
```

---

## 8. save_conversation() & load_conversation()

Purpose:

* Save conversation to JSON.
* Load the same conversation later.

Test:

```
Save
   ↓
Load
   ↓
Compare
```

Expected:

```
Loaded History == Saved History

Loaded Summary == Saved Summary
```

---

# Why import the metrics module?

Instead of:

```python
from src.metrics import total_input_tokens
```

Use:

```python
import src.metrics as metrics
```

Reason:

The values change during the program, so reading them through the module always gives the latest value.

---

# Why did we store previous values?

Example:

```python
previous_input = metrics.total_input_tokens
```

Reason:

We need to compare the values before and after calling `update_metrics()`.

---

# Running Tests

Run all tests:

```bash
python -m pytest
```

Run one file:

```bash
python -m pytest tests/test.py
```

Verbose mode:

```bash
python -m pytest tests/test.py -vv
```

---

# Understanding the Command

```bash
python -m pytest tests/test.py -vv
```

## python

Runs the Python interpreter.

---

## -m

Runs a Python module as a program.

---

## pytest

Starts the pytest testing framework.

---

## tests/test.py

Runs only the tests inside `tests/test.py`.

---

## -vv

Shows detailed information for every test.

---

# Understanding the Output

```
collected 8 items
```

Meaning:

Pytest found 8 test functions.

---

```
PASSED
```

Meaning:

The function behaved exactly as expected.

---

```
8 passed
```

Meaning:

* All tests executed successfully.
* No assertion failed.
* No syntax errors.
* No import errors.
* All functions worked correctly.

---

# README

A README explains your project.

A good README should include:

* Project name
* Description
* Features
* Installation
* Requirements
* Usage
* Commands
* Folder structure
* Technologies used
* Future improvements

---

# Key Concepts Learned

* Unit Testing
* pytest
* assert
* Test Functions
* Automated Testing
* Test Discovery
* Module Imports
* Project Structure
* Session Metrics Testing
* Saving & Loading Data
* Verbose Test Output

---

# Key Takeaway

Writing tests allows you to verify your code automatically. Every test follows the same cycle: prepare input, call the function, compare the result with `assert`. Running tests with `pytest` ensures that changes to your project do not accidentally break existing functionality.
