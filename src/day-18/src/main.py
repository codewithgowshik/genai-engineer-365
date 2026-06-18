from llm import llm
from logger_config import logger
import asyncio

from models import requests
from helper import clean_prompt

from memory import (
    add_to_history,
    history,
    add_assistant_response,
    trim_history,
    summary
)

from summary_memory import summarize_memory

logger.info("App is started")


async def main():

    global summary # because we declared the variable as a global in the memory.py

    while True:

        question = input("Ask anything: ")

        question = clean_prompt(
            question
        )

        # Exit condition
        if question.lower() == "exit":
            break

        # Store user message
        add_to_history(
            history,
            question
        )

        # Build prompt using summary + recent history
        request = requests(
            prompt=f"""
Summary:

{summary}

Recent Conversation:

{"\n".join(history)}
"""
        )

        # Generate response
        response = await llm(
            request
        )

        # Store assistant response
        add_assistant_response(
            history,
            response.answer
        )

        # If history grows too large
        if len(history) > 5:

            # Extract old messages
            old_messages = history[:-5]

            # Compress old messages into summary
            summary = await summarize_memory(
                summary,
                old_messages
            )

            # Keep only recent messages
            trim_history(
                history
            )


# Run main() only when executed directly
if __name__ == "__main__":
    asyncio.run(main())