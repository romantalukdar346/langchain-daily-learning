from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

# Recreate the document objects from the previous data
docs = [
    Document(page_content=(
        """The Grand Canyon is one of the most visited natural wonders in the world.
        Photosynthesis is the process by which green plants convert sunlight into energy.
        Millions of tourists travel to see it every year. The rocks date back millions of years."""
    ), metadata={"source": "Doc1"}),

    Document(page_content=(
        """In medieval Europe, castles were built primarily for defense.
        The chlorophyll in plant cells captures sunlight during photosynthesis.
        Knights wore armor made of metal. Siege weapons were often used to breach castle walls."""
    ), metadata={"source": "Doc2"}),

    Document(page_content=(
        """Basketball was invented by Dr. James Naismith in the late 19th century.
        It was originally played with a soccer ball and peach baskets. NBA is now a global league."""
    ), metadata={"source": "Doc3"}),

    Document(page_content=(
        """The history of cinema began in the late 1800s. Silent films were the earliest form.
        Thomas Edison was among the pioneers. Photosynthesis does not occur in animal cells.
        Modern filmmaking involves complex CGI and sound design."""
    ), metadata={"source": "Doc4"})
]


vector_store= FAISS.from_documents(
    documents=docs,
    embedding=OllamaEmbeddings(model="phi3:mini")
)

retriever = vector_store.as_retriever(search_kwargs={"k": 4})


llm=OllamaLLM(model="phi3:mini")
compressor =LLMChainExtractor.from_llm(llm=llm)

contextual_compression_retriever = ContextualCompressionRetriever(
    base_retriever=retriever,
    base_compressor=compressor
)

query = "What is photosynthesis?"
result = contextual_compression_retriever.invoke(query)

for i, doc in enumerate(result):
    print(f"Result {i + 1}:")
    print(f"Content: {doc.page_content}")
    print("----------------------------------------------------")

