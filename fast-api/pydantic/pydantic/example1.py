# create product model with id price and in stock

from pydantic import BaseModel
class Stock(BaseModel):
    id: int
    price: float
    in_stock: bool = True 
    
stock = {
    'id':202,
    'price':200.0, 
    'in_stock':False
}   

is_available = Stock(**stock)
print(is_available)