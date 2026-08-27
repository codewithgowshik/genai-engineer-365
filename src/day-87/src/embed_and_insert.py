import chromadb
from sentence_transformers import SentenceTransformer


# 1. Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Create a persistent local Chroma database
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# 3. Create or load a collection
collection = client.get_or_create_collection(
    name="document_set"
)


# 4. Document set
documents = [
    "Python is a programming language.",
    "Machine learning allows computers to learn from data.",
    "Deep learning uses neural networks.",
    "Pizza is a popular Italian food.",
    "London is the capital of the United Kingdom.",
    "Paris is the capital of France.",
]


# 5. Convert documents into embeddings
embeddings = model.encode(documents)


# 6. Display embedding information
print("Embedding shape:", embeddings.shape)


# 7. Insert documents + embeddings into Chroma
collection.upsert(
    ids=[
        "doc1",
        "doc2",
        "doc3",
        "doc4",
        "doc5",
        "doc6",
    ],
    documents=documents,
    embeddings=embeddings.tolist(),
)


# 8. Check how many documents are stored
print("Documents stored:", collection.count())


# 9. Search the collection
query = "I want to learn programming."

results = collection.query(
    query_texts=[query],
    n_results=3
)


# 10. Display the results
print("\nQuery:")
print(query)

print("\nMost similar documents:")

for document in results["documents"][0]:
    print("-", document)