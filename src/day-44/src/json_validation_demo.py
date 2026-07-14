import asyncio
import json

from pydantic import ValidationError

from llm import llm
from models import requests
from schemas import SustainabilityAnalysis


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

    print("Raw LLM Response:\n")
    print(response.answer)

    try:

        # Remove whitespace
        clean_response = response.answer.strip()

        # Remove Markdown code fences if Gemini adds them
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

        # Convert JSON string into Python dictionary
        data = json.loads(clean_response)

        # Validate JSON against the schema
        analysis = SustainabilityAnalysis(**data)

        print("\n✅ JSON validated successfully!\n")

        print("Topic:")
        print(analysis.topic)

        print("\nSummary:")
        print(analysis.summary)

        print("\nRecommendations:")
        for recommendation in analysis.recommendations:
            print("-", recommendation)

    except json.JSONDecodeError as e:

        print("\n❌ Invalid JSON returned by Gemini.")
        print(e)

    except ValidationError as e:

        print("\n❌ JSON Schema Validation Failed.")
        print(e)


if __name__ == "__main__":
    asyncio.run(main())