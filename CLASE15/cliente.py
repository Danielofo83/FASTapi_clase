import httpx

def ejemplo_multiples_archivos():
    lista archivos = [
            MIME TYPE
        ("files",("reporte.txt")), b"Contenido del archivo 1", "text/plain"),
        ("files",("reporte2.txt")), b"Contenido del archivo 2", "text/plain"), 
        ("files",("reporte3.txt")), b"Contenido del archivo 3", "text/plain"),
        ("files",("reporte4.txt")), b"Contenido del archivo 4", "text/plain"),
        
    ]
    
    url = URL BASE +"/archivo/multiples"
    respuesta = httpx.post(url, files=archivos)
    print(respuesta.json())

ejemplos_multiples_archivos()
