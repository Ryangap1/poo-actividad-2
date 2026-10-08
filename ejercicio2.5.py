from enum import Enum

class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"

class CuentaBancaria:

    def __init__(self, nombre: str, apellidos: str, numero_cuenta: int, tipo_cuenta: TipoCuenta, interes_mensual: float):

        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0
        self.interes_mensual = interes_mensual

    def depositar(self, montod: float) -> None:
        
        if montod > 0:
            self.saldo += montod
            print(f"Deposito exitoso. Nuevo saldo: {self.saldo}")

    def retirar(self, montor: float) -> None:
        
        if montor > self.saldo:
            print("El monto a retirar supera el saldo de la cuenta")
        elif montor <= 0:
            print("El monto a retirar debe ser mayor a 0.")
        else:
            self.saldo -= montor
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")

    def aplicar_interes(self) -> None:
        interes = self.saldo*(self.interes_mensual/100)
        self.saldo += interes
        print(
            f"Se aplicó un interés del {self.interes_mensual}%. "
            f"Interés generado: {interes:.2f}. Nuevo saldo: {self.saldo:.2f}"
        )

    def informacion_cuenta(self) -> str:

        return(
            f"\nINFORMACIÓN DE LA CUENTA"
            f"\nNombre del titular: {self.nombre}"
            f"\nApellidos del titular: {self.apellidos}"
            f"\nNumero de cuenta: {self.numero_cuenta}"
            f"\nTipo de cuenta: {self.tipo_cuenta.value}"
            f"\nSaldo: {self.saldo}"
            f"\nPorcentaje de interes mensual: {self.interes_mensual}"
        )

def main():

    print("CUENTA BANCARIA")
    nombre = input("Ingrese el nombre del titular: ")
    apellidos = input("Ingrese los apellidos del titular: ")
    numero = int(input("Ingrese el numero de su cuenta bancaria: "))
    interes = float(input("Ingrese el porcentaje de interes mensual: "))
    print("\nSeleccione el tipo de cuenta:")
    print("1. Ahorros | 2. Corriente ")
    opcion_cuenta = int(input("Opcion: "))
    cuenta = {
        1: TipoCuenta.AHORROS,
        2: TipoCuenta.CORRIENTE
    }
    tipo_cuenta = cuenta.get(opcion_cuenta, TipoCuenta.AHORROS)
    mi_cuenta = CuentaBancaria(nombre, apellidos, numero, tipo_cuenta, interes)
    print(mi_cuenta.informacion_cuenta())
    monto_depositar = float(input("\nIngrese el monto a depositar: "))
    mi_cuenta.depositar(monto_depositar)
    print("\nAplicando interés mensual...")
    mi_cuenta.aplicar_interes()
    monto_retirar = float(input("\nIngrese el monto a retirar: "))
    mi_cuenta.retirar(monto_retirar)
    print(mi_cuenta.informacion_cuenta())

if __name__ == "__main__":
    main()