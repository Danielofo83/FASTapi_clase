#PASCAL CASE
Class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


def depositar(self,cantidad:float):
    if cantidad > 0:
        self.saldo += cantidad
        print(f"Se han depositado {cantidad}. Nuevo saldo: {self.saldo}")
        return "La cantidad a depositar fue menor que cero."

def retirar(self,cantidad:float):
    if cantidad > 0:
        if cantidad >0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes.")
    else:
        return f"La cantidad a retirar fue menor que cero."
            
cuenta1 = CuentaBancaria("Juan Perez", 1000)
"""print("saldo inicial", cuenta1.saldo)
print("cuenta1.depositar(10_000)")"""

from fastapi import FastAPI

app = FastAPI("API con POO", description="Clase 6: POO con peticiones HTTP =D")

@app.get("/cuenta/estado")
def obtener_estado_cuenta():
    return {cuenta1.consultar_estado(): "saldo": cuenta1.saldo}

@app.post("/cuenta/depositar")
def depositar(cantidad: float):
    cuenta1.depositar(cantidad)
    return {"message": "Depósito realizado con éxito"}

@app.post("/cuenta/retirar")
def retirar(cantidad: float):
    cuenta1.retirar(cantidad)
    return {"message": "Retiro realizado con éxito"}

    
