import chromadb
from sentence_transformers import SentenceTransformer


# 1. Load embedding model

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# 2. Connect to Chroma

client = chromadb.PersistentClient(
    path="./chroma_data"
)

collection = client.get_collection(
    name="documents"
)


# 3. Search function

def search(query, k=3):

    # Convert query into an embedding
    query_embedding = model.encode(query)

    # Search Chroma
    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=k
    )

    return results


# 4. Test the backend

query = "I want to learn programming"

results = search(query, k=3)

print("Query:")
print(query)

print("\nSearch results:")

for i, document in enumerate(results["documents"][0]):

    print(f"\nResult {i + 1}:")
    print(document)