# Model de resposta per a paraules
class WordOption(BaseModel):
    option: str

# Funció asíncrona per obtenir les paraules per una temàtica
async def fetch_words_by_theme(theme: str):
    conn = await asyncpg.connect(user='usuari', password='contrasenya', database='nom_base_dades', host='localhost')
    # Consulta per obtenir les paraules per la temàtica
    rows = await conn.fetch('SELECT word FROM words WHERE theme=$1 LIMIT 100', theme)
    await conn.close()
    # Si hi ha paraules, seleccionem una aleatòria
    if rows:
        random_word = random.choice(rows)
        return [{"option": random_word['word']}]
    return []

# Endpoint per obtenir una paraula aleatòria per temàtica
@app.get("/penjat/tematica/{option}", response_model=List[WordOption])
async def get_word_by_theme(option: str):
    words = await fetch_words_by_theme(option)  # Crida a la funció asíncrona
    return words
