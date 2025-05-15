from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def hello():
    return "hello world"

@app.get("/items/{item_id}")
def items(item_id: int):
    return item_id