from fastapi import FastAPI

# ==========================================
# Parte 1: El Inventario
# ==========================================
# TODO: Define una variable 'inventario' que sea una lista vacía
lista_inventario = []
# TODO: Agrega directamente a la lista al menos 3 diccionarios que representen pociones
# Cada diccionario debe tener las llaves: "nombre", "tipo", "precio", "cantidad"
lista_inventario.append({"nombre":"Poción de Curación", "tipo": "Curación", "precio": 50, "cantidad": 10})
lista_inventario.append({"nombre":"Poción de Mana", "tipo": "Mana", "precio": 30, "cantidad": 5})
lista_inventario.append({"nombre":"Poción de Fuerza", "tipo": "Fuerza", "precio": 70, "cantidad": 3})

# ==========================================
# Parte 2: Funciones Auxiliares
# ==========================================
# TODO: Define la función agregar_pocion(nombre, tipo, precio, cantidad)
# Esta función debe armar un diccionario y hacer un .append() a la lista 'inventario'


# TODO: Define la función obtener_todas()
# Esta función simplemente retorna la lista 'inventario'


# TODO: Define la función obtener_por_tipo(tipo_buscado)
# Esta función recibe un string, filtra la lista 'inventario' y retorna las pociones que coincidan


# ==========================================
# Parte 3: Usando las funciones
# ==========================================
# TODO: Llama a agregar_pocion() para añadir una poción extra a la lista


# TODO: Haz un print de obtener_todas() para verificar en consola que tu lista tiene todos los datos


# ==========================================
# Parte 4: Exponiendo los datos con FastAPI
# ==========================================
# TODO: Crea la instancia de la aplicación FastAPI llamada 'app'
# app = FastAPI()

# TODO: Crea un endpoint GET en la ruta "/" que retorne un mensaje de bienvenida


# TODO: Crea un endpoint GET en la ruta "/pociones" que retorne todas las pociones (usa obtener_todas)


# TODO (Opcional): Crea un endpoint GET en "/pociones/curacion" que retorne solo las de tipo "Curación" (usa obtener_por_tipo)
