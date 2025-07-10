from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from langchain_ollama import OllamaLLM
from langchain_community.chat_models import ChatOllama

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     task="text_generation"
# )   

# model = ChatHuggingFace(llm=llm)
model = OllamaLLM(model="phi3:mini")

class person(BaseModel):

    name : str = Field(description="Name of the person")
    age : int = Field(gt=18, description="Age of the person")
    city : str = Field(description="City of the person")

parser= PydanticOutputParser(pydantic_object=person)

format_instruction = parser.get_format_instructions()


template1= PromptTemplate(
    template=(
        "Give information about a historical person lived in {place}.\n"
        "Only return with the following format:\n"
        "{format_instruction}\n"
        "Do not include explanation, markdown or code formatting."
    ),
    input_variables=["topic"],
    partial_variables={"format_instruction":  format_instruction}
)


chain = template1 | model | parser

result = chain.invoke({"place": "Bangladesh"})

print(result)

