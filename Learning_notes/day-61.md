# Day 61 / 365 – Evaluating Structured Extraction with an Accuracy Test Set

## 🎯 Objective

Today I focused on evaluating the performance of my Structured Extraction Service by creating a small accuracy test set.

Building an AI extraction system is only the first step. To improve it over time, I need a reliable way to measure whether the extracted information is correct. Instead of manually checking every result, I created a small benchmark dataset containing sample documents and their expected structured outputs.

This evaluation process allows me to measure extraction accuracy, identify weak areas, and compare future improvements objectively.

---

# Why Evaluation is Important

An AI system may produce valid JSON but still extract incorrect information.

For example, if a sustainability report states:

- Company: Tesla
- Report Year: 2025
- Net Zero Target: 2040

The model might incorrectly extract:

```json
{
    "company_name": "Tesla",
    "report_year": 2024,
    "net_zero_target": 2050
}
```

Although the JSON format is correct, the extracted information is inaccurate.

Evaluation helps detect these errors and provides confidence that the system is producing reliable results.

---

# What is an Accuracy Test Set?

An accuracy test set is a collection of documents with predefined expected outputs.

Each test case contains:

- Input document
- Expected JSON output
- AI-generated JSON output

The generated output is compared against the expected output to determine how accurately the extraction system performs.

---

# Evaluation Workflow

The evaluation process follows these steps:

```text
Sample PDF

↓

Extraction Engine

↓

Generated JSON

↓

Expected JSON

↓

Compare Fields

↓

Accuracy Report
```

Instead of relying on manual inspection, the system automatically compares extracted values with the expected results.

---

# Test Dataset Structure

To evaluate my extraction system, I organised the project into three main components.

```text
test_data/
│
├── report1.pdf
├── report2.pdf
├── report3.pdf

expected_outputs/
│
├── report1.json
├── report2.json
├── report3.json

tests/
│
└── test_accuracy.py
```

The PDF files represent the input documents, while the JSON files contain the correct expected extraction results.

---

# Ground Truth

The expected JSON is often called the **ground truth**.

It represents the correct values that the extraction system should produce.

Example:

Input document:

```text
Tesla Sustainability Report

Year: 2025

Country: USA

Net Zero Target: 2040
```

Expected JSON:

```json
{
    "company_name": "Tesla",
    "report_year": 2025,
    "country": "USA",
    "net_zero_target": 2040
}
```

The AI-generated output is compared against this reference.

---

# Field-Level Evaluation

Instead of checking whether the entire JSON matches perfectly, each field is evaluated individually.

Example:

| Field | Expected | Generated | Result |
|--------|----------|-----------|--------|
| Company Name | Tesla | Tesla | ✅ |
| Report Year | 2025 | 2025 | ✅ |
| Country | USA | USA | ✅ |
| Net Zero Target | 2040 | 2050 | ❌ |

This makes it easy to identify which specific fields need improvement.

---

# Calculating Accuracy

A simple accuracy metric can be calculated using:

```text
Accuracy = Correct Fields ÷ Total Fields
```

Example:

```
Correct Fields = 8

Total Fields = 10

Accuracy = 80%
```

This provides a clear and objective way to measure extraction performance.

---

# Why Small Test Sets Matter

Even a small collection of representative documents provides valuable insights.

A test set helps to:

- Detect extraction errors
- Measure improvements
- Compare prompt versions
- Prevent regressions
- Validate parser changes
- Increase confidence before deployment

As the project grows, the dataset can be expanded with more document types and scenarios.

---

# Current Evaluation Pipeline

My extraction pipeline now follows this workflow:

```text
PDF

↓

Extract Text

↓

Gemini

↓

Structured JSON

↓

Compare with Expected JSON

↓

Accuracy Report
```

The evaluation process is separate from the extraction process, allowing the quality of the system to be measured independently.

---

# Why Evaluation is Important in AI Engineering

Unlike traditional software, AI systems are probabilistic.

Changing a prompt, parser, or model may improve one document while reducing accuracy on another.

Without evaluation, it is impossible to know whether changes have actually improved the system.

A structured evaluation process provides measurable evidence of performance.

---

# Real-World Applications

Evaluation datasets are used extensively in production AI systems, including:

- Document Intelligence Platforms
- ESG Reporting Tools
- Financial Analysis Systems
- Resume Parsing
- Invoice Processing
- Legal Document Analysis
- Medical Record Extraction

Companies continuously evaluate their AI models to ensure reliability before deploying updates.

---

# Skills Learned

Today I learned:

- Why AI systems require evaluation.
- What an accuracy test set is.
- The concept of ground truth.
- Field-level comparison of structured outputs.
- Measuring extraction accuracy.
- Building repeatable evaluation workflows.
- Using evaluation to improve prompt quality and extraction performance.

---

# Key Takeaways

- Building an AI system is only the first step; measuring its performance is equally important.
- Ground truth data provides a reliable benchmark for comparison.
- Field-level evaluation identifies exactly where extraction errors occur.
- Accuracy testing enables continuous improvement.
- Evaluation is a fundamental part of production AI engineering.

---

# Today's Deliverables

- Created a small accuracy test dataset.
- Defined expected JSON outputs for sample documents.
- Compared extracted results with ground truth.
- Calculated field-level extraction accuracy.
- Established an evaluation workflow for future improvements.

---

# Summary

Today I introduced a structured evaluation process for my Structured Extraction Service by creating a small accuracy test set. Instead of relying solely on manual inspection, I compared AI-generated structured data against predefined expected outputs to measure extraction quality objectively. This evaluation framework provides a repeatable method for tracking improvements, identifying weaknesses, and ensuring that future changes to prompts, parsers, or models enhance the overall reliability of the system. Continuous evaluation is an essential practice in AI engineering because it allows performance to be measured rather than assumed.
