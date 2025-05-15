from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    item: List[str]
    quantity: Dict[str, int]
    
class BlogPost(BaseModel):
    title:str
    content:str
    image_url: Optional[str]   
    
cart = {
    'user_id': 104,
    'item': ["mobile", "glasses", "bag"],
    'quantity':{
        'mobile':1,
        'glasses':2,
        "bag":3
    }
}   
cart = Cart(**cart)
print(cart)

blog_post = {
    'title':'Courage',
    'content':'positivity',
    'image_url':None
}
blog_post = BlogPost(**blog_post)
print(blog_post)