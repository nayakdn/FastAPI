from fastapi import FastAPI

app = FastAPI()

@app.post("/items")
def get_items(
    age: int,
    college: str,
    semester: str,
    name: str 
):
    return {
        "message": "user created",
        "name": name,
        "age": age,
        "college": college,
        "semester": semester
    }

# http://127.0.0.1:8000/docs