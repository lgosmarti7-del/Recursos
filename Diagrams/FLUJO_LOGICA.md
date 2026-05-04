flowchart TD
    A[Inicio: Llamada a hacer_gol] --> B{¿Hubo anotación?}
    B -- Sí --> C[Sumar 1 a __goles]
    C --> D[Imprimir mensaje de GOOOL]
    B -- No --> E[Fin del método]
    D --> E
