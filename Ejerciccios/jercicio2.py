# Función para saludar
def saludar(nombre):
    return f"Hola {nombre}, ¡Hola!"

# Función para calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Ejemplo de uso con los datos del usuario
print(saludar(nombre))
peso = float(input("Introduce tu peso en kg: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

