from google import genai
from google.genai import types

from config import GEMINI_API_KEY, MODEL_NAME


client = genai.Client(api_key=GEMINI_API_KEY)


def generate_text(prompt, temperature):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=200,
        ),
    )

    return response.text