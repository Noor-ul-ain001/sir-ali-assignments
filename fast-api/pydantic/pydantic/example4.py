from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    username: str

    @field_validator('username')
    @classmethod
    def validate_username(cls, v: str) -> str:
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v

class Signup(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self

class Product(BaseModel):
    price: float
    quantity: int
    
    @computed_field
    @property
    def total(self)->float:
        return self.price * self.quantity
    
p = Product(price = 100.0, quantity = 3)    
print(p.model_dump())
