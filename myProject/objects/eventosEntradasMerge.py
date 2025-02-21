import os
import pandas as pd

# Obtener el directorio del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Rutas de los archivos CSV
ruta_eventos = os.path.join(script_dir, "../documents/EventoExport.csv")
ruta_ventas = os.path.join(script_dir, "../correctedDocuments/ventas_entradas.csv")
ruta_salida = os.path.join(script_dir, "../correctedDocuments/eventosEntradasMerge.csv")

# Cargar los archivos CSV
eventos = pd.read_csv(ruta_eventos, dtype=str)  # Asegurar que los datos sean strings
ventas = pd.read_csv(ruta_ventas, dtype=str)

# Renombrar columna de eventos para facilitar el merge
eventos.rename(columns={"Record ID": "Evento_ID", "Nombre del Evento": "Evento"}, inplace=True)

# Hacer el reemplazo de nombres por IDs
ventas_actualizado = ventas.merge(eventos, on="Evento", how="left")

# Reemplazar la columna Evento con el ID correspondiente
ventas_actualizado["Evento"] = ventas_actualizado["Evento_ID"]

# Eliminar la columna extra "Evento_ID"
ventas_actualizado.drop(columns=["Evento_ID"], inplace=True)

# Crear la carpeta de salida si no existe
os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

# Guardar el nuevo archivo CSV corregido
ventas_actualizado.to_csv(ruta_salida, index=False, encoding="utf-8")

print(f"✅ Archivo 'eventosEntradasMerge.csv' generado correctamente en: {ruta_salida}")
