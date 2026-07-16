from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI (title="Mi primera API con FastAPI", description="Esta es una API de ejemplo creada con FastAPI", version="1.0.0")

TEXTFILE = "nombres.txt"

class NombreItem(BaseModel):
    nombre: str
    
@app.post("/texto/nombres")
def guardar_nombre(nombre_item: NombreItem):
    #print(item.nombre)
    with open(TEXTFILE, "a",encoding="utf-8" ) as f:
        f.write(nombre_item.nombre + "\n")
    return {"mensaje": f"Nombre: {nombre_item.nombre} guardado correctamente"}

@app.get("/texto/nombres")
def leer_nombres():
    if not os.path.exists(TEXTFILE):
        return {"nombres: []}
                
import json
@app.get("/json/usuarios")  
def guardar_usuarios_json