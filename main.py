from fastapi  import FastAPI

app = FastAPI()
@app .get ("/")
def home ():
    return {"message": "Welecome FastAPI" }


@app.get("/about")
def about ():
    return {"about ": "this website is about ecommerce "}

@app.get("/contact")
def contact ():
    return {"contact": "you can contact us on linkedin "}
