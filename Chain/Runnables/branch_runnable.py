from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import  RunnableSequence, RunnableBranch, RunnablePassthrough

model =OllamaLLM(model='llama3.2')

parser= StrOutputParser()

prompt1= PromptTemplate(
    template=("Genarate a report about {topic} topic"),
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template=("Summarize this text {text} less then 500 words"),
    input_variables=['text']
)

def count(word):
    return len(word.split())

chain1= RunnableSequence( prompt1 | model | parser)
chain2= RunnableBranch(
        (lambda x: count(x)>500, RunnableSequence(prompt2 | model | parser)),
        RunnablePassthrough()
    )


final_chain= RunnableSequence(chain1 | chain2 )
result = final_chain.invoke({'topic':'AI'})

print("----------------------------------")
print(result)
print("----------------------------------")
print(f"Total no of words are :{count(result)}")

