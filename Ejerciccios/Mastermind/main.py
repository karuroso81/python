import funciones_mastermind as fn

def main():
    """Función principal que ejecuta el juego Mastermind."""
    fn.mostrar_leyenda()
    
    codigo_secreto = fn.generar_codigo_secreto()
    intentos = 0
    adivinado = False

    while not adivinado:
        intentos += 1
        intento_valido = False
        
        while not intento_valido:
            propuesta_str = input(f"\nIntento #{intentos}: Introduce 4 letras (ej. RAVA): ").upper()
            
            if len(propuesta_str) != fn.LONGITUD_CODIGO:
                print(f"Error: Debes introducir exactamente {fn.LONGITUD_CODIGO} letras.")
            elif not all(letra in fn.LETRAS_COLORES for letra in propuesta_str):
                print(f"Error: Solo puedes usar las letras {', '.join(fn.LETRAS_COLORES)}.")
            else:
                intento_valido = True

        intento_jugador = list(propuesta_str)
        
        print(f"Tu combinación: {fn.mostrar_combinacion_emojis(intento_jugador)}")
        
        aciertos_posicion, aciertos_color = fn.evaluar_intento(codigo_secreto, intento_jugador)
        
        print(f"Aciertos de color en la posición correcta: {aciertos_posicion}")
        print(f"Aciertos de color en la posición incorrecta: {aciertos_color}")

        if aciertos_posicion == fn.LONGITUD_CODIGO:
            adivinado = True

    print("\n" + "=" * 30)
    print(f"¡Felicidades! 🎉 Has adivinado la combinación en {intentos} intentos.")
    print(f"La combinación secreta era: {fn.mostrar_combinacion_emojis(codigo_secreto)}")
    print("=" * 30)


if __name__ == "__main__":
    main()