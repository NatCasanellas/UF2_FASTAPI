from fastapi import FastAPI
from pydantic import BaseModel
from conn import get_db_connection
from read import create_game

app = FastAPI()

class GameResponse(BaseModel):
    message: str
    game_id: int


#primer endpoint boto començar partida
@app.post("/start_game", response_model=GameResponse)
async def start_game():
    conn = get_db_connection()
    game_id = create_game(conn)
    conn.close()
    return {"message": "Game started", "game_id": game_id}

#segon endpoint titol començar partida


#tercer endpoint per mostrar intents


#quart endpoint per mostrar abecedari


#cinque endpoint estadistiques jugador
