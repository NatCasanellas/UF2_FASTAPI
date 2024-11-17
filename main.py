from fastapi import FastAPI
from pydantic import BaseModel



#model POST
class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float =None
    category: str
    in_stock: bool

app = FastAPI()


#funcio POST
@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}