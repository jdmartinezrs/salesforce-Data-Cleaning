import os
import pandas as pd
from datetime import datetime

# Obtener el directorio del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir las rutas de los archivos CSV
ruta_bandas = os.path.join(script_dir, "../documents/BANDASID.csv")
ruta_eventos = os.path.join(script_dir, "../documents/EVENTOS.csv")
ruta_salida = os.path.join(script_dir, "../correctedDocuments/eventosMerge.csv")

# Cargar los archivos CSV
bandas = pd.read_csv(ruta_bandas, dtype=str)  # Asegurar que los datos sean tratados como strings
eventos = pd.read_csv(ruta_eventos, dtype=str)

# Renombrar columnas para facilitar la fusión (merge)
bandas.rename(columns={"Record ID": "Banda Principal", "Nombre de la Banda": "Nombre de la Banda"}, inplace=True)

# Hacer el reemplazo de nombres por IDs
eventos_actualizado = eventos.merge(bandas, left_on="Banda Principal", right_on="Nombre de la Banda", how="left")

# Reemplazar la columna Banda Principal con el ID correspondiente
eventos_actualizado["Banda Principal"] = eventos_actualizado["Banda Principal_y"]

# Eliminar columnas innecesarias
eventos_actualizado.drop(columns=["Banda Principal_x", "Nombre de la Banda", "Banda Principal_y"], inplace=True)

# Función para convertir fechas a formato YYYY-MM-DD
def convertir_fecha(fecha):
    if pd.isna(fecha) or fecha.strip() == "":
        return None  # Considerar fechas vacías como inválidas
    formatos = ["%d/%m/%Y", "%m-%d-%Y", "%Y-%m-%d"]  # Formatos comunes detectados
    for formato in formatos:
        try:
            return datetime.strptime(fecha, formato).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None  # Si no coincide con ningún formato, devolver None

# Normalizar la columna de fecha (si existe en el dataset)
columna_fecha = "Fecha del Evento"  # Ajustar según el nombre exacto de la columna en tu CSV
if columna_fecha in eventos_actualizado.columns:
    eventos_actualizado[columna_fecha] = eventos_actualizado[columna_fecha].apply(lambda x: convertir_fecha(x) if pd.notna(x) else None)

# Eliminar eventos sin fecha
eventos_actualizado = eventos_actualizado.dropna(subset=[columna_fecha])

# Rellenar valores vacíos en la columna "Capacidad del Evento" con 10000
columna_capacidad = "Capacidad del Evento"
if columna_capacidad in eventos_actualizado.columns:
    eventos_actualizado[columna_capacidad] = eventos_actualizado[columna_capacidad].fillna(10000)

# Eliminar eventos duplicados si tienen el mismo nombre y la misma fecha
eventos_actualizado = eventos_actualizado.drop_duplicates(subset=["Nombre del Evento", columna_fecha])

# Crear la carpeta de salida si no existe
os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

# Guardar el nuevo archivo CSV corregido
eventos_actualizado.to_csv(ruta_salida, index=False, encoding="utf-8")

print(f"✅ Archivo 'eventosMerge.csv' generado correctamente en: {ruta_salida}")
