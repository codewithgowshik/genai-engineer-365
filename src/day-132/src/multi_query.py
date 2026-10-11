from src.llm import generate_multi_queries
from src.retrieval import retrieve


def remove_duplicates(documents):

    unique_documents = []

    for document in documents:

        if document not in unique_documents:
            unique_documents.append(document)

    return unique_documents


def multi_query_retrieve(
    query,
    k=3
):

    queries = generate_multi_queries(
        query,
        number_of_queries=3
    )

    all_documents = []

    for search_query in queries:

        results = retrieve(
            search_query,
            k=k
        )

        documents = results["documents"][0]

        for document in documents:

            all_documents.append(document)

    unique_documents = remove_duplicates(
        all_documents
    )

    return queries, unique_documents


def main():

    query = "How do computers learn?"

    print("=" * 60)
    print("MULTI-QUERY RETRIEVAL")
    print("=" * 60)

    print("\nOriginal question:")
    print(query)

    print("\nGenerating search queries...")

    queries, documents = multi_query_retrieve(
        query,
        k=3
    )

    print("\nGenerated queries:")

    for i, search_query in enumerate(queries):

        print(
            f"{i + 1}. {search_query}"
        )

    print("\nCombined results:")

    for i, document in enumerate(documents):

        print(f"\nResult {i + 1}:")
        print(document)

    print("\n")
    print("=" * 60)

    print(
        "TOTAL UNIQUE RESULTS:",
        len(documents)
    )

    print("=" * 60)


if __name__ == "__main__":
    main()