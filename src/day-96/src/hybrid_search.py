import chromadb
from sentence_transformers import SentenceTransformer


# -----------------------------
# 1. Load model and Chroma
# -----------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path="./chroma_data"
)

collection = client.get_collection(
    name="documents"
)


# -----------------------------
# 2. Keyword score
# -----------------------------

def keyword_score(query, document):

    query_words = query.lower().split()
    document_words = document.lower()

    matches = 0

    for word in query_words:
        if word in document_words:
            matches += 1

    if len(query_words) == 0:
        return 0

    return matches / len(query_words)


# -----------------------------
# 3. Hybrid search
# -----------------------------

def hybrid_search(query, k=3):

    # Get documents
    data = collection.get(
        include=["documents"]
    )

    documents = data["documents"]

    # Create query embedding
    query_embedding = model.encode(query)

    # Get vector search results
    vector_results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=len(documents),
        include=["documents", "distances"]
    )

    vector_documents = vector_results["documents"][0]
    distances = vector_results["distances"][0]

    results = []

    for document, distance in zip(
        vector_documents,
        distances
    ):

        # Convert distance into a simple similarity score
        vector_score = 1 / (1 + distance)

        keyword = keyword_score(
            query,
            document
        )

        combined_score = (
            keyword * 0.3
            +
            vector_score * 0.7
        )

        results.append(
            (combined_score, document)
        )

    # Highest score first
    results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return results[:k]


# -----------------------------
# 4. Test
# -----------------------------

query = "Python programming"

results = hybrid_search(
    query,
    k=3
)

print("Query:", query)

print("\nHybrid search results:")

for i, (score, document) in enumerate(results):

    print(f"\nResult {i + 1}")
    print("Score:", round(score, 4))
    print("Document:", document)