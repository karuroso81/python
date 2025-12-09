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
            "descripcion": "Devuelve la nota indicada del alumno.",
            "campos_validos": CAMPOS_NOTAS,
            "ejemplo": "/notas?id=1001&nota=Parcial1"
        }

    # Si ponen nota pero no ID → error
    if id is None:
        return JSONResponse(status_code=400, content={"error": "Si indicas 'nota' debes indicar 'id'."})

    fila = df[df["ID"] == id]
    if fila.empty:
        return JSONResponse(status_code=404, content={"error": "ID no encontrado"})

    fila = fila.iloc[0]

    # Si no se indica qué nota → devolver TODAS las notas (versión simplificada)
    if nota is None:
        return {
            "ID": id,
            "nombre": nombre_completo(fila),
            "notas": {campo: fila[campo] for campo in CAMPOS_NOTAS}
        }

    # Validar campo nota
    if nota not in CAMPOS_NOTAS:
        return JSONResponse(status_code=400, content={
            "error": "Campo de nota inválido.",
            "permitidos": CAMPOS_NOTAS
        })

    return {
        "ID": id,
        "nombre": nombre_completo(fila),
        "nota": nota,
        "valor": fila[nota]
    }


# Página raíz (opcional)
@app.get("/")
def root():
    return {"api": "iesazarquiel", "endpoints": ["/info-alumnos", "/asistencia", "/notas"]}

