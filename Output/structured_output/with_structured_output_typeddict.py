from typing import TypedDict,Annotated,Optional, Literal
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()


llm= HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text_generation"
)
model = ChatHuggingFace(llm=llm)


# Define the structure of the output using TypedDict
# This will help in parsing the output into a structured format
# -----------------------------------------------------------------------------------------------------------------------

class Review(TypedDict):

    summary: str
    sentiment: str

structured_output = model.with_structured_output(Review)

res= structured_output.invoke("""The hardware is great,There are too many pre-installed apps that I can't remove.compared to other brands. 
                              Hoping for a software update tobut the software feels bloated.Also, the IJI looks outdated fix this.""")

print("---------------------------------------------------------")
print(res)
print("---------------------------------------------------------")
print("Summary: ",res['summary'])
print("---------------------------------------------------------")
print("Sentiment: ",res['sentiment'])

# -----------------------------------------------------------------------------------------------------------------------

class other(TypedDict):

    summary: Annotated[str, "Summary for the given review"]
    sentiment: Annotated[Literal["pos","neg"], "Sentiment analysis of that givrn review"]
    pros : Annotated[Optional[list[str]], "List of pros for the given review"]
    cons: Annotated[Optional[list[str]], "List of cons for the given review"]

str_output = model.withstructured_ouptut(other)

result = str_output.invoke("""The hardware is great,There are too many pre-installed apps that I can't remove.compared to other brands.""")
print("---------------------------------------------------------")
print(result)
print("---------------------------------------------------------")
print("Summary: ",result['summary'])    
print("---------------------------------------------------------")
print("Sentiment: ",result['sentiment'])
print("---------------------------------------------------------")
print("Pros: ",result['pros'])  
print("---------------------------------------------------------")

# -----------------------------------------------------------------------------------------------------------------------

