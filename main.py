from fastapi import FastAPI

app = FastAPI()

#funcio GET que retorna un missatge
@app.get("/")
async def root():
    return {"message": "Hello World!!"}
