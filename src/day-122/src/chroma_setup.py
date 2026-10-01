import chromadb


# 1. Create a persistent local Chroma database
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# 2. Create or load a collection
collection = client.get_or_create_collection(
    name="documents"
)


# 3. Add documents
collection.upsert(
    ids=[
        "doc1",
        "doc2",
        "doc3",
        "doc4"
    ],
    documents=[
        "Python is a programming language.",
        "Machine learning allows computers to learn from data.",
        "Pizza is a popular Italian food.",
        "London is the capital of the United Kingdom."
    ]
)


# 4. Show number of stored documents
print("Documents stored:", collection.count())


# 5. Search the collection
query = "I want to learn about programming."

results = collection.query(
    query_texts=[query],
    n_results=2
)


# 6. Display results
print("\nQuery:")
print(query)

print("\nMost relevant documents:")

for document in results["documents"][0]:
    print("-", document)