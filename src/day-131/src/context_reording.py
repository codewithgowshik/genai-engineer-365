def reorder_context(documents):
    """
    Place documents alternately at the beginning and end,
    starting with the first document at the beginning.
    """

    reordered = []

    left = 0
    right = len(documents) - 1

    while left <= right:
        reordered.append(documents[left])
        left += 1

        if left <= right:
            reordered.append(documents[right])
            right -= 1

    return reordered


if __name__ == "__main__":

    documents = [
        "Document A: Highly relevant information.",
        "Document B: Somewhat relevant information.",
        "Document C: Another highly relevant document.",
        "Document D: Less relevant information.",
        "Document E: Important supporting information."
    ]

    print("=" * 50)
    print("CONTEXT REORDERING EXPERIMENT")
    print("=" * 50)

    print("\nOriginal order:")

    for i, document in enumerate(documents, start=1):
        print(f"{i}. {document}")

    reordered_documents = reorder_context(documents)

    print("\nReordered context:")

    for i, document in enumerate(reordered_documents, start=1):
        print(f"{i}. {document}")

    print("\nExperiment complete!")