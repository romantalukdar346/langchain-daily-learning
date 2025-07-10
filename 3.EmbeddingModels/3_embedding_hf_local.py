from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents = [
    "The capital of Bangladesh is Dhaka.",
    "The capital of India is New Delhi.",
    "The capital of Nepal is Kathmandu.",
    "The capital of Bhutan is Thimphu.",
    "The capital of Sri Lanka is Sri Jayawardenepura Kotte."
]

emb = HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2")

res= emb.embed_documents(documents)

print(str(res[0]))  # Output the content of the response



