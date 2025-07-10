from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
# from langchain_ollama import ChatOllama
load_dotenv()

model= ChatOpenAI(model="gpt-3.5-turbo")
# model = ChatOllama(model="llama3.2")

res= model.invoke("What is the capital of Bangladesh?")

print(res.content)
