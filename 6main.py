from  fastapi  import FastAPI

app = FastAPI()

@app .get ("/items")
def get_items(name :str=None, price: int =0  ):
    return {"name ":name,
            "price " :price
            }
#items?name =amol&price=1000  (this is the url which we have to add at the back )