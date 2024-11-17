from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#funcio GET que retorna un missatge
@app.get("/")
async def root():
    return {"message": "Hello World!!"}


#model POST
class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float
    category: str
    in_stock: bool

app = FastAPI()


#funcio POST
@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}