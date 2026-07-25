from google.genai import types

from config import tavily_client

# Cap per-result extract length to keep the transcript affordable
MAX_CONTENT_CHARS = 1200


# ---------------------------------------------------------------
# The actual tool implementation
#
# In MANUAL tool calling we execute this ourselves, so it stays a
# plain function that returns JSON-serialisable data. No UI here —
# the agent loop owns the display.
# ---------------------------------------------------------------
def search_web(query: str, max_results: int = 5) -> dict:

    raw = tavily_client.search(
        query=query,
        search_depth="advanced",
        max_results=max_results,
    )

    # Trim Tavily's payload down to what the model actually needs.
    # "advanced" depth returns very long extracts, and every one of
    # those characters is resent on each following turn.
    results = [
        {
            "title": item.get("title"),
            "url": item.get("url"),
            "content": (item.get("content") or "")[:MAX_CONTENT_CHARS],
            "score": item.get("score"),
        }
        for item in raw.get("results", [])
    ]

    return {
        "query": query,
        "answer": raw.get("answer"),
        "results": results,
    }


# ---------------------------------------------------------------
# The declaration Gemini sees
#
# With automatic calling the SDK built this from the signature and
# docstring. Declaring it by hand means we control the wording the
# model reasons over — which is what drives tool-choice quality.
# ---------------------------------------------------------------
SEARCH_WEB_DECLARATION = types.FunctionDeclaration(
    name="search_web",
    description=(
        "Search the live web for current, factual information. Use this "
        "whenever the question depends on recent events, current figures, "
        "prices, dates, or regulations and standards that may have changed, "
        "or on anything you are not confident is up to date. Prefer "
        "searching over guessing when accuracy matters."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "query": types.Schema(
                type=types.Type.STRING,
                description=(
                    "The search query. Write it as a focused, keyword-rich "
                    "phrase rather than a full sentence."
                ),
            ),
            "max_results": types.Schema(
                type=types.Type.INTEGER,
                description="How many results to return (1-10). Defaults to 5.",
            ),
        },
        required=["query"],
    ),
)


# Name -> callable, used by the agent loop to dispatch a function_call
TOOL_REGISTRY = {
    "search_web": search_web,
}

# Everything we expose to Gemini
TOOL_DECLARATIONS = [
    SEARCH_WEB_DECLARATION,
]
