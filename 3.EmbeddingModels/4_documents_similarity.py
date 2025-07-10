from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()

documents = [
    "Tamim Equbal is a prominent Bangladeshi cricketer known for his aggressive batting style. He is one of the best openers in the history of Bangladesh cricket.",
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

emb = HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2")

Query= "Who is the best cricketer in Bangladesh as a Opener?"

doc_emb= emb.embed_documents(documents)

query_emb= emb.embed_query(Query)

score= cosine_similarity([query_emb], doc_emb)

index,score=  sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(Query)
print(f"Most similar document: {documents[index]}")
print(f"Similarity score: {score[0]:.3f}")  # Print the similarity score