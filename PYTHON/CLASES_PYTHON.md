## Encapsulación

### ¿Cómo se encapsula código en Python?
Se hace poniendo dos guiones bajos `__` antes del nombre de un atributo o un método. Al hacer esto, Python "esconde" esa variable para que no se pueda tocar directamente desde afuera de la clase, protegiendo los datos del personaje.

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
