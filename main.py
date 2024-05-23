# En main.py

"""API candidato"""

from fastapi import FastAPI
from routers import candidato_router
from models.ins import Candidato
import sqlite3

DESCRIPTION = """
API que añade nuevos candidatos a la BBDD del sistema
"""

app = FastAPI(
    title="API candidato",
    description=DESCRIPTION,
    version='0.01'
)

def create_table():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    
    # Insertar datos del candidato en la base de datos
    cursor.execute('''CREATE TABLE IF NOT EXISTS candidatos
                      (dni TEXT PRIMARY KEY, nombre TEXT, apellido TEXT)''')
    conn.commit()
    
try:
    create_table()
except Exception:
    print('La tabla ya está creada')

app.include_router(candidato_router)

# Ejecutar la aplicación FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)