# Evaluation Plan — MarketMate AI

## Objective

Test whether adapting the base model improves its ability to complete the defined marketing tasks while avoiding unacceptable errors.

## Comparison

Compare:
1. The original base model
2. The same base model with the trained LoRA adapter

Use the same held-out prompts, prompt instructions and generation settings for both models.

## Evaluation dimensions

| Dimension | What to assess |
|---|---|
| Task relevance | Does the answer address the actual request? |
| Audience fit | Is the message suitable for the stated audience? |
| Brand voice | Does it follow the supplied tone and style? |
| Clarity | Is the answer understandable and well organised? |
| Completeness | Does it include the requested elements? |
| Constraint following | Does it respect channel, length and format requirements? |
| Factual discipline | Does it avoid inventing product facts or unsupported claims? |
| Practical usefulness | Could a business owner reasonably use or adapt the recommendation? |

## Suggested scoring rubric

Use a 1–5 scale for each dimension:

- **1 — Poor:** misses the requirement or contains serious problems.
- **2 — Weak:** partially addresses the requirement, with major gaps.
- **3 — Adequate:** mostly useful but needs noticeable revision.
- **4 — Strong:** meets the requirement with minor improvements needed.
- **5 — Excellent:** fully meets the requirement and is ready for human review.

Scores should be accompanied by short evidence-based notes. A numerical score alone is not enough.

## Test-set design

Include:
- Straightforward caption and hook requests
- Different platforms and audience types
- Brand-voice adaptation tasks
- Campaign-planning briefs
- Product descriptions with strict factual constraints
- Ambiguous requests with missing information
- Requests containing unsupported claims that the assistant should not repeat as facts

## Fair comparison controls

Keep constant:
- Test examples
- System and user prompt wording
- Generation parameters
- Scoring rubric
- Evaluation process

Where possible, have outputs reviewed without revealing which model produced them.

## Reporting

Record the base model identifier, adapter version, dataset version, prompt template, generation settings, evaluation date, scores and reviewer notes.

Do not claim that fine-tuning improved performance unless the results support that conclusion.

## Current status

Evaluation design only. No model has been evaluated and no scores have been produced.
