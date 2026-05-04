classDiagram
    class Jugador {
        +String nombre
        +String equipo
        -int goles
        +hacer_gol() void
        +transferir(nuevo_equipo) void
        +ver_ficha() void
    }
