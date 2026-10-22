from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

from reranking import rerank_results


# Project configuration
BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_DIR = BASE_DIR / "chroma_data"

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
COLLECTION_NAME = "knowledge_base"

RETRIEVAL_K = 10
FINAL_TOP_K = 3


def retrieve_candidates(query, top_k=RETRIEVAL_K):
    """Retrieve candidate passages from ChromaDB."""
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    collection = client.get_collection(
        name=COLLECTION_NAME
    )

    if collection.count() == 0:
        return []

    model = SentenceTransformer(MODEL_NAME)

    query_embedding = model.encode(
        query,
        normalize_embeddings=True,
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(top_k, collection.count()),
        include=["documents", "metadatas", "distances"],
    )

    candidates = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for document, metadata, distance in zip(
        documents,
        metadatas,
        distances,
    ):
        candidates.append(
            {
                "text": document,
                "source": metadata.get("source", "unknown"),
                "chunk_id": metadata.get("chunk_id", "unknown"),
                "vector_distance": float(distance),
            }
        )

    return candidates


def retrieve_and_rerank(query):
    """Retrieve candidates and return the most relevant passages."""
    candidates = retrieve_candidates(query)

    ranked_results = rerank_results(
        query=query,
        results=candidates,
        top_k=FINAL_TOP_K,
    )

    return ranked_results


def main():
    print("Production RAG — Retrieval and Reranking")

    query = input("\nEnter your question: ").strip()

    if not query:
        print("Please enter a question.")
        return

    print("\nRetrieving and reranking passages...")

    results = retrieve_and_rerank(query)

    if not results:
        print("No passages found. Run ingestion first.")
        return

    print("\nTop-ranked passages:\n")

    for result in results:
        citation = result["citation_id"]

        print(f"[{citation}] Source: {result['source']}")
        print(f"Chunk ID: {result['chunk_id']}")
        print(f"Reranker score: {result['rerank_score']:.4f}")
        print(f"Vector distance: {result['vector_distance']:.4f}")
        print(f"Text: {result['text']}")
        print("-" * 60)


if __name__ == "__main__":
    main()
