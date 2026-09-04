import chromadb
from sentence_transformers import SentenceTransformer


# 1. Load embedding model

model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Connect to Chroma

client = chromadb.PersistentClient(
    path="./chroma_data"
)

collection = client.get_collection(
    name="documents"
)


# 3. Keyword search

def keyword_search(query):

    data = collection.get(
        include=["documents"]
    )

    query_words = query.lower().split()

    matches = []

    for document in data["documents"]:

        document_lower = document.lower()

        score = sum(
            word in document_lower
            for word in query_words
        )

        if score > 0:
            matches.append((score, document))

    matches.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        document
        for score, document in matches
    ]


# 4. Semantic search

def semantic_search(query, k=3):

    query_embedding = model.encode(query)

    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=k
    )

    return results["documents"][0]


# 5. Search with fallback

def search(query):

    semantic_results = semantic_search(
        query,
        k=3
    )

    if semantic_results:

        return semantic_results

    return keyword_search(query)


# 6. Test

query = "Python programming"

results = search(query)

print("Query:", query)

print("\nResults:")

for i, document in enumerate(results):

    print(f"\n{i + 1}. {document}")