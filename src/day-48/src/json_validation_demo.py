import asyncio
import json

from pydantic import ValidationError

from llm import llm
from models import requests
from schemas import SustainabilityAnalysis


def validate_json(response: str):

    clean_response = response.strip()

    if clean_response.startswith("```json"):
        clean_response = clean_response.replace(
            "```json",
            "",
            1
        )

    if clean_response.startswith("```"):
        clean_response = clean_response.replace(
            "```",
            "",
            1
        )

    if clean_response.endswith("```"):
        clean_response = clean_response[:-3]

    clean_response = clean_response.strip()

    data = json.loads(clean_response)

    return SustainabilityAnalysis(**data)


async def repair_json(previous_response: str):

    repair_prompt = f"""
Your previous response was invalid.

Previous Response:

{previous_response}

Return ONLY valid JSON.

Do NOT include markdown.

Return exactly this schema:

{{
    "topic": "",
    "summary": "",
    "recommendations": []
}}
"""

    request = requests(
        prompt=repair_prompt
    )

    response = await llm(request)

    return response.answer


async def main():

    request = requests(
        prompt="""
You are a sustainability consultant.

Explain Carbon Neutrality in 20 words.

Return ONLY valid JSON.

Do NOT wrap the JSON inside Markdown.

Do NOT include ```json or ```.

Return exactly this schema:

{
    "topic": "",
    "summary": "",
    "recommendations": []
}
"""
    )

    print("Sending request to Gemini...\n")

    response = await llm(request)

    current_response = response.answer

    MAX_RETRIES = 2

    for attempt in range(MAX_RETRIES + 1):

        try:

            analysis = validate_json(current_response)

            print("\nJSON validated successfully!\n")

            print("Topic:")
            print(analysis.topic)

            print("\nSummary:")
            print(analysis.summary)

            print("\nRecommendations:")

            for recommendation in analysis.recommendations:
                print("-", recommendation)

            break

        except (json.JSONDecodeError, ValidationError):

            print(f"\nValidation Failed (Attempt {attempt + 1})")

            if attempt == MAX_RETRIES:

                print("\nMaximum retry limit reached.")

                break

            print("\nRequesting Gemini to repair the JSON...\n")

            current_response = await repair_json(
                current_response
            )


if __name__ == "__main__":
    asyncio.run(main())