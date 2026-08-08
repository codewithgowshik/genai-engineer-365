# Day 68 / 365 — Testing and Reproducibility

## 🎯 Objective

Today I learned how automated testing helps make software more reliable and how reproducibility is especially important when building AI applications.

My Structured Extraction Service already works, but a working application is not necessarily a reliable application. As I continue adding features and changing code, I need a way to automatically check that existing functionality still works.

Today's goal was to understand how tests provide that safety net.

---

# 🧪 What Is Automated Testing?

A test is code that checks whether another part of an application behaves as expected.

Instead of manually checking the application every time I make a change, automated tests perform those checks for me.

For example:

```python
assert report.company_name == "Future City Initiative"
```

If the condition is true:

```text
PASSED
```

If the condition is false:

```text
FAILED
```

The main purpose of testing is to detect problems early and give confidence when changing the codebase.

---

# Why Do We Need Tests?

Imagine I change my `SustainabilityReport` model.

The change might accidentally affect another part of the extraction pipeline.

Without tests:

```text
Change Code
    ↓
Run Application
    ↓
Manually Check Everything
    ↓
Maybe Something Broke
```

With automated tests:

```text
Change Code
    ↓
Run Tests
    ↓
PASSED / FAILED
```

Tests allow me to make changes without having to manually verify the entire application every time.

---

# 🔁 What Is Reproducibility?

Reproducibility means being able to run the same process again under the same conditions and obtain consistent and understandable results.

For my Structured Extraction Service, I want the same code and configuration to behave predictably when processing the same type of input.

Conceptually:

```text
Same Input
+
Same Code
+
Same Schema
+
Same Prompt
+
Same Configuration
        ↓
Predictable Result
```

Reproducibility is important because it allows developers to understand whether a change in behaviour came from their code or from another factor.

---

# 🤖 Reproducibility in LLM Applications

LLMs are different from normal deterministic functions.

A traditional function may produce the same output every time when given the same input.

An LLM can sometimes produce different wording or responses.

Therefore, I should not build tests that depend on the exact wording of an LLM response.

For example, this is not a good test:

```python
assert response == "Future City Initiative is a smart infrastructure company."
```

The model could express the same information differently.

Instead, I should test important properties of the output.

For example:

```text
Required fields exist
        ↓
Correct data types
        ↓
Valid Pydantic object
        ↓
Important values are correct
```

This makes testing an AI application more reliable.

---

# 🧩 What Should I Test?

My application contains several components:

```text
PDF Reader
     ↓
Prompt Builder
     ↓
LLM
     ↓
Pydantic
     ↓
Extractor
     ↓
FastAPI
```

I don't need to test the entire system at once.

I can start by testing individual components.

This makes it easier to identify exactly where a problem occurs.

---

# 📋 Testing the Sustainability Model

The `SustainabilityReport` is an important part of my application because it defines the structure of the information extracted from sustainability reports.

A test can create a `SustainabilityReport` and verify that the values are stored correctly.

Example:

```python
report = SustainabilityReport(
    company_name="Future City Initiative",
    country="United Kingdom",
    report_year=2026
)

assert report.company_name == "Future City Initiative"
assert report.country == "United Kingdom"
assert report.report_year == 2026
```

This test verifies that the Pydantic model accepts the expected data and stores it correctly.

---

# Testing Optional Values

My sustainability model contains optional fields.

For example:

```python
industry: str | None = None
```

This means that the field can contain a string or `None`.

For example:

```python
report = SustainabilityReport(
    company_name="Future City Initiative"
)

assert report.industry is None
```

This is important for sustainability reports because a document may not contain every field that my application is looking for.

The application should be able to represent missing information without crashing.

---

# Testing Validation

Pydantic also performs type validation.

For example, if my schema expects:

```python
report_year: int | None = None
```

then the application expects a year to be represented as an integer.

A test can verify that invalid data produces a validation error.

Example:

```python
import pytest
from pydantic import ValidationError

with pytest.raises(ValidationError):
    SustainabilityReport(
        company_name="Future City Initiative",
        report_year="not a year"
    )
```

The purpose of this test is to verify that the schema rejects invalid input.

---

# 📝 Testing the Prompt Builder

I can also test my prompt-building code.

For example:

```python
document = "This is a sustainability report."

prompt = build_extraction_prompt(document)

assert document in prompt
```

This test does not test Gemini.

It tests my own code.

The purpose is to make sure the document text is actually included in the prompt before it is sent to the LLM.

---

# 📄 Testing the PDF Reader

I can test whether my PDF reader successfully extracts text from a PDF.

For example:

```python
text = read_pdf("uploads/Report.pdf")

assert text.strip() != ""
```

This verifies that the PDF reader returns readable text.

If the PDF reader stops working after a code change, the test should detect the problem.

---

# ⚠️ Why We Should Not Test Gemini Directly Yet

I should avoid making my basic test suite depend on an exact Gemini response.

For example:

```python
assert response == "Future City Initiative"
```

This is not a good test for an LLM application.

LLM responses can vary, and external API calls can introduce additional problems.

Directly testing the model can also:

- Make tests slower.
- Consume API credits.
- Require an internet connection.
- Depend on an external service.
- Fail because of model behaviour rather than a problem in my code.

For now, I should focus on testing the components that I control directly.

Later, I can learn about **mocking** and how to test the LLM integration separately.

