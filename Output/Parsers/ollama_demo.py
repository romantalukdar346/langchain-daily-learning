from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# Load environment variables if needed
load_dotenv()

# Initialize the model
model = OllamaLLM(model="llama3.2")

# Define the expected JSON structure
schema = [
    ResponseSchema(name="fact_1", description="The first fact about the topic"),
    ResponseSchema(name="fact_2", description="The second fact about the topic"),
    ResponseSchema(name="fact_3", description="The third fact about the topic"),
]

# Create the output parser
parser = StructuredOutputParser.from_response_schemas(schema)

# Get format instructions from the parser
format_instructions = parser.get_format_instructions()

# Create the prompt template
prompt = PromptTemplate(
    template=(
        "You are an expert assistant. Write a detailed 100-word report on the topic: {topic}.\n"
        "Only return a JSON object in the following format:\n"
        "{format_instructions}"
    ),
    input_variables=["topic"],
    partial_variables={"format_instructions": format_instructions}
)

# Build the chain
chain = prompt | model | parser

print("----------------------------------------------------------")
topic = input("Enter the topic for the report: ")
print("----------------------------------------------------------")
# Invoke the chain with input
result = chain.invoke({"topic": topic})

# Print the final structured result
print("----------------------------------------------------------")
print(result)
print("----------------------------------------------------------")
