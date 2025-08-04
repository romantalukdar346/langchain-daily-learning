from langchain_core.tools import tool



# Decorator to define a tool
@tool
def add_two_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


result = add_two_numbers.invoke({"a": 5, "b": 4})

print("Result of adding two numbers:", result)
# This code defines a tool to add two numbers and invokes it with sample inputs.

print(add_two_numbers.name)
print(add_two_numbers.description)
print(add_two_numbers.args)