---

# 🧪 What Is Pytest?

`pytest` is a Python testing framework.

I can install it with:

```bash
pip install pytest
```

Then I can run my tests with:

```bash
python -m pytest
```

Pytest automatically discovers test files and test functions.

A typical test file is named:

```text
test_*.py
```

For example:

```text
tests/
├── test_sustainability.py
├── test_prompt.py
└── test_pdf_reader.py
```

A test function normally starts with:

```python
test_
```

Example:

```python
def test_sustainability_report():
    ...
```

---

# 📁 Test Project Structure

My project can contain a dedicated test directory:

```text
structured-extraction-service/

├── app.py
│
├── src/
│   ├── config.py
│   ├── llm.py
│   ├── extractor/
│   ├── prompts/
│   ├── routes/
│   └── tools/
│
├── uploads/
│
└── tests/
    ├── test_sustainability.py
    ├── test_prompt.py
    └── test_pdf_reader.py
```

The `tests/` directory keeps testing code separate from application code.

---

# 📊 Understanding Test Results

When I run:

```bash
python -m pytest
```

pytest discovers my tests and executes them.

A successful test appears as:

```text
PASSED
```

For example:

```text
tests/test_prompt.py PASSED
tests/test_pdf_reader.py PASSED
tests/test_sustainability.py PASSED
```

If a test fails, pytest shows information about the failure so I can investigate the problem.

---

# 🐍 Python Virtual Environment

My project uses a virtual environment so that its dependencies are isolated from the rest of my computer.

On Windows PowerShell, I can activate it with:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the terminal displays:

```text
(.venv)
```

This tells me that the project's virtual environment is active.

I can then run:

```powershell
python -m pytest
```

and pytest will use the Python environment associated with my project.

---

# 🔄 Development Workflow

My development workflow is becoming more professional:

```text
Write Code
    ↓
Run Application
    ↓
Write Tests
    ↓
Run pytest
    ↓
Find Problems
    ↓
Fix Problems
    ↓
Run Tests Again
    ↓
Commit
    ↓
Push to GitHub
```

This is safer than changing code and assuming that everything still works.

---

# 🧠 Unit Testing vs. Full Application Testing

Today I started working with tests for individual components.

For example:

```text
PDF Reader
```

can be tested separately.

The:

```text
Prompt Builder
```

can also be tested separately.

And:

```text
SustainabilityReport
```

can be tested separately.

These are examples of testing individual pieces of an application.

Later, I can test the complete workflow:

```text
PDF
 ↓
FastAPI
 ↓
Extractor
 ↓
Gemini
 ↓
Pydantic
 ↓
JSON
```

That type of testing verifies that multiple components work together.

---

# 🎯 Why Testing Is Important for My AI Project

My application is becoming more complex.

It now contains:

```text
PDF Processing
+
Prompt Engineering
+
LLM Integration
+
Structured Output
+
Pydantic
+
FastAPI
```

Changing one component could potentially affect another component.

Automated tests provide a safety net.

If I change the PDF reader, I can run the tests.

If I change the Pydantic model, I can run the tests.

If I change the prompt builder, I can run the tests.

This allows me to develop the project with more confidence.

---

# 🔑 Key Takeaways

1. **A working application is not necessarily a reliable application.**

2. **Automated tests verify that existing functionality continues to work.**

3. **Reproducibility is important for understanding and maintaining AI systems.**

4. **LLM outputs should not usually be tested as exact strings.**

5. **AI applications should test predictable properties such as schemas, types, required fields, and important values.**

6. **Pydantic validation can be tested independently of the LLM.**

7. **Prompt construction can be tested without calling Gemini.**

8. **PDF extraction can be tested independently.**

9. **Pytest automatically discovers and runs Python tests.**

10. **A virtual environment keeps project dependencies isolated.**

11. **Testing individual components makes it easier to find problems.**

12. **Automated tests make future development safer.**

---

# 🛠️ Today's Practical Work

Today I created a testing structure for the project:

```text
tests/
```

I added tests for important components such as:

```text
test_sustainability.py
test_prompt.py
test_pdf_reader.py
```

I installed pytest:

```bash
pip install pytest
```

I learned how to activate my virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

And I learned how to run the test suite:

```bash
python -m pytest
```

---

# 📦 Today's Deliverables

- [x] Learn what automated testing is.
- [x] Understand reproducibility.
- [x] Create a `tests/` directory.
- [x] Test the sustainability model.
- [x] Test the prompt builder.
- [x] Test the PDF reader.
- [x] Install pytest.
- [x] Activate the Python virtual environment.
- [x] Run tests using `python -m pytest`.
- [x] Understand why LLM outputs should not be tested as exact text.

---

# 📝 Summary

Today I learned how testing and reproducibility help turn an AI application into a more reliable software system. My Structured Extraction Service already performs PDF extraction, prompt construction, Gemini processing, Pydantic validation, and FastAPI API handling. However, without automated tests, changes to the project could introduce bugs without me noticing.

I learned how pytest can automatically test individual components such as the sustainability model, prompt builder, and PDF reader. I also learned that testing AI applications requires a slightly different approach because LLM responses can vary. Instead of testing exact generated text, I should test predictable properties such as data structure, types, required fields, and important values.

This gives my project a testing foundation that I can expand as the application becomes more advanced.
