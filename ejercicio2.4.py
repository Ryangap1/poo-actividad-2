import math

class Circulo:

    def __init__(self, radio: float):

        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi*(self.radio**2)

    def calcular_perimetro(self) -> float:
        return 2*math.pi*self.radio

class Rectangulo:

    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

class Cuadrado:

    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado**2

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

class Triangulo:

    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self) -> float:
        return math.sqrt(self.base**2 + self.altura**2)

    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self) -> str:
        if self.base == self.altura:
            return "Isósceles"
        else:
            return "Escaleno"

class Rombo:

    def __init__(self, diagonal_mayor: float, diagonal_menor: float):

        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_area(self) -> float:
        return (self.diagonal_menor*self.diagonal_mayor)/2

    def calcular_lado(self) -> float:
        return math.sqrt((self.diagonal_mayor/2)**2+(self.diagonal_menor/2)**2)

    def calcular_perimetro(self) -> float:
        return 4*self.calcular_lado()

class Trapecio:

    def __init__(self, base_mayor: float, base_menor: float, altura: float):

        self.base_mayor =base_mayor
        self.base_menor =base_menor
        self.altura = altura

    def calcular_area(self) -> float:
        return ((self.base_mayor+self.base_menor)*self.altura)/2

    def calcular_lado_inclinado(self) -> float:
        cateto_base = (self.base_mayor-self.base_menor)/2
        return math.sqrt(cateto_base**2+self.altura**2)

    def calcular_perimetro(self) -> float:
        return (self.base_mayor+self.base_menor+(2*self.calcular_lado_inclinado()))

def main():
    print("CALCULO DE FIGURAS GEOMETRICAS\n")

    print("CIRCULO")
    radio = float(input("Ingrese el radio en cm: "))
    circulo = Circulo(radio)
    print(f"Area: {circulo.calcular_area():.2f} cm²")
    print(f"Perimetro: {circulo.calcular_perimetro():.2f} cm\n")

    print("RECTANGULO")
    base_r = float(input("Ingrese la base en cm: "))
    altura_r = float(input("Ingrese la altura en cm: "))
    rectangulo = Rectangulo(base_r, altura_r)
    print(f"Area: {rectangulo.calcular_area():.2f} cm²")
    print(f"Perimetro: {rectangulo.calcular_perimetro():.2f} cm\n")

    print("CUADRADO")
    lado = float(input("Ingrese la longitud del lado en cm: "))
    cuadrado = Cuadrado(lado)
    print(f"Area: {cuadrado.calcular_area():.2f} cm²")
    print(f"Perimetro: {cuadrado.calcular_perimetro():.2f} cm\n")

    print("TRIANGULO")
    base_t = float(input("Ingrese la base en cm: "))
    altura_t = float(input("Ingrese la altura en cm: "))
    triangulo = Triangulo(base_t, altura_t)
    print(f"Area: {triangulo.calcular_area():.2f} cm²")
    print(f"Hipotenusa: {triangulo.calcular_hipotenusa():.2f} cm")
    print(f"Perimetro: {triangulo.calcular_perimetro():.2f} cm")
    print(f"Tipo: {triangulo.determinar_tipo_triangulo()}\n")

    print("ROMBO")
    d_mayor = float(input("Ingrese la diagonal mayor en cm: "))
    d_menor = float(input("Ingrese la diagonal menor en cm: "))
    rombo = Rombo(d_mayor, d_menor)
    print(f"Area: {rombo.calcular_area():.2f} cm²")
    print(f"Lado: {rombo.calcular_lado():.2f} cm")
    print(f"Perimetro: {rombo.calcular_perimetro():.2f} cm\n")

    print("TRAPECIO")
    b_mayor = float(input("Ingrese la base mayor en cm: "))
    b_menor = float(input("Ingrese la base menor en cm: "))
    alt_trap = float(input("Ingrese la altura en cm: "))
    trapecio = Trapecio(b_mayor, b_menor, alt_trap)
    print(f"Area: {trapecio.calcular_area():.2f} cm²")
    print(f"Lado inclinado: {trapecio.calcular_lado_inclinado():.2f} cm")
    print(f"Perimetro: {trapecio.calcular_perimetro():.2f} cm\n")


if __name__ == "__main__":
    main()