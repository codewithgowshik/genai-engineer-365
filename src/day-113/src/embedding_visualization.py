from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Sentences
sentences = [
    "I love programming in Python.",
    "Python is my favourite programming language.",
    "I enjoy building software.",

    "I enjoy eating pizza.",
    "Pizza is one of my favourite foods.",
    "I love cooking delicious meals.",

    "I love travelling around Europe.",
    "I want to visit France and Italy.",
    "Travelling is one of my favourite hobbies.",
]


# 3. Generate embeddings
embeddings = model.encode(sentences)

print("Original embedding shape:", embeddings.shape)


# 4. Reduce 384 dimensions to 2 dimensions
pca = PCA(n_components=2)

embeddings_2d = pca.fit_transform(embeddings)

print("2D embedding shape:", embeddings_2d.shape)


# 5. Plot the embeddings
plt.figure(figsize=(10, 7))

plt.scatter(
    embeddings_2d[:, 0],
    embeddings_2d[:, 1]
)


# 6. Add sentence labels
for i, sentence in enumerate(sentences):
    plt.annotate(
        sentence,
        (
            embeddings_2d[i, 0],
            embeddings_2d[i, 1]
        )
    )


plt.title("Sentence Embeddings Visualised in 2D")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.tight_layout()
plt.show()