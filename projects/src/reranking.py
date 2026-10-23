from sentence_transformers import CrossEncoder


# A cross-encoder scores each query-passage pair directly.
RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

_model = None


def get_reranker():
    """Load the reranker once and reuse it."""
    global _model

    if _model is None:
        _model = CrossEncoder(RERANKER_MODEL)

    return _model


def rerank_results(query, results, top_k=3):
    """
    Rerank retrieved passages against the query.

    Args:
        query: User's question.
        results: List of retrieval results containing text and metadata.
        top_k: Maximum number of passages to return.

    Returns:
        Passages sorted by reranker score, highest first.
    """
    if not results:
        return []

    model = get_reranker()

    pairs = [
        (query, result["text"])
        for result in results
    ]

    scores = model.predict(pairs)

    ranked_results = []

    for result, score in zip(results, scores):
        ranked_results.append(
            {
                **result,
                "rerank_score": float(score),
            }
        )

    ranked_results.sort(
        key=lambda item: item["rerank_score"],
        reverse=True,
    )

    # Assign citation IDs after reranking.
    for index, result in enumerate(ranked_results[:top_k], start=1):
        result["citation_id"] = index

    return ranked_results[:top_k]