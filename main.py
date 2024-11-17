from fastapi import FastAPI, Response
from typing import Optional

app = FastAPI()

data = {"1": "Item 1", "2": "Item 2"}


@app.get("/items/{item_id}")
async def read_item(item_id: str, respose: Response):
    if item_id not in data_
        response.status_code = 404
        return{"error": "item not found"}
    return {"item_id": item_id, "name": data[item_id]}