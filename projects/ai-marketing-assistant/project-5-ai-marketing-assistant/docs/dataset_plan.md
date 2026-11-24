# Dataset Plan — MarketMate AI

## Purpose

Plan a high-quality instruction dataset for the assistant's defined marketing tasks.

## Proposed format

JSONL instruction examples will be considered during the data-building stage. The exact schema and formatting will be finalised after selecting the base model and training framework.

Conceptually, each example should contain:
- An instruction describing the task
- A business brief or input context
- A high-quality target response

## Initial topic coverage

| Category | Initial target |
|---|---:|
| Audience and customer needs | 15 |
| Brand positioning and value proposition | 15 |
| Brand voice adaptation | 15 |
| Social content and captions | 15 |
| Hooks and calls to action | 10 |
| Product messaging | 10 |
| Campaign planning | 10 |
| Marketing strategy support | 10 |
| **Total** | **100** |

These are planning targets, not a claim that 100 examples are sufficient for a production-quality model.

## Quality principles

- Each example must represent a realistic request.
- Target responses must be useful, clear and accurate.
- Include different business types, objectives and audience contexts.
- Include constraints such as tone, channel and length.
- Avoid repetitive examples with only superficial wording changes.
- Do not include private customer information.
- Do not invent product facts, testimonials or performance results.
- Review examples for bias, stereotypes and misleading claims.

## Dataset separation

Create separate training, validation and test sets. Keep the test set isolated from training and model selection. The split should reflect dataset size and diversity; a fixed percentage is not automatically appropriate for every dataset.

## Evaluation coverage

The held-out test set should include examples from every important task category, including requests with missing information, conflicting constraints and requests that should be handled cautiously.

## Current status

Planning only. No dataset has been created, cleaned, validated or used for training yet.
