from src.hybrid_search import hybrid_search


test_queries = [
    "Python programming",
    "computers learn from data",
    "Italian food",
    "capital of the United Kingdom"
]


experiments = [
    {
        "name": "Vector Heavy",
        "keyword_weight": 0.3,
        "vector_weight": 0.7
    },
    {
        "name": "Balanced",
        "keyword_weight": 0.5,
        "vector_weight": 0.5
    },
    {
        "name": "Keyword Heavy",
        "keyword_weight": 0.7,
        "vector_weight": 0.3
    }
]


for experiment in experiments:

    print("\n====================")
    print(experiment["name"])
    print("====================")

    for query in test_queries:

        results = hybrid_search(
            query,
            k=3,
            keyword_weight=experiment["keyword_weight"],
            vector_weight=experiment["vector_weight"]
        )

        print("\nQuery:", query)

        for score, document in results:

            print(
                "Score:",
                round(score, 4)
            )

            print(
                "Document:",
                document
            )