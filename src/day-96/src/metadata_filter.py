import chromadb
from sentence_transformers import SentenceTransformer


# 1. Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Connect to the existing Chroma database
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# 3. Create a separate collection for today's metadata exercise
collection = client.get_or_create_collection(
    name="metadata_demo"
)


# 4. Our existing 4 documents
documents = [
    "Python is a programming language.",
    "Machine learning allows computers to learn from data.",
    "Pizza is a popular Italian food.",
    "London is the capital of the United Kingdom."
]


# 5. Metadata for each document
metadatas = [
    {"category": "programming"},
    {"category": "machine-learning"},
    {"category": "food"},
    {"category": "geography"}
]


# 6. Create embeddings
embeddings = model.encode(documents)


# 7. Store documents, embeddings, IDs and metadata
collection.upsert(
    ids=[
        "doc1",
        "doc2",
        "doc3",
        "doc4"
    ],
    documents=documents,
    embeddings=embeddings.tolist(),
    metadatas=metadatas
)


# 8. Check how many documents are stored
print("Documents stored:", collection.count())


# 9. User query
query = "I want to learn programming."


# 10. Convert the query into an embedding
query_embedding = model.encode(query)


# 11. Search only documents with programming category
results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    where={"category": "programming"},
    n_results=2
)


# 12. Display results
print("\nQuery:")
print(query)

print("\nFiltered results:")

for i, document in enumerate(results["documents"][0]):
    print(f"{i + 1}. {document}")