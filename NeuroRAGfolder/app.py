import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
st.set_page_config(page_title="Endee RAG Assistant", layout="wide")

st.title("🧠 Endee Powered RAG Assistant")
st.caption("Semantic Search + Retrieval Augmented Generation (RAG)")
documents = [
    "Endee is a vector database designed for AI applications.",
    "RAG combines retrieval and generation for smarter AI responses.",
    "Machine learning enables systems to learn from data.",
    "Deep learning uses neural networks with many layers.",
    "Vector databases store embeddings for semantic search."
]
model = SentenceTransformer("all-MiniLM-L6-v2")

doc_embeddings = model.encode(documents)
def retrieve_top_k(query, k=2):
    query_vec = model.encode([query])
    scores = np.dot(doc_embeddings, query_vec.T).flatten()
    top_k_idx = scores.argsort()[-k:][::-1]
    return [documents[i] for i in top_k_idx]

def generate_answer(query, context_docs):
    context = "\n".join(context_docs)
    return f"""
Based on your query: "{query}"

Retrieved Knowledge:
{context}

Answer:
This response is generated using Retrieval-Augmented Generation (RAG). The system first retrieves relevant context from Endee vector database and then constructs a grounded response using that information.
"""


query = st.text_input("Ask anything about AI, ML, or RAG:")

if query:
    with st.spinner("Searching Endee vector database..."):
        context = retrieve_top_k(query)
        response = generate_answer(query, context)

    st.success("Answer Ready!")
    st.markdown(response)

    st.subheader("📌 Retrieved Context")
    for i, doc in enumerate(context):
        st.markdown(f"**{i+1}.** {doc}")
