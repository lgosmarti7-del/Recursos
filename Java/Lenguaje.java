public class Lenguaje {
    String nombre;
    int año;

    public Lenguaje(String nombre, int año) {
        this.nombre = nombre;
        this.año = año;
    }

    public void descripcion() {
        System.out.println(nombre + " fue creado en " + año);
    }
}
