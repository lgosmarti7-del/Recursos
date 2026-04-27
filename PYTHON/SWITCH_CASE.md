# Explicacion

En el video aprendí que en Python moderno existe algo llamado `match`. Es como un `if` pero mucho más ordenado cuando tienes muchas opciones


**Ejemplo que hice:**
```python
dia = "Sábado"

match dia:
    case "Lunes":
        print("A estudiar duro")
    case "Sábado" | "Domingo":
        print("¡Día de descanso! 😴")
    case _:
        print("Es un día normal")
```
