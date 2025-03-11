# Explicación del código

El código maneja la operación para obtener todos los vuelos de la base de datos SQLite para gestionar información de los vuelos. Se usan consultas SQL con la biblioteca sqlite3 en Python.

---
## 1. obtener_vuelos_categoria(categoria, destino)

### ¿Para qué sirve?
Esta función obtiene todos los vuelos de un destino con una categoría en específico.

### ¿Cómo lo hace?
1. Conexión a la base de datos con sqlite3.connect("viajes.db").
2. Se crea un cursor para ejecutar la consulta SQL.
3. Consulta SQL con JOINs para obtener información de varias tablas relacionadas:
   - avion (tabla principal)
   - vuelo (para relacionar el vuelo con un avión)
   - destino (para saber a qué destino pertenece el avion)
4. Se ejecuta la consulta con el destino y la categoría como parámetro.
5. Se obtiene el resultado con fetchall().
6. Se cierra la conexión y se devuelve la lista de aviones de un destino y un tipo de categoría.

---
## Tecnologías utilizadas

- Python: Lenguaje de programación utilizado para manejar la lógica del sistema.
- SQLite (sqlite3): Base de datos ligera y embebida en el proyecto.
- SQL: Lenguaje de consulta para manejar la base de datos.