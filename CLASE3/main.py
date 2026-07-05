"""clase 03: Ciclos y listas


"""
print("listas de Python")

#Lista de cadenas de Caracteres
endpoints_api =["/users","products","/login","/orders"]
print(endpoints_api)

#Acceso a elementos de la lista
print(endpoints_api[2])

indice = 2
print(f"Endpoint en la posicion : {indices} es: {endpoints_api[indice]}"))


# Adicion
endpoints_api.append("/settings")
print(f"Lista actualizada: {endpoints_api}")

#ultimo elemento
ultimo = endpoints_api[-1]
print(f"Ultimo elemento de la lista: {ultimo}")
print(f"Ultimo elemento de la lista: {endpoints_api[-1]}")

print("Diccionarios")

# Diccionario de Python
user_payload = {
  "id": 1,
  "name": "Luis",
  "is_active": True,
  "roles": "superuser"
}

print(user_payload)

#print(type(user_payload)

print(f"Roles del usuario: {user_payload['roles']}")


#simulamos una base de datos con una lista de diccionarios productos

products_db = [
    {"id": 1, "name": "Laptop", "price": 100,"Stock": 10},
    {"id": 2, "name": "Mouse Inalambrico", "price": 200,"Stock": 5},
    {"id": 3, "name": "Teclado Inalambrico", "price": 300,"Stock": 15}
    
]

print("conexion existosa")

#Actualizar el precio del primer producto con el IVA para todos los producto

for i in range(len(products_db)):
    products_db[i]['price'] = products_db[i]['price'] * 1.16
    
    
inventario = [
    {"id": 1, "nombre": "papitas", "precio": 100,"Stock": 13},
    {"id": 2, "nombre": "refresco", "precio": 25,"Stock": 15},
    {"id": 3, "nombre": "queso", "precio": 50,"Stock": 20},
    {"id": 4, "nombre": "Cerveza", "precio": 45,"Stock": 30},
    {"id": 5, "nombre": "agua", "precio": 10,"Stock": 10},   
]

orden_compra = {"id_orden": 1, "cliente": "Luis", "productos_ids": [1,2,3]}
  

print("procesando la orden")  

for i in range(len(inventario)):
  if inventario[i]["id"] in orden_compra ["productos_ids"]:
    
  

