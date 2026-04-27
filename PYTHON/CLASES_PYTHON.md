## Parte 1: Lo básico de los personajes

### El constructor (`__init__`)
Es algo inicial. Cuando creo un personaje, esta parte se encarga de ponerle su nombre, su vida y su fuerza sin necesidad de agregar mas cossas.

```python
def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
    self.nombre = nombre
    self.fuerza = fuerza
    self.inteligencia = inteligencia
    self.defensa = defensa
    self.vida = vida
```

### ¿Qué es `self`?
Es una palabra para decir este. Si tengo a dos personas peliando, `self` ayuda a que Python sepa que la vida es de este personaje y no del otro.

### ¿Qué es `def`?
Es la palabra que uso cada vez que voy a crear una acción (como atacar o morir)

### ¿Cómo ver un dato (atributo)?
Solo pongo el nombre del personaje, un punto y lo que quiero saber.
```python
print(guerrero.nombre)
```

### ¿Cómo usar una acción (método)?
Igual que arriba, pero le pongo paréntesis al final para que la acción se mueva.
```python
guerrero.atributos()
```

---

## Parte 2: Encapsulación

### ¿Cómo se encapsula el código?
Solo le pongo **dos guiones bajos** `__` antes del nombre a las variables. Con eso, Python las esconde para que nadie las cambie por error desde afuera.

```python
self.__fuerza = fuerza  # Ahora tiene candado
```

### ¿Para qué sirven el Get y el Set?
Como los datos están escondidos, necesito una forma de usarlos:
* **Get:** Es para pedir el dato y poder verlo.
* **Set:** Es para cambiar el dato pero con cuidado (por ejemplo, para que nadie me ponga vida negativa).

### ¿Se puede entrar a lo que tiene candado?
No se puede entrar directo (con el punto), porque sale error. Solo se puede entrar usando los Get y Set que yo mismo creé. Esto sirve para que el código sea más seguro y no se rompa nada por accidente.

---

### Mis archivos de práctica
* [Código con candados: personaje_encapsulado.py](./personaje_encapsulado.py)







## 2.- Encapsulación

### ¿Cómo se encapsula código en Python?
Se hace poniendo dos guiones bajos `__` antes del nombre de un atributo o un método. Al hacer esto, Python esconde esa variable para que no se pueda tocar directamente desde afuera de la clase, protegiendo los datos del personaje.

```python
self.__fuerza = fuerza  # Atributo encapsulado
```

### ¿Para qué se usan los métodos Get y Set?
Se usan para poder interactuar con los datos que escondimos. 
* **Get:** sirve para "obtener" o leer el valor del atributo.
* **Set:** sirve para "asignar" o cambiar el valor, permitiéndonos controlar que el nuevo dato sea correcto (por ejemplo, que no nos pongan vida negativa).

### ¿Se puede acceder a los métodos o atributos una vez encapsulados?
No se puede acceder de la forma normal (objeto.atributo) porque Python lanzará un error indicando que no existe. La única forma de entrar es creando funciones específicas dentro de la clase (los Get y Set), ya que esto asegura que el programador tenga el control total sobre cómo y cuándo se modifican los valores internos del objeto.



## 3.- Herencia 

### ¿Por qué da error al crear la clase Guerrero al inicio?
El error ocurre porque al heredar de `Personaje`, la clase `Guerrero` también necesita que le pasemos los datos al constructor (`__init__`). Si intentamos crear un Guerrero sin decirle cómo se llama o cuánta vida tiene, Python no sabe qué hacer y lanza un error.

### ¿A qué se refiere con "Súper Clase"?
La súper clase (o clase padre) es la clase principal de donde sacamos los datos. En nuestro ejemplo, `Personaje` es la súper clase y `Guerrero` es la subclase (clase hija).

### ¿Para qué sirve `pass`?
La palabra `pass` es como un "relleno". Se usa cuando quieres crear una clase o una función pero todavía no vas a escribir nada dentro. Le dice a Python: "No hagas nada, solo deja este espacio vacío por ahora" para que no dé error.

### ¿Qué es la función `super` y para qué sirve?
Es una función que sirve para llamar a los métodos de la clase padre desde la clase hija. Su beneficio es que nos ahorra escribir otra vez todo el código del constructor; simplemente le decimos a Python: "Usa lo que ya tiene la súper clase".

### ¿Qué es la herencia múltiple?
Se refiere a que una clase hija puede heredar de **varias** clases padres al mismo tiempo. Es como si un personaje pudiera heredar habilidades de una clase Mago y de una clase Guerrero a la vez.

### ¿Cuál es el beneficio de la Herencia?
El mayor beneficio es que **ahorramos código**. No tenemos que escribir lo mismo una y otra vez para cada tipo de personaje; escribimos lo básico en una clase y las demás solo copian lo que necesitan y añaden sus cosas especiales.

---
### Archivo de Herencia ( EJ Codigo)
Puedes ver la práctica aquí: [personaje_herencia.py](./personaje_herencia.py)

---
### Archivo de Código Refactorizado (Ej Codigo )
Puedes ver la práctica de encapsulación aquí: [personaje_encapsulado.py](./personaje_encapsulado.py)

## 4.- polimorfismo

¿Para qué se usa el polimorfismo?
Se utiliza para permitir que diferentes objetos (como un Guerrero o un Mago) respondan al mismo método (como daño()) de maneras distintas. Esto facilita que el código sea flexible, ya que podemos tratar a todos los personajes como una clase base pero ejecutar la lógica específica de cada uno

¿En el método daño(self, enemigo) qué deberíamos hacer en el caso de que la fuerza sea menor a la defensa?
Debemos agregar una validación para que el daño no sea un número negativo. Si la fuerza es menor a la defensa, el daño debe igualarse a 0, Sino al restar un daño negativo, el enemigo terminaría "curándose" en lugar de recibir daño

* Ejemplo Polimorfismo

```python
class Transporte:
    def desplazarse(self):
        pass

class Avion(Transporte):
    def desplazarse(self):
        return "Estoy volando por los aires"

class Barco(Transporte):
    def desplazarse(self):
        return "Estoy navegando por el océano"

class Bicicleta(Transporte):
    def desplazarse(self):
        return "Estoy pedaleando por la via"

def iniciar_viaje(vehiculo):
    print(vehiculo.desplazarse())

mi_avion = Avion()
mi_barco = Barco()

iniciar_viaje(mi_avion)  # Resultado: Estoy volando...
iniciar_viaje(mi_barco)  # Resultado: Estoy navegando...
```

#### 5.- Proyecto Final: Fundamentos de programacion computacional
## Proyecto Final: Clase Heroe

**Explicación:**
Cree el codigo para gestionar personajes de ficción elegí los atributos nombre y salud maxima para definir la identidad y resistencia del los personaje Los métodos permiten que el daño y la curación usando un atributo  para la salud actual.
**Enlace al script:**
[Ver código de práctica final](PROYECTO_practica.py)



