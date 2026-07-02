"""
Ejercicio Práctico: Sistema de Órdenes y Pagos (Trabajo en Equipo)

Contexto:
Su equipo está construyendo el backend de una tienda en línea. Tienen que validar una 
orden de compra, calcular el total, descontar inventario y simular el cobro al cliente.

Instrucciones: Completen el código en las secciones marcadas con "TODO".
"""

# ==========================================
# 1. Base de Datos Simulada
# ==========================================
# TODO: Creen una lista llamada 'inventario' que contenga al menos 4 productos.
# Cada producto debe ser un diccionario con las llaves: 'id', 'nombre', 'precio' y 'stock'.
inventario = [
    # Escriban aquí sus productos...
]


# ==========================================
# 2. Petición (Payload) del Cliente
# ==========================================
# TODO: Creen un diccionario llamado 'orden_compra' que simule los datos que envía el frontend.
# Debe contener: 'id_orden', 'cliente', y 'productos_ids' (una LISTA con 2 o 3 IDs de los productos que quiere comprar).
orden_compra = {
    # Escriban aquí el payload...
}


# ==========================================
# 3. Lógica del Carrito (Ciclo FOR)
# ==========================================
# TODO: Implementen la lógica para calcular el total a pagar y actualizar el stock.
print("--- Procesando Orden ---")
total_a_pagar = 0

# a) Recorran la lista 'inventario' con un ciclo FOR.
# b) Si el 'id' del producto está en la lista de 'productos_ids' de la orden:
# c) Verifiquen si el 'stock' es mayor a 0 (Condicional).
# d) Si hay stock: sumen el precio a 'total_a_pagar' y resten 1 al 'stock' (Operaciones Aritméticas).
# e) Si no hay stock: Impriman que el producto está agotado.

for producto in inventario:
    pass # Reemplacen 'pass' por su lógica aquí
    

print(f"\nTotal calculado a pagar: ${total_a_pagar}")
print("Inventario actualizado:", inventario)
print("\n")


# ==========================================
# 4. Pasarela de Pago (Ciclo WHILE)
# ==========================================
# TODO: Simulen la conexión a un banco para cobrar el 'total_a_pagar'.
print("--- Pasarela de Pago ---")
pago_exitoso = False
intentos = 0
limite_intentos = 3

# a) Creen un ciclo WHILE que se ejecute mientras el pago NO sea exitoso Y los intentos sean menores al límite.
# b) En cada iteración, sumen 1 a los intentos e impriman "Contactando al banco... (Intento X)"
# c) Simulen que el pago se aprueba (pago_exitoso = True) solo cuando el intento sea igual a 2.

# Escriban aquí su ciclo WHILE...



# Validación Final
if pago_exitoso:
    print("✅ ¡Pago aprobado! Orden completada con éxito.")
else:
    print("❌ Error: El pago fue declinado por el banco después de 3 intentos.")

