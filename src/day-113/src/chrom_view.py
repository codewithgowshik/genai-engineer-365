import chromadb

client = chromadb.PersistentClient(
    path="./chroma_data"
)

print("Collections:")

for collection in client.list_collections():
    print("-", collection.name)
collection = client.get_collection(
    name="document_set"
)

data = collection.get()

print("\nDocuments:")

for id, document in zip(data["ids"], data["documents"]):
    print(f"{id} → {document}")