from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Items we want to search
items = [
    "I love programming in Python.",
    "Python is my favourite programming language.",
    "I enjoy building software.",
    "I enjoy eating pizza.",
    "Pizza is one of my favourite foods.",
    "I love travelling around Europe.",
    "I want to visit France and Italy.",
]


# 3. Create embeddings for the items
item_embeddings = model.encode(items)


# 4. User query
query = "I want to learn Python programming."


# 5. Create embedding for the query
query_embedding = model.encode([query])


# 6. Calculate similarity
similarities = cosine_similarity(
    query_embedding,
    item_embeddings
)[0]


# 7. Find the most similar item
best_index = similarities.argmax()


# 8. Display result
print("Query:", query)

print("\nMost similar item:")
print(items[best_index])

print("\nSimilarity score:")
print(similarities[best_index])