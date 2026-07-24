import asyncio
import json

from pydantic import ValidationError

from llm import llm
from models import requests
from schemas import ESGClassification


def clean_json(response: str):

    response = response.strip()

    if response.startswith("```json"):
        response = response.replace(
            "```json",
            "",
            1
        )

    if response.startswith("```"):
        response = response.replace(
            "```",
            "",
            1
        )

    if response.endswith("```"):
        response = response[:-3]

    return response.strip()


async def classify_text(text: str):

    request = requests(
        prompt=f"""
You are an ESG classification assistant.

Classify the following statement into ONLY ONE category.

Allowed Categories:

ENVIRONMENT
SOCIAL
GOVERNANCE

Return ONLY valid JSON.

Do NOT include markdown.

Return exactly this schema:

{{
    "category": ""
}}

Statement:

{text}
"""
    )

    print("Sending request to Gemini...\n")

    response = await llm(
        request=request,
        show_output=False
    )

    try:

        clean_response = clean_json(
            response.answer
        )

        data = json.loads(
            clean_response
        )

        classification = ESGClassification(
            **data
        )

        print("Classification Successful\n")

        print(
            f"Category : {classification.category.value}"
        )

    except json.JSONDecodeError as e:

        print("Invalid JSON Returned")
        print(e)

    except ValidationError as e:

        print(" Schema Validation Failed")
        print(e)


async def main():

    text = """
The company reduced carbon emissions
by installing solar panels.
"""

    await classify_text(text)


if __name__ == "__main__":
    asyncio.run(main())