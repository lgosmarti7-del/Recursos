# Mis apuntes de Clases en Python 🐍

Aquí explico lo que aprendí en el video sobre cómo crear personajes y proteger sus datos.

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
Es una palabra para decir "este". Si tengo a Goku y a Vegeta, `self` ayuda a que Python sepa que la vida es de "este" personaje y no del otro. Siempre hay que ponerlo de primero.

### ¿Qué es `def`?
Es la palabra que uso cada vez que voy a crear una acción (como atacar o morir). Le dice a Python: "Oye, aquí empieza una función".

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

## Parte 2: Encapsulación (Poner candados)

### ¿Cómo se encapsula el código?
Es fácil: solo le pongo **dos guiones bajos** `__` antes del nombre a las variables. Con eso, Python las esconde para que nadie las cambie por error desde afuera.

```python
self.__fuerza = fuerza  # Ahora tiene candado
```

### ¿Para qué sirven el Get y el Set?
Como los datos están escondidos, necesito una forma de usarlos:
* **Get:** Es para "pedir" el dato y poder verlo.
* **Set:** Es para "cambiar" el dato pero con cuidado (por ejemplo, para que nadie me ponga vida negativa).

### ¿Se puede entrar a lo que tiene candado?
No se puede entrar directo (con el punto), porque sale error. Solo se puede entrar usando los Get y Set que yo mismo creé. Esto sirve para que el código sea más seguro y no se rompa nada por accidente.

---

### Mis archivos de práctica
* [Código con candados: personaje_encapsulado.py](./personaje_encapsulado.py)







## Encapsulación

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

---
### Archivo de Código Refactorizado
Puedes ver la práctica de encapsulación aquí: [personaje_encapsulado.py](./personaje_encapsulado.py)
