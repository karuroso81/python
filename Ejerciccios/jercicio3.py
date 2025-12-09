def presentar_persona(nombre="Usuario", edad=None, *aficiones):
    mensaje = f"{nombre}"
    if edad:
        mensaje += f" tiene {edad} años"
    if aficiones:
        mensaje += " y le gusta: " + ", ".join(aficiones)
    print(mensaje)

# Ejemplos de uso
presentar_persona("Ana", 25, "leer", "correr", "viajar")
presentar_persona("Luis", 30)
presentar_persona()
