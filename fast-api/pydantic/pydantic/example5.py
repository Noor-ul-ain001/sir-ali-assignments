from pydantic import BaseModel, ValidationError
class User(BaseModel):
    id:int
    name:str
    email:str
    age:int
    
user = {
    'id':1,
    'name':'noor',
    'email':'abc@gmail.com',
    'age':23
} 
user = User(**user)
print(user)
print(user.model_dump())
try:
     invalid_user = User(id="not_an_int", name="Bob", email="abc@example.com")
except ValidationError as e:
    print(e)   