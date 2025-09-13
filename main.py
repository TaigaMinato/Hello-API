from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}
