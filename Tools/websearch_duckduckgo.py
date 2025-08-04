from langchain_community.tools import DuckDuckGoSearchRun

search_tool= DuckDuckGoSearchRun()

result = search_tool.invoke("Good thing about Bangladesh?")
print("Search Result:")
print(result)
