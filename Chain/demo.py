from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = OllamaLLM(model="phi3:mini")

parser= StrOutputParser()

prompt= PromptTemplate(
    template=("Write a joke about the given topic: topic is {topic}"),
    input_variables=['topic']
)

chain = prompt | model | parser
print("-------------------------------")
topic = input("Enter topic name : ")
print("-------------------------------")

result= chain.invoke({"topic": topic})

print(result)

chain.get_graph().print_ascii()