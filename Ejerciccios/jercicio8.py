import sys

def main():
    print("Argumentos recibidos:", sys.argv)
    if len(sys.argv) > 1:
        nombre = sys.argv[1]
        mensaje = f"Hola, {nombre} 👋"
        if len(sys.argv) > 2:
            edad = sys.argv[2]
            mensaje += f", tienes {edad} años"
        if len(sys.argv) > 3:
            ciudad = sys.argv[3]
            mensaje += f" y vives en {ciudad}"
        print(mensaje)
    else:
        print("No se proporcionó ningún argumento")

if __name__ == "__main__":
    main()
