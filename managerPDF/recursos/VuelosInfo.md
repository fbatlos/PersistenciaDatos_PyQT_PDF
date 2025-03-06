# Explicación del código

El código maneja la operación para obtener todos los vuelos de la base de datos SQLite para gestionar información de los vuelos. Se usan consultas SQL con la biblioteca sqlite3 en Python.

---
## 1. getVuelos(destino)

### ¿Para qué sirve?
Esta función obtiene todos los vuelos de un destino para comprar el vuelo.

### ¿Cómo lo hace?
1. Conexión a la base de datos con sqlite3.connect("viajes.db").
2. Se crea un cursor para ejecutar la consulta SQL.
3. Consulta SQL con JOINs para obtener información de varias tablas relacionadas:
   - vuelos (tabla principal)
   - avion (para relacionar el vuelo con un avión)
   - destino (para saber a qué destino pertenece el vuelo)
4. Se ejecuta la consulta con el destino como parámetro.
5. Se obtiene el resultado con fetchall().
6. Se cierra la conexión y se devuelve la lista de viajes.

### Resultado de la consulta

Viajes encontrados: 
[(1, 'prueba1', 'Francia', '2025-02-28', '2025-02-28', 198.0), 
 (2, 'prueba1', 'Italia', '2025-03-03', '2025-03-05', 275.0), 
 (3, 'prueba1', 'Italia', '2025-03-03', '2025-03-03', 275.0), 
 (4, 'prueba1', 'Italia', '2025-02-27', '2025-03-03', 275.0), 
 (5, 'prueba1', 'Italia', '2025-03-03', '2025-03-03', 275.0), 
 (6, 'prueba1', 'Italia', '2025-03-03', '2025-03-03', 275.0), 
 (7, 'prueba1', 'Francia', '2025-03-03', '2025-03-03', 270.0), 
 (8, 'prueba1', 'Italia', '2025-03-03', '2025-03-03', 375.0), 
 (9, 'prueba1', 'Italia', '2025-03-03', '2025-03-03', 300.0)]

---
## Tecnologías utilizadas

- Python: Lenguaje de programación utilizado para manejar la lógica del sistema.
- SQLite (sqlite3): Base de datos ligera y embebida en el proyecto.
- SQL: Lenguaje de consulta para manejar la base de datos.