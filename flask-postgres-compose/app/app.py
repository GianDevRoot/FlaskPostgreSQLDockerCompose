from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    # Intentamos conectar a la DB
    conn = psycopg2.connect(
        host="db",        # nombre del servicio docker
        database="mydb",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    result = cur.fetchone()

    return f"Hola desde Flask + PostgreSQL → {result}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)