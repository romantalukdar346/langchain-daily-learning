from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence

model =OllamaLLM(model='llama3.2')

parser= StrOutputParser()

prompt1= PromptTemplate(
    template=("Write a post about {topic} so that I can post it in Tweeter"),
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template=("Write a post about {topic} so that I can post it in Linkedin"),
    input_variables=['topic']
)

chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1 | model | parser),
    'linkedin': RunnableSequence(prompt2 |model | parser)
})

result = chain.invoke({'topic': "Importance of snakes"})
print(result['tweet'])
print("------------------------------")
print(result['linkedin'])