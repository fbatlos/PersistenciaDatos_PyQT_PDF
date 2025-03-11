import sys
import os
from PyQt6.QtWidgets import *
from PyQt6 import uic
import pyrebase
import requests
import sqlite3
import json
import re
import models.cliente as model
import BD.basedatos as baseLocal
from PyQt6.QtGui import QIcon
import hashlib


#Ventana Login / Register
class Ventana(QMainWindow):
    def __init__(self,manager):
        super(Ventana, self).__init__()
        #Buscamos la .ui
        file_log = "login.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)
        uic.loadUi(full_path_lo, self)
        self.setWindowIcon(QIcon("recursos/iconos/icon.ico"))
        #Añadimos lso datos de firebase.
        self.manager = manager
        self.firebaseConfig = {
            "apiKey": "AIzaSyDtWlIUbITDQtvTI6pi4k0WxxOlimBIXxY",
            "authDomain": "prueba1-79b1f.firebaseapp.com",
            "databaseURL": "https://prueba1-79b1f-default-rtdb.firebaseio.com/",
            "projectId": "prueba1-79b1f",
            "storageBucket": "prueba1-79b1f.appspot.com",
            "messagingSenderId": "827606316467",
            "appId": "1:827606316467:web:7cd3fcc0d0d4af6edec7c6"
        }

        #Nos autorzamos y conectamos con firebase
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        #Damos funcionalidad a los diferentes botones.
        self.bu_login.clicked.connect(self.gui_login)
        self.bu_reg.clicked.connect(self.gui_reg)

    #Hacemos el register
    def gui_reg(self):
        #Obtenemos los datos 
        nombre = self.li_nombre.text()
        apellido = self.li_apellido.text()
        dni = self.li_dni.text()
        email = self.li_usuario_2.text()
        passw = self.li_contra_2.text()
        
        #Verificamos los datos vacíos
        if not (nombre and apellido and dni and email and passw):
            QMessageBox.critical(self, 'Error', "Ingrese todos los datos")
            return
        #Validamos el dni
        if not validar_dni(dni):
            QMessageBox.critical(self, 'Error', "El dni no es cumple el formato.")
            return

        try:
            #Ingresamos el usuario en firebase
            user = self.auth.create_user_with_email_and_password(email, passw)
            passw = hashlib.md5(passw.encode()).hexdigest()
            #Ingresamos los datos en la bd
            cliente = model.Cliente(0,nombre,passw, email, apellido, dni)
            existo = baseLocal.insertar_cliente(cliente)
            #Comprobamos que fue exitoso
            if existo is None:
                QMessageBox.critical(self, 'Error', "No se ingresó el usuario en la base de datos")

            print(user)
            #Relacionamos los diferentes datos 
            self.manager.usuario = cliente
            self.manager.mostrarVentana("menu")
            self.manager.token = user["idToken"]
            print(user["idToken"])
            #Mandamos si fue correcto o no 
            self.correcto("r")

        #Controlamos las excepciones
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            QMessageBox.critical(self, 'Error', error)
            self.delete_line()
        except Exception as e:
            QMessageBox.critical(self, 'Error', "Error")

    #Realizamos el login
    def gui_login(self):
        #Obtenemos los datos
        email = self.li_usuario.text()
        passw = self.li_contra.text()

        #Comprobamos si hay datos
        if not (email and passw):
            QMessageBox.critical(self, 'Error', "Ingrese todos los datos")
            return
        
        try:
            #Comprobamos que esté en Firebase y la bd local
            user = self.auth.sign_in_with_email_and_password(email, passw)
            cliente = baseLocal.obtener_cliente(email)

            baseLocal.prueba()
            
            #Asignamos los datos y pasamos de pantalla
            self.manager.usuario = cliente   
            self.manager.mostrarVentana("menu")
            self.manager.token = user["idToken"]

            #Pequeña comprobación del cliente
            if cliente is not None:
                self.correcto("l")
            else:
                QMessageBox.critical(self, 'Error', "No se encontró el usuario en la base de datos")
        #Verificamos todos los posibles errores 
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            QMessageBox.critical(self, 'Error', error)
            self.delete_line()

    #Si los datos son correctos, enseñará diferentes mensajes.
    def correcto(self, estatus):
        if estatus == "l":
            QMessageBox.information(self, '¡Login correcto!', "Acceso garantizado")
        else:
            QMessageBox.information(self, '¡Usuario creado correctamente!', "Creación de usuario")
        
    #Eliminamos los datos
    def delete_line(self):
        self.li_usuario.setText("")
        self.li_contra.setText("")
        self.li_usuario.setFocus()
#Validamos el dni 
def validar_dni(dni):
    return bool(re.fullmatch(r"\d{8}[A-Za-z]", dni))
