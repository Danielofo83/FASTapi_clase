from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/health")
def health_check():
    if not os.path.isdir("imagenes"):
        os.mkdir("imagenes")
    if not os.path.isdir("usuarios"):
        os.mkdir("usuarios")
    if not os.path.isdir("db"):
        os.mkdir("db")
    return {"status": "ok"}

