from langchain_ollama import OllamaLLM # type: ignore
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda

model = OllamaLLM(model="phi3:mini")

class review(BaseModel):
    sentiment : Literal['Positive','Negative'] = Field(description="Sentiment of the feedback")

parser1= PydanticOutputParser(pydantic_object=review)

prompt = PromptTemplate(
    template=("""Classify the sentiment of the feedback text into positive or negative \n {feedback} \n {format_instruction}.
              You should reply only with one word either 'Possitive' or 'Negative' """),
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser1.get_format_instructions()}
)




chain = prompt | model | parser1

parser2= StrOutputParser()

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback in 5 line only \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback in 5 line only \n {feedback}',
    input_variables=['feedback']
)


branch_chain = RunnableBranch(
    
        (lambda x:x.sentiment == 'Positive',prompt2 | model | parser2),
        (lambda x:x.sentiment == 'Negative',prompt3 | model | parser2),
        RunnableLambda(lambda x: "could not find sentiment")
)

final_chain= chain | branch_chain

result = final_chain.invoke({'feedback':" The phone bettary is not so good"})

print(result)

final_chain.get_graph().print_ascii()
