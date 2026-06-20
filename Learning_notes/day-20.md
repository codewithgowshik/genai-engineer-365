# Day 20: Building CLI Applications with Typer and Rich

## Objective

Learn how to transform a Python script into a professional command-line application using Typer and Rich.

---

# Topics Covered

* Command Line Interface (CLI)
* Typer
* Rich
* Commands
* Decorators
* Entry points
* `__name__`
* `__main__`

---

# What is a CLI?

CLI stands for:

```text
Command Line Interface
```

A CLI allows users to interact with an application through terminal commands.

Examples:

```bash
git add
git commit
git push
docker run
pip install
```

---

# Typer

Typer is a Python library used to create custom command-line commands.

Installation:

```bash
pip install typer
```

---

# Creating a Typer Application

```python
import typer

app = typer.Typer()
```

Purpose:

Create a CLI application object.

---

# Creating Commands

```python
@app.command()
def hello():

    print(
        "Hello World"
    )
```

Purpose:

Convert a Python function into a terminal command.

---

# Meaning of

```python
@app.command()
```

It tells Typer:

> Register the function below as a command.

---

# Single Command Mode

Example:

```python
import typer

app = typer.Typer()


@app.command()
def hello():

    print(
        "Hello World"
    )


if __name__ == "__main__":

    app()
```

Running:

```bash
python app.py
```

Output:

```text
Hello World
```

Typer treats the only command as the default command.

---

# Multiple Command Mode

Example:

```python
import typer

app = typer.Typer()


@app.command()
def hello():

    print(
        "Hello World"
    )


@app.command()
def bye():

    print(
        "Bye"
    )


if __name__ == "__main__":

    app()
```

Running:

```bash
python app.py hello
```

Output:

```text
Hello World
```

Running:

```bash
python app.py bye
```

Output:

```text
Bye
```

---

# Typer Architecture

```text
Terminal Command
        ↓
Typer
        ↓
Corresponding Function
        ↓
Execution
```

Example:

```text
python app.py hello
        ↓
hello()
        ↓
Hello World
```

---

# Rich

Rich is a library used to beautify terminal output.

Installation:

```bash
pip install rich
```

---

# Creating a Console

```python
from rich.console import Console

console = Console()
```

---

# Printing with Colors

```python
console.print(
    "[green]Hello[/green]"
)
```

Purpose:

Display text with colors.

---

# Panels

```python
from rich.panel import Panel

console.print(
    Panel(
        "Welcome"
    )
)
```

Purpose:

Display information inside a box.

---

# Rules

```python
console.rule(
    "[blue]Gemini Chatbot[/blue]"
)
```

Purpose:

Create a divider.

---

# **name**

Python automatically creates:

```python
__name__
```

Its value depends on how the file is used.

---

# Running Directly

Suppose:

```bash
python app.py
```

Python internally sets:

```python
__name__ = "__main__"
```

---

# Importing

Suppose:

```python
import app
```

Python sets:

```python
__name__ = "app"
```

because the file name is:

```text
app.py
```

---

# Meaning of

```python
if __name__ == "__main__":
```

This checks:

```python
if "__main__" == "__main__":
```

when the file is executed directly.

---

# Purpose

Run code only when the file itself is executed.

Do not run the code automatically when another file imports it.

---

# Example

```python
if __name__ == "__main__":

    app()
```

Meaning:

> Execute app() only if this file is the starting point of the program.

---

# Why is this useful?

Without:

```python
if __name__ == "__main__":
```

importing a file would automatically execute everything inside it.

The condition prevents unwanted execution.

---

# Flow

Running directly:

```text
python app.py
        ↓
__name__ = "__main__"
        ↓
Condition True
        ↓
app()
```

Importing:

```text
import app
        ↓
__name__ = "app"
        ↓
Condition False
        ↓
Skip app()
```

---

# Entry Point

```python
if __name__ == "__main__":

    app()
```

acts as the entry point of the application.

It determines where execution starts.

---

# Key Takeaways

* Typer creates command-line applications.
* `app = typer.Typer()` creates a CLI object.
* `@app.command()` converts functions into commands.
* One command becomes the default command.
* Multiple commands become subcommands.
* Rich improves terminal appearance.
* Python automatically creates `__name__`.
* `__main__` is assigned to the file executed directly.
* `if __name__ == "__main__"` prevents accidental execution during imports.
* `app()` starts the Typer application.

---

# Reflection

Today I learned how professional command-line applications are built using Typer and Rich. I understood how decorators transform functions into terminal commands and how Python uses `__name__` and `__main__` to determine the entry point of a program. These concepts help transform simple scripts into reusable and maintainable applications.
