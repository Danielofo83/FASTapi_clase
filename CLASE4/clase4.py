"""
Ejercicio Práctico: Funciones para API de Tienda en Línea

Contexto:
Estás refactorizando el código de la tienda en línea (de la clase anterior) 
para que sea más modular y esté listo para integrarse con FastAPI. 
Debes crear diferentes funciones que manejen partes específicas de la lógica del negocio.
"""

# 1. Función de Validación de Stock
# TODO: Crea una función llamada 'hay_stock_disponible'.
# Debe recibir DOS parámetros: el inventario_actual (número entero) y la cantidad_solicitada (número entero).
# Debe RETORNAR True si el inventario es mayor o igual a la cantidad solicitada, y False en caso contrario.

# Escribe tu función aquí:



# 2. Función de Cálculo de Total con Impuestos
# TODO: Crea una función llamada 'calcular_total'.
# Debe recibir DOS parámetros: el 'subtotal' y un parámetro opcional 'porcentaje_iva' (por defecto que sea 16).
# La función debe calcular el monto del IVA, sumarlo al subtotal y RETORNAR el total redondeado a 2 decimales.

# Escribe tu función aquí:



# 3. Función Principal de Procesamiento (Endpoint Simulado)
# TODO: Crea una función llamada 'procesar_compra'.
# Debe recibir: 'nombre_producto', 'precio_unitario', 'cantidad', 'stock_en_bd'.
# Dentro de la función:
#   a) Llama a tu función 'hay_stock_disponible'.
#   b) Si hay stock: calcula el subtotal (precio_unitario * cantidad), luego llama a 'calcular_total', 
#      y retorna un diccionario de éxito: {"status": 200, "mensaje": "Compra exitosa", "total": el_total_calculado}
#   c) Si NO hay stock: retorna un diccionario de error: {"status": 400, "mensaje": "Inventario insuficiente"}

# Escribe tu función aquí:




# Casos de Prueba (NO MODIFICAR)
# Ejecuta este archivo para verificar que tus funciones trabajan correctamente.
print("--- Pruebas de Sistema ---")

try:
    print("Prueba 1 (Compra Exitosa):")
    resultado1 = procesar_compra(nombre_producto="Laptop", precio_unitario=1500, cantidad=2, stock_en_bd=5)
    print(resultado1) # Debería imprimir un status 200 con el total calculado
    
    print("\nPrueba 2 (Sin Stock):")
    resultado2 = procesar_compra(nombre_producto="Monitor", precio_unitario=300, cantidad=5, stock_en_bd=2)
    print(resultado2) # Debería imprimir un status 400 de inventario insuficiente
except NameError as e:
    print(f"\n⚠️ Error: Aún no has definido todas las funciones requeridas. Falla: {e}")
