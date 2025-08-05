# Imagen base con Python
FROM python:3.10-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install -r requirements.txt

# Copiar el archivo principal de la app
COPY app.py .

# Comando para ejecutar Flask
CMD ["python", "app.py"]
