from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans


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


# 3. Convert sentences into embeddings
embeddings = model.encode(sentences)

print("Embedding shape:", embeddings.shape)


# 4. Choose number of clusters
kmeans = KMeans(
    n_clusters=3,
    random_state=17,
    n_init=10
)


# 5. Assign vectors to clusters
labels = kmeans.fit_predict(embeddings)


# 6. Display clusters
for i, sentence in enumerate(sentences):
    print(f"Cluster {labels[i]}: {sentence}")