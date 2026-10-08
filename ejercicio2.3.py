from enum import Enum


class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas Natural"


class TipoAutomovil(Enum):
    CIUDAD = "Carro de Ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"


class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    PLATEADO = "Plateado"

class Automovil:

    def __init__(self, marca: str, modelo: int, motor: float, tipo_combustible: TipoCombustible, tipo_automovil: TipoAutomovil, numero_puertas: int, cantidad_asientos: int, velocidad_maxima: int, color: Color, es_automatico: bool):

        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.es_automatico = es_automatico
        self.velocidad_actual = 0
        self.multas = 0
        self.valor_multa = 633200

    def get_es_automatico(self) -> bool:
        return self.es_automatico

    def set_es_automatico(self, automatico: bool) -> None:
        self.es_automatico = automatico

    def acelerar(self, incremento: int) -> None:
        if self.velocidad_actual + incremento > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
            self.multas += 1 
            print(
                f"No se puede superar la velocidad maxima ({self.velocidad_maxima} km/h). "
                f"Se ha generado una multa."
            )
        else:
            self.velocidad_actual += incremento

    def desacelerar(self, decremento: int) -> None:
        if self.velocidad_actual - decremento < 0:
            print("No se puede decrementar a una velocidad negativa.")
            self.velocidad_actual = 0
        else:
            self.velocidad_actual -= decremento

    def frenar(self) -> None:
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia: float) -> float:
        if self.velocidad_actual == 0:
            print(
                "El vehículo está detenido (0 km/h). No se puede calcular el tiempo."
            )
            return 0.0
        return distancia / self.velocidad_actual

    def tiene_multas(self) -> bool:
        return self.multas > 0

    def total_multas(self) -> float:
        return self.multas * self.valor_multa

    def informacion_carro(self) -> str:

        return(
            f"\nMarca: {self.marca}"
            f"\nModelo: {self.modelo}"
            f"\nMotor: {self.motor}"
            f"\nTipo de combustible: {self.tipo_combustible.value}"
            f"\nTipo de automovil: {self.tipo_automovil.value}"
            f"\nNumero de puertas: {self.numero_puertas}"
            f"\nCantidad de asientos: {self.cantidad_asientos}"
            f"\nVelocidad maxima: {self.velocidad_maxima}"
            f"\nColor: {self.color.value}"
            f"\n¿Tiene multas?: {'Sí' if self.tiene_multas() else 'No'}"
            f"\nTotal multas: ${self.total_multas():,.0f}"
        )

def main():

    print("--- REGISTRO DE AUTOMOVIL ---")
    marca = input("Ingrese la marca del automovil: ")
    modelo = int(input("Ingrese el año de fabricacion del automovil: "))
    motor = float(input("Ingrese el volumen en litros del cilindraje del motor: "))
    print("\nSeleccione el tipo de combustible:")
    print("1. Gasolina | 2. Bioetanol | 3. Diésel | 4. Biodiésel | 5. Gas Natural")
    opc_comb = int(input("Opcion: "))
    combustibles = {
        1: TipoCombustible.GASOLINA,
        2: TipoCombustible.BIOETANOL,
        3: TipoCombustible.DIESEL,
        4: TipoCombustible.BIODIESEL,
        5: TipoCombustible.GAS_NATURAL,
    }
    tipo_combustible = combustibles.get(opc_comb, TipoCombustible.GASOLINA)
    print("\nSeleccione el tipo de automovil:")
    print(
        "1. Ciudad | 2. Subcompacto | 3. Compacto | 4. Familiar | 5. Ejecutivo | 6. SUV"
    )
    opc_auto = int(input("Opcion: "))
    automoviles = {
        1: TipoAutomovil.CIUDAD,
        2: TipoAutomovil.SUBCOMPACTO,
        3: TipoAutomovil.COMPACTO,
        4: TipoAutomovil.FAMILIAR,
        5: TipoAutomovil.EJECUTIVO,
        6: TipoAutomovil.SUV,
    }
    tipo_automovil = automoviles.get(opc_auto, TipoAutomovil.CIUDAD)
    puertas = int(input("\nIngrese el numero de puertas: "))
    asientos = int(input("Ingrese la cantidad de asientos: "))
    vel_maxima = int(input("Ingrese la velocidad maxima (km/h): "))
    print("\nSeleccione el color:")
    print(
        "1. Blanco | 2. Negro | 3. Rojo | 4. Naranja | 5. Amarillo | 6. Verde | 7. Azul | 8. Plateado"
    )
    opc_color = int(input("Opcion: "))
    colores = {
        1: Color.BLANCO,
        2: Color.NEGRO,
        3: Color.ROJO,
        4: Color.NARANJA,
        5: Color.AMARILLO,
        6: Color.VERDE,
        7: Color.AZUL,
        8: Color.PLATEADO,
    }
    color = colores.get(opc_color, Color.NEGRO)
    print("\n¿El vehiculo es automatico?")
    print("1. Sí | 2. No")
    opc_trans = int(input("Opcion: "))
    es_automatico = True if opc_trans == 1 else False
    carro = Automovil(
        marca,
        modelo,
        motor,
        tipo_combustible,
        tipo_automovil,
        puertas,
        asientos,
        vel_maxima,
        color,
        es_automatico,
    )
    print("\n" + "=" * 30)
    print(carro.informacion_carro())
    print("\n--- PRUEBAS DE MOVIMIENTO ---")
    carro.acelerar(100)
    print(f"Velocidad actual = {carro.velocidad_actual}")
    carro.acelerar(20)
    print(f"Velocidad actual = {carro.velocidad_actual}")
    carro.desacelerar(50)
    print(f"Velocidad actual = {carro.velocidad_actual}")
    carro.frenar()
    print(f"Velocidad actual = {carro.velocidad_actual}")
    carro.desacelerar(20)
    print()

if __name__ == "__main__":
    main()