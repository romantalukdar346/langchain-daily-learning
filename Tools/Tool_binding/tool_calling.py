from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage,ToolMessage

@tool
def add_two_numbers(a: int , b: int) -> int:
    """A tool to add two numbers."""
    return a + b

llm = ChatOllama(model="llama3.2")

# Binding the tool to the llm
llm_with_tools = llm.bind_tools([add_two_numbers])

message=[]

query = "What is the sum of 500 and 7 ?"

message.append(HumanMessage(content=query))

result1 = llm_with_tools.invoke("What is the sum of 500 and 7 ?")
message.append(AIMessage(content=str(result1)))


# print("Result of invoking the tool:", result1.tool_calls[0])
print("---------------------------------------------------")
result2 = add_two_numbers.invoke(result1.tool_calls[0])
# print(result2)
print("------------------------------------------------------")
message.append(ToolMessage(content=str(result2), tool_call_id=result1.tool_calls[0]['id']))

print("Final message history:", message)
print("------------------------------------------------------")

print(llm.invoke(message).content)
print("------------------------------------------------------")
print(llm_with_tools.invoke(message).content)