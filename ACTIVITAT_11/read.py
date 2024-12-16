import psycopg2
import os
from datetime import datetime

def create_game(conn):
    cur = conn.cursor()
    # Creem la partida a la taula 'games' amb un timestamp
    cur.execute("""
        INSERT INTO games (start_time) 
        VALUES (%s) 
        RETURNING game_id;
    """, (datetime.now(),))
    
    game_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    return game_id
