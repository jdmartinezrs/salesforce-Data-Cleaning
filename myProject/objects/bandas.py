import pandas as pd
import os

# Obtener la ruta del script
script_dir = os.path.dirname(__file__)

# Rutas de los archivos CSV
ruta_csv = os.path.join(script_dir, "../documents/BANDAS.csv")
ruta_salida = os.path.join(script_dir, "../correctedDocuments/bandas.csv")

# Cargar el archivo CSV con codificación 'latin1' (puedes probar con 'ISO-8859-1' o 'utf-8' si sigue fallando)
df = pd.read_csv(ruta_csv, encoding="latin1")

# **Corregir nombres de columnas manualmente**
df.columns = df.columns.str.encode('latin1').str.decode('utf-8')

# Imprimir nombres de columnas corregidos
print("Nombres de columnas corregidos:", df.columns)

# Asegurar que no haya espacios extra en los nombres
df.columns = df.columns.str.strip()

# **Verificar si 'Género Musical' ahora existe**
if "Género Musical" not in df.columns:
    raise KeyError(f"La columna 'Género Musical' sigue sin encontrarse. Columnas disponibles: {df.columns}")

# Corrección de Género Musical a valores válidos
genero_correcciones = {
    "Altemativo": "Alternativo",
    "Metl": "Metal",
    "Indi": "Indie",
    "Puk": "Punk",
    "Rockk": "Rock"
}
df["Género Musical"] = df["Género Musical"].replace(genero_correcciones)

# Validar que solo existan los géneros permitidos
generos_validos = {"Rock", "Metal", "Punk", "Indie", "Alternativo"}
df["Género Musical"] = df["Género Musical"].apply(lambda x: x if x in generos_validos else "Alternativo")

# Guardar el archivo corregido
df.to_csv(ruta_salida, index=False, encoding="utf-8")

print(f"Archivo corregido guardado en '{ruta_salida}'")
