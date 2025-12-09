#Aqui vemos los bucles
# Pedimos los datos al usuario
nombre = input("Introduce tu nombre: ")

# Para la edad y altura usamos bucles con validación
while True:
    try:
        edad = int(input("Introduce tu edad: "))
        break
    except ValueError:
        print("Error: debes ingresar un número entero para la edad.")

while True:
    try:
        altura = float(input("Introduce tu altura en metros: "))
        break
    except ValueError:
        print("Error: debes ingresar un número decimal para la altura.")

# Mostramos el mensaje con f-string
print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

# Mostramos el tipo de cada variable
print(f"Tipo de nombre: {type(nombre)}")
print(f"Tipo de edad: {type(edad)}")
print(f"Tipo de altura: {type(altura)}")
