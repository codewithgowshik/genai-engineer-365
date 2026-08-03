from src.config import client
from google.genai import types


async def generate(prompt: str, model: str = "gemini-2.5-flash") -> str:

    response = await client.aio.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig()
    )

    return response.text