import psycopg2
conn = psycopg2.connect(user="postgres",
                        password="1234567890",
                        database="Kurs_4",
                        host="localhost",
                        port=5432)
cur = conn.cursor()
login = 'Vovanshik'
cur.execute(f"SELECT password FROM log_user WHERE log = '{login}'")
result = cur.fetchone()
print(result)

if result is not None:
    print("YEY")
else:print("NOT YEY")