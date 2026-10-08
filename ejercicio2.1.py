class Persona:

    def __init__(self, nombre: str, apellidos: str, numero_documento: int, ano_nacimiento: int, genero: str, pais_nacimiento: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento = numero_documento
        self.ano_nacimiento = ano_nacimiento
        self.genero = genero.upper()
        self.pais_nacimiento = pais_nacimiento

    def obtener_genero(self) -> str:
        if self.genero in ['H', 'M']:
            return self.genero
        else:
            return "Genero no valido"

    def informacion_persona(self) -> str:

        return(
            f"\nNombre completo: {self.nombre} {self.apellidos}"
            f"\nDocumento: {self.numero_documento}"
            f"\nAño de nacimiento: {self.ano_nacimiento}"
            f"\nGenero: {self.obtener_genero()}"
            f"\nPais de nacimiento: {self.pais_nacimiento}"
        )

def main():
    nombre1 = input("Ingrese el nombre de la persona #1: ")
    apellidos1 = input("Ingrese los apellidos de la persona #1: ")
    documento1 = int(input("Ingrese el numero de documento de la persona #1: "))
    ano1 = int(input("Ingrese el año de nacimiento de la persona #1: "))
    genero1 = input("Ingrese el genero de la persona #1 con H o M para hombre o mujer respectivamente: ")
    pais1 = input("Ingrese el pais de nacimiento de la persona #1: ")

    persona1 = Persona(nombre1, apellidos1, documento1, ano1, genero1, pais1)

    nombre2 = input("Ingrese el nombre de la persona #2: ")
    apellidos2 = input("Ingrese los apellidos de la persona #2: ")
    documento2 = int(input("Ingrese el numero de documento de la persona #2: "))
    ano2 = int(input("Ingrese el año de nacimiento de la persona #2: "))
    genero2 = input("Ingrese el genero de la persona #2 con H o M para hombre o mujer respectivamente: ")
    pais2 = input("Ingrese el pais de nacimiento de la persona #2: ")     

    persona2 = Persona(nombre2, apellidos2, documento2, ano2, genero2, pais2)

    print(f"\nLos datos de la persona #1 son: {persona1.informacion_persona()}")
    print(f"\nLos datos de la persona #2 son: {persona2.informacion_persona()}")
    print()

if __name__ == "__main__":
    main()