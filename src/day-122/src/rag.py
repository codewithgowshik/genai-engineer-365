import chromadb
from sentence_transformers import SentenceTransformer


# 1. LOAD EMBEDDING MODEL

model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. CONNECT TO CHROMA

client = chromadb.PersistentClient(
    path="./chroma_data"
)

collection = client.get_or_create_collection(
    name="rag_documents"
)


# 3. LOAD DOCUMENTS

def load_documents(file_path):

    documents = []

    with open(file_path, "r", encoding="utf-8") as file:

        for line in file:

            line = line.strip()

            if line != "":
                documents.append(line)

    return documents


# 4. CHUNK DOCUMENTS

def chunk_documents(
    documents,
    chunk_size=100,
    overlap=20
):

    chunks = []

    for document_index, document in enumerate(documents):

        start = 0

        while start < len(document):

            end = start + chunk_size

            chunk = document[start:end]

            chunks.append({
                "text": chunk,
                "parent_id": f"parent{document_index + 1}"
            })

            start += chunk_size - overlap

    return chunks


# 5. CREATE METADATA

def create_metadata(chunk, index):

    text = chunk["text"].lower()

    # Simple topic classification
    # This is only for today's metadata experiment.

    if any(word in text for word in [
        "python",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "semantic search",
        "embedding",
        "vector",
        "database",
        "api",
        "programming",
        "software"
    ]):

        topic = "technology"

    elif any(word in text for word in [
        "london",
        "nottingham",
        "leicester",
        "united kingdom",
        "england"
    ]):

        topic = "location"

    elif any(word in text for word in [
        "pizza",
        "coffee",
        "food",
        "beverage"
    ]):

        topic = "food"

    else:

        topic = "general"

    return {
        "source": "documents.txt",
        "topic": topic,
        "parent_id": chunk["parent_id"]
    }


# 6. STORE CHUNKS IN CHROMA

def store_chunks(chunks):

    texts = []

    ids = []

    metadatas = []

    for i, chunk in enumerate(chunks):

        texts.append(chunk["text"])

        ids.append(
            f"chunk{i + 1}"
        )

        metadata = create_metadata(
            chunk,
            i
        )

        metadatas.append(metadata)

    # Create embeddings
    embeddings = model.encode(texts)

    # Store everything in Chroma
    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    print("Chunks stored:", len(texts))


# 7. RETRIEVE DOCUMENTS

def retrieve(
    query,
    k=3,
    topic=None
):

    # Convert question into embedding
    query_embedding = model.encode(query)

    # Build query arguments
    query_arguments = {
        "query_embeddings": [
            query_embedding.tolist()
        ],
        "n_results": k,
        "include": [
            "documents",
            "distances",
            "metadatas"
        ]
    }

    # Add metadata filter if provided
    if topic is not None:

        query_arguments["where"] = {
            "topic": topic
        }

    # Search Chroma
    results = collection.query(
        **query_arguments
    )

    return results


# 8. BUILD CONTEXT

def build_context(results):

    documents = results["documents"][0]

    context = "\n\n".join(
        documents
    )

    return context


# 9. BUILD RAG PROMPT

def build_prompt(
    query,
    context
):

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{query}

Answer using only the provided context.

If the answer cannot be found in the context,
say that the information is not available.
"""

    return prompt


# 10. GET SOURCE CITATIONS

def get_sources(results):

    sources = []

    ids = results["ids"][0]

    metadatas = results["metadatas"][0]

    for chunk_id, metadata in zip(
        ids,
        metadatas
    ):

        sources.append({
            "chunk_id": chunk_id,
            "source": metadata["source"],
            "topic": metadata["topic"],
            "parent_id": metadata["parent_id"]
        })

    return sources


# 11. COMPLETE RAG PIPELINE

def rag_pipeline(
    query,
    k=3,
    topic=None
):

    # Retrieve relevant chunks
    results = retrieve(
        query,
        k=k,
        topic=topic
    )

    # Build context
    context = build_context(
        results
    )

    # Build prompt
    prompt = build_prompt(
        query,
        context
    )

    # Get sources
    sources = get_sources(
        results
    )

    return {
        "query": query,
        "context": context,
        "prompt": prompt,
        "sources": sources
    }


# 12. TEST THE SYSTEM

if __name__ == "__main__":

    print("=" * 50)
    print("RAG METADATA FILTER EXPERIMENT")
    print("=" * 50)


    # Load documents

    documents = load_documents(
        "data/documents.txt"
    )

    print(
        "\nDocuments loaded:",
        len(documents)
    )


    # Create chunks

    chunks = chunk_documents(
        documents,
        chunk_size=100,
        overlap=20
    )

    print(
        "Chunks created:",
        len(chunks)
    )


    # Store chunks + metadata

    store_chunks(
        chunks
    )


    # TEST 1
    # Technology filter

    print("\n")
    print("=" * 50)
    print("TEST 1: TECHNOLOGY FILTER")
    print("=" * 50)

    query = (
        "How do computers learn from data?"
    )

    result = rag_pipeline(
        query,
        k=3,
        topic="technology"
    )


    print("\nQUESTION:")
    print(result["query"])


    print("\nRETRIEVED CONTEXT:")
    print(result["context"])


    print("\nSOURCES:")

    for source in result["sources"]:

        print(
            "-",
            source["chunk_id"],
            "| topic:",
            source["topic"],
            "| parent:",
            source["parent_id"]
        )


    # TEST 2
    # Location filter

    print("\n")
    print("=" * 50)
    print("TEST 2: LOCATION FILTER")
    print("=" * 50)

    query = (
        "What is the capital of the United Kingdom?"
    )

    result = rag_pipeline(
        query,
        k=3,
        topic="location"
    )


    print("\nQUESTION:")
    print(result["query"])


    print("\nRETRIEVED CONTEXT:")
    print(result["context"])


    print("\nSOURCES:")

    for source in result["sources"]:

        print(
            "-",
            source["chunk_id"],
            "| topic:",
            source["topic"],
            "| parent:",
            source["parent_id"]
        )


    # TEST 3
    # Food filter

    print("\n")
    print("=" * 50)
    print("TEST 3: FOOD FILTER")
    print("=" * 50)

    query = (
        "What is a popular Italian food?"
    )

    result = rag_pipeline(
        query,
        k=3,
        topic="food"
    )


    print("\nQUESTION:")
    print(result["query"])


    print("\nRETRIEVED CONTEXT:")
    print(result["context"])


    print("\nSOURCES:")

    for source in result["sources"]:

        print(
            "-",
            source["chunk_id"],
            "| topic:",
            source["topic"],
            "| parent:",
            source["parent_id"]
        )


    # TEST 4
    # Wrong filter

    print("\n")
    print("=" * 50)
    print("TEST 4: WRONG FILTER")
    print("=" * 50)

    query = (
        "How do computers learn from data?"
    )

    result = rag_pipeline(
        query,
        k=3,
        topic="location"
    )


    print("\nQUESTION:")
    print(result["query"])


    print("\nRETRIEVED CONTEXT:")

    if len(result["context"]) == 0:

        print(
            "No matching context found."
        )

    else:

        print(
            result["context"]
        )


    print("\nSOURCES:")

    for source in result["sources"]:

        print(
            "-",
            source["chunk_id"],
            "| topic:",
            source["topic"],
            "| parent:",
            source["parent_id"]
        )


    print("\n")
    print("=" * 50)
    print("EXPERIMENT COMPLETE")
    print("=" * 50)