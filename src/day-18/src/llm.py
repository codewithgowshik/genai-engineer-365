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
    model: str = "gemini-2.5-flash",
    show_output: bool = True
):
    # Retry up to 3 times
    for attempt in range(3):

        try:

            # Show spinner while Gemini is generating
            with console.status("Thinking..."):

                # Log request
                logger.info(
                    "Sending request to Gemini..."
                )

                # Combine system prompt with user prompt
                full_prompt = (
                    f"{SYSTEM_PROMPT}\n\n"
                    f"{request.prompt}"
                )

                # Create response stream
                stream = await client.aio.models.generate_content_stream(
                    model=model,
                    contents=full_prompt
                )

                # Collect the complete response
                full_response = ""

                # Process chunks as they arrive
                async for chunk in stream:

                    # Ignore empty chunks
                    if chunk.text:

                        # Add chunk to full response
                        full_response += chunk.text

                        # Print only if requested
                        if show_output:

                            print(
                                chunk.text,
                                end="",
                                flush=True
                            )

                # Move to next line after streaming
                if show_output:
                    print()

                # Log success
                logger.info(
                    "Response received successfully"
                )

            # Return Pydantic response object
            return response(
                answer=full_response
            )

        except Exception as e:

            # Log error
            logger.error(
                f"Attempt {attempt + 1} failed: {e}"
            )

            # Wait before retrying
            await asyncio.sleep(2)

    # Return failure response
    return response(
        answer="Unable to get response from Gemini."
    )