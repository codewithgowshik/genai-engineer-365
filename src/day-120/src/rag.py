import chromadb
from sentence_transformers import SentenceTransformer


# 1. LOAD EMBEDDING MODEL


model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. CONNECT TO CHROMA

client = chromadb.PersistentClient(path="./chroma_data")

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

def chunk_documents(documents, chunk_size=100, overlap=20):

    chunks = []

    for document in documents:

        start = 0

        while start < len(document):

            end = start + chunk_size

            chunk = document[start:end]

            chunks.append(chunk)

            start += chunk_size - overlap

    return chunks


# 5. STORE CHUNKS IN CHROMA

def store_chunks(chunks):

    embeddings = model.encode(chunks)

    ids = []

    for i in range(len(chunks)):
        ids.append(f"chunk{i + 1}")

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )

    print("Chunks stored:", len(chunks))


# 6. RETRIEVE RELEVANT CHUNKS

def retrieve(query, k=3):

    query_embedding = model.encode(query)

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=k,
        include=["documents", "distances"]
    )

    return results


# 7. BUILD CONTEXT

def build_context(results):

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    return context


# 8. BUILD RAG PROMPT

def build_prompt(query, context):

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


# 9. SOURCE CITATIONS

def get_sources(results):

    sources = results["ids"][0]

    return sources


# 10. COMPLETE RAG PIPELINE

def rag_pipeline(query, k=3):

    # Retrieve relevant chunks
    results = retrieve(query, k=k)

    # Build context
    context = build_context(results)

    # Build prompt
    prompt = build_prompt(query, context)

    # Get source IDs
    sources = get_sources(results)

    return {
        "query": query,
        "context": context,
        "prompt": prompt,
        "sources": sources
    }


# 11. TEST THE PIPELINE

if __name__ == "__main__":

    # Load documents
    documents = load_documents(
        "data/documents.txt"
    )

    print("Documents loaded:", len(documents))


    # Experiment with chunk size and overlap
    chunks = chunk_documents(
        documents,
        chunk_size=100,
        overlap=20
    )

    print("Chunks created:", len(chunks))


    # Store chunks
    store_chunks(chunks)


    # Ask a question
    query = "How do computers learn from data?"


    # Run RAG
    result = rag_pipeline(
        query,
        k=3
    )


    # Display question
    print("\nQUESTION:")
    print(result["query"])


    # Display retrieved context
    print("\nRETRIEVED CONTEXT:")

    print(result["context"])


    # Display prompt
    print("\nRAG PROMPT:")

    print(result["prompt"])


    # Display sources
    print("\nSOURCES:")

    for source in result["sources"]:
        print("-", source)