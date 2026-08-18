from fastapi import FastAPI, File, UploadFile


app = FastAPI(title="Clase 15: Recepcion de archivos con FASTAPI parte2 (y formularios)")

@app.post("/archivos/multiples")
async def subir_mutilpes_archivos(
    files: list[UploadFile] = File(description="Recibir multiples archivos")
):
    resultado = []

    for f in files:
        contenido = await f.read()
        resultado.append({
            "filename": f.filename, 
            "content_type": f.content_type,
            "size": len(contenido)
        })
        with open(f.filename, "wb") as archivo:
            archivo.write(contenido)

    return {"archivos": resultado}
    