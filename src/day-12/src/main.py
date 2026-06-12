from llm import llm
from logger_config import logger
import asyncio

logger.info("App is started")


async def main():

    while True:

        question = input("Ask anything: ")

        # Exit condition
        if question.lower() == "exit":
            break
        # llm() already prints the response while streaming
        await llm(question)


# Run main() only when this file is executed directly.
# If another file imports this file, main() will NOT run automatically.
if __name__ == "__main__":
    asyncio.run(main())