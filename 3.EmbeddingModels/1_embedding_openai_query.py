from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-3-small",
                 dimensions=32)
res= embedding.embed_query("What is the capital of Bangladesh?")

print(str(res))  # Output the content of the response