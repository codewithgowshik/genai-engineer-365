from llm import llm
from logger_config import logger
import asyncio
from models import requests, response

logger.info("App is started")


async def main():

    while True:

        question = input("Ask anything: ")

        request = requests(
            prompt=question
        )

        # Exit condition
        if question.lower() == "exit":
            break
        # llm() already prints the response while streaming
        await llm(request)


# Run main() only when this file is executed directly.
# If another file imports this file, main() will NOT run automatically.
if __name__ == "__main__":
    asyncio.run(main())