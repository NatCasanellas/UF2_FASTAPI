from fastapi import FastAPI, HTTPException


app = FastAPI()

data = {"1": "Item 1", "2": "Item 2"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in data:
        raise HTTPException(status_code = 404, detail="Item not found")
    return {"item_id": item_id, "name": data[item_id]}