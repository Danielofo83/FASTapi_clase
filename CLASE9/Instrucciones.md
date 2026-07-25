Miniproyecto: Inventario de Tienda de Pociones Mágicas
En este miniproyecto pondremos en práctica todo lo aprendido en las clases anteriores.
Objetivo: Construir la lógica de un inventario utilizando estructuras de datos básicas (listas y diccionarios) y funciones, para luego exponer sus datos a través de una API básica con FastAPI.
Tiempo estimado de resolución: 1 hora y 30 minutos (más 30 minutos de revisión en conjunto).
Requisitos previos
Tipos de datos, condicionales, ciclos y estructuras de datos (listas y diccionarios).
Creación de funciones.
Creación de una aplicación básica con FastAPI (`@app.get`).
Instrucciones
Abre el archivo `main.py`. Encontrarás un template con comentarios `TODO` que te guiarán paso a paso. A continuación se detalla lo que debes hacer en cada sección:
Parte 1: El Inventario (Tiempo estimado: 15 min)
Crea la estructura base para almacenar nuestros datos.
Define una variable global llamada `inventario` que sea una lista vacía.
Agrega directamente a la lista al menos 3 diccionarios que representen diferentes pociones (ej. Poción de Curación, Poción de Maná, Poción de Fuerza), como en un videojuego.
Cada diccionario debe tener las siguientes claves: `"nombre"` (texto), `"tipo"` (texto), `"precio"` (decimal/float), y `"cantidad"` (entero).
Parte 2: Funciones Auxiliares (Tiempo estimado: 30 min)
Crea funciones para gestionar y consultar las pociones de tu inventario.
Crea una función `agregar_pocion(nombre, tipo, precio, cantidad)` que construya un diccionario con estos datos y lo agregue a la lista `inventario`.
Crea una función `obtener_todas()` que simplemente retorne la lista completa de pociones.
Crea una función `obtener_por_tipo(tipo_buscado)` que reciba un texto (string) y, mediante un ciclo `for`, filtre y retorne una nueva lista de diccionarios con las pociones que coincidan con ese tipo.
Parte 3: Usando las funciones (Tiempo estimado: 15 min)
Llama a tu función `agregar_pocion` para añadir una poción nueva a tu inventario (por ejemplo, una "Poción de Velocidad").
Llama a `obtener_todas()` y utiliza `print()` para verificar en consola que la poción se agregó correctamente y la lista tiene todos tus elementos.
Parte 4: Exponiendo los datos con FastAPI (Tiempo estimado: 30 min)
Importa `FastAPI` (ya está en el template) y crea una instancia de la aplicación llamada `app`.
Crea un endpoint en la ruta raíz (`/`) que responda al método GET y retorne un diccionario con un mensaje de bienvenida (ej. `{"mensaje": "Bienvenido a la Tienda de Pociones"}`).
Crea un endpoint en la ruta `/pociones` que responda al método GET y retorne el resultado de tu función `obtener_todas()`.
Opcional: Crea un endpoint en la ruta `/pociones/curacion` que retorne únicamente las pociones de tipo "Curación", haciendo uso de tu función `obtener_por_tipo`.
---
Recuerda probar tu API ejecutando el servidor de desarrollo en tu terminal:
```bash
uvicorn main:app --reload
```