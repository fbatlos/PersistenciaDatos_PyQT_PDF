class Cliente:
    def __init__(self,id, nombre,password,email, apellido, dni):
        self.id = id
        self.nombre = nombre
        self.password = password
        self.email = email
        self.apellido = apellido
        self.dni = dni

    def __repr__(self):
        return f"Cliente( id='{self.id} nombre='{self.nombre}', email='{self.email}', apellido='{self.apellido}', dni='{self.dni}')"