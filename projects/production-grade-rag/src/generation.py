import os
from collections.abc import Iterator

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing from your .env file.")

client = genai.Client(api_key=API_KEY)


def generate_answer(
    question: str,
    passages: list[dict],
) -> Iterator[str]:
    """Stream an answer grounded in retrieved passages."""

    if not passages:
        yield "I couldn't find relevant information in the available documents."
        return

    context_parts = []

    for passage in passages:
        citation_id = passage.get("citation_id", "?")
        source = passage.get("source", "unknown")
        chunk_id = passage.get("chunk_id", "unknown")
        text = passage.get("text", "")

        context_parts.append(
            f"[{citation_id}] Source: {source} | "
            f"Chunk: {chunk_id}\n{text}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are a helpful assistant answering questions using the supplied documents.

Rules:
- Use the supplied document passages as your factual evidence.
- Do not invent facts that are not supported by the passages.
- If the passages do not contain enough information, say so.
- Cite supporting passages using their citation numbers, such as [1] or [2].
- Be clear and concise.

DOCUMENT PASSAGES:
{context}

USER QUESTION:
{question}

ANSWER:
"""

    response = client.models.generate_content_stream(
        model=MODEL_NAME,
        contents=prompt,
    )

    for chunk in response:
        if chunk.text:
            yield chunk.text
