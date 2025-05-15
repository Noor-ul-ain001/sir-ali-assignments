from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str
    is_active: bool
    
user_input = {
    'id':101,
    'name':'noor',
    'is_active': True
}   
user = User(**user_input)
print(user) 
    