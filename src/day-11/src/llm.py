import time  # Used to wait before retrying after a failure

from rich.console import Console  # Used to show the loading spinner

from config import client  # Import the Gemini client created in config.py

from logger_config import logger  # Import the logger object

import asyncio

# Create a Rich console object
console = Console()


async def llm(
    prompt: str,
    model: str = "gemini-2.5-flash"
):
    # Retry the request up to 3 times if an error occurs
    for attempt in range(3):

        try:

            # Show "Thinking..." spinner while Gemini generates the response
            with console.status("Thinking..."):

                # Record that a request is being sent
                logger.info("Sending request to Gemini...")

                # Send the prompt to Gemini
                response = await client.aio.models.generate_content( # client.aio provides async interface.
                    model=model,
                    contents=prompt
                )

                # Record that Gemini responded successfully
                logger.info("Response received successfully")

            # Return only the generated text
            return response.text

        except Exception as e:

            # Record the error message in the logs
            logger.error(
                f"Attempt {attempt + 1} failed: {e}"
            )

            # This task pauses for 2 seconds Other tasks may continue
            await asyncio.sleep(2)

    # If all attempts fail, return a message to the user
    return "Unable to get response from Gemini."