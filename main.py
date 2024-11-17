from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#funcio GET que retorna un missatge
@app.get("/")
async def root():
    return {"message": "Hello World!!"}

