from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class AddTwoNumbersInput(BaseModel):
    a: int = Field(required=True, description="The first number to add.")
    b: int = Field(required=True, description="The second number to add.")

class AddTwoNumbersTool(BaseTool):
    name: str = "add_two_numbers",
    description: str = "A tool to add two numbers."
    args_schema: Type[BaseModel] = AddTwoNumbersInput

    def _run(self, a: int ,b : int) -> int:
        return a + b
    
add_two_numbers_tool = AddTwoNumbersTool()
result = add_two_numbers_tool.invoke({"a": 234, "b": 4})

print("Result of adding two numbers:", result)
print(add_two_numbers_tool.name)
print(add_two_numbers_tool.description)
print(add_two_numbers_tool.args)

