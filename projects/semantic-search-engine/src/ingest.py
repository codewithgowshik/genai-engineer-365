import chromadb
from sentence_transformers import SentenceTransformer


# 1. Load the embedding model

model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Connect to Chroma

client = chromadb.PersistentClient(
    path="./chroma_data"
)

collection = client.get_or_create_collection(
    name="documents"
)


# 3. Read the documents

documents = []

with open(
    "data/documents.txt",
    "r",
    encoding="utf-8"
) as file:

    for line in file:

        line = line.strip()

        if line != "":
            documents.append(line)


# 4. Create IDs

ids = []

for i in range(len(documents)):

    ids.append(f"doc{i + 1}")


# 5. Create embeddings

embeddings = model.encode(documents)


# 6. Store documents in Chroma

collection.upsert(
    ids=ids,
    documents=documents,
    embeddings=embeddings.tolist()
)


# 7. Show result

print("Ingestion complete!")
print("Documents stored:", collection.count())