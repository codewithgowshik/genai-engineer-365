# Day 29: Making a Python CLI Installable with an Entry Point

## Objective

Learn how to package a Python application so it can be installed and executed as a command-line tool using a custom command.

---

# What is a CLI Application?

A Command Line Interface (CLI) application is a program that users interact with through the terminal.

Examples:

```text
git

pip

pytest

docker

npm
```

Instead of opening a graphical interface, users type commands.

---

# Our CLI Application

Before today, the application was started with:

```bash
python src/main.py
```

After creating an entry point, it can be started with:

```bash
envora
```

This makes the project behave like a professional CLI tool.

---

# What is an Entry Point?

An entry point tells Python:

> "When the user types this command, execute this function."

Example:

```text
User types

envora

↓

Python imports

src.main

↓

Runs

run()
```

The entry point acts as the starting point of the application.

---

# pyproject.toml

`pyproject.toml` is the configuration file for a modern Python project.

It contains information such as:

* Project name
* Version
* Description
* Dependencies
* Build system
* Console scripts

---

# Build System

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
```

Purpose:

Tells Python how to build and install the project.

---

# Project Information

```toml
[project]
name = "envora"
version = "0.1.0"
description = "AI Sustainability Assistant"
requires-python = ">=3.12"
```

Purpose:

Stores the project's metadata.

---

# Project Dependencies

```toml
dependencies = [
    "google-genai",
    "rich",
    "python-dotenv",
    "pydantic",
    "typer"
]
```

Purpose:

Automatically installs the required libraries when someone installs the project.

---

# Console Script

```toml
[project.scripts]
envora = "src.main:run"
```

Meaning:

```text
envora
      ↓
src.main
      ↓
run()
```

When the user types `envora`, Python imports `src.main` and calls the `run()` function.

---

# Why Create run()?

Originally:

```python
async def main():
```

The application starts with an asynchronous function.

However, a console script must point to a normal Python function.

Solution:

```python
def run():
    asyncio.run(main())
```

The `run()` function acts as a bridge between the CLI and the asynchronous application.

---

# Understanding asyncio.run()

```python
asyncio.run(main())
```

Purpose:

* Creates an asynchronous event loop.
* Executes the `main()` coroutine.
* Closes the event loop when the application finishes.

Flow:

```text
run()
   ↓
Create Event Loop
   ↓
Execute main()
```

---

# Why Keep This Block?

```python
if __name__ == "__main__":
    run()
```

Purpose:

Allows the application to work in two different ways.

### Method 1

```bash
python src/main.py
```

Python runs the file directly.

### Method 2

```bash
envora
```

Python imports the module and executes `run()` through the entry point.

This makes the application usable both during development and after installation.

---

# Installing the Project

Command:

```bash
pip install -e .
```

Meaning:

* Install the current project.
* `-e` stands for **editable mode**.
* Changes made to the source code are reflected immediately without reinstalling.

---

# Editable Mode

Without editable mode:

```text
Modify Code

↓

Reinstall Package
```

With editable mode:

```text
Modify Code

↓

Run Again

↓

Changes are available immediately
```

This is ideal during development.

---

# Project Execution Flow

```text
User

↓

envora

↓

Console Script

↓

src.main:run

↓

run()

↓

asyncio.run(main())

↓

Application Starts
```

---

# Package Imports

When the project became a package, imports changed from:

```python
from llm import llm
```

to:

```python
from .llm import llm
```

The dot (`.`) tells Python:

> "Import from the current package."

This avoids importing modules with the same name from other installed packages.

---

# Difference Between Function Calls and Imports

Function call (same file):

```python
main()
```

No dot is required because the function is defined in the same file.

Import (another module):

```python
from .helper import clean_prompt
```

The dot tells Python to import from the current package.

---

# Troubleshooting Learned Today

### Missing Version

Error:

```text
project must contain ['version']
```

Cause:

The `version` field was missing in `pyproject.toml`.

---

### Command Not Found

Error:

```text
envora is not recognized
```

Cause:

The project had not been installed successfully.

---

### API Key Error

Error:

```text
No API key was provided.
```

Cause:

The `.env` file was not being loaded correctly, and package imports needed adjustment.

---

# Key Commands Learned

Install project:

```bash
pip install -e .
```

Run application:

```bash
envora
```

Traditional method:

```bash
python src/main.py
```

---

# Key Concepts Learned

* CLI Applications
* Entry Points
* `pyproject.toml`
* Build System
* Project Metadata
* Console Scripts
* Editable Installation (`pip install -e .`)
* `asyncio.run()`
* Event Loop
* Package Imports
* Relative Imports
* `__name__ == "__main__"`

---

# Key Takeaway

Today you transformed your Python script into an installable command-line application. By using `pyproject.toml`, a console script entry point, and a `run()` wrapper, your project can now be launched with a simple command (`envora`) just like professional tools such as `git`, `pip`, and `pytest`. This is a major step from writing standalone scripts to building distributable Python software.
