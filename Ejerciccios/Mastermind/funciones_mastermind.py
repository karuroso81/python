import random
import emoji

# Definimos los colores disponibles y su correspondencia con letras y emojis
COLORES = {
    "R": ":red_circle:",
    "A": ":blue_circle:",
    "V": ":green_circle:",
    "M": ":yellow_circle:",
    "N": ":orange_circle:",
    "B": ":white_circle:",
}

LETRAS_COLORES = list(COLORES.keys())
LONGITUD_CODIGO = 4

def generar_codigo_secreto():
    """Genera una combinación aleatoria de 4 colores."""
    return random.choices(LETRAS_COLORES, k=LONGITUD_CODIGO)

def mostrar_combinacion_emojis(combinacion):
    """Convierte una lista de letras en una cadena de emojis."""
    emojis = [COLORES[letra] for letra in combinacion]
    return emoji.emojize(" ".join(emojis), language="alias")

def evaluar_intento(codigo_secreto, intento_jugador):
    """
    Evalúa el intento del jugador y devuelve el número de aciertos
    en posición y en color.
    """
    aciertos_posicion = 0
    aciertos_color = 0
    
    # Copias para poder modificarlas sin afectar las originales
    secreto_copia = list(codigo_secreto)
    intento_copia = list(intento_jugador)

    # 1. Buscar aciertos en posición (color y lugar correctos)
    for i in range(LONGITUD_CODIGO):
        if intento_copia[i] == secreto_copia[i]:
            aciertos_posicion += 1
            # Marcamos como "revisado" para no contarlos dos veces
            secreto_copia[i] = None
            intento_copia[i] = None

    # 2. Buscar aciertos de color (color correcto, lugar incorrecto)
    for i in range(LONGITUD_CODIGO):
        if intento_copia[i] is not None and intento_copia[i] in secreto_copia:
            aciertos_color += 1
            # Lo eliminamos de la copia del secreto para no volver a contarlo
            secreto_copia.remove(intento_copia[i])
            
    return aciertos_posicion, aciertos_color

def mostrar_leyenda():
    """Muestra la leyenda de colores y letras al jugador."""
    print("Bienvenido a Mastermind!")
    print("Intenta adivinar la combinación de 4 colores.")
    print("Leyenda de colores:")
    for letra, emoji_str in COLORES.items():
        print(f"  {letra}: {emoji.emojize(emoji_str, language='alias')}")
    print("-" * 30)
    
if __name__ == "__main__":
    main()