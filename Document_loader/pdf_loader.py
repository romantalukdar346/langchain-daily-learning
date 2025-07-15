from langchain_community.document_loaders import PyPDFLoader
# from langchain_ollama import OllamaLLM
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import PromptTemplate

loader = PyPDFLoader(file_path="Document_loader/Deep Learning with Python.pdf")

doc= loader.load()
print("-----------------------------------")
print(len(doc))
print("-----------------------------------")
print(doc[0].page_content)
print("-----------------------------------")
print(doc[0].metadata)  
print("-----------------------------------")


# model = OllamaLLM(model='phi3:mini',streming= True)

# parser = StrOutputParser()

# prompt = PromptTemplate(
#     template="Summarize the following text with in 5 lines:\n\n{text}",
#     input_variables=["text"]
# )

# chain = prompt | model | parser
# result = chain.invoke({'text': doc[50].page_content})
# print(result)