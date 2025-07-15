from langchain_community.document_loaders import TextLoader
from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


# This code snippet demonstrates how to load a text document, process it with an LLM, and output a summary.
model = OllamaLLM(model='llama3.2',streming= True)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Summarize the following text with in 5 lines:\n\n{text}",
    input_variables=["text"]
)

loader= TextLoader(
    file_path="Document_loader\cricket.txt",
    encoding='utf-8')

doc = loader.load()
print("-----------------------------------")
# print(doc)
# print("-----------------------------------")
print(len(doc))
print("-----------------------------------")
# print(doc[0].page_content)
# print("-----------------------------------")
# print(doc[0].metadata)
# print("-----------------------------------")

chain = prompt | model | parser

result = chain.invoke({'text': doc[0].page_content})
print(result)
print("-----------------------------------")