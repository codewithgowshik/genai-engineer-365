# Day 67 / 365 – Understanding Containerisation and Writing a Professional README

## 🎯 Objective

Today I learned the fundamentals of containerisation and why it is widely used in modern software engineering. I also completed the final README for my Structured Extraction Service, making the project easier for other developers to understand, install, and use.

Although I did not build a Docker container today, I learned the concepts behind containerisation and how it simplifies deployment across different environments.

---

# What is Containerisation?

Containerisation is the process of packaging an application together with everything it needs to run.

A container includes:

- Application source code
- Runtime environment
- Required libraries
- Dependencies
- Configuration

Instead of relying on a developer's local machine, the application runs inside an isolated environment that behaves the same everywhere.

```
Application

↓

Dependencies

↓

Runtime

↓

Container

↓

Runs Anywhere
```

---

# Why Containerisation?

One of the biggest problems in software development is environment inconsistency.

For example:

Developer A has:

- Python 3.13
- Latest libraries

Developer B has:

- Python 3.11
- Missing dependencies

The application may work perfectly on one machine but fail on another.

This problem is commonly described as:

> "It works on my machine."

Containerisation solves this problem by ensuring every developer and deployment environment uses exactly the same software configuration.

---

# What is Docker?

Docker is the most widely used containerisation platform.

It allows developers to package an application into a container and run it consistently across different operating systems and cloud platforms.

Docker is especially popular for:

- Backend services
- APIs
- AI applications
- Microservices
- Cloud deployments

---

# Docker Image

A Docker Image is the blueprint for creating a container.

It contains:

- Base operating system
- Programming language
- Required packages
- Application source code

The image itself does not run.

It is simply a template.

```
Docker Image

↓

Create

↓

Docker Container
```

---

# Docker Container

A Docker Container is a running instance of a Docker Image.

It contains the complete application in an isolated environment.

Every container created from the same image behaves identically.

This guarantees consistent execution regardless of the underlying operating system.

---

# Dockerfile

A Dockerfile is a text file containing instructions for building a Docker Image.

Typical instructions include:

- Selecting a base image
- Installing dependencies
- Copying project files
- Running the application

Example workflow:

```
Dockerfile

↓

Docker Build

↓

Docker Image

↓

Docker Run

↓

Container
```

---

# Why AI Applications Use Docker

Modern AI applications often depend on many external libraries.

Examples include:

- FastAPI
- Pydantic
- PyMuPDF
- Google GenAI SDK
- NumPy

Installing these libraries manually on every machine is time-consuming and error-prone.

Docker packages the entire environment so the AI application behaves consistently everywhere.

---

# Why Documentation Matters

A software project is not complete simply because the code works.

Other developers should be able to:

- Understand the project's purpose.
- Install it.
- Configure it.
- Run it.
- Test it.
- Extend it.

Documentation makes collaboration easier and improves long-term maintainability.

---

# README

The README file is usually the first document another developer reads.

A professional README should explain:

- Project overview
- Features
- Installation steps
- Environment variables
- Running the application
- API usage
- Example requests
- Example responses
- Project structure
- Technology stack
- Future improvements

A clear README reduces setup time and improves the developer experience.

---

# My Structured Extraction Service

By the end of this project, my application contains:

```
Client

↓

FastAPI

↓

API Routes

↓

Extractor

↓

PDF Reader

↓

Prompt Builder

↓

Gemini

↓

Pydantic Validation

↓

Structured JSON Response
```

The application exposes a REST API capable of extracting structured sustainability information from PDF reports.

---

# Current Project Structure

```
structured-extraction-service/

app.py

src/

├── config.py
├── llm.py
├── extractor/
├── prompts/
├── routes/
├── schemas/
└── tools/

uploads/
```

Each module has a single responsibility, making the project modular and maintainable.

---

# Skills Learned

Today I learned:

- What containerisation is.
- Why containerisation solves environment inconsistency.
- The purpose of Docker.
- The difference between a Docker Image and a Docker Container.
- The purpose of a Dockerfile.
- Why AI services commonly use Docker.
- Why professional documentation is important.
- The essential sections of a production-quality README.
- How documentation improves collaboration and maintainability.

---

# Key Takeaways

- Containerisation packages an application with everything it needs to run.
- Docker ensures applications behave consistently across different environments.
- Docker Images are blueprints used to create containers.
- Docker Containers are running instances of Docker Images.
- A Dockerfile defines how an image should be built.
- AI backend services commonly use Docker for deployment.
- A README is an essential part of every software project.
- Good documentation is as important as writing clean code.

---

# Today's Deliverables

- Learned the fundamentals of containerisation.
- Understood the purpose of Docker.
- Learned the difference between Images and Containers.
- Completed the final project README.
- Added installation instructions.
- Added API examples.
- Added project architecture.
- Added technology stack.
- Improved project documentation.

---

# Summary

Today I learned the core concepts of containerisation and how Docker enables software to run consistently across different environments. Although I did not build a Docker container yet, I now understand the relationship between Dockerfiles, Images, and Containers, and why they are widely used for backend and AI applications. I also completed the final README for my Structured Extraction Service, documenting the project's purpose, architecture, installation, API usage, and examples. This improved both the professionalism and maintainability of the project, making it easier for other developers to understand and use.
