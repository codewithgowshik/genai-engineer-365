# Day 163: Instruction Dataset (JSONL)

## Objective

Build a small instruction dataset containing examples
that can be used for supervised fine-tuning.

## What is JSONL?

JSONL stands for JSON Lines.

It stores multiple independent JSON objects, with
one JSON object per line.

## Dataset Structure

Each example contains three fields:

- instruction: The task given to the model.
- input: Additional information for the task.
- output: The expected response.

## Dataset Information

- Dataset name: Instruction Dataset
- Format: JSONL
- Number of examples: 10
- File: train.jsonl
- Training approach: Supervised Fine-Tuning (SFT)

## Example

{
  "instruction": "Explain AI in simple English.",
  "input": "",
  "output": "AI allows computers to perform tasks that normally require human intelligence."
}

## Learning Outcomes

1. Understand different types of fine-tuning.
2. Understand supervised fine-tuning.
3. Understand JSONL format.
4. Understand instruction, input and output fields.
5. Create a small instruction dataset.

## Important Note

This is a small educational dataset.
It is not a complete production-ready training dataset.

A real fine-tuning project requires more examples,
data quality checks and an appropriate training format.