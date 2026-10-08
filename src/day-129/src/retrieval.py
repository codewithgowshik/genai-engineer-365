import chromadb
from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"
DATABASE_PATH = "./chroma_data"
COLLECTION_NAME = "documents"


print("Loading embedding model...")

model = SentenceTransformer(MODEL_NAME)


client = chromadb.PersistentClient(
    path=DATABASE_PATH
)


collection = client.get_collection(
    name=COLLECTION_NAME
)


def retrieve(query, k=3):

    query_embedding = model.encode(query)

    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=k
    )

    return results


def get_documents(results):

    return results["documents"][0]


if __name__ == "__main__":

    query = "How do computers learn?"

    results = retrieve(
        query,
        k=3
    )

    documents = get_documents(results)

    print("\nQuery:")
    print(query)

    print("\nResults:")

    for i, document in enumerate(documents):

        print(f"\nResult {i + 1}:")
        print(document)