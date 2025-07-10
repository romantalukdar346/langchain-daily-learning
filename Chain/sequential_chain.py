from langchain_ollama import OllamaLLM  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = OllamaLLM(model="phi3:mini")

parser= StrOutputParser()

prompt1= PromptTemplate(
    template=("Generate a detailed report on {topic}"),
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

print("-------------------------------")
topic = input("Enter topic name : ")
print("-------------------------------")

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': topic})

print("-------------------------------")
print(result)
print("-------------------------------")
chain.get_graph().print_ascii()
