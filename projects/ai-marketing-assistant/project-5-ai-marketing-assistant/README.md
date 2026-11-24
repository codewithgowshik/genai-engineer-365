# MarketMate AI — Fine-Tuned Marketing Assistant

## Project overview

MarketMate AI is a domain-specific assistant designed to help small businesses and early-stage brands think through marketing tasks and create useful marketing content.

The project will explore whether a language model can be adapted through instruction fine-tuning to produce more consistent, structured and brand-aware marketing assistance.

**Current stage:** Project definition and planning. No model has been trained and no application has been built yet.

## The problem

Small businesses often have limited time and marketing resources. They may struggle to identify their target audience, communicate product benefits, maintain a consistent brand voice, and plan content across social platforms.

Generic AI tools can produce content, but their answers may be inconsistent, generic or disconnected from a business's positioning and objectives.

## Proposed solution

MarketMate AI will act as a marketing strategist and content assistant. It will help a user clarify the marketing goal, understand the intended audience, choose an appropriate message and produce a structured recommendation.

## Intended users

- Small-business owners
- Startup founders
- Solo entrepreneurs
- Freelance marketers
- Social-media managers

## Planned capabilities

1. **Audience understanding** — describe customer segments, needs, motivations and pain points.
2. **Brand positioning** — explain what makes a brand distinct and how it should be positioned.
3. **Brand voice guidance** — adapt wording to a defined tone and communication style.
4. **Content planning** — suggest content themes and platform-appropriate formats.
5. **Social content creation** — draft hooks, captions and calls to action.
6. **Product messaging** — translate product features into relevant customer benefits.
7. **Campaign planning** — propose campaign concepts, objectives, messages and content ideas.
8. **Marketing strategy support** — organise recommendations around a stated business goal.

## Example use case

**User brief:** “I sell oversized T-shirts to university students. I want to introduce a new collection on Instagram.”

A useful response should identify the likely audience, clarify the campaign objective, recommend a suitable message, suggest a content format and draft an example caption. It should avoid inventing product facts, prices, customer results or performance claims.

## Learning and technology direction

The project is intended as a learning project using:

- An open-source language model as the base model
- Instruction-style examples
- Parameter-Efficient Fine-Tuning (PEFT)
- LoRA (Low-Rank Adaptation)
- Hugging Face Transformers and PEFT
- A held-out evaluation set for comparison

The exact base model, dataset and training configuration will be selected after the task and evaluation criteria are finalised.

## Important distinction: fine-tuning, prompting and RAG

- **Prompting** provides instructions and context at the time of a request.
- **RAG** retrieves relevant external information, such as an approved brand guide or product catalogue, and supplies it as context.
- **Fine-tuning** adapts model behaviour using examples. It may help with consistent response patterns, task formats and style, but it does not automatically provide current facts or guarantee better marketing results.

These approaches solve different problems and may be combined.

## Project success criteria

The assistant will be assessed for:

- Relevance to the user's stated objective
- Audience fit
- Clarity and usefulness
- Brand-voice consistency
- Completeness of the requested output
- Following instructions and output constraints
- Avoiding unsupported claims and invented facts

Evaluation should compare the base model and adapted model on the same unseen prompts, with the same generation settings and scoring rubric.

## Scope and limitations

This is an educational prototype, not a replacement for professional marketing judgement. Generated suggestions require human review. The assistant cannot guarantee reach, engagement, leads, sales or return on investment. Marketing effectiveness depends on the product, offer, audience, creative execution, distribution, budget and market conditions.

## Repository guide

- `docs/` — task definition, concepts, dataset plan and evaluation plan
- `data/` — dataset planning notes; actual examples will be added later
- `training/` — fine-tuning concepts and future training notes
- `evaluation/` — evaluation framework and future results

## Current milestone

**Milestone 1: Define the project and its domain task.**

The next milestones are to design high-quality instruction examples, prepare a separate evaluation set, select a suitable base model, run a controlled fine-tuning experiment and document the results.
