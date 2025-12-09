#  REPOSITORIO DE PRÁCTICAS DEL MÓDULO DE PROGRAMACIÓN PYTHON



---

#  EJERCICIOS INDIVIDUALES (1–9)

##  Ejercicio 1

###  Descripción
Ejercicio de práctica 1.

###  Código ejemplo

```python
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
```

---

##  Ejercicio 2

###  Descripción
Ejercicio de práctica 2.

###  Código ejemplo

```python
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

```

---

##  Ejercicio 3

###  Descripción
Ejercicio de práctica 3.

###  Código ejemplo

```python
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
```

---

##  Ejercicio 4

###  Descripción
Ejercicio de práctica 4.

###  Código ejemplo

```python
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
```

---

##  Ejercicio 5

### Descripción
Ejercicio de práctica 5.

###  Código ejemplo

```python
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

```

---

##  Ejercicio 6

###  Descripción
Ejercicio de práctica 6.

###  Código ejemplo

```python
# Crear entorno virtual
#python -m venv env

# Activar
# Windows:
#.\env\Scripts\activate

# Instalar librería
#pip install emoji

# Guardar dependencias
#pip freeze > requirements.txt
```

---

##  Ejercicio 7

###  Descripción
Ejercicio de práctica 7.

###  Código ejemplo

```python
numeros_str = input("Introduce números separados por coma: ")
numeros = [int(n) for n in numeros_str.split(",")]

suma = sum(numeros)
promedio = sum(numeros)/len(numeros)
maximo = max(numeros)
minimo = min(numeros)

print(f"La suma es {suma}, el promedio es {promedio}, el máximo {maximo}, el mínimo {minimo}")
```

---

##  Ejercicio 8

###  Descripción
Ejercicio de práctica 8.

###  Código ejemplo

```python
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
```

---

##  Ejercicio 9

###  Descripción
Ejercicio de práctica 9.

###  Código ejemplo

```python
def calculadora():
    print("=== Calculadora Simple ===")
    print("Operaciones disponibles: +  -  *  /")
    
    num1 = float(input("Ingresa el primer número: "))
    operacion = input("Elige la operación (+, -, *, /): ")
    num2 = float(input("Ingresa el segundo número: "))
    
    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error: no se puede dividir entre 0")
            return
```

---

##  PROYECTO MASTERMINd

Carpeta: `Ejerciccios/Mastermind`

### main.py (fragmento)

```python
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
```

### funciones_mastermind.py (fragmento)

```python
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

```

---




##  TAREA 1.3
Carpeta: `Ejerciccios/tarea 1.3`

###  Descripción
Proyecto que utiliza FastAPI para exponer endpoints relacionados con datos del alumno (o similar, ver el código).

###  Código ejemplo (fragmento de `main.py`)
```python
# main.py
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI(title="iesazarquiel")

# Cargar el CSV REAL
df = pd.read_csv("datos_alumnos.csv", dtype={"ID": str})

# Para obtener nombre completo
def nombre_completo(row):
    return f"{row['Nombre']} {row['Apellidos']}"

# Campos de notas válidos
CAMPOS_NOTAS = ["Parcial1", "Parcial2", "Ordinario1", "Practicas", "OrdinarioPracticas"]


# -----------------------------
# 1) INFO-ALUMNOS (sin parámetros)
# -----------------------------
@app.get("/info-alumnos")
def info_alumnos():
    return {"ids_alumnos": df["ID"].tolist()}


# -----------------------------
# 2) ASISTENCIA (id opcional)
# -----------------------------
@app.get("/asistencia")
def asistencia(id: str = Query(None)):
    if id is None:
        return {
            "uso": "/asistencia?id=<ID>",
            "descripcion": "Devuelve el nombre y % asistencia del alumno.",
            "ids_disponibles": df["ID"].tolist()
        }

    fila = df[df["ID"] == id]
    if fila.empty:
        return JSONResponse(status_code=404, content={"error": "ID no encontrado"})

    fila = fila.iloc[0]
    return {
        "ID": id,
        "nombre": nombre_completo(fila),
        "asistencia": fila["Asistencia"]
    }


# -----------------------------
# 3) NOTAS (id y nota opcionales)
# -----------------------------
@app.get("/notas")
def notas(id: str = Query(None), nota: str = Query(None)):

    # Ningún parámetro → explicación
    if id is None and nota is None:
        return {
            "uso": "/notas?id=<ID>&nota=<campo>",
```

---

##  CALCULADORA (Ejercicio 9)
Archivo: `Ejerciccios/jercicio9.py`

###  Descripción
Pequeña calculadora interactiva por consola que realiza operaciones básicas (+, -, *, /) y controla la división por cero.

###  Código ejemplo (fragmento de `jercicio9.py`)
```python
def calculadora():
    print("=== Calculadora Simple ===")
    print("Operaciones disponibles: +  -  *  /")
    
    num1 = float(input("Ingresa el primer número: "))
    operacion = input("Elige la operación (+, -, *, /): ")
    num2 = float(input("Ingresa el segundo número: "))
    
    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error: no se puede dividir entre 0")
            return
    else:
        print("Operación no válida")
        return
    
    print(f"Resultado: {resultado}")

# Ejecutar la calculadora
calculadora()
   
```

---
#  AUTOR
Carlos — Prácticas del módulo Python.
