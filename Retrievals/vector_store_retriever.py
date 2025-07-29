from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

embedding = OllamaEmbeddings(model="llama3.2")

docs =[
    Document(page_content="The geopolitical history of India and Bangladesh from the perspective of a Chinese."),
    Document(page_content="The economic relations between India and Bangladesh in the 21st century."),
    Document(page_content="Cultural exchanges between India and Bangladesh: A historical overview."),
    Document(page_content="The impact of colonialism on India and Bangladesh's modern relations."),
    Document(page_content="Environmental challenges faced by India and Bangladesh in the context of climate change.")
]
vector_store = Chroma.from_documents(
    collection_name="india_bangladesh",
    embedding=embedding,
    persist_directory="vector_store",
    documents=docs
)


retriever = vector_store.as_retriever(
    search_kwargs={ "k": 2 }
)

query = "the geopolitical history of india and Bangladesh from the perspective of a chinese"

result = retriever.invoke(query)

for i , doc in enumerate(result):
    print(f"Document {i+1}:")
    print(f"Content: {doc.page_content}")
    print('---------------------------------')
