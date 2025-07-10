from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings= OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=32)

documents= [
    "The capital of Bangladesh is Dhaka.",
    "Dhaka is known for its rich history and vibrant culture.",
    "Bangladesh is located in South Asia, bordered by India and Myanmar."
]


res= embeddings.embed_documents(documents)


print(str(res))  # Output the content of the response