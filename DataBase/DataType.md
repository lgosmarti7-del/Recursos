## E.3.1 
## 1. Sobre el tipo CHAR
- Almacenamiento: Guarda texto con una longitud fija, lo que significa que siempre va a ocupar exactamente el mismo espacio en la memoria sin importar lo que escribas

### 2. Sobre el tipo VARCHAR
- Diferencia con CHAR: VARCHAR es de longitud variable; la "N" solo marca el límite máximo permitido de letras, no lo que ocupa obligatoriamente.
Es más eficiente: Porque la base de datos solo usa el espacio real de lo que escribes, Si guardas un nombre corto, no se desperdicia ni un solo espacio de memoria.

### 3. Sobre el tipo TEXT
- Escenarios de diseño: Está hecho para guardar bloques gigantes de texto, como descripciones largas de productos o comentarios extensos
Ventaja clave: No tienes que preocuparte por poner un límite estricto de caracteres, ya que te permite almacenar textos muy amplios sin que se corten

### 4. Análisis de caso práctico
Tipo elegido: Elegiría CHAR.
Por qué: Como todas las matrículas tienen exactamente el mismo tamaño 7 caracteres CHAR es perfecto porque no hay riesgo de desperdiciar espacio y es más rápido de procesar para datos fijos.

### 5. Gestión de almacenamiento
Riesgo en VARCHAR: Si se le pone un tamaño exageradamente grande, el riesgo principal es que estás perdiendo el control del límite de tus datos y podrías perder rendimiento en las consultas Además, si un usuario mete un texto enorme por error, la base de datos lo aceptará y podrías terminar saturando el almacenamiento de forma ineficiente.
