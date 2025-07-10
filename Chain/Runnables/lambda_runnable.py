from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnableLambda, RunnablePassthrough

model =OllamaLLM(model='llama3.2')

parser= StrOutputParser()

prompt1= PromptTemplate(
    template=("Genarate a Joke about {topic} topic"),
    input_variables=['topic']
)

def count(text):
    return len(text.split())

chain1= RunnableSequence(prompt1 | model | parser)
chain2 = RunnableParallel({
    'pass': RunnablePassthrough(),
    'function': RunnableLambda(count)
})

final_chain = RunnableSequence( chain1 | chain2)

result = final_chain.invoke({'topic': 'Human'})
print("----------------------------------")
print(f"{result['pass']}------------No of words are :{result['function']}")

