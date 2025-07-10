from langchain_anthropic import ChatAnthropic
from dotenv import  load_dotenv
load_dotenv()

model=ChatAnthropic(model="claude-2")

res= model.invoke("What is the capital of Bangladesh?")

print(res.content)  # Output the content of the response