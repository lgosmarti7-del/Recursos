<img width="3676" height="2090" alt="IMG_5473" src="https://github.com/user-attachments/assets/3cde47a0-e21e-410e-a2fa-ff9811b3ddea" />


#### 1- ¿Que formas normales uso y por que?
R.- Qué usé: Usé 1NF, 2NF y 3NF
- Por qué: Para eliminar datos duplicados y ordenar la base de datos Asi , si cambio la ciudad de un equipo o el nombre de un jugador, se actualiza en un solo lugar y no se genera desorden.

#### 2- ¿Cual fue la parte más compleja de resolver y por qué?
R.- La complejidad fue Diseñar la tabla intermedia Fichajes
- Porque los jugadores y los equipos tienen una relación de muchos a muchos. Tuve que crear esta tabla para conectar bien los ID_Jugador y los ID_Equipo

#### 3- Que tablas aun le faltaría a su sistema para producción y por qué?
R.- 
Algunas tablas que aun faltan son: 
* Contratos: Para registrar sueldos y fechas de vencimiento de los jugadores por un tema legal.
* Partidos: Para poder calendarizar el campeonato y saber qué equipos juegan en cada fecha.
* Estadísticas: Para registrar los goles, minutos y tarjetas de cada jugador en los *partidos reales.
