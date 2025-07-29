from langchain_community.retrievers import WikipediaRetriever 


retriever = WikipediaRetriever( 
    doc_content_chars_max=500,
    top_k_results=5,
    lang="en" )

# Example usage
query = "the geopolitical history of india and Bangladesh from the perspective of a chinese"
docs = retriever.invoke(query)

for doc in docs:
    print(f"Title: {doc.metadata['title']}")
    print('---------------------------------')

    # print(f"URL: {doc.metadata['url']}")
    # print('---------------------------------')

    print(f"Summary: {doc.metadata['summary']}")
    print('---------------------------------')

    print(f"Content: {doc.page_content}...")


