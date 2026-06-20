from llm import llm
from logger_config import logger
import asyncio

from models import requests
from helper import clean_prompt

# Functions for managing recent conversation memory
from memory import (
    add_to_history,
    add_assistant_response,
    trim_history
)

# Function used to compress old messages into a summary
from summary_memory import summarize_memory

# Functions for saving and loading conversation from JSON
from storage import (
    save_conversation,
    load_conversation
)

logger.info("App is started")


async def main():

    # Load previous history and summary from conversation.json
    history, summary = load_conversation()

    while True:

        # Take user input
        question = input("Ask anything: ")

        # Remove unnecessary spaces
        question = clean_prompt(question)

        # Exit condition
        if question.lower() == "exit":
            break

        # Store the user question in recent history
        add_to_history(
            history,
            question
        )

        # Build the prompt using:
        # 1. Long-term memory (summary)
        # 2. Recent conversation (history)
        request = requests(
            prompt=f"""
Summary:

{summary}

Recent Conversation:

{"\n".join(history)}
"""
        )

        # Send request to Gemini
        response = await llm(
            request
        )

        # Store Gemini's response in history
        add_assistant_response(
            history,
            response.answer
        )

        # If history becomes too large
        if len(history) > 5:

            # Take the older messages
            old_messages = history[:-5]

            # Compress them into a summary
            summary = await summarize_memory(
                summary,
                old_messages
            )

            # Keep only the most recent messages
            trim_history(
                history
            )

        # Save history and summary into conversation.json
        save_conversation(
            history,
            summary
        )


# Run main() only when this file is executed directly
if __name__ == "__main__":
    asyncio.run(main())