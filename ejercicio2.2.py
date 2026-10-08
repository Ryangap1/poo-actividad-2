from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"

class Planeta:

    def __init__(self, nombre: str, cantidad_satelites: int, masa: float, volumen: float, diametro: float, distancia_sol: float, tipo_planeta: TipoPlaneta, observable: bool, periodo_orbital: float, periodo_rotacion: float):

        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo_planeta = tipo_planeta
        self.observable = observable
        self.periodo_orbital = periodo_orbital
        self.periodo_rotacion = periodo_rotacion

    def calcular_densidad(self) -> float:

        return self.masa/self.volumen

    def planeta_exterior(self) -> bool:

        return self.distancia_sol > 508.5

    def informacion_planeta(self) -> str:

        return (
            f"\n--- Informacion del Planeta: {self.nombre} ---"
            f"\nSatelites: {self.cantidad_satelites}"
            f"\nMasa: {self.masa} kg"
            f"\nVolumen: {self.volumen} km³"
            f"\nDiametro: {self.diametro} km"
            f"\nDistancia al Sol: {self.distancia_sol} millones de km"
            f"\nTipo de planeta: {self.tipo_planeta.value}"
            f"\nObservable a simple vista: {self.observable}"
            f"\nPeriodo orbital: {self.periodo_orbital} años"
            f"\nPeriodo de rotacion: {self.periodo_rotacion} días"
            f"\nDensidad: {self.calcular_densidad():.4f} kg/km³"
            f"\n¿Es planeta exterior?: {self.planeta_exterior()}"
        )

def main():
    nombre1 = input("Ingrese el nombre del planeta #1: ")
    satelites1 = int(input("Ingrese el numero de satelites que tiene el planeta #1: "))
    masa1 = float(input("Ingrese la masa del planeta #1 en kg: "))
    volumen1 = float(input("Ingrese el volumen del planeta #1 en km³: "))
    diametro1 = float(input("Ingrese el diametro del planeta #1 en km: "))
    sol1 = float(input("Ingrese la distancia media al sol del planeta #1 en millones de km: "))
    print("\nSeleccione el tipo de planeta del planeta #1: ")
    print("1. Gaseoso")
    print("2. Terrestre")
    print("3. Enano")
    opcion1 = int(input("Ingrese el numero de la opcion: "))
    if opcion1 == 1:
        tipo_elegido1 = TipoPlaneta.GASEOSO
    elif opcion1 == 2:
        tipo_elegido1 = TipoPlaneta.TERRESTRE
    elif opcion1 == 3:
        tipo_elegido1 = TipoPlaneta.ENANO
    else:
        print("Opcion invalida. Se asignara Terrestre por defecto.")
        tipo_elegido1 = TipoPlaneta.TERRESTRE
    print("\nSeleccione si el planeta #1 es observable o no: ")
    print("1. Si")
    print("2. No")
    observa1 = int(input("ingrese el numero de la opcion: "))
    if observa1 == 1:
        observable1 = True
    elif observa1 == 2:
        observable1 = False
    else:
        print("Opcion invalida. Se asignara No por defecto.")
        observable1 = False
    orbital1 = float(input("Ingrese el periodo orbital del planeta #1 en años: "))
    rotacion1 = float(input("Ingrese el periodo de rotacion del planeta #1 en dias: "))

    planeta1 = Planeta(nombre1, satelites1, masa1, volumen1, diametro1, sol1, tipo_elegido1, observable1, orbital1, rotacion1)

    nombre2 = input("Ingrese el nombre del planeta #2: ")
    satelites2 = int(input("Ingrese el numero de satelites que tiene el planeta #2: "))
    masa2 = float(input("Ingrese la masa del planeta #2 en kg: "))
    volumen2 = float(input("Ingrese el volumen del planeta #2 en km³: "))
    diametro2 = float(input("Ingrese el diametro del planeta #2 en km: "))
    sol2 = float(input("Ingrese la distancia media al sol del planeta #2 en millones de km: "))
    print("\nSeleccione el tipo de planeta del planeta #2: ")
    print("1. Gaseoso")
    print("2. Terrestre")
    print("3. Enano")
    opcion2 = int(input("Ingrese el numero de la opcion: "))
    if opcion2 == 1:
        tipo_elegido2 = TipoPlaneta.GASEOSO
    elif opcion2 == 2:
        tipo_elegido2 = TipoPlaneta.TERRESTRE
    elif opcion2 == 3:
        tipo_elegido2 = TipoPlaneta.ENANO
    else:
        print("Opcion invalida. Se asignara Terrestre por defecto.")
        tipo_elegido2 = TipoPlaneta.TERRESTRE
    print("\nSeleccione si el planeta #2 es observable o no: ")
    print("1. Si")
    print("2. No")
    observa2 = int(input("ingrese el numero de la opcion: "))
    if observa2 == 1:
        observable2 = True
    elif observa2 == 2:
        observable2 = False
    else:
        print("Opcion invalida. Se asignara No por defecto.")
        observable2 = False
    orbital2 = float(input("Ingrese el periodo orbital del planeta #2 en años: "))
    rotacion2 = float(input("Ingrese el periodo de rotacion del planeta #2 en dias: "))

    planeta2 = Planeta(nombre2, satelites2, masa2, volumen2, diametro2, sol2, tipo_elegido2, observable2, orbital2, rotacion2)

    print(planeta1.informacion_planeta())
    print(planeta2.informacion_planeta())
    print()

if __name__ == "__main__":
    main()