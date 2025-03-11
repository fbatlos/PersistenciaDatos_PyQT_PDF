# Explicación del código

El codigo permite actualizar al usuario en la base de datos local y eliminar su cuenta tanto de firebase como de nuestra base de datos

---
## 1. actualizarUsuario()

### ¿Para qué sirve?
Estafuncion actualiza al usuario en la bd y lo recupera ya actualizado
### ¿Cómo lo hace?
#### actualizar
1. Conexión a la base de datos con sqlite3.connect("viajes.db").
2. Se crea un cursor para ejecutar la consulta SQL.
4. se da los parametro nombre nuevo del usuario, nuevo apellido, nuevo dni y correo
3. actualiza la tabla cliente, mediante un update buscnado por email
4. Se ejecuta el update.
5. Se obtiene el resultado con fetchall().
6. Se guarda la base de datos y cierra la conexión.
#### obtener
1. Conexión a la base de datos con sqlite3.connect("viajes.db").
2. Se crea un cursor para ejecutar la consulta SQL.
3. hace un select de cliente con la condicion de email sea igual al buscado
4. Se ejecuta la consulta con el correo como parámetro.
5. Se obtiene el resultado con fetchone().
6. Se cierra la conexión.
7. retorna el cliente
### Resultado de la consulta

(1, 'Juan', 'juan@email.com', 'Pérez', '12345678A')

---
## 2. eliminarusuario()

### ¿Para qué sirve?
El codigo elimina al usuario tando del firebase como de nuestra base de datos local

### ¿Cómo lo hace?
1. Conexión a la base de datos con sqlite3.connect("viajes.db").
2. Se crea un cursor para eliminar los viajes del cliente.
3. Se ejecuta la consulta como correo del usuario como parametro
4. Se crea un cursor para eliminar al cliente.
5. Se ejecuta la consulta como correo del usuario como parametro
6. Se guarda la basede datos
9. Se cierra la conexión

---
## Tecnologías utilizadas

- Python: Lenguaje de programación utilizado para manejar la lógica del sistema.
- SQLite (sqlite3): Base de datos ligera y embebida en el proyecto.
- SQL: Lenguaje de consulta para manejar la base de datos.
