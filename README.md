
 **Salesforce - Limpieza de Datos**

Eres Developer un que trabaja para la empresa ,donde tu equipo quiere mejorar la administración de datos de las bandas, eventos y ventas de entradas del festival utilizando Salesforce.
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





