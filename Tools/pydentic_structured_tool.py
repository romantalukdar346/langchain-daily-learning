from langchain.tools import StructuredTool
from pydantic import BaseModel, Field


def add_two_numbers(a: int, b: int) -> int:
    return a + b

class AddTwoNumbersInput(BaseModel):
    a: int = Field( required=True, description="The first number to add.")
    b: int = Field( required= True, description="The second number to add.")

add_two_numbers_tool = StructuredTool.from_function(
    func=add_two_numbers,
    name="add_two_numbers",
    description="A tool to add two numbers.",
    args_schema=AddTwoNumbersInput
)

result = add_two_numbers_tool.invoke({"a": 100, "b": 4})
print("Result of adding two numbers:", result)
print(add_two_numbers_tool.name)
print(add_two_numbers_tool.description)
print(add_two_numbers_tool.args)
