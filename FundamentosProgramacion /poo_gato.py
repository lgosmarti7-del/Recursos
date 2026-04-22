class Gato:
    def __init__(self, nombre, color, edad):
        self.nombre = nombre
        self.color = color
        self.edad = edad

    def maullar(self):
        print(self.nombre, "dice: ¡Miau!")

    def description(self):
        print("Este es", self.nombre, "es de color", self.color, "y tiene", self.edad, "años.")

# --- Prueba del gato ---
mi_gato = Gato("Pelusa", "Blanco", 3)
mi_gato.description()
mi_gato.maullar()

