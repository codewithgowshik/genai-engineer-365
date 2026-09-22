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
# 3. Chunking function
# -----------------------------

def chunk_text(text, chunk_size=100, overlap=20):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# -----------------------------
# 4. Example long text
# -----------------------------

text = """
Python is a programming language that is widely used for software development.
Python is also commonly used in artificial intelligence and machine learning.
Machine learning allows computers to learn patterns from data.
Deep learning uses neural networks to solve complex problems.
Python is popular for data analysis because it has many useful libraries.
Vector databases are used to store and search vector embeddings efficiently.
Semantic search finds information based on meaning rather than exact keywords.
Embeddings represent text as numerical vectors that can be compared for similarity.
"""


# -----------------------------
# 5. Create chunks
# -----------------------------

chunks = chunk_text(
    text,
    chunk_size=100,
    overlap=20
)


print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):

    print(f"\nChunk {i + 1}")
    print(chunk)


# -----------------------------
# 6. Create embeddings
# -----------------------------

embeddings = model.encode(chunks)


# -----------------------------
# 7. Store chunks in Chroma
# -----------------------------

chunk_ids = [
    f"day94_chunk_{i}"
    for i in range(len(chunks))
]

collection.upsert(
    ids=chunk_ids,
    documents=chunks,
    embeddings=embeddings.tolist()
)


print("\nChunks stored in Chroma.")


# -----------------------------
# 8. Semantic search
# -----------------------------

query = "How does semantic search work?"

query_embedding = model.encode(query)


results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=3
)


# -----------------------------
# 9. Display results
# -----------------------------

print("\nSearch results:")

for i, document in enumerate(results["documents"][0]):

    print(f"\nResult {i + 1}")
    print(document)