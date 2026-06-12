import asyncio

from rich.console import Console
from config import client
from logger_config import logger


# Used to display the spinner
console = Console()


async def llm(
    prompt: str,
    model: str = "gemini-2.5-flash"
):
    # Retry up to 3 times
    for attempt in range(3):

        try:

            # Show spinner while Gemini is generating
            with console.status("Thinking..."):

                # Log request
                logger.info("Sending request to Gemini...")

                # Create a response stream
                stream = await client.aio.models.generate_content_stream(
                    model=model,
                    contents=prompt
                )

                # Print chunks as they arrive
                async for chunk in stream:

                    # Ignore empty chunks
                    if chunk.text:

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

            return

        except Exception as e:

            # Log failure
            logger.error(
                f"Attempt {attempt + 1} failed: {e}"
            )

            # Wait before retrying
            await asyncio.sleep(2)

    return "Unable to get response from Gemini."