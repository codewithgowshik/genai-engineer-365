import asyncio

from rich.console import Console
from config import client
from logger_config import logger
from models import requests, response
from system_prompts import SYSTEM_PROMPT

# Used to display the spinner
console = Console()


async def llm(
    request: requests,
    model: str = "gemini-2.5-flash"
):
    # Retry up to 3 times
    for attempt in range(3):

        try:

            # Show spinner while Gemini is generating
            with console.status("Thinking..."):

                # Log request
                logger.info("Sending request to Gemini...")

                #feeding the llm with the system prompts
                full_prompt = f"{SYSTEM_PROMPT} {request.prompt}"

                # Create a response stream
                stream = await client.aio.models.generate_content_stream(
                    model=model,
                    contents=full_prompt # feed the converstion with the system prompt 
                )

                # Print chunks as they arrive
                async for chunk in stream:

                    # Ignore empty chunks
                    if chunk.text:
                        full_response = ""
                        full_response += chunk.text

                        # Print immediately without new line
                        print(
                            chunk.text,
                            end="",
                            flush=True
                        )

                # Move to the next line after streaming finishes
                print()

                # Log success
                logger.info(
                    "Response received successfully"
                )

            return response(
                answer=full_response
            )

        except Exception as e:

            # Log failure
            logger.error(
                f"Attempt {attempt + 1} failed: {e}"
            )

            # Wait before retrying
            await asyncio.sleep(2)

    return "Unable to get response from Gemini."