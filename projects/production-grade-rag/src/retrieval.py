import chromadb
from sentence_transformers import SentenceTransformer

CHROMA_PATH = "chroma_data"
COLLECTION_NAME = "knowledge_base"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def retrieve(query: str, k: int = 3) -> dict:
    if not query or not query.strip():
        raise ValueError("query must not be empty")
    if k < 1:
        raise ValueError("k must be at least 1")

    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    if collection.count() == 0:
        raise RuntimeError(
            "The knowledge base is empty. Run ingestion first: "
            "python -m src.ingestion"
        )

    model = SentenceTransformer(EMBEDDING_MODEL)
    query_embedding = model.encode([query], convert_to_numpy=True).tolist()

    return collection.query(
        query_embeddings=query_embedding,
        n_results=min(k, collection.count()),
        include=["documents", "metadatas", "distances"],
    )


if __name__ == "__main__":
    question = input("Ask a question about the documents: ").strip()
    results = retrieve(question, k=3)

    for rank, document in enumerate(results["documents"][0], start=1):
        metadata = results["metadatas"][0][rank - 1]
        distance = results["distances"][0][rank - 1]
        print(
            f"\nResult {rank} | source={metadata.get('source')} "
            f"| distance={distance:.4f}"
        )
        print(document)
