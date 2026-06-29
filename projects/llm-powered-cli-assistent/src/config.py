import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# Get the directory where config.py is located
BASE_DIR = Path(__file__).resolve().parent

# Load the .env file from src/
load_dotenv(BASE_DIR / ".env")

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("API_KEY")
)