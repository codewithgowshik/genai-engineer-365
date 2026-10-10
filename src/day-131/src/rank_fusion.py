def reciprocal_rank_fusion(result_lists, k=60):
    scores = {}

    for results in result_lists:
        for rank, document in enumerate(results, start=1):

            score = 1 / (k + rank)

            if document not in scores:
                scores[document] = 0

            scores[document] += score

    ranked_results = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked_results


if __name__ == "__main__":

    semantic_results = [
        "Python",
        "Java",
        "C++"
    ]

    keyword_results = [
        "Java",
        "Python",
        "JavaScript"
    ]

    result_lists = [
        semantic_results,
        keyword_results
    ]

    final_results = reciprocal_rank_fusion(result_lists)

    print("=" * 50)
    print("RECIPROCAL RANK FUSION")
    print("=" * 50)

    print("\nSemantic Search:")
    for i, document in enumerate(semantic_results, start=1):
        print(f"{i}. {document}")

    print("\nKeyword Search:")
    for i, document in enumerate(keyword_results, start=1):
        print(f"{i}. {document}")

    print("\nFinal RRF Ranking:")

    for rank, (document, score) in enumerate(final_results, start=1):
        print(
            f"{rank}. {document} "
            f"(score: {score:.6f})"
        )