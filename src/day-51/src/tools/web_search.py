from config import tavily_client
from agentic_ui import searching_web


def search_web(query: str):
    with searching_web():
        response = tavily_client.search(
            query=query,
            search_depth="advanced",
            max_results=5,
        )

    return response