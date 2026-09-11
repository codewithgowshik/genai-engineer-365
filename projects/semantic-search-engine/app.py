import streamlit as st
from src.search import search


st.title("Semantic Search Engine")

query = st.text_input("Enter your search query")

if st.button("Search"):

    if query.strip() == "":
        st.warning("Please enter a search query.")

    else:
        results = search(query, k=3)

        st.subheader("Search Results")

        for i, document in enumerate(results["documents"][0]):
            st.write(f"**Result {i + 1}**")
            st.write(document)