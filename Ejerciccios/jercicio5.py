import emoji

# Mensaje simple con emoji
print(emoji.emojize("¡Bienvenido! :smile:", language="alias"))

# Función IMC con emoji
def calcular_imc_con_emoji(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        estado = "Bajo peso " + emoji.emojize(":warning:", language="alias")
    elif imc < 25:
        estado = "Normal " + emoji.emojize(":smile:", language="alias")
    else:
        estado = "Sobrepeso " + emoji.emojize(":exclamation:", language="alias")
    return imc, estado

# Pedir datos al usuario
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

# Calcular IMC
imc, estado = calcular_imc_con_emoji(peso, altura)
print(f"IMC: {imc:.2f}, Estado: {estado}")
