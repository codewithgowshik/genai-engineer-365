import chromadb
from sentence_transformers import SentenceTransformer


# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Connect to Chroma
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# 3. Load your existing collection
collection = client.get_collection(
    name="documents"
)


# 4. Semantic search function
def semantic_search(query, n_results=2):

    # Convert query into an embedding
    query_embedding = model.encode(query)

    # Search Chroma
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )

    return results["documents"][0]


# 5. Test the function
query = "I want to learn programming."

results = semantic_search(query, n_results=2)


print("Query:")
print(query)

print("\nSemantic search results:")

for i, document in enumerate(results):
    print(f"{i + 1}. {document}")