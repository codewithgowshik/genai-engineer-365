import time
from rich.console import Console
from config import client

console = Console()


def llm(
    prompt: str,
    model: str = "gemini-2.5-flash"
):
    for attempt in range(3):
        try:
            with console.status("Thinking..."):
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

            return response.text

        except Exception as e:
            print(
                f"Attempt {attempt + 1} failed: {e}"
            )
            time.sleep(2)

    return "Unable to get response from Gemini."
