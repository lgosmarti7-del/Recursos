# Diseño Lógico - Apuntes de Base de Datos

## 📊 Tablas de la Clase (Pasadas en Limpio)

A continuación se presentan los datos de la pizarra organizados de forma estructurada.

### 🐾 Tabla: MASCOTA
Almacena el registro de los animales atendidos en el sistema.


| ID | Nombre | Raza | Género | Fecha_Nacimiento | Especie |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **10** | DUQUE | Mestizo | M | 2018-03-09 | PERRO |
| **7** | CHIRIPA | Poodle | F | 2017-04-15 | PERRO |
| **2** | MOTA | Pug | M | 2012-01-20 | PERRO |

### 👤 Tabla: TUTOR
Contiene la información de contacto e identificación de los dueños de las mascotas.


| ID | Nombre | Dirección | Correo_Electrónico | Teléfono | RUT |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | TAMARA | Calle Principal 123 | tamara@email.com | +56911111111 | 11.111.111-1 |
| **2** | ALBERTO | Avenida Central 456 | alberto@email.com | +56922222222 | 22.222.222-2 |
| **3** | RAMIRO | Pasaje Interior 789 | ramiro@email.com | +56933333333 | 33.333.333-3 |

### 🔗 Tabla Intermedia: MASCOTA_TUTOR
Entidad intermedia utilizada para resolver la relación lógica entre los tutores y sus mascotas.


| ID | ID_TUTOR | ID_MASCOTA |
| :--- | :--- | :--- |
| **1** | 1 | 10 |
| **2** | 3 | 7 |
| **3** | 2 | 2 |

---

## 📷 Evidencia del Trabajo en Clase
*(Nota: Recuerda guardar tu foto de la pizarra en esta misma carpeta con el nombre `pizarra_clase.jpg`)*

![Pizarra de la Clase](pizarra_clase.jpg)

---

## ❓ Cuestionario E.1.2

### 1. ¿Según sus palabras qué es una base de datos?
Es un sistema digital estructurado diseñado para almacenar, organizar y administrar grandes volúmenes de datos de forma segura y relacionada. Permite a los usuarios e aplicaciones realizar consultas, actualizaciones y análisis de la información de manera rápida y eficiente, garantizando que los datos no se pierdan con el tiempo.

### 2. ¿Por qué es en el ejemplo visto en clases, es mejor usar float a cambios de int en el ingreso del campo edad?
Porque el tipo `FLOAT` permite almacenar valores decimales indispensables para registrar la edad de animales muy jóvenes (cachorros). Por ejemplo, un cachorro de 6 meses se puede guardar de forma precisa como `0.5`. Si usáramos un tipo `INT`, el sistema obligaría a redondear a `0` o `1`, perdiendo exactitud clínica.

### 3. ¿Por qué ingresar edad en un sistema de base de datos no es recomendable y cuál sería una mejor opción en este caso justifique?
No es recomendable porque la edad es un atributo dinámico que cambia automáticamente cada día, lo que obligaría a actualizar la base de datos constantemente para evitar datos obsoletos. La mejor opción es almacenar de forma fija la fecha de nacimiento (`DATE`) y calcular la edad en tiempo real mediante programación.

### 4. El "Dato" vs. "Realidad": Si el sistema debe enviar un saludo automático de "Feliz Cumpleaños" cada año, ¿qué problema técnico enfrentaríamos si solo guardamos 0.5 y no la fecha de nacimiento (DATE)?
El problema técnico es que el valor `0.5` es una magnitud estática que no posee ninguna referencia temporal en el calendario actual (carece de día y mes de nacimiento). Al no saber la fecha exacta en la que el animal nació, el motor de software es incapaz de activar un disparador o alerta automatizada el día del cumpleaños real.
