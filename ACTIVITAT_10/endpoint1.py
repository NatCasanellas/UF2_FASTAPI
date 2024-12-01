from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import asyncpg
import random

# Inicia la teva aplicació FastAPI
app = FastAPI()

# Model de resposta per a temàtiques
class Option(BaseModel):
    option: str

# Connexió asíncrona a la base de dades (usant asyncpg per PostgreSQL)
async def fetch_themes_from_db():
    conn = await asyncpg.connect(user='usuari', password='contrasenya', database='nom_base_dades', host='localhost')
    # Recupera totes les temàtiques
    rows = await conn.fetch('SELECT DISTINCT theme FROM tematicas')
    await conn.close()
    # Converteix els resultats a una llista de diccionaris
    return [{"option": row['theme']} for row in rows]

# Endpoint per obtenir les temàtiques
@app.get("/penjat/tematica/opcions", response_model=List[Option])
async def get_options():
    themes = await fetch_themes_from_db()  # Crida a la funció asíncrona
    return themes
