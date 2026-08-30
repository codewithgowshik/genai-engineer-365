import chromadb


# 1. Connect to the persistent Chroma database
client = chromadb.PersistentClient(
    path="./chroma_data"
)


# 2. Load the existing collection
collection = client.get_collection(
    name="documents"
)


# 3. Check how many documents survived
print("Collection:", collection.name)
print("Documents stored:", collection.count())


# 4. Read the stored documents
data = collection.get(
    include=["documents"]
)


print("\nStored documents:")

for id, document in zip(
    data["ids"],
    data["documents"]
):
    print(f"{id} → {document}")


# 5. Run a query
query = "I want to learn programming."

results = collection.query(
    query_texts=[query],
    n_results=2
)


# 6. Display search results
print("\nQuery:")
print(query)

print("\nMost similar documents:")

for document in results["documents"][0]:
    print("-", document)