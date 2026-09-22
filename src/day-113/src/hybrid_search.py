import chromadb

from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


client = chromadb.PersistentClient(
    path="./chroma_data"
)


collection = client.get_collection(
    name="documents"
)


def keyword_score(query, document):

    query_words = query.lower().split()

    document_words = document.lower()

    matches = 0

    for word in query_words:

        if word in document_words:
            matches += 1

    if len(query_words) == 0:
        return 0

    return matches / len(query_words)


def hybrid_search(
    query,
    k=3,
    keyword_weight=0.3,
    vector_weight=0.7
):

    query_embedding = model.encode(query)

    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=collection.count(),
        include=[
            "documents",
            "distances"
        ]
    )

    documents = results["documents"][0]

    distances = results["distances"][0]

    ranked_results = []

    for document, distance in zip(
        documents,
        distances
    ):

        vector_score = 1 / (1 + distance)

        keyword = keyword_score(
            query,
            document
        )

        combined_score = (
            keyword * keyword_weight
            + vector_score * vector_weight
        )

        ranked_results.append(
            (
                combined_score,
                document
            )
        )

    ranked_results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return ranked_results[:k]