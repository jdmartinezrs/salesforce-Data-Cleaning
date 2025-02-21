import pandas as pd
import os

# Obtener la ruta del script
script_dir = os.path.dirname(__file__)

# Rutas de los archivos CSV
ruta_csv = os.path.join(script_dir, "../documents/VENTAS_ENTRADAS.csv")
ruta_salida = os.path.join(script_dir, "../correctedDocuments/ventas_entradas.csv")

# Cargar el archivo CSV con la codificación correcta
df = pd.read_csv(ruta_csv, encoding="latin1")

# Reemplazar caracteres mal interpretados
df = df.map(lambda x: x.encode('latin1').decode('utf-8') if isinstance(x, str) else x)

# Asignar "Comprador Anónimo" si no hay nombre del comprador
df["Nombre del Comprador"] = df["Nombre del Comprador"].fillna("Comprador Anónimo")
df["Nombre del Comprador"] = df["Nombre del Comprador"].replace("", "Comprador Anónimo")

# Corrección de precios al formato numérico estándar con 2 decimales y sin símbolos
df["Precio"] = df["Precio"].astype(str).str.replace("[^0-9.]", "", regex=True).str.strip()
df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce").round(2)

# Asegurar que el formato de precio sea compatible con Salesforce (10 dígitos, 2 decimales)
df["Precio"] = df["Precio"].apply(lambda x: "{:.2f}".format(x) if pd.notnull(x) else "0.00")

# Corrección de valores en la columna "Estado"
estado_correcciones = {
    "Pagadoo": "Pagado",
    "Resevado": "Reservado",
    "Cancled": "Cancelado",
    "Canceladoo": "Cancelado",
    "Resrvado": "Reservado"
}
df["Estado"] = df["Estado"].replace(estado_correcciones)

# Filtrar solo estados válidos
iestados_validos = ["Reservado", "Pagado", "Cancelado"]
df = df[df["Estado"].isin(iestados_validos)]

# Guardar el archivo corregido
df.to_csv(ruta_salida, index=False, encoding="utf-8")

print(f"Archivo corregido guardado en '{ruta_salida}'")