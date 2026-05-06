# SINTAXIS JAVA

## Texto:
```java
class Main {
    public static void main(String[] args) {
        String libro = "El programador pragmático"; // Guarda texto
    }
}
```

## NUMERO:

```class Main {
    public static void main(String[] args) {
        int entero = 100; 
        double decimal = 3.14; 
    }
}
```
## Booleans:
```class Main {
    public static void main(String[] args) {
        boolean autorizado = true;
        boolean seleccionado = false;
    }
}
```
## LISTA
```import java.util.ArrayList;

class Main {
    public static void main(String[] args) { // Creación de una lista
        ArrayList<Integer> numeros = new ArrayList<>(); // Lista para almacenar números enteros
        numeros.add(10); // Añadimos el número 10 a la lista
    }
}
```
## OBJETO:
```class Personaje {
    String nombre;
    int nivel;
class Main {
    public static void main(String[] args) {
        Personaje heroe = new Personaje(); // Creamos un nuevo objeto de la clase Personaje
        heroe.nombre = "Arturo";
    }
}
```

## Hashmap
¿Qué es y para qué se utiliza un hashmap?
* Es una estructura de datos que almacena pares de llave-valor para realizar búsquedas rápidas utilizando una clave única.

¿Cómo se importa?
* Se importa usando la línea: import java.util.HashMap;.

¿Cuántos tipos se mencionan en el video?
* Se mencionan 2 tipos de parámetros: la Llave (Key) y el Valor (Value).

Ejemplo de código:

```import java.util.HashMap;

class Main {
    public static void main(String[] args) {
        HashMap<Integer, String> jugadores = new HashMap<>();
        jugadores.put(10, "Messi"); // 10 es la llave, "Messi" es el valor
    }
}
```
## MODULOS
¿Para qué se usan los módulos?
* Se usan para organizar y dividir el código en diferentes archivos, facilitando que el proyecto sea más fácil de mantener y escalar.

¿Qué es el comando javac y cuál es su función?
* Es el compilador de Java. Su función es transformar el código fuente escrito por el programador en archivos de bytecode (.class) que la máquina virtual de Java puede ejecutar.
