from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

DATA_PATH = Path("data/documents.txt")
CHROMA_PATH = "chroma_data"
COLLECTION_NAME = "knowledge_base"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def load_text(path: Path = DATA_PATH) -> str:
    if not path.exists():
        raise FileNotFoundError(
            f"Document file not found: {path}. Create it and add some text first."
        )
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError(f"Document file is empty: {path}")
    return text


def chunk_text(text: str, chunk_size: int = 700, overlap: int = 100) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be >= 0 and smaller than chunk_size")

    chunks = []
    start = 0
    while start < len(text):
        chunk = text[start:start + chunk_size].strip()
        if chunk:
            chunks.append(chunk)
        start += chunk_size - overlap
    return chunks


def ingest_documents() -> int:
    chunks = chunk_text(load_text())
    model = SentenceTransformer(EMBEDDING_MODEL)
    embeddings = model.encode(chunks, convert_to_numpy=True).tolist()

    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    ids = [f"documents_chunk_{i}" for i in range(len(chunks))]
    metadatas = [
        {"source": DATA_PATH.name, "chunk_index": i}
        for i in range(len(chunks))
    ]

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )
    return len(chunks)


if __name__ == "__main__":
    count = ingest_documents()
    print(f"Ingested {count} chunks into ChromaDB.")
