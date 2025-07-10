from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text_generation"
)

model = ChatHuggingFace(llm=llm)

st.header("HuggingFace Reseach paper summarizer Tools")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )



# # Define the prompt template
# template= PromptTemplate(
#     template="""
# Please summarize the research paper titled \"{paper_input}\" with the following specifications:
# Explanation Style: {style_input}  
# Explanation Length: {length_input} .
#  1.Mathematical Details:  
#    - Include relevant mathematical equations if present in the paper.  
#    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
#  2.Analogies:    
#  - Use relatable analogies to simplify complex ideas.  
# 3.Programming Examples:  
#    - Provide code snippets to illustrate key concepts or algorithms discussed in the paper.  
#    - Ensure the code is well-commented and easy to understand.
#  If certain information is not available in the paper, respond with: "Insufficient information available\" instead of guessing. 
# Ensure the summary is clear, accurate, and aligned with the provided style and length.",
# """,
# input_variables=["paper_input", "style_input", "length_input"],
# validate_template=True
# )


template= load_prompt("Prompt/prompt_template.json")

# fill the placeholder with the prompt template
# prompt= template.invoke({
#     "paper_input": paper_input,
#     "style_input": style_input,
#     "length_input": length_input
# })



if st.button("Generate Summary"):
    chain= template | model  # Chain the prompt with the model
    res= chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    st.write(res.content)  # Output the content of the response
