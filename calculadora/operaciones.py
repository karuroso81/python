def calcular(num1, operador, num2):
    """
    Realiza una operación matemática básica.
    Devuelve el resultado o un mensaje de error como una cadena.
    """
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: No se puede dividir por cero."
    else:
        return "Error: Operador no válido. Usa +, -, * o /."