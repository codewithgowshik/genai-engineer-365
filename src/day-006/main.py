from google import genai
import os
from dotenv import load_dotenv
from rich.console import Console
import time

# Load values from .env
load_dotenv()

# Create Rich console object
console = Console()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("API_KEY")
)


def llm(
    prompt: str,
    model: str = "gemini-2.5-flash"
):
    # Retry up to 3 times
    for attempt in range(3):

        try:
            # Show loading spinner
            with console.status("Thinking..."):

                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

            return response.text

        except Exception:
            print(
                f"Attempt {attempt + 1} failed, retrying..."
            )

            time.sleep(2)

    return "Unable to get response from Gemini."


question = input("Ask anything: ")

print("\nAnswer:")
print(llm(question))
