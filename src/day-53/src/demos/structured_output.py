import asyncio

from google.genai import types

from config import client
from schemas import SustainabilityAnalysis


async def main():

    response = await client.aio.models.generate_content(

        model="gemini-2.5-flash",

        contents="""
You are a sustainability consultant.

Explain Carbon Neutrality in about 20 words.

Give three recommendations.
""",

        config=types.GenerateContentConfig(

            response_mime_type="application/json",

            response_schema=SustainabilityAnalysis

        )

    )

    analysis = response.parsed

    print("\nStructured Output Received\n")

    print("Topic:")
    print(analysis.topic)

    print("\nSummary:")
    print(analysis.summary)

    print("\nRecommendations:")

    for recommendation in analysis.recommendations:

        print("-", recommendation)


if __name__ == "__main__":
    asyncio.run(main())