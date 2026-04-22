## Encapsulación

### ¿Cómo se encapsulaa el codigo en Python?
En Python la encapsulación se logra usando guiones bajos antes del nombre de un atributo o método. 
* Si usas un guion (`_atributo`), es un aviso de que es privado (por convención).
* Si usas dos guiones (`__atributo`), Python "esconde" el nombre para que no sea fácil acceder a él desde fuera de la clase.

```python
class Personaje:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo encapsulado (privado)
```

### ¿Para qué se usan los métodos Get y Set?
Se usan como "intermediarios" o porteros. 
* **Get (Obtener):** Sirve para leer el valor de un atributo privado.
* **Set (Establecer):** Sirve para modificar el valor de un atributo privado, permitiéndonos validar la información (por ejemplo, evitar que la vida sea un número negativo).

```python
def get_fuerza(self):
    return self.__fuerza

def set_fuerza(self, valor):
    if valor > 0:
        self.__fuerza = valor
```

### ¿Se puede acceder a los métodos o atributos una vez encapsulados?
No se puede acceder a ellos de forma directa usando el punto (ej. `personaje.__vida` dará error). La única forma correcta de acceder es a través de los métodos **Get** y **Set** que definimos dentro de la clase. Esto se justifica porque la encapsulación busca proteger la integridad de los datos, evitando que el estado interno del objeto sea alterado de manera accidental o malintencionada desde el exterior del programa.

---
### Archivo de Código Encapsulado
Puedes ver la versión protegida aquí: [personaje_encapsulado.py](./personaje_encapsulado.py)
