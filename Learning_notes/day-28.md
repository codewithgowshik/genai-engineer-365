# Day 28: Publishing, Reproducibility & Open Source

## Objective

Learn how to prepare a project for other developers by making it reproducible, documenting it properly, and publishing it publicly.

---

# What is Reproducibility?

Reproducibility means another developer can download your project and run it successfully without changing your code.

A reproducible project should always produce the same behaviour.

---

# Why is Reproducibility Important?

Without reproducibility:

* Different package versions may cause errors.
* Features may stop working.
* Bugs become difficult to reproduce.

With reproducibility:

* Everyone uses the same environment.
* Bugs are easier to debug.
* Projects are easier to maintain.

---

# Dependency Management

Python projects depend on external libraries.

Example:

```text
google-genai

rich

typer

pydantic
```

These libraries are installed using **pip**.

---

# requirements.txt

The `requirements.txt` file stores all project dependencies.

Example:

```text
google-genai==1.24.0

rich==14.0.0

pytest==9.1.1

python-dotenv==1.1.1

pydantic==2.11.7
```

The `==` symbol pins the exact version.

---

# Pinned Dependencies

Instead of:

```text
rich
```

Use:

```text
rich==14.0.0
```

Reason:

Every developer installs exactly the same version.

---

# Generating requirements.txt

Command:

```bash
pip freeze > requirements.txt
```

Purpose:

Export all installed packages with their versions.

---

# Installing Dependencies

Command:

```bash
pip install -r requirements.txt
```

Purpose:

Install every package listed in `requirements.txt`.

---

# Why Do We Pin Versions?

Example:

Developer A:

```text
rich==14.0.0
```

Developer B:

```text
rich==15.0.0
```

The project may behave differently.

Pinned versions eliminate this problem.

---

# Project Demonstration

A demo allows others to see the project working before downloading it.

A demo should show:

* Starting the application
* Main features
* Commands
* Expected output

---

# Demo GIF

A demo GIF is a short screen recording demonstrating the application.

Typical flow:

```text
Run Application
        ↓
Ask Question
        ↓
Use Commands
        ↓
Show Features
        ↓
Exit
```

Recommended duration:

30–90 seconds.

---

# Suggested Demo

```text
python src/main.py

↓

Ask:
"What is ESG?"

↓

/help

↓

/profile teacher

↓

Ask another question

↓

/usage

↓

/save

↓

/exit
```

---

# README Review

A professional README should contain:

* Project title
* Description
* Features
* Installation
* Usage
* Commands
* Folder structure
* Technologies
* Future improvements

The README is the first document users read.

---

# Publishing an Open Source Project

Publishing means making your work available to others.

Typical workflow:

```text
Build
      ↓
Test
      ↓
Document
      ↓
Publish
```

---

# Git Workflow

Stage files:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Complete Project 1 - LLM CLI Assistant"
```

Upload to GitHub:

```bash
git push
```

---

# Why Record a Demo?

A demo helps users understand the project without reading the source code.

Benefits:

* Easier to understand.
* Better GitHub presentation.
* Useful for portfolios.
* Helpful for recruiters.

---

# Why Write Articles?

Writing helps:

* Reinforce learning.
* Build a public portfolio.
* Demonstrate communication skills.
* Track long-term progress.

---

# What is Technical Writing?

Technical writing explains technical concepts clearly.

Examples:

* README
* Documentation
* Blog posts
* Tutorials

Good technical writing focuses on clarity, accuracy, and structure.

---

# Project Completion Checklist

Before publishing:

* Code works correctly.
* Tests pass.
* README completed.
* Dependencies pinned.
* Demo recorded.
* Repository pushed to GitHub.

---

# Project Lifecycle

```text
Idea
   ↓
Planning
   ↓
Development
   ↓
Testing
   ↓
Documentation
   ↓
Publishing
```

This is the complete software development workflow.

---

# Key Commands Learned

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Freeze dependencies:

```bash
pip freeze > requirements.txt
```

Run project:

```bash
python src/main.py
```

Run tests:

```bash
python -m pytest
```

Push project:

```bash
git add .

git commit -m "Complete Project 1"

git push
```
# Key Takeaway

Building the application is only one part of software engineering. A professional project also includes testing, documentation, reproducible dependencies, version control, and a clear demonstration. Completing these steps makes your project easy for others to understand, run, and contribute to.

