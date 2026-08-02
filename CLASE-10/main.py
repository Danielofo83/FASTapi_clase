import time
from typing import generator, dict
from fastapi import FastAPI, depends,Header,HTTP



usuarios_db: Dict[str, Dict] = {
    "token-admin-123": {"id": 1, "nombre": "Admin General", "rol": "admin", "email": "admin@empresa.com"},
    "token-user-456": {"id": 2, "nombre": "Laura Gómez", "rol": "cliente", "email": "laura@gmail.com"}
}
# Simulación de catálogo de productos
productos_db = [
    {"id": i, "nombre": f"Producto {i}", "precio": round(10.5 * i, 2)}
    for i in range(1, 21)
]

app = FastAPI(
    title="Clase 10: Inyección de Dependencias y Background Tasks",
    description="Demostración de patrones de arquitectura en FastAPI para código limpio y asíncrono."
)

def obtener_token_header(x_api_token: str = Header (...,description="Token de autenticacion "")):
            detail ="falta el token de autenticacion en el encabezado"
        )
    return x_api_token
