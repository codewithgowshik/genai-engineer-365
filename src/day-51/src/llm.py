import asyncio

from rich.console import Console
from config import client
from logger_config import logger
from models import requests, response
from prompts.system_prompts import SYSTEM_PROMPT
from metrics import (
    estimate_tokens,
    calculate_cost,
    update_metrics
)

from google.genai import types
from tools.web_search import search_web
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

                # Pass the plain Python function directly as a tool.
                # The SDK reads its signature + docstring, exposes it to
                # Gemini, and calls it automatically when the model asks.
                api_response = await client.aio.models.generate_content(
                    model=model,
                    contents=full_prompt,
                    config=types.GenerateContentConfig(
                        tools=[search_web],
                    ),
                )

                # Full text of the model's answer
                full_response = api_response.text or ""

                # Print if requested
                if show_output:
                    print(full_response)

                # Log success
                logger.info(
                    "Response received successfully"
                )

            # Calculate input tokens from the prompt
            input_tokens = estimate_tokens(request.prompt)

            # Calculate output tokens from the answer
            output_tokens = estimate_tokens(full_response)

            cost = calculate_cost(input_tokens, output_tokens)
            update_metrics(input_tokens, output_tokens, cost)

            # Return Pydantic response object
            return response(answer=full_response)

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