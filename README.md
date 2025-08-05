# Flask + PostgreSQL with Docker Compose

Proyecto de demostración de una aplicación web básica utilizando **Flask** como backend en Python y **PostgreSQL** como base de datos, todo orquestado mediante **Docker Compose**. Este stack permite levantar una arquitectura web funcional con un solo comando.

---

## 📦 Tecnologías utilizadas

- Docker & Docker Compose
- Python 3 / Flask
- PostgreSQL 15
- Psycopg2 (conector Python → PostgreSQL)

---

## 📁 Estructura del proyecto

````
flask-postgres-compose/
├── docker-compose.yml
├── app/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
└── README.md
````

Para crear Dockerfile
````
nano Dockerfile
````

## ⚙️ Uso

### 1. Clonar el repositorio

````
git clone https://github.com/usuario/flask-postgres-compose.git
cd flask-postgres-compose
````

### 2. Levantar los servicios
````
docker compose up -d
````
🎯 Esto crea dos contenedores:

web → aplicación Flask en http://localhost:5000

db → contenedor PostgreSQL accesible internamente

### 3. Acceder
Abra en su navegador:

http://localhost:5000

## 🛠 Contenido del docker-compose.yml
````
version: "3.9"

services:
  web:
    build: ./app
    ports:
      - "5000:5000"
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: mydb
    ports:
      - "5432:5432"
````
## 🧪 Conexión desde Flask (app/app.py)
````
conn = psycopg2.connect(
    host="db",
    database="mydb",
    user="postgres",
    password="postgres"
)
````
## ❌ Parar los servicios
````
sudo docker-compose down
````

## ✍️ Autor
Giancarlos Mamani Benitez 

