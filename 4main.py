from  fastapi  import FastAPI

app = FastAPI()
# notice  there is NO {name } in the route path here 
@app .get ("/users ")
def get_users(name :str=None ):
    return {"name ":name}

# users?name=nilesh ( if name  is given )