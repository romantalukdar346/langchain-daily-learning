from pydantic import BaseModel, Field,EmailStr
from typing import Optional,Literal
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

# load_dotenv()
# llm = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     task="text_generation"
# )
# model = ChatHuggingFace(llm=llm)
# Define the structure of the output using Pydantic
# This will help in parsing the output into a structured format

model= OllamaLLM(model="llama3.2")


class Review(BaseModel):
     Key_themes :list[str] = Field( description="Key themes identified in the review")
     summary : str = Field(description="Summary of the review")
     sentiment : Literal['pos','neg'] =Field(description="Sentiment of the review, either 'pos' or 'neg'")
     pros :Optional[list[str]]
     cons : Optional[list[str]]
     name : str = Field(default="roman",description="Name of the person providing the review")
     email : EmailStr 

user = model.with_structured_output(Review)

result = user.invoke("""The hardware is great,There are too many pre-installed apps that I can't remove.compared to other brands. Hoping for a software update to fix this.""")
print("---------------------------------------------------------")  
print(result.Key_themes)
print(result.summary)
print(result.sentiment)
print(result.pros) 
print(result.cons)
print(result.name)
print(result.email)
print("---------------------------------------------------------")
