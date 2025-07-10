from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text_generation"
)


model = ChatHuggingFace(llm=llm)
res= model.invoke("What is the capital of Bangladesh?")

print(res.content)  # Output the content of the response
