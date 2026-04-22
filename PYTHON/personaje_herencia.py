class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

# Aquí empieza la Herencia
class Guerrero(Personaje):
    # La clase Guerrero hereda de Personaje
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        # Usamos super() para no repetir el código del padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada # Atributo nuevo solo del guerrero

    # Podemos cambiar un método (Sobrecarga)
    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)

# Prueba básica
mi_guerrero = Guerrero("Aragorn", 20, 10, 10, 100, 5)
mi_guerrero.atributos()
