from src.config import client
from src.schemas.sustainability import SustainabilityReport
from google.genai import types


async def generate(prompt: str):

    response = await client.aio.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=SustainabilityReport,
        ),
    )

    return response.parsed