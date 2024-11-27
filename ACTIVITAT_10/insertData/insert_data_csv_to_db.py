import psycopg2

def insert_data_csv_to_db(pos,data):

    conn = psycopg2.connect(
        database="postgres",
        user="user_postgres",
        password="pass_postgres",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    sql = "INSERT INTO paraules(word, theme)VALUES(%S, %S);"

    values = ((data.get("WORD")[pos], data.get("THEME")[pos]))

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()

    return{"Message":"Data inerted"}