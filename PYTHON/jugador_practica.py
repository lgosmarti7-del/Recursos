class Jugador:
    # 2. El "Nacimiento"
    def __init__(self, nombre, equipo):
        self.nombre = nombre
        self.equipo = equipo
        self.__goles = 0 

    # 3. El "Cajero"
    def goles(self):
        return self.__goles

    # 4. Las "Acciones" (Métodos)
    
    # Acción 1: Meter un gol (Suma 1 al contador)
    def hacer_gol(self):
        self.__goles = self.__goles + 1
        print(f"¡GOOOOL de {self.nombre}! Ya lleva {self.__goles}")

  
    def transferir(self, nuevo_equipo)
        self.equipo = nuevo_equipo
        print(f"{self.nombre} ahora juega en {self.equipo}")

    # Acción 3: Ver ficha completa
    def ver_ficha(self):
        print(f"Jugador: {self.nombre} | Equipo: {self.equipo} | Goles: {self.__goles}")

jugador1 = Jugador("Alexis", "Marsella")
jugador1.hacer_gol()
jugador1.transferir("Inter")
jugador1.ver_ficha()

jugador2 = Jugador("Vidal", "Colo Colo")
jugador2.hacer_gol()
jugador2.ver_ficha()

