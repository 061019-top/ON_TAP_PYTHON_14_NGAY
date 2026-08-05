from pydantic import BaseModel, ConfigDict

class UpdateBook(BaseModel):
    title: str
    author: str
    price: float
    quantity: int
    

class CreateBook(BaseModel):
    title: str
    author: str
    price: float
    quantity: int
    
class BookResponse(CreateBook):
    id: int
    
    model_config = ConfigDict(from_attributes=True)