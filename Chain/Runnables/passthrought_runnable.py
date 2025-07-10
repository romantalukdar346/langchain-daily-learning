from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough

model =OllamaLLM(model='llama3.2')

parser= StrOutputParser()

prompt1= PromptTemplate(
    template=("Genarate a Joke about {topic} topic"),
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template=("Explain the joke for me  {joke}"),
    input_variables=['joke']
)

chain1= RunnableSequence(prompt1 | model | parser)

chain2 = RunnableParallel({
    'pass': RunnablePassthrough(),
    'explain': RunnableSequence(prompt2 | model | parser)
})

final_chain =RunnableSequence(chain1 | chain2)

result = final_chain.invoke({'topic':'Football'})

print("---------------------------------")
print(result['pass'])
print('--------------------------------')
print(result['explain'])