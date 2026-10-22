from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "documents.txt"
CHROMA_DIR = BASE_DIR / "chroma_data"

# Configuration
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
COLLECTION_NAME = "knowledge_base"
CHUNK_SIZE = 700
CHUNK_OVERLAP = 100


def load_documents():
    """Load the source document."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Document file not found: {DATA_FILE}")

    text = DATA_FILE.read_text(encoding="utf-8").strip()

    if not text:
        raise ValueError("The document file is empty.")

    return text


def split_into_chunks(text):
    """Split text into overlapping character chunks."""
    chunks = []
    start = 0

    while start < len(text):
        end = min(start + CHUNK_SIZE, len(text))
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == len(text):
            break

        start = end - CHUNK_OVERLAP

    return chunks


def main():
    print("Loading document...")

    text = load_documents()
    chunks = split_into_chunks(text)

    print(f"Created {len(chunks)} chunks.")

    model = SentenceTransformer(MODEL_NAME)

    print("Generating embeddings...")

    embeddings = model.encode(
        chunks,
        normalize_embeddings=True,
        show_progress_bar=True,
    ).tolist()

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    # Replace existing indexed chunks for this source file.
    # This prevents stale chunks when the source document changes.
    existing = collection.get(
        where={"source": DATA_FILE.name},
        include=[],
    )

    if existing["ids"]:
        collection.delete(ids=existing["ids"])

    ids = [
        f"{DATA_FILE.name}_chunk_{index:04d}"
        for index in range(len(chunks))
    ]

    metadatas = [
        {
            "source": DATA_FILE.name,
            "chunk_id": chunk_id,
        }
        for chunk_id in ids
    ]

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    print(f"Indexed {len(chunks)} chunks.")
    print(f"Collection: {COLLECTION_NAME}")
    print("Ingestion completed successfully.")


if __name__ == "__main__":
    main()
