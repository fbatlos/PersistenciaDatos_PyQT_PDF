# Explicación del código

El código maneja operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en una base de datos SQLite para gestionar información de viajes. Se usan consultas SQL con la biblioteca sqlite3 en Python.

---
## 1. obtener_viajes_por_mes(mes):

### ¿Para qué sirve?
Obtiene todos los viajes almacenados en la base de datos cuya fecha de salida coincide con el mes ingresado por el usuario.

### ¿Cómo lo hace?

1. Se conecta a la base de datos SQLite.
2. Ejecuta una consulta SQL utilizando strftime('%m', fecha_salida), que extrae el mes de la fecha de salida de cada viaje.
3. Se usa mes.zfill(2) para asegurarse de que el mes tenga dos dígitos (Ejemplo: 03 en vez de 3).
4. Filtra los viajes donde el mes de fecha_salida coincide con el ingresado por el usuario.
5. Recupera los datos y los devuelve como resultado.
6. Cierra la conexión.

---
## Tecnologías utilizadas

- Python: Lenguaje de programación utilizado para manejar la lógica del sistema.
- SQLite (sqlite3): Base de datos ligera y embebida en el proyecto.
- SQL: Lenguaje de consulta para manejar la base de datos.