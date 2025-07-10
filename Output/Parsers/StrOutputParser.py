from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

# llm= HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     task="text_generation"
# )

# model = ChatHuggingFace(llm=llm)

# model = OllamaLLM(model="llama3.2")
model = OllamaLLM(model="phi3:mini")


template1 = PromptTemplate(
    template="write a details report on {topic} in 100 words",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=["text"]
    )

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser


result = chain.invoke({"topic": "Artificial Intelligence"})

print(result)