# Day 014 - Writing Simple Unit Tests with Pytest

## Objective

Learn how to write simple unit tests using pytest and understand how tests help ensure our code behaves as expected.

---

## Topics Covered

### What is Testing?

Testing is the process of verifying that our code works correctly.

Instead of manually checking our code every time, we let a program automatically verify that our functions behave as expected.

---

## Why Do We Need Tests?

Benefits:

* Detect bugs early.
* Prevent breaking existing code.
* Increase confidence when making changes.
* Reduce manual testing.
* Improve code quality.

---

## What is a Unit Test?

A unit test checks one small piece of code.

Examples:

* A helper function.
* A utility function.
* A parser.
* A validator.

Unit tests focus on a single function or component.

---

## What is Pytest?

Pytest is a Python testing framework.

It automatically runs our tests and reports whether they pass or fail.

Flow:

```text
Function
    ↓
Pytest
    ↓
Assert Statements
    ↓

PASS ✓

or

FAIL ✗
```

---

## What is assert?

`assert` checks whether something is True.

Syntax:

```python
assert condition
```

Example:

```python
assert 2 + 3 == 5
```

Python checks:

```text
Is 5 equal to 5?
```

Answer:

```text
Yes
```

Result:

```text
PASS
```

Example:

```python
assert 2 + 3 == 6
```

Python checks:

```text
Is 5 equal to 6?
```

Answer:

```text
No
```

Result:

```text
FAIL
```

---

## Example Function

helper.py

```python
def add(a, b):

    return a + b
```

Test:

test_helper.py

```python
from helper import add


def test_add():

    assert add(2, 3) == 5
```

---

## Naming Convention

Pytest automatically discovers:

Files:

```text
test_*.py
```

Functions:

```text
test_*
```

Example:

```python
def test_add():
```

---

## Running Tests

Install pytest:

```bash
pip install pytest
```

Add to requirements.txt:

```text
google-genai
python-dotenv
rich
pydantic
pytest
```

Run:

```bash
pytest
```

Example output:

```text
====================

1 passed

====================
```

---

## Testing Helper Functions

helpers.py

```python
def clean_prompt(prompt: str):

    return prompt.strip()
```

Purpose:

Remove spaces from the beginning and end of a string.

Example:

```python
clean_prompt(
    "   Hello   "
)
```

Returns:

```text
Hello
```

---

## Test for clean_prompt

test_helpers.py

```python
from helpers import clean_prompt


def test_clean_prompt():

    assert clean_prompt(
        "   Hello   "
    ) == "Hello"
```

---

## How Testing Works

Pytest acts like a user.

Flow:

```text
pytest
   ↓

test_clean_prompt()

   ↓

clean_prompt(
"   Hello   "
)

   ↓

prompt.strip()

   ↓

"Hello"

   ↓

assert "Hello" == "Hello"

   ↓

PASS ✓
```

---

## Why Use Hardcoded Values?

Tests use controlled inputs and known expected outputs.

Example:

```python
assert clean_prompt(
"   Hello   "
) == "Hello"
```

The purpose is not to test the word "Hello".

The purpose is to verify the behavior:

```text
String with spaces
       ↓
clean_prompt()
       ↓
String without spaces
```

The word itself is not important.

Examples:

```python
assert clean_prompt(
"   What is AI?   "
) == "What is AI?"
```

```python
assert clean_prompt(
"   Python   "
) == "Python"
```

The behavior being tested remains the same.

---

## Real Application vs Testing

Real Application:

```text
User
 ↓

input()

 ↓

Function
```

Testing:

```text
Pytest
 ↓

Hardcoded Input

 ↓

Function

 ↓

Expected Output

 ↓

PASS or FAIL
```

Pytest simulates the user.

---

## Breaking the Function

Suppose we accidentally write:

```python
def clean_prompt(prompt):

    return prompt
```

Running:

```bash
pytest
```

Produces:

```text
FAILED

assert "   Hello   " == "Hello"
```

Pytest catches the bug automatically.

---

## What Should We Test?

Good candidates:

* Helper functions.
* Utility functions.
* Pydantic models.
* Parsers.
* Validators.

Examples:

```text
✓ clean_prompt()
✓ Request model
✓ Response model
```

Avoid testing:

```text
✗ Gemini
✗ External APIs
✗ Internet connections
```

These are tested by their providers.

---

