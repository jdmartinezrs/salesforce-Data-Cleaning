import pandas as pd
import os

# Obtener la ruta absoluta del script
script_dir = os.path.dirname(__file__)

# Ruta correcta del archivo CSV dentro de "documents"
ruta_csv = os.path.join(script_dir, "../documents/EVENTOS.csv")
ruta_salida = os.path.join(script_dir, "../correctedDocuments/eventos.csv")

# Cargar el archivo CSV con la codificación correcta
df = pd.read_csv(ruta_csv, encoding="latin1")

# Reemplazar caracteres mal interpretados
df = df.applymap(lambda x: x.encode('latin1').decode('utf-8') if isinstance(x, str) else x)

# Convertir la columna de fecha al formato YYYY-MM-DD
df["Fecha del Evento"] = pd.to_datetime(df["Fecha del Evento"], errors='coerce').dt.strftime('%Y-%m-%d')

# Rellenar valores vacíos en "Capacidad del Evento" con 10000
df["Capacidad del Evento"] = df["Capacidad del Evento"].fillna(10000).astype(int)


# Eliminar eventos duplicados con el mismo "Nombre del Evento" y "Fecha del Evento"
df = df.drop_duplicates(subset=["Nombre del Evento", "Fecha del Evento"], keep="first")

# Guardar el archivo corregido dentro de "documents"
df.to_csv(ruta_salida, index=False, encoding="utf-8")

print(f"Archivo corregido guardado en '{ruta_salida}'")
