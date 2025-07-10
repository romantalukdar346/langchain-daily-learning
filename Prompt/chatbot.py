from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text_generation")

model= ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]


while True:
    user_input= input('You:')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    res= model.invoke(chat_history)
    chat_history.append(AIMessage(content=res.content))
    print(f"Bot: {res.content}")  # Output the content of the response

print(chat_history)


