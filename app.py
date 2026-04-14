from sentence_transformers import SentenceTransformer
import numpy as np

# Sample documents
documents = [
    "AI is transforming the world",
    "Machine learning is a subset of AI",
    "Python is widely used in AI"
]

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert docs to embeddings
doc_embeddings = model.encode(documents)

def retrieve(query):
    query_embedding = model.encode([query])
    similarities = np.dot(doc_embeddings, query_embedding.T)
    return documents[np.argmax(similarities)]

# Simple RAG
query = input("Ask something: ")
result = retrieve(query)

print("Retrieved:", result)
