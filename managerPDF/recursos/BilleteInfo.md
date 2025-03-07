# Explicación del código

El código maneja la operación para obtener los datos del billete de la base de datos SQLite para gestionar información del viaje que se va a realizar. Se usan consultas SQL con la biblioteca sqlite3 en Python.

---
## 1. obtener_destinos_y_aviones(vuelo_id)

### ¿Para qué sirve?
Esta función obtiene los datos del billete del viaje para mostrar nuestros datos, la fecha, el destino y el número de asientos que hemos reservado, y por último el precio.

### ¿Cómo lo hace?
1. Conexión a la base de datos con sqlite3.connect("viajes.db").
2. Se crea un cursor para ejecutar la consulta SQL.
3. Consulta SQL con JOINs para obtener información de varias tablas relacionadas:
   - vuelo (tabla principal)
   - avion (para relacionar el vuelo con un avión)
   - destino (para saber a qué destino pertenece el vuelo)
4. Se ejecuta la consulta con el destino como parámetro.
5. Se obtiene el resultado con fetchall().
6. Se cierra la conexión y se devuelve la lista de viajes.

---
## Tecnologías utilizadas

- Python: Lenguaje de programación utilizado para manejar la lógica del sistema.
- SQLite (sqlite3): Base de datos ligera y embebida en el proyecto.
- SQL: Lenguaje de consulta para manejar la base de datos.