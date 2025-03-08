import sqlite3

from models.cliente import Cliente

#Crear las tablas que necesiteis brothers nico gay

def update_cliente(nuevo_nombre, nuevo_email, dni,correo):
    conn = sqlite3.connect('viajes.db')
    cursor = conn.cursor()
    # Ejecutar la actualización
    cursor.execute("""
        UPDATE cliente
        SET nombre = ?, apellido = ?, dni = ?
        WHERE email = ? 
    """, (nuevo_nombre, nuevo_email, dni,correo,))
    conn.commit()
    conn.close()

def obtenerElIdDelClienteUnaVezLogeado(correo):
    conn = sqlite3.connect('viajes.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT id FROM cliente WHERE email = ?""", (correo,))
    id = cursor.fetchone()
    conn.close()
    return id

def obtenerSoloElNombreDelDestinoParaLaPantallaMenu():
    conn = sqlite3.connect('viajes.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT nombre FROM destino""")
    destinos = cursor.fetchall()
    conn.close()
    return destinos

def obtenerSoloElNombreDelViajeParaLaPantallaMenu(email):
    conn = sqlite3.connect("viajes.db") 
    cursor = conn.cursor()
    cursor.execute("""
    SELECT destino.nombre
    FROM viaje
    JOIN cliente ON viaje.cliente_email = cliente.email
    JOIN vuelo ON viaje.vuelo_id = vuelo.id
    JOIN destino ON vuelo.destino_id = destino.id
    WHERE cliente.email = ?
    """, (email,))
    # Porquee cojoneeees no sale nadaaaaaaaaa
    viajes = cursor.fetchall()
    conn.close()
    return viajes

def obtenerUsuarioPorCorreo(correo):
    conn = sqlite3.connect('viajes.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM cliente WHERE email = ?""", (correo,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def obtener_cliente(email):
    conn = sqlite3.connect("viajes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cliente WHERE email = ?", (email,))
    cliente = cursor.fetchone()
    conn.close()
    return Cliente(0,cliente[1],cliente[2],cliente[3],cliente[4])

def eliminarClientePorCorreo(correo):
    conexion = sqlite3.connect("viajes.db")
    cursor = conexion.cursor()

    try:
        # Primero eliminamos los viajes del cliente
        cursor.execute("DELETE FROM viaje WHERE cliente_email = ?", (correo,))
        # Luego eliminamos al cliente
        cursor.execute("DELETE FROM cliente WHERE email = ?", (correo,))

        conexion.commit()
        print("Cliente y sus viajes eliminados correctamente.")
    except sqlite3.Error as e:
        print("Error al eliminar cliente:", e)
    finally:
        cursor.close()
        conexion.close()



def prueba():
    conn = sqlite3.connect("viajes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cliente")
    cliente = cursor.fetchall()
    conn.close()
    print (cliente)

#prueba()


def insertar_cliente(cliente):
    conn = sqlite3.connect("viajes.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO cliente (nombre, email, apellido, dni)
        VALUES (?, ?, ?, ?)
    """, (cliente.nombre, cliente.email, cliente.apellido, cliente.dni))
    
    conn.commit()
    conn.close()
    return True
    print("Cliente insertado correctamente.")

def obtener_viajes_por_mes(mes,email):
    conn = sqlite3.connect("viajes.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT viaje.id, cliente.nombre, destino.nombre, viaje.fecha_salida, viaje.fecha_regreso, viaje.precio
    FROM viaje
    JOIN cliente ON viaje.cliente_email = cliente.email
    JOIN vuelo ON viaje.vuelo_id = vuelo.id
    JOIN destino ON vuelo.destino_id = destino.id
    WHERE strftime('%m', viaje.fecha_salida) = ?
    AND cliente.email = ?
    """, (mes.zfill(2),email))

    viajes = cursor.fetchall()
    conn.close()
    return viajes

def getMisViajes(email):
    conn = sqlite3.connect("viajes.db") 
    cursor = conn.cursor()

    cursor.execute("""
    SELECT viaje.id, cliente.nombre, destino.nombre, viaje.fecha_salida, viaje.fecha_regreso, viaje.precio
    FROM viaje
    JOIN cliente ON viaje.cliente_email = cliente.email
    JOIN vuelo ON viaje.vuelo_id = vuelo.id
    JOIN destino ON vuelo.destino_id = destino.id
    WHERE cliente.email = ?
    """, (email,))


    # Porquee cojoneeees no sale nadaaaaaaaaa
    viajes = cursor.fetchall()

    conn.close()
    return viajes

def putMisViajes(nueva_fecha_salida, nueva_fecha_regreso, viaje_id):
    conn = sqlite3.connect("viajes.db")  
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE viaje SET fecha_salida = ?, fecha_regreso = ? WHERE id = ?
    """, (nueva_fecha_salida, nueva_fecha_regreso, viaje_id))
    conn.commit()
    conn.close()

def delMisViajes(viaje_id):
    conn = sqlite3.connect("viajes.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM viaje WHERE id = ?", (viaje_id,))
    conn.commit()
    conn.close()

def insertar_viaje(cliente_email, vuelo_id, fecha_salida, fecha_regreso, precio):
    con = sqlite3.connect("viajes.db")
    cur = con.cursor()
    id = obtener_ultimo_id_viaje() + 1 
    cur.execute('''
        INSERT INTO viaje (id, cliente_email, vuelo_id, fecha_salida, fecha_regreso, precio)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (id, cliente_email, vuelo_id, fecha_salida, fecha_regreso, precio)) 
    con.commit()
    con.close()

def obtener_ultimo_id_viaje():
    con = sqlite3.connect("viajes.db")
    cur = con.cursor()
    cur.execute('''
        SELECT MAX(id) FROM viaje
    ''')
    id = cur.fetchone()
    con.close()
    print(f"ID: {id}")
    if id[0] == None:
        return 0
    else:
        return int(id[0])


def actualizar_asientos(cantidad_asientos, vuelo_id):
    con = sqlite3.connect("viajes.db")
    cur = con.cursor()
    cur.execute('''
        UPDATE vuelo
        SET cantidad_asientos = cantidad_asientos - ?
        WHERE id = ?
    ''', (cantidad_asientos, vuelo_id))
    con.commit()
    con.close()


def obtener_destinos_y_aviones(vuelo_id):
    conn = sqlite3.connect("viajes.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT destino.nombre AS destino, avion.modelo AS modelo
        FROM vuelo
        JOIN destino ON vuelo.destino_id = destino.id
        JOIN avion ON vuelo.avion_id = avion.id
        WHERE vuelo.id = ?;
    """, (vuelo_id,))

    destinos = cursor.fetchall()
    conn.close()
    return destinos


def obtener_vuelos(destino, orden):
    conn = sqlite3.connect("viajes.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.modelo, a.categoria, ROUND(v.precio, 2), v.cantidad_asientos,v.id 
        FROM avion a
        JOIN vuelo v ON a.id = v.avion_id
        JOIN destino d ON v.destino_id = d.id
        WHERE d.nombre = ?
        ORDER BY ?
    """, (destino, orden))
    aviones = cursor.fetchall()
    conn.close()
    return aviones


def restablecer():
    conn = sqlite3.connect("viajes.db")
    cursor = conn.cursor()

    # DROP PARA CREAR LAS TABLAS DE NUEVO
    #cursor.execute("DROP TABLE IF EXISTS cliente") 
    cursor.execute("DROP TABLE IF EXISTS destino") 
    cursor.execute("DROP TABLE IF EXISTS vuelo") 
    cursor.execute("DROP TABLE IF EXISTS avion") 
    cursor.execute("DROP TABLE IF EXISTS viaje") 

    # CREACION DE TABLAS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            apellido TEXT NOT NULL,
            dni TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS destino (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vuelo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            destino_id INTEGER NOT NULL,
            avion_id INTEGER NOT NULL,
            cantidad_asientos INTEGER NOT NULL,
            precio REAL NOT NULL,
            FOREIGN KEY (destino_id) REFERENCES destino(id) 
            FOREIGN KEY (avion_id) REFERENCES avion(id) 
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS avion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            porcentaje_precio REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS viaje (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_email TEXT NOT NULL,
            vuelo_id INTEGER NOT NULL,
            fecha_salida TEXT NOT NULL,
            fecha_regreso TEXT NOT NULL,
            precio REAL NOT NULL,
            FOREIGN KEY (cliente_email) REFERENCES cliente(id),
            FOREIGN KEY (vuelo_id) REFERENCES vuelos(id)
        )
    """)


    ## INSERTS PARA PRUEBAS
    #insert para clientes
    #cursor.execute("""
    #    INSERT INTO cliente (nombre, email, apellido, dni)
    #    VALUES (?, ?, ?, ?)
    #""", ("Juan", "juan@example.com", "Pérez", "12345678A"))

    # INSERTS DE DESTINOS
    cursor.execute("""
        INSERT INTO destino (nombre, precio) VALUES 
        ('España', 200),
        ('Italia', 250),
        ('Francia', 180);
    """)

    # INSERTS DE AVIONES
    cursor.execute("""
        INSERT INTO avion (modelo, categoria, porcentaje_precio) VALUES 
        ('Boeing 737', 'Económico', 1.2),
        ('Airbus A320', 'Económico', 1.1),
        ('Boeing 777', 'Premium', 1.5);
    """)
    # INSERTS DE VUELOS

    cursor.execute("""
        INSERT INTO vuelo (destino_id, avion_id, cantidad_asientos, precio) 
        VALUES 
        (1, 1, 180, 
         (SELECT precio * porcentaje_precio FROM destino, avion WHERE destino.id = 1 AND avion.id = 1)),

        (1, 2, 160, 
         (SELECT precio * porcentaje_precio FROM destino, avion WHERE destino.id = 1 AND avion.id = 2)),

        (1, 3, 300, 
         (SELECT precio * porcentaje_precio FROM destino, avion WHERE destino.id = 1 AND avion.id = 3));
    """)

    cursor.execute("""
        INSERT INTO vuelo (destino_id, avion_id, cantidad_asientos, precio) 
        VALUES 
        (2, 1, 180, 
         (SELECT precio * porcentaje_precio FROM destino, avion WHERE destino.id = 2 AND avion.id = 1)),

        (2, 2, 160, 
         (SELECT precio * porcentaje_precio FROM destino, avion WHERE destino.id = 2 AND avion.id = 2)),

        (2, 3, 300, 
         (SELECT precio * porcentaje_precio FROM destino, avion WHERE destino.id = 2 AND avion.id = 3));
    """)

    cursor.execute("""
        INSERT INTO vuelo (destino_id, avion_id, cantidad_asientos, precio) 
        VALUES 
        (3, 1, 160, 
         (SELECT precio * porcentaje_precio FROM destino, avion WHERE destino.id = 3 AND avion.id = 1)),

        (3, 2, 180, 
         (SELECT precio * porcentaje_precio FROM destino, avion WHERE destino.id = 3 AND avion.id = 2)),

        (3, 3, 300, 
         (SELECT precio * porcentaje_precio FROM destino, avion WHERE destino.id = 3 AND avion.id = 3));
    """)

    conn.commit()
    conn.close()