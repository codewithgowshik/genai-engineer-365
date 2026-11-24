# Concepts and Theory — Marketing Assistant

This document explains the marketing and AI concepts that guide MarketMate AI. It is a learning reference, not implementation code.

## 1. Marketing fundamentals

### Marketing objective

The specific outcome a marketing activity is intended to support. Examples include increasing awareness, generating qualified enquiries, encouraging trial or supporting repeat purchases.

An objective should be clear enough to guide the message and later evaluation. “Make a viral post” is not a reliable business objective.

### Target audience

The group of people a business intends to reach. Useful audience descriptions go beyond age or location and consider needs, behaviours, motivations, context and barriers.

### Customer persona

A research-informed representation of a relevant customer segment. A persona can summarise goals, needs, frustrations, buying context and decision factors. It should be based on evidence where possible, not stereotypes or invented certainty.

### Pain point

A problem, frustration or unmet need experienced by a potential customer. Marketing can explain how an offering addresses a relevant need, but must not exaggerate or manufacture a problem.

### Value proposition

A concise explanation of who an offering is for, what value it provides and why it may be preferable to alternatives. A value proposition should be specific and supported by the actual product or service.

### Positioning

The place a brand aims to occupy in the audience's mind relative to alternatives. Positioning involves the intended audience, category, point of difference and supporting reasons to believe.

### Features and benefits

A **feature** describes what a product has or does. A **benefit** explains why that feature matters to a customer. The assistant should connect features to plausible benefits without making claims that the business has not substantiated.

### Brand voice

The consistent personality and communication style expressed through words. A voice may be described using dimensions such as formal/casual, playful/serious, technical/simple or premium/approachable.

### Call to action (CTA)

A clear next step for the audience, such as learn more, compare options, visit a page or contact the business. The CTA should fit the campaign objective and should not create false urgency.

### Marketing funnel

A simplified way to describe stages in a customer journey:
- Awareness: people discover the brand or problem.
- Consideration: people evaluate whether the offering is relevant.
- Conversion: people take the intended action.
- Retention: existing customers continue engaging or purchasing.
- Advocacy: satisfied customers may recommend the brand.

Real customer journeys are not always linear.

## 2. Content and campaign planning

### Content pillar

A recurring theme that helps organise a brand's content. Examples for a clothing brand might include styling ideas, product education, customer stories and behind-the-scenes content.

### Content format

The form used to communicate a message, such as a short video, carousel, static image, story, email or article. The format should support the objective and audience.

### Campaign concept

The central idea that connects a set of marketing activities. A campaign concept should align the audience, objective, message, creative direction, channel and CTA.

### Platform adaptation

Content should be adapted to the conventions and constraints of each channel. Reusing the same wording everywhere may ignore differences in audience expectations, format and context.

## 3. AI and language-model concepts

### Large Language Model (LLM)

A model trained to process and generate language. It predicts likely next tokens based on the context it receives. Fluent output does not guarantee factual accuracy.

### Prompt engineering

The practice of giving the model clear instructions, context, examples and output constraints at request time. It does not update the model's weights.

### Retrieval-Augmented Generation (RAG)

A method that retrieves relevant information from an external source and supplies it to the model as context. For MarketMate AI, this could later provide an approved brand guide, product catalogue or campaign brief. RAG is useful when the information must be updated or traceable.

### Fine-tuning

Additional training that adapts a pretrained model using examples. For this project, the aim is to teach consistent task behaviour, response structure and instruction following. Fine-tuning does not automatically make the model know a business's latest products or market conditions.

### Supervised Fine-Tuning (SFT)

A training approach that uses examples of inputs and desired outputs. The model learns to produce responses similar to the examples. Dataset quality and coverage matter greatly.

### Parameter-Efficient Fine-Tuning (PEFT)

A family of methods that adapts a model while training a smaller subset of parameters or additional parameters, rather than updating all original model weights.

### LoRA (Low-Rank Adaptation)

A PEFT method that adds trainable low-rank matrices to selected model layers. The base model weights are typically frozen while the adapter parameters are trained. The adapter is used with its compatible base model.

### Training data and evaluation data

Training examples are used to update the model. Evaluation examples are held aside to measure performance. Evaluation data should not be included in training; otherwise, results may be misleading.

### Generalisation

The ability to perform well on new examples that differ from the training examples. Memorising training examples is not the same as learning a reusable behaviour.

### Hallucination and unsupported claims

A model may produce plausible-sounding but false details. In marketing, this can lead to invented product features, discounts, testimonials, certifications or performance claims. The assistant should use only supplied or verified facts and flag uncertainty.

## 4. Choosing the right approach

- Use prompting first when clear instructions may be enough.
- Use RAG when the assistant needs current, private or business-specific reference information.
- Consider fine-tuning when repeated tests show that the model struggles with a stable task pattern, output format or style despite good prompting.
- Combine methods when the task needs both consistent behaviour and access to changing facts.

## 5. Responsible marketing principles

- Do not invent testimonials, reviews, endorsements or statistics.
- Do not make unsupported health, financial, environmental or performance claims.
- Do not use deceptive scarcity or false urgency.
- Avoid discriminatory audience assumptions.
- Respect privacy and use customer data only with appropriate permission.
- Make assumptions visible and ask for missing facts when necessary.
- Require human review before publishing consequential marketing claims.
