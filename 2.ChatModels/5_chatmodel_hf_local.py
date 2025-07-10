from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    model_kwargs={
        "temperature": 0.5,
        "max_length": 100
    }
)

model =ChatHuggingFace(llm=llm)

res= model.invoke('what is the capital of Bangladesh?')

print(res.content)