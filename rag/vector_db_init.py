from langchain_qdrant import FastEmbedSparse, RetrievalMode, QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from llms import embeddings
#in memory line
client = QdrantClient(":memory:")

#on disk line, need to edit the path
#client = QdrantClient(path="/tmp/langchain_qdrant")


qdrant = QdrantVectorStore.from_documents(
    docs,
    embedding=embeddings,
    sparse_embedding=sparse_embeddings,
    location=":memory:",
    collection_name="my_documents",
    retrieval_mode=RetrievalMode.HYBRID,
)


#data is kept in memory, may pivot to ondisk storage in the future
client.create_collection(
    collection_name="ai_agent",
    vectors_config=VectorParams(size=3072, distance=Distance.COSINE),
)

vector_store = QdrantVectorStore(
    client=client,
    collection_name="ai_agent",
    embedding=embedding,
)