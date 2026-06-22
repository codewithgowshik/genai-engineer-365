# Day 22: Define Project 1 and Write the Specification

## Objective

Learn how to define a product before building it.

---

# Topics Covered

* Product thinking
* Scope
* Target users
* Functional requirements
* Non-functional requirements
* Product specifications
* Project structure
* Monorepo organization

---

# From Scripts to Products

Previous weeks focused on:

```text
Python
↓
LLMs
↓
Memory
↓
CLI
```

Week 4 focuses on:

```text
Features
↓
Products
↓
Software Engineering
```

---

# What is a Product?

A product solves a problem for a group of users.

A product answers:

```text
Who is this for?

What problem does it solve?

What features should it have?

What should it not have?
```

---

# Project 1

```text
LLM CLI Assistant
```

---

# Target Users

Users who interact with the product.

Examples:

```text
Students

Developers

AI Enthusiasts

Learners
```

---

# Problem Statement

Users need an AI assistant that runs in the terminal and remembers conversations.

---

# Scope

Scope defines what the application should do.

Included:

```text
Answer questions

Conversation memory

Summary memory

Save and load conversations

Usage metrics

CLI commands
```

---

# Out of Scope

Defines what will NOT be built.

Examples:

```text
GUI

Web application

Authentication

Database

Multi-user support
```

---

# Functional Requirements

Features the system must provide.

Examples:

### Chat

```text
User
↓
Question
↓
Gemini
↓
Response
```

---

### Memory

Short-term memory:

```python
history = []
```

Long-term memory:

```python
summary = ""
```

---

### Persistence

Store memory in:

```text
conversation.json
```

---

### Usage Metrics

Command:

```text
/usage
```

Displays:

```text
Input tokens

Output tokens

Total tokens

Cost
```

---

### Commands

Examples:

```text
/help

/usage

/clear

/exit
```

---

# Non-Functional Requirements

Properties of the system.

Examples:

```text
Maintainable

Simple

Fast

Reliable

Readable
```

---

# Product Specification

A blueprint describing:

```text
Purpose

Users

Features

Architecture

Limitations
```

---

# Folder Structure

Instead of creating a separate repository immediately:

```text
genai-engineer-365/

├── src/
│   ├── day-001
│   ├── day-002
│   └── ...
│
├── projects/
│
│   └── project-1-llm-cli-assistant/
│       ├── src/
│       ├── README.md
│       ├── requirements.txt
│       └── .gitignore
│
└── README.md
```

This structure is called a:

```text
Monorepo
```

---

# Monorepo

A repository containing multiple projects.

Example:

```text
genai-engineer-365
│
├── Learning
│
└── Projects
```

Benefits:

```text
Easy organization

Single GitHub repository

Track progress

Centralized code
```

---

# README.md

Purpose:

Document the project.

Typical sections:

```text
Overview

Features

Installation

Usage

Commands

Future Improvements
```

---

# Architecture

```text
User
    ↓

CLI

    ↓

main.py

    ↓

llm.py

    ↓

Gemini

    ↓

Memory

history + summary

    ↓

storage.py

conversation.json
```

---

# Key Concepts Learned

## Product Thinking

Focus on:

```text
Users

Problems

Solutions
```

instead of just writing code.

---

## Scope

Defines:

```text
What we build

What we do not build
```

---

## Functional Requirements

Features the product must provide.

---

## Non-Functional Requirements

Quality attributes such as:

```text
Maintainability

Reliability

Performance
```

---

## Product Specification

The blueprint of the project.

---

## Monorepo

One repository containing:

```text
Daily Learning

Projects
```

---

# Key Takeaways

* Building software begins with defining the problem.
* Products are designed for users.
* Scope prevents feature creep.
* Specifications act as blueprints.
* README files document projects.
* Monorepos help organize learning and projects.
* Software engineering is about planning as much as coding.

---

# Reflection

Today I learned that software projects should begin with a clear specification rather than immediately writing code. I understood how to define users, scope, requirements, and project structure. This marks the transition from learning individual concepts to designing complete products.
