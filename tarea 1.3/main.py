# main.py
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import pandas as pd
import os

app = FastAPI(title="iesazarquiel")

CSV_FILENAME = "datos_alumnos.csv"


CSV_CONTENT = """Apellidos,Nombre,ID,Asistencia,Parcial1,Parcial2,Ordinario1,Practicas,OrdinarioPracticas
"Anido Bonet",David,1001,90%,5.5,2.75,4,5,6
"Bueno Cerdeira",Patricia,1002,95%,9.5,9,8,6.25,6
"Casariego García",Raúl,1003,98%,4.25,5.75,6,4,5
"Curbelo Sánchez",Jorge,1004,75%,6.75,4.25,6,7,6.5
"Díaz Souto",Sofía,1005,82%,7,6.5,7,9,8
"García Perez",Yaiza,1006,85%,10,8,7,7.5,9
"Sánchez Jordán",María,1007,92%,8.75,9,8.5,6.5,8
"Lorenzo García",Jaime,1008,100%,9.75,8.25,9,7.5,7
"Martínez Lucas",Cecilia,1009,86%,7,4,5,6.25,5
"Mora Peñaloza",Sandra,1010,70%,5.25,2,3,6.5,4.5
"Morillo Escudero",Ana,1011,100%,9.5,10,9,8.75,6.5
"Muñoz Gómez",Carolina,1012,94%,7.75,6.5,8,4,5
"Ramirez de la Puente",Raquel,1013,75%,0,1,1,2.25,3.25
"Riego Pizarro",Carlos,1014,75%,4,2.5,5,7,8
"Rodríguez de Blas",Ignacio,1015,80%,8.25,5.25,6.5,6.5,9
"Moreno Angulo",Antonio,1016,88%,9,6.75,7,5.25,5
"""

def ensure_csv_exists():
    if not os.path.exists(CSV_FILENAME):
        with open(CSV_FILENAME, "w", encoding="utf-8") as f:
            f.write(CSV_CONTENT)

def load_dataframe():
    ensure_csv_exists()
    df = pd.read_csv(CSV_FILENAME, dtype={"ID": str})
    # Normalize columns: trim spaces
    df.columns = [c.strip() for c in df.columns]
    return df

df = load_dataframe()

# Helpers
def get_fullname(row):
    # Apellidos + Nombre (separado por una coma si prefieres otra forma, cámbialo)
    return f"{row['Nombre']} {row['Apellidos']}"

def allowed_nota_fields():
    return ["Parcial1", "Parcial2", "Ordinario1", "Practicas", "OrdinarioPracticas"]

# Endpoints
@app.get("/info-alumnos")
def info_alumnos():
    """
    Devuelve el listado de IDs de los alumnos.
    """
    ids = df["ID"].tolist()
    return {"alumnos_ids": ids, "count": len(ids)}

@app.get("/asistencia")
def asistencia(id: str = Query(None, description="ID del alumno (p. ej. 1001)")):
    """
    Si se pasa id -> devuelve nombre, apellidos y % de asistencia.
    Si no se pasa -> devuelve mensaje explicativo con número de parámetros y valores posibles.
    """
    if id is None:
        return JSONResponse(
            status_code=200,
            content={
                "modo_uso": "asistencia",
                "descripcion": "Este endpoint acepta 1 parámetro opcional: 'id' (ID del alumno).",
                "ejemplo": "/asistencia?id=1001",
                "valores_posibles_id": df["ID"].tolist(),
                "mensaje": "Si no especificas 'id', indica el ID del alumno que quieres consultar."
            }
        )

    # buscar alumno
    row = df[df["ID"] == id]
    if row.empty:
        return JSONResponse(status_code=404, content={"error": f"No se encontró alumno con ID {id}"})

    row = row.iloc[0]
    return {
        "ID": id,
        "nombre_completo": get_fullname(row),
        "asistencia": row["Asistencia"]
    }

@app.get("/notas")
def notas(
    id: str = Query(None, description="ID del alumno (p. ej. 1001)"),
    nota: str = Query(None, description=f"campo de nota. Posibles: {', '.join(allowed_nota_fields())}")
):
    """
    Recibe parámetros opcionales:
      - id (ID del alumno)
      - nota (nombre de la nota a consultar: Parcial1, Parcial2, Ordinario1, Practicas, OrdinarioPracticas)

    Si no se especifica ningún parámetro => devuelve mensaje explicativo.
    """
    if id is None and nota is None:
        return JSONResponse(
            status_code=200,
            content={
                "modo_uso": "notas",
                "descripcion": "Este endpoint acepta 0-2 parámetros opcionales: 'id' y 'nota'.",
                "detalles": {
                    "si_no_parametros": "Se muestra este mensaje explicativo.",
                    "si_solo_id": "Se debe indicar también 'nota' para consultar una categoría concreta, o se puede devolver todas las notas (implementación actual pide 'nota').",
                    "si_id_y_nota": "Se devolverá la calificación solicitada."
                },
                "nota_valores_posibles": allowed_nota_fields(),
                "ejemplos": ["/notas?id=1001&nota=Parcial1", "/notas?id=1002&nota=Practicas"]
            }
        )

    if id is None and nota is not None:
        return JSONResponse(
            status_code=400,
            content={"error": "Si indicas 'nota' también debes indicar 'id' del alumno a consultar."}
        )

    # id está presente (posible que nota no lo esté)
    row = df[df["ID"] == id]
    if row.empty:
        return JSONResponse(status_code=404, content={"error": f"No se encontró alumno con ID {id}"})
    row = row.iloc[0]

    if nota is None:
        return JSONResponse(
            status_code=200,
            content={
                "ID": id,
                "nombre_completo": get_fullname(row),
                "mensaje": "No se ha especificado la nota a consultar. Parámetros válidos para 'nota': "
                           + ", ".join(allowed_nota_fields())
            }
        )

    # validar campo nota
    if nota not in allowed_nota_fields():
        return JSONResponse(
            status_code=400,
            content={"error": f"Campo 'nota' inválido. Valores válidos: {', '.join(allowed_nota_fields())}"}
        )

    # devolver nota
    valor = row.get(nota)
    return {
        "ID": id,
        "nombre_completo": get_fullname(row),
        "nota_consultada": nota,
        "valor": valor
    }

# Mensaje raíz (opcional)
@app.get("/")
def root():
    return {
        "api": "iesazarquiel",
        "endpoints": ["/info-alumnos", "/asistencia", "/notas"],
        "nota": "Consulta /docs para ver la documentación automática de FastAPI."
    }
