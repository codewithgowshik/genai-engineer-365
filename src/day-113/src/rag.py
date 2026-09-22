from src.search import search


def build_context(query, k=3):
    results = search(query, k=k)
    documents = results["documents"][0]

    context = "\n\n".join(documents)

    return context


def build_prompt(query, context):
    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{query}

Answer using only the provided context.
If the answer cannot be found in the context, say that the information is not available.
"""

    return prompt


def rag_pipeline(query, k=3):
    context = build_context(query, k=k)
    prompt = build_prompt(query, context)

    return {
        "query": query,
        "context": context,
        "prompt": prompt
    }


if __name__ == "__main__":
    query = "How do computers learn from data?"

    result = rag_pipeline(query, k=3)

    print("QUESTION:")
    print(result["query"])

    print("\nRETRIEVED CONTEXT:")
    print(result["context"])

    print("\nRAG PROMPT:")
    print(result["prompt"])
