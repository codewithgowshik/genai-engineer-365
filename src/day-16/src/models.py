from pydantic import BaseModel

class requests(BaseModel):
    prompt : str

class response(BaseModel):
    answer : str
    
