# Explicación del código

El código permite visualizar los destinos vigente y destinos ya adquirido del usuario.

---
## 1. cargarDatos()

### ¿Para qué sirve?
Esta función carga y muestra en una tabla los destinos disponibles obtenidos de la base de datos.
### ¿Cómo lo hace?
1. Conexión a la base de datos con sqlite3.connect("viajes.db").
2. Se crea un cursor para ejecutar la consulta SQL.
3. Consulta SQL  en la tabla destino
4. Se ejecuta la consulta.
5. Se obtiene el resultado con fetchall().
6. Se cierra la conexión y se devuelve la lista de nombres de viajes.
7. inserta los datos en la tabla destinos

### Resultado de la consulta

[('París',), ('Tokio',), ('Nueva York',)]

---
## 2. cargarDatosLista()

### ¿Para qué sirve?
Carga en la lista de la interfaz gráfica todos los viajes que tiene el usuario actualmente en la base de datos.

### ¿Cómo lo hace?
1. Conexión a la base de datos con sqlite3.connect("viajes.db").
2. Se crea un cursor para ejecutar la consulta SQL.
3. Consulta SQL, que devuelve los viajesque ha contratado el usuario
4. Se ejecuta la consulta con el email como parámetro.
5. Se obtiene el resultado con fetchall().
6. Se cierra la conexión y se devuelve la lista de nombre de viajes referente al email.


---
## Tecnologías utilizadas

- Python: Lenguaje de programación utilizado para manejar la lógica del sistema.
- SQLite (sqlite3): Base de datos ligera y embebida en el proyecto.
- SQL: Lenguaje de consulta para manejar la base de datos.
