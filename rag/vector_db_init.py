from langchain_qdrant import QdrantVectorStore, RetrievalMode
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from llms import embeddings

from rag.db_doc import documents, uuids
#in memory line
client = QdrantClient(":memory:")

#on disk line, need to edit the path
#client = QdrantClient(path="/tmp/langchain_qdrant")


#data is kept in memory, may pivot to ondisk storage in the future
client.create_collection(
    collection_name="ai_agent",
    vectors_config=VectorParams(size=768, distance=Distance.COSINE),
)

vector_store = QdrantVectorStore(
    client=client,
    collection_name="ai_agent",
    embedding=embeddings,
    retrieval_mode=RetrievalMode.DENSE,
)

vector_store.add_documents(documents=documents, ids=uuids)

results = vector_store.similarity_search_with_score(
    query="Will it be hot tomorrow", k=1
)
for doc, score in results:
    print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")