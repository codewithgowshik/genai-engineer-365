from llm import llm
from logger_config import logger
import asyncio
from models import requests
from helper import clean_prompt
from memory import add_to_history , history ,  add_assistant_response, trim_history

logger.info("App is started")


async def main():
    while True:

        question = input("Ask anything: ")
        question = clean_prompt(question)

        add_to_history(history, question)


        request = requests(
            prompt=question
        )

        # Exit condition
        if question.lower() == "exit":
            break

        #used to combain all request in single list 
        request = requests(
            prompt="\n".join(history)
                                )
        # llm() already prints the response while streaming
        response = await llm(request)
        add_assistant_response(#used to store the ai respone
    history,
    response.answer )
        trim_history(history)

# Run main() only when this file is executed directly.
# If another file imports this file, main() will NOT run automatically.
if __name__ == "__main__":
    asyncio.run(main())