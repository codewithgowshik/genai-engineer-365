import time

from retrieval import retrieve


def run_query(query, k=3):
    """Retrieve documents and measure retrieval time."""

    start_time = time.perf_counter() #  perf_counter used to measure how long would it takes to execute.

    results = retrieve(query, k=k)

    end_time = time.perf_counter()

    latency = end_time - start_time

    documents = results["documents"][0]

    return documents, latency


def main():
    test_queries = [
        "How do computers learn from data?",
        "What is a vector database?",
        "How does semantic search work?",
        "What is the purpose of an API?",
        "What is the capital of the United Kingdom?"
    ]

    total_latency = 0

    print("=" * 60)
    print("LARGER CORPUS RETRIEVAL TEST")
    print("=" * 60)

    for query in test_queries:
        documents, latency = run_query(query, k=3)

        total_latency += latency

        print("\nQuestion:")
        print(query)

        print("\nRetrieved documents:")

        if not documents:
            print("No documents retrieved.")
        else:
            for rank, document in enumerate(documents, start=1):
                print(f"\nResult {rank}:")
                print(document)

        print(f"\nRetrieval latency: {latency:.4f} seconds")
        print("-" * 60)

    average_latency = total_latency / len(test_queries)

    print("\nEXPERIMENT SUMMARY")
    print("=" * 60)
    print("Number of test queries:", len(test_queries))
    print(f"Average retrieval latency: {average_latency:.4f} seconds")


if __name__ == "__main__":
    main()