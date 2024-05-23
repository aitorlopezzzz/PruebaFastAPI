'''
Modelo de entrada de validación de datos del candidato
'''

from pydantic import BaseModel

class Candidato(BaseModel):
    '''
    Modelo de datos con los tipo de datos del candidato
    '''
    dni: str
    nombre: str
    apellido: str
        