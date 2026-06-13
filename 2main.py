from fastapi import FastAPI

app = FastAPI()
#user {user_id } in  the path  is the path parameter 
@app.get("/users/{user_id}")
def get_user(user_id):
    # we use the dyanamic user_id  to return sepcific  data 
    return {"user_id":user_id}