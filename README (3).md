
# Salesforce - Limpieza de Datos

Eres un que trabaja para la empresa ,donde tu equipo quiere mejorar la administración de datos de las bandas, eventos y ventas de entradas del festival utilizando Salesforce.
En Salesforce, crea los siguientes objetos personalizados con sus respectivos campos:
Nombre de la Banda (Texto)
Género Musical (Picklist: [Rock, Metal, Punk, Indie, Alternativo])
Número de Integrantes (Número)
País de Origen (Texto)
Año de Formación (Número)
Nombre del Evento (Texto)
Fecha del Evento (Fecha)
Ubicación (Texto)
Capacidad del Evento (Número)
Banda Principal (Lookup a "Banda")
Número de Ticket (Auto Number)
Evento (Lookup a "Evento")
Precio (Moneda)
Estado (Picklist: [Reservado, Pagado, Cancelado])
Nombre del Comprador (Texto)
Descarga los siguientes archivos CSV que contienen datos para importar a Salesforce:
✅ → Contiene 500 registros de bandas de rock y metal (datos limpios).
⚠️ → Contiene 100 registros con errores en fechas, valores vacíos y duplicados.
⚠️ → Contiene 1000 registros con errores en formatos de precio, estados mal escritos y nombres de compradores faltantes.

📌 Intenta revisar  y . ¿Qué errores encuentras?
Antes de importar y , debes limpiarlos para evitar errores en Salesforce.
📌
Convierte todas las fechas al formato YYYY-MM-DD.
Rellena los valores vacíos en "Capacidad del Evento" con 10000.
Elimina eventos duplicados con el mismo nombre y fecha.
Corrige los precios a formato numérico estándar (100.00).
Arregla estados erróneos (Pagadoo → Pagado, Resevado → Reservado, etc.).
Si un comprador no tiene nombre, asígnale Comprador Anónimo.
📊 → Clasificación de bandas por género musical. → Total de ingresos por evento.
📈
Cantidad de entradas vendidas por evento.
Total de ingresos generados en todos los eventos.
Distribución de bandas por género.

## Lightning APP SalesFestival

Aplicación Salesfestival creada en la Lightning Experience que permite a los usuarios acceder a los objetos bandas, venta de entradas y eventos , además permite ver los reportes y el dashboard.


![Logo](https://i.pinimg.com/1200x/4c/92/7a/4c927a7be1c7c395f741686fbb473161.jpg)


## dataloader.io
Importación de documentos, a los objetos: Banda , Venta de Entrada, Evento

![Logo](https://i.pinimg.com/1200x/36/eb/43/36eb43c7af386408ef53c8cdcca2691d.jpg)

## Bandas

•Corrección de Género Musical a valores válidos



```bash
  genero_correcciones = {
    "Altemativo": "Alternativo",
    "Metl": "Metal",
    "Indi": "Indie",
    "Puk": "Punk",
    "Rockk": "Rock"
}
df["Género Musical"] = df["Género Musical"].replace(genero_correcciones)
```
•Validar que solo existan los géneros permitidos

```bash
generos_validos = {"Rock", "Metal", "Punk", "Indie", "Alternativo"}
df["Género Musical"] = df["Género Musical"].apply(lambda x: x if x in generos_validos else "Alternativo")
```
**Detalle de una Banda**

![Logo](https://i.pinimg.com/1200x/79/8f/09/798f098118c9514bf526ecc86054274f.jpg)

## Venta de Entradas

•Corrección de precios al formato numérico estándar con 2 decimales y sin símbolos


```bash

df["Precio"] = df["Precio"].astype(str).str.replace("[^0-9.]", "", regex=True).str.strip()
df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce").round(2)
```
•Asegurar que el formato de precio sea compatible con Salesforce (10 dígitos, 2 decimales)

```bash
df["Precio"] = df["Precio"].apply(lambda x: "{:.2f}".format(x) if pd.notnull(x) else "0.00")
```
•Asignar "Comprador Anónimo" si no hay nombre del comprador

```bash
df["Nombre del Comprador"] = df["Nombre del Comprador"].fillna("Comprador Anónimo")
df["Nombre del Comprador"] = df["Nombre del Comprador"].replace("", "Comprador Anónimo")
```
•Corrección de valores en la columna "Estado”
```bash
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
```
**Detalle Venta de Entradas**

![Logo](https://i.pinimg.com/1200x/64/a0/98/64a098fa033934c3c3b4d9aa1f548eef.jpg)

## Eventos

•Rellenar valores vacíos en "Capacidad del Evento" con 10000
```bash
df["Capacidad del Evento"] = df["Capacidad del Evento"].fillna(10000).astype(int)
```
•Eliminar eventos duplicados con el mismo "Nombre del Evento" y "Fecha del Evento”
```bash
df = df.drop_duplicates(subset=["Nombre del Evento", "Fecha del Evento"], keep="first")
```

• Convierte todas las fechas al formato YYYY-MM-DD.
```bash
df["Fecha del Evento"] = pd.to_datetime(df["Fecha del Evento"], errors='coerce').dt.strftime('%Y-%m-%d')
```
**Detalle Venta de Eventos**
![Logo](https://i.pinimg.com/1200x/16/a9/9a/16a99a946d0a1b060a0b8c8667f05ca4.jpg)


**Insignia del Trailhead**

![Logo](https://i.pinimg.com/1200x/74/59/a7/7459a7b6f1031662a06e704ea89164df.jpg)



## Reportes 📈

•Clasificación de bandas por género musical
![Logo](https://i.pinimg.com/1200x/2a/1e/af/2a1eaf7d62b1914e131778c40deceeaf.jpg)



•Cantidad de entradas vendidas por evento
![Logo](https://i.pinimg.com/1200x/18/26/15/1826158e3fc92028f00fa632d2e92da4.jpg)
![Logo](https://i.pinimg.com/1200x/80/88/e4/8088e49113a4817e7f4f0fed930feef9.jpg)

•Total de ingresos generados en todos los eventos.
![Logo](https://i.pinimg.com/1200x/43/4b/9c/434b9c5ef4a6050e647d505302b6380e.jpg)
![Logo](https://i.pinimg.com/1200x/0a/1b/ab/0a1babc0ef1ecea6b24026e00a400975.jpg)

•Total de ingresos por evento.
![Logo](https://i.pinimg.com/1200x/f2/b0/62/f2b062848b80772f4c71df061d82184f.jpg)

•Distribución de bandas por género.
![Logo](https://i.pinimg.com/1200x/22/89/63/228963c93d75623dce0b7029583478c2.jpg)

## Dashboard Salesfestival

![Logo](https://i.pinimg.com/1200x/b6/82/88/b682884775e8d8f35bba5e9283108b22.jpg)



