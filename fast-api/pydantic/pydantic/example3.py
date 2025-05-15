from pydantic import BaseModel, Field
from typing import List, Dict, Optional
class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,   #required
        min_length=5, 
        max_length=15,
        description="Employee name",
        example="Noor ul ain"
    )
    department:Optional[str] = None
    
emp = Employee(id=1, name="Noor ul ain", department="HR")
print(emp)
    