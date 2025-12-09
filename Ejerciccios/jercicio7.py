numeros_str = input("Introduce números separados por coma: ")
numeros = [int(n) for n in numeros_str.split(",")]

suma = sum(numeros)
promedio = sum(numeros)/len(numeros)
maximo = max(numeros)
minimo = min(numeros)

print(f"La suma es {suma}, el promedio es {promedio}, el máximo {maximo}, el mínimo {minimo}")
