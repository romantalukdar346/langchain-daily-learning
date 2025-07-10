from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage
load_dotenv()


chat_template= ChatPromptTemplate([
    ("system", " You are a helpful {domain} expert."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{query}")
])


chat_history=[]
with open("Prompt/chat_history.txt") as file:
    chat_history.extend(file.readlines())

 
llm= HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)

model= ChatHuggingFace(llm=llm)


domain= input("Enter the domain:  ")

while True:

    query= input("Enter your Query:  (for exit type 'exit')  ")

    if query=='exit':
        break

    chain= chat_template | model  # Chain the prompt with the model

    res= chain.invoke({
    "domain": domain,
    "query": query,
    "chat_history": chat_history})

    print("--------------------------------------------------------------------")
    print(res.content)  # Output the content of the response
    print("--------------------------------------------------------------------")

    chat_history.append(HumanMessage(content=query))
    chat_history.append(AIMessage(content=res.content))

    input_text= input("Want Rest All:  ")
    if input_text.lower() == 'yes':
        domain = input("Enter the domain:  ")
        chat_template= ChatPromptTemplate([
                ("system", " You are a helpful {domain} expert."),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human","{query}")
]) # Reset chat history

print(chat_history)

