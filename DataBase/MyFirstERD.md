#### 1- ¿Que formas normales uso y por que?
R.- Qué usé: Usé 1NF, 2NF y 3NF

 Por qué: Para eliminar datos duplicados y ordenar la base de datos Asi , si cambio la ciudad de un equipo o el nombre de un jugador, se actualiza en un solo lugar y no se genera desorden.

#### 2- ¿Cual fue la parte más compleja de resolver y por qué?
R.- La complejidad fue Diseñar la tabla intermedia Fichajes, Porque los jugadores y los equipos tienen una relación de muchos a muchos. Tuvimos que crear esta tabla al medio para romper esa relación y conectar bien los ID_Jugador y los ID_Equipo

#### 3- Que tablas aun le faltaría a su sistema para producción y por qué?
R.- 
Algunas tablas que aun faltan son: 
* Contratos: Para registrar sueldos y fechas de vencimiento de los jugadores por un tema legal.
* Partidos: Para poder calendarizar el campeonato y saber qué equipos juegan en cada fecha.
* Estadísticas: Para registrar los goles, minutos y tarjetas de cada jugador en los *partidos reales.
