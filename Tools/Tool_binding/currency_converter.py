from langchain_ollama import ChatOllama
from langchain_core.tools import tool, InjectedToolArg
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage, SystemMessage
from typing import Annotated
import requests
import json

@tool
def get_exchange_rate(base_currency: str, target_currency: str) -> float:
    """A tool to get the exchange rate between two currencies."""
    url = f'https://v6.exchangerate-api.com/v6/c754eab14ffab33112e380ca/pair/{base_currency}/{target_currency}'
    response = requests.get(url)
    return response.json()


@tool
def convert( base_currency_value: float, conversion_rate: Annotated[float,InjectedToolArg]) -> float:
    """A tool to convert currency using the exchange rate."""
    return base_currency_value * conversion_rate


llm = ChatOllama(model="llama3.2")
# Binding the tools to the llm

llm_with_tools = llm.bind_tools([convert,get_exchange_rate])
message = [SystemMessage(content="""This is a currency conversion tool.If user asks for conversion," \
                                    Always first get the exchange rate from get_exchange_rate tool fuction and
                                     then convert it from convert tool function.""")]

query =  "Use the exchange rate from INR to BDT and convert 10 INR to BDT. Provide the result."

message.append(HumanMessage(content=query))
Ai_message = llm_with_tools.invoke(message)
message.append(AIMessage(content=str(Ai_message)))



for tool_call in Ai_message.tool_calls:
    if tool_call['name'] == 'get_exchange_rate':
        tool_message1 = get_exchange_rate.invoke(tool_call)
        conversion_rate = json.loads(tool_message1.content)['conversion_rate']
        message.append(ToolMessage(content=str(tool_message1), tool_call_id=tool_call['id']))

    elif tool_call['name'] == 'convert':
        tool_call['args']['conversion_rate'] = conversion_rate
        tool_message2 = convert.invoke(tool_call)
        message.append(ToolMessage(content=str(tool_message2), tool_call_id=tool_call['id']))


final_result = llm_with_tools.invoke(message).content


print("------------------------------------------------------") 
print("Final Result:", final_result)
