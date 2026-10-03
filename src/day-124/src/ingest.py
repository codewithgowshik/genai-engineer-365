import chromadb
from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"
DATABASE_PATH = "./chroma_data"
COLLECTION_NAME = "documents"


def load_documents(file_path):
    documents = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if line != "":
                documents.append(line)

    return documents


def create_ids(documents):
    ids = []

    for i in range(len(documents)):
        ids.append(f"doc{i + 1}")

    return ids


def main():

    print("Loading embedding model...")

    model = SentenceTransformer(MODEL_NAME)

    print("Connecting to Chroma...")

    client = chromadb.PersistentClient( # used to save datas
        path=DATABASE_PATH
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    documents = load_documents(
        "data/documents.txt"
    )

    ids = create_ids(documents)

    print("Documents loaded:", len(documents))

    print("Creating embeddings...")

    embeddings = model.encode(documents)

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist()
    )

    print("Ingestion complete!")

    print("Documents stored:", collection.count())


if __name__ == "__main__":
    main()