from langchain_core.prompts import ChatPromptTemplate

chat_template= ChatPromptTemplate([
    ("system"," You are a helpful {domain} expert."),
    ("human","Please summarize the research paper titled {paper_input} with the following specifications")
])

prompt= chat_template.invoke({
    "domain": "cricket",
    "paper_input": "A Comprehensive Study on Quantum Computing"
})

print(prompt) # Output the content of the system message