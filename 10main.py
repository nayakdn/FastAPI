from fastapi import FastAPI
from pydantic import BaseModel  # Step A: Import BaseModel

app = FastAPI()

class Address(BaseModel):
    city:str
    pincode:int

#define the parent schema and the link  the child schema 
class   User (BaseModel):
    name :str 
    age: int 
    address: Address  # linking the address model here 

    # create the  route 
    @app.post ("/create_user ")
    def create_user (user :User):
        return user  # returns the  validated naested jso
   