from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore


embedding = OllamaEmbeddings(model="llama3.2")

docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more.")
]

vector_store = FAISS.from_documents(
    documents=docs,
    embedding=embedding
)

mmr_retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.5}
)

query = "What is langchain?"
result = mmr_retriever.invoke(query)

for i , doc in enumerate(result):
    print(f"Result :{i + 1}")
    print(f"Content: {doc.page_content}")
