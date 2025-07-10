from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

model = OllamaLLM(model='llama3.2')

prompt = PromptTemplate(
    template=("write a joke about {topic} topic"),
    input_variables=['topic']
)

parser =StrOutputParser()

chain = RunnableSequence(prompt | model | parser)

result = chain.invoke({'topic': "Bangladesh cricket team (roast them)"})

print(result)
