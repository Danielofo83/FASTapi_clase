@Controlador("2", "ejercicio_7")
def ejercicio_7(status_code):
    """
    Instrucciones:
        La función "ejercicio_7" recibe un código de estado HTTP "status_code" (entero).
        Debe clasificar el código y regresar un string según los siguientes rangos:
        - Si está en el rango 200 a 299 (inclusive ambos): regresa "SUCCESS"
        - Si está en el rango 400 a 499 (inclusive ambos): regresa "CLIENT_ERROR"
        - Si está en el rango 500 a 599 (inclusive ambos): regresa "SERVER_ERROR"
        - Para cualquier otro código: regresa "OTHER"

    Ejemplo:
        Si status_code = 200, regresa "SUCCESS".
        Si status_code = 404, regresa "CLIENT_ERROR".
    """

    # Escribe aquí tu código ↓
    if 200 <= status_code <= 299:
        return "SUCCESS"
    elif 400 <= status_code <= 499:
        return "CLIENT_ERROR"
    elif 500 <= status_code <= 599:
        return "SERVER_ERROR"
    else:
        return "OTHER"
    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código