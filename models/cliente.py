class Cliente:
<<<<<<< HEAD
    def __init__(self,id, nombre,password,email, apellido, dni):
=======
    def __init__(self,id, nombre, password, email, apellido, dni):
>>>>>>> e46a49aae729d76d8f3f194246fd6a8b7fe204c7
        self.id = id
        self.nombre = nombre
        self.password = password
        self.email = email
        self.apellido = apellido
        self.dni = dni

    def __repr__(self):
        return f"Cliente( id='{self.id} nombre='{self.nombre}', email='{self.email}', apellido='{self.apellido}', dni='{self.dni}')"