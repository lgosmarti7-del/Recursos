class Heroe:
    def __init__(self, nombre, salud_maxima):
      
        self.nombre = nombre
        self.salud_maxima = salud_maxima
        
        self.__salud_actual = salud_maxima 

    def salud_actual(self):
        return self.__salud_actual

    salud_actual.setter
    def salud_actual(self, valor):
        if valor < 0:
            self.__salud_actual = 0
        elif valor > self.salud_maxima:
            self.__salud_actual = self.salud_maxima
        else:
            self.__salud_actual = valor
          
    def recibir_danio(self, cantidad):
        self.salud_actual -= cantidad
        print(f"{self.nombre} ha recibido {cantidad} de daño. Salud restante: {self.salud_actual}")
      
    def curar(self, puntos):
        self.salud_actual += puntos
        print(f"{self.nombre} se ha curado. Salud actual: {self.salud_actual}")

    def estado_critico(self):
        # Realiza un cálculo basado en atributos
        porcentaje = (self.salud_actual / self.salud_maxima) * 100
        if porcentaje <= 20:
            print(f"¡ALERTA! {self.nombre} está en estado crítico ({porcentaje}% de vida).")
        else:
            print(f"{self.nombre} se encuentra estable ({porcentaje}% de vida).")


guerrero = Heroe("Ragnar", 100)
guerrero.recibir_danio(85)
guerrero.estado_critico()
guerrero.curar(10)

print("-" * 10)

maga = Heroe("Morgana", 60)
maga.recibir_danio(10)
maga.estado_critico()
maga.curar(50) # El setter limitará a su salud_maxima
