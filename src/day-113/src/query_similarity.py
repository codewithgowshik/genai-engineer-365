import chromadb
from sentence_transformers import SentenceTransformer


# 1. Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Connect to our existing Chroma database
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# 3. Load the existing collection
collection = client.get_or_create_collection(
    name="documents"
)


# 4. User query
query = "I want to learn coding."


# 5. Convert query into an embedding
query_embedding = model.encode(query)


# 6. Search Chroma using the query embedding
results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=2
)


# 7. Display results
print("Query:")
print(query)

print("\nMost similar documents:")

for i, document in enumerate(results["documents"][0]):
    print(f"{i + 1}. {document}")