from config import tavily_client


def search_web(query: str):
    response = tavily_client.search(
        query=query,
        search_depth="advanced",
        max_results=5,
    )
    return response


if __name__ == "__main__":
    result = search_web("Latest CSRD sustainability reporting requirements")
    print(result)