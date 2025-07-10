from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama import OllamaLLM
# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     task="text_generation"
# )
# model = ChatHuggingFace(llm=llm)

# model= OllamaLLM(model="llama3.2")
model= OllamaLLM(model="phi3:mini")


parser = JsonOutputParser()

format_instruction = parser.get_format_instructions()

template1= PromptTemplate(
    template=("write a details report on {topic} in 100 words /n {format_instruction}"),
    input_variables=["topic"],
    partial_variables={"format_instruction": format_instruction}
)

chain = template1 | model | parser

result = chain.invoke({"topic": "Artificial Intelligence"})

print(result)