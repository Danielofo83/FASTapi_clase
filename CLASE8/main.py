from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI (title="Mi primera API con FastAPI", description="Esta es una API de ejemplo creada con FastAPI", version="1.0.0")

usuarios_db = {
    1: {"nombre": "Juan", "edad": 25},
    2: {"nombre": "María", "edad": 30},
}

class UsuarioItem(BaseModel):
    nombre: str
    edad: int   

@app.get("/usuarios",status_code=status.HTTP_200_OK)
def obtener_usuarios():
    return usuarios_db

@app.post("/usuarios",status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario: Usuario):
    num_usuarios = len(usuarios_db) 
    usuarios_db[num_usuarios + 1] = usuario.model_dump()
    return {"mensaje": "Usuario creado correctamente", "usuario": usuario+1}
