from pydantic import BaseModel, EmailStr,Field
from typing import Optional

class person(BaseModel):

    name : str = "Roman"
    address : Optional[str]= None
    age : int
    email : EmailStr
    cgpa : float = Field(gt=4, le=10, description="CGPA should be between 4 and 10")



new_user ={ 'age': 25, 'email' : 'abc@gmail.com', 'cgpa': 8.5}
user = person(**new_user)

print(user.name)
print(user.age)
print(user.address)
print(user.email)
print(user.cgpa)
print('---------------------------------------------------------')
# Convert to dictionary
# This will convert the Pydantic model to a dictionary format   
print("Converting to dictionary:")
conver_to_dict = user.model_dump()
print(conver_to_dict['name'])
print(conver_to_dict['cgpa'])
print('---------------------------------------------------------')
# Convert to JSON
# This will convert the Pydantic model to a JSON format
print("Converting to JSON:")
conver_to_json= user.model_dump_json()
import json
conver_to_json_dict = json.loads(conver_to_json)

print(conver_to_json_dict['address'])
print(conver_to_json_dict['email'])
print(conver_to_json_dict)
print('---------------------------------------------------------')