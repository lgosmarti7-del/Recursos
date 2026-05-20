# 1.1 
## Apuntes de Clase 

## Tablas de la Pizarra


### Tablas de clase ( ejemplo ) 
<img width="1200" height="1600" alt="WhatsApp Image 2026-05-15 at 9 02 24 AM" src="https://github.com/user-attachments/assets/e74a4d99-ab5c-45d6-a2c3-9e7163830139" />


---

## 1.2

### 1. ¿Según sus palabras qué es una base de datos?
Es un sistema organizado que permite almacenar modificar y recuperar grande información , Funciona como un contenedor digital donde los datos se relacionan entre sí para ser consultados rápidamente cuando se necesitann

### 2. ¿Por qué en el ejemplo visto en clases es mejor usar float a cambio de int en el ingreso del campo edad?
Porque permite registrar edades fraccionadas o menores a un año, como un cachorro de 6 meses representado con 0,5

### 3. ¿Por qué ingresar edad en un sistema de base de datos no es recomendable y cuál sería una mejor opción en este caso? Justifique.
No es recomendable porque la edad es un dato dinámico que cambia cada año, lo que obligaría a actualizar la base de datos constantemente la mejor opción es registrar la fecha de nacimiento 

### 4. El "Dato" vs. "Realidad": Si el sistema debe enviar un saludo automático de "Feliz Cumpleaños" cada año, ¿qué problema técnico enfrentaríamos si solo guardamos 0.5 y no la fecha de nacimiento (DATE)?
El problema es que el valor 0.5 es estático y no vee el día ni el mes específico del nacimiento. Sin un tipo de dato `DATE`, el sistema tendra de un activador cronológico temporal, haciendo dificil programar un script automatizado que detecte el día exacto del cumpleaños


# 2.2 
## 1. Detección de Error

La tabla intermedia solo se usa cuando la relación es Muchos a Muchos (N:M). Sirve para ordenar el caos de que muchos se junten con muchos, creando un puente entre las dos tablas En el video, como la relación es de Muchos a Uno (N:1), hacer esa tabla es complicarse la vida por gusto Lo correcto y más fácil es meter el ID del Tutor directamente en la tabla de la Mascota y estaria no hace falta inventar otra tabla

## 2. Contexto de Negocio
Caso A: Clínica Veterinaria Hogar
Cardinalidad: Muchos a Uno (N:1)
En palabras: Una mascota tiene un solo dueño, pero un dueño puede llevar varias mascotas a la clínica.

Caso B: Hotel de Mascotas Premium
Cardinalidad: Muchos a Muchos (N:M)
En palabras: La mascota (perro) puede tener varios dueños y esos personas pueden tener varios perritos. Aquí sí va la tabla intermedia.

