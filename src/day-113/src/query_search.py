import chromadb
from sentence_transformers import SentenceTransformer


# -----------------------------
# 1. Load embedding model
# -----------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")


# -----------------------------
# 2. Connect to Chroma
# -----------------------------

client = chromadb.PersistentClient(
    path="./chroma_data"
)

collection = client.get_collection(
    name="documents"
)


# -----------------------------
# 3. User query
# -----------------------------

query = "I want to learn programming"


# -----------------------------
# 4. Convert query into embedding
# -----------------------------

query_embedding = model.encode(query)


# -----------------------------
# 5. Retrieve top-k results
# -----------------------------

k = 3

results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=k
)


# -----------------------------
# 6. Display results
# -----------------------------

print("Query:")
print(query)

print("\nTop", k, "results:")

for i, document in enumerate(results["documents"][0]):

    print(f"\nResult {i + 1}:")
    print(document)