from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
# from langchain_community.llms import ollama
from langchain_ollama import OllamaLLM
load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     task="text_generation"
# )
# model = ChatHuggingFace(llm=llm)

model = OllamaLLM(model="llama3.2")

schema =[

    ResponseSchema(name="fact_1", description="The first fact about the topic"),
    ResponseSchema(name="fact_2", description="The second fact about the topic"),
    ResponseSchema(name="fact_3", description="The third fact about the topic"),
]

parser= StructuredOutputParser.from_response_schemas(schema)

format_instruction= parser.get_format_instructions()

template1= PromptTemplate(
    template=("write a details report on {topic} in 100 words /n {format_instruction}"),
    input_variables=["topic"],
    partial_variables={"format_instruction": format_instruction}
)

chain = template1 | model | parser

print("----------------------------------------------------------")
topic = input("Enter the topic for the report: ")
print("----------------------------------------------------------")
# Invoke the chain with input
result = chain.invoke({"topic": topic})

# Print the final structured result
print("----------------------------------------------------------")
print(result)
print("----------------------------------------------------------")