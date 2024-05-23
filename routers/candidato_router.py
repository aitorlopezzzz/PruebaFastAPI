# En routers/candidato_router.py

"""Router para insertar candidatos"""

from fastapi import APIRouter
from models import Candidato
import sqlite3

router = APIRouter()

@router.post("/candidato")
def crear_candidato(candidato: Candidato):
    '''
    POST para insertar candidatos en la BBDD SQlite
    '''
    try:
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        # Insertar datos del candidato en la base de datos
        cursor.execute('''INSERT INTO candidatos (dni, nombre, apellido)
                          VALUES (?, ?, ?)''', (candidato.dni, candidato.nombre, candidato.apellido))
        conn.commit()
        return {"mensaje": "Candidato creado correctamente"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="El usuario ya existe")