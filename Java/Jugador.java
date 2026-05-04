public class Jugador {
    // Atributos con su tipo de dato
    public String nombre;
    public String equipo;
    private int goles = 0;

    // El Constructor
    public Jugador(String nombre, String equipo) {
        this.nombre = nombre;
        this.equipo = equipo;
    }

    // Métodos (Acciones)
    public void hacerGol() {
        this.goles++;
        System.out.println("¡GOOOOL de " + this.nombre + "!");
    }

    public void transferir(String nuevoEquipo) {
        this.equipo = nuevoEquipo;
        System.out.println(this.nombre + " ahora juega en " + this.equipo);
    }
}
