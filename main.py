from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#funcio GET que retorna un missatge
@app.get("/")
async def root():
    return {"message": "Hello World!!"}

class Item(BaseModel):
    name: str
    description: str | none = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
