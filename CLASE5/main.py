from fastapi import FastAPI
from django.utils.translation import ugettext_lazy as _f
app = FastAPI(
  
  title="Miprimra API con FastAPI",
  description="Esta es una API de ejemplo creada con FastAPI",
  
)
  
@app.get("/")
def home():
    return {"message": "¡Bienvenido a mi primera API con FastAPI!"}
  
#Parametro de ruta - Path Parameters
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id
            "nombre":"usuario de prueba"
            "status":"activo"
            }
  
  
productos db = [
    {"id": 1, "nombre": "Producto 1", "precio": 10.0},
    {"id": 2, "nombre": "Producto 2", "precio": 20.0},
    {"id": 3, "nombre": "Producto 3", "precio": 30.0},
]
  
#Parametro de peticion Query Parameters
@app.get("/productos")
def obtener_productos(skip: int = 0, solo_disponibles: bool = False, limit: int = 100):
    return {"skip": skip, "limit": limit}
  
  if solo_disponibles:
	resultado =[]
	for p in productos_db:
		if p["stock"] > 0: 
			resultado.append(p)
	return resultado[:limit]	