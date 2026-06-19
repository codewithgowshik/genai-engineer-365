import os
from dotenv import load_dotenv
from google import genai

# Load values from .env
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("API_KEY")
)
