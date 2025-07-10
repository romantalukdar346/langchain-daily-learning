from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text_generation"
)

model = ChatHuggingFace(llm=llm)

st.header("HuggingFace Chat Model")
user_input = st.text_input("Ask a question:")

if st.button("Submit"):
    res = model.invoke(user_input)
    st.write(res.content)  # Output the content of the response


# res= model.invoke("What is the capital of Bangladesh?")

# print(res.content)  # Output the content of the response