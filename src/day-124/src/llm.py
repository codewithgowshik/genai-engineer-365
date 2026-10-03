import os

from dotenv import load_dotenv
from google import genai


# Load environment variables from .env
load_dotenv()


# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")


if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found in the .env file."
    )


# Create Gemini client
client = genai.Client(
    api_key=api_key
)


# Gemini model
MODEL_NAME = "gemini-2.5-flash"


def generate_multi_queries(
    query,
    number_of_queries=3
):
    """
    Generate multiple search queries from one user question.
    """

    prompt = f"""
You are a search query generation system.

Generate {number_of_queries} different search queries
for the user's question below.

The queries should:

- Keep the original meaning.
- Use different wording.
- Focus on the information the user wants.
- Help a semantic search system retrieve relevant documents.
- Do not answer the question.

User question:

{query}

Return exactly {number_of_queries} search queries,
one query per line.

Do not add numbering.
Do not add explanations.
"""

    # Send prompt to Gemini
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    # Get Gemini's text response
    text = response.text.strip()

    # Convert response into a list of queries
    queries = []

    for line in text.splitlines():

        line = line.strip()

        if line != "":
            queries.append(line)

    # Make sure we only return the requested number
    return queries[:number_of_queries]


# Test the function directly
if __name__ == "__main__":

    query = "How do computers learn?"

    print("=" * 60)
    print("GEMINI MULTI-QUERY GENERATION")
    print("=" * 60)

    print("\nOriginal query:")
    print(query)

    queries = generate_multi_queries(
        query,
        number_of_queries=3
    )

    print("\nGenerated queries:")

    for i, search_query in enumerate(queries):

        print(f"{i + 1}. {search_query}")

    print("\n")
    print("=" * 60) 