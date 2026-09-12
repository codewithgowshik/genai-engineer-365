import streamlit as st
from src.search import search


st.title("Semantic Search Engine")

query = st.text_input("Enter your search query")

k = st.selectbox(
    "Number of results",
    [1, 2, 3, 4]
)

if st.button("Search"):

    if query.strip() == "":
        st.warning("Please enter a search query.")

    else:
        results = search(query, k=k)

        st.subheader("Search Results")

        documents = results["documents"][0]

        for i, document in enumerate(documents):

            st.write(f"### Result {i + 1}")

            st.write(document)

            st.divider()