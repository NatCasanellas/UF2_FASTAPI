from fastapi import FastAPI

app = FastAPI()

#funcio GET que retorna un missatge de benvinguda
@app.get("/")
def read_root():
    return {"message": "Benvingut a la nostra API!"}

#funcio GET que retorna informacio d'un usuari segons el seu id
@app.get("/user/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id, "name": "Usuari Exemplar"}

#funcio GET que retorna una llista d'items
@app.get("/items/")
def read_items():
    return {"items": ["item1" , "item2", "item3"]}