import time
import chromadb
from sentence_transformers import SentenceTransformer


# 1. Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Connect to the persistent Chroma database
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# 3. Load the collection
collection = client.get_collection(
    name="documents"
)


# 4. Query
query = "I want to learn programming."


# 5. Convert query into an embedding
query_embedding = model.encode(query)


# 6. Start timer
start_time = time.perf_counter()


# 7. Run similarity search
results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=2
)


# 8. Stop timer
end_time = time.perf_counter()


# 9. Calculate latency
latency = end_time - start_time


# 10. Display results
print("Query:")
print(query)

print("\nResults:")

for document in results["documents"][0]:
    print("-", document)

print("\nQuery latency:")
print(f"{latency:.6f} seconds")