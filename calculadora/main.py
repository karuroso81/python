# Importamos la función del otro archivo
from operaciones import calcular

def main():
    """Función principal que ejecuta la calculadora de forma continua."""
    print("=== Calculadora Simple ===")
    print("Puedes escribir 'salir' en cualquier momento para terminar.")

    while True:
        try:
            # Pedimos el primer número
            entrada_num1 = input("\nIngresa el primer número: ")
            if entrada_num1.lower() == 'salir':
                break
            num1 = float(entrada_num1)

            # Pedimos la operación
            operador = input("Elige la operación (+, -, *, /): ")
            if operador.lower() == 'salir':
                break

            # Pedimos el segundo número
            entrada_num2 = input("Ingresa el segundo número: ")
            if entrada_num2.lower() == 'salir':
                break
            num2 = float(entrada_num2)

            # Llamamos a la función y guardamos el resultado
            resultado = calcular(num1, operador, num2)

            # Imprimimos el resultado
            print(f"Resultado: {resultado}")

        except ValueError:
            print("Error: Debes ingresar valores numéricos. Inténtalo de nuevo.")
    
    print("¡Hasta luego!")

# Si este archivo se ejecuta directamente, llama a la función main()
if __name__ == "__main__":
    main()