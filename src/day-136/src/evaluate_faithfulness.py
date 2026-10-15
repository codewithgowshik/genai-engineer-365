import json
import os

from dotenv import load_dotenv
from google import genai

from retrieval import retrieve


# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-2.5-flash"


def generate_answer(question, context):
    """
    Generate an answer using the retrieved context.
    """

    prompt = f"""
You are a helpful question-answering assistant.

Answer the user's question using ONLY the provided context.

If the context does not contain enough information,
say that you do not have enough information.

Do not invent facts.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text.strip()


def evaluate_faithfulness(question, context, answer):
    """
    Use an LLM judge to evaluate answer faithfulness.
    """

    prompt = f"""
You are an evaluator for a Retrieval-Augmented Generation system.

Your task is to evaluate whether the answer is supported
by the provided context.

Do not use outside knowledge to justify claims.

Question:
{question}

Retrieved context:
{context}

Generated answer:
{answer}

Evaluate the answer using these rules:

1. Score 1.0 if all factual claims are supported by the context.
2. Score 0.5 if some claims are supported and others are not.
3. Score 0.0 if the answer is largely unsupported.

An answer saying that the context does not contain enough
information can be faithful if that is accurate.

Return ONLY valid JSON in this format:

{{
    "faithfulness_score": 1.0,
    "explanation": "Explain which claims are supported or unsupported."
}}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    # Parse the judge's JSON response
    result_text = response.text.strip()

    # Handle JSON wrapped in Markdown code fences
    if result_text.startswith("```"):
        lines = result_text.splitlines()
        result_text = "\n".join(
            line for line in lines
            if not line.strip().startswith("```")
        )

    result = json.loads(result_text)

    score = float(result["faithfulness_score"])

    # Validate the score
    if score not in (0.0, 0.5, 1.0):
        raise ValueError(
            f"Unexpected faithfulness score: {score}"
        )

    return result


def main():
    question = "What is semantic search?"

    print("=" * 60)
    print("RAG FAITHFULNESS EVALUATION")
    print("=" * 60)

    # Step 1: Retrieve relevant documents
    results = retrieve(question, k=3)

    documents = results["documents"][0]

    if not documents:
        print("No documents were retrieved.")
        return

    # Step 2: Combine retrieved documents into context
    context = "\n\n".join(documents)

    print("\nQUESTION:")
    print(question)

    print("\nRETRIEVED CONTEXT:")
    print(context)

    # Step 3: Generate an answer
    answer = generate_answer(question, context)

    print("\nGENERATED ANSWER:")
    print(answer)

    # Step 4: Evaluate answer faithfulness
    evaluation = evaluate_faithfulness(
        question,
        context,
        answer
    )

    print("\nFAITHFULNESS EVALUATION:")
    print(
        "Score:",
        evaluation["faithfulness_score"]
    )

    print(
        "Explanation:",
        evaluation["explanation"]
    )

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()