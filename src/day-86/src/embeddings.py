from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# 1. Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Create sentences
sentences = [
    "I love programming in Python.",
    "Python is my favourite programming language.",
    "I enjoy building software.",
    "I enjoy eating pizza.",
    "Pizza is one of my favourite foods.",
    "I love travelling around Europe.",
]


# 3. Generate embeddings
embeddings = model.encode(sentences)


# 4. Display basic information
print("Number of sentences:", len(sentences))
print("Embedding shape:", embeddings.shape)


# 5. Display each sentence and its first 10 embedding values
for sentence, embedding in zip(sentences, embeddings):
    print("\nSentence:", sentence)
    print("First 10 values:", embedding[:10])


# 6. Calculate cosine similarity
similarities = cosine_similarity(embeddings)


# 7. Display similarity matrix
print("\n" + "=" * 50)
print("COSINE SIMILARITY MATRIX")
print("=" * 50)

print(similarities)


# 8. Find the most similar pair of different sentences
best_score = -1
best_pair = None

for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):

        score = similarities[i][j]

        if score > best_score:
            best_score = score
            best_pair = (i, j)


print("\n" + "=" * 50)
print("MOST SIMILAR SENTENCES")
print("=" * 50)

i, j = best_pair

print("Sentence 1:", sentences[i])
print("Sentence 2:", sentences[j])
print("Cosine similarity:", round(best_score, 4))