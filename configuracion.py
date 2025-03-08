# -*- coding: utf-8 -*-
import re
import sqlite3

import os
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import QtWidgets, uic
import BD.basedatos as baseLocal
from models.cliente import Cliente  # Librería para trabajar con el archivo de la interfaz
from PyQt6.QtGui import QIcon
import glob
import markdown2
from managerPDF.ManagerPDF import PDF4
#clase que se encarga de actualizar el usuario, eliminar la cuenta del usuario o cerrar la sesion
class Configuracion(QtWidgets.QMainWindow):
    def __init__(self,manager):
        super(Configuracion, self).__init__()
        #archivo donde se aloja la pantalla
        file_log = "configuracion.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)
        uic.loadUi(full_path_lo, self)
        self.setWindowIcon(QIcon("recursos/iconos/icon.ico"))
        #nuestro windowManager, este es el que se encarga de la navegacion y saber que usuario esta logeado
        self.manager = manager
        #conecto los diferente elementos del mismo
        self.QPBVolver.clicked.connect(lambda: self.irAMenu())
        self.buttonBox_2.button(self.buttonBox_2.StandardButton.Apply).clicked.connect(lambda: self.eliminarusuario())
        self.BBActualizarUsuario.clicked.connect(lambda :self.actualizarUsuario())
        #debido a que nuestro navigation (manager), lo instancia antes de tiempo, debemos asegurarno si el usuario a iniciado antes para poner los campos
        if self.manager.usuario is not None:
            self.QTENombre.setPlainText(self.manager.usuario.nombre)
            self.QTEApellido.setPlainText(self.manager.usuario.apellido)
            self.QTEDni.setPlainText(self.manager.usuario.dni)
        self.BcerrarSesion.clicked.connect(self.cerrarSesion)
        self.PBDescargar.clicked.connect(self.pdf)

    #navega hasta la ventana menu
    def irAMenu(self):
        self.manager.mostrarVentana("menu")

    #pone en None el usuario, eso significa que no hay nadie logeado y navega hasta login donde hara de nuevo un register o login
    def cerrarSesion(self):
        self.manager.usuario = None
        self.manager.mostrarVentana("login")

    #actualiza al usuario en la base de datos local de nuestro sistema 
    def actualizarUsuario(self):

        # Obtener el texto de los QTextEdit para el nombre,email y dni
        nuevo_nombre = self.QTENombre.toPlainText()
        nuevo_email = self.QTEApellido.toPlainText()
        dni = self.QTEDni.toPlainText()

        #busque del usuario mediante el usuario registrado gracias a nuestro navigation
        correo = self.manager.usuario.email
            #validamos el dni
        if bool(re.fullmatch(r"\d{8}[A-Za-z]", dni)):
            #le informamos al usuario una confirmacion mediante un QMesaageBox
            respuesta = QMessageBox.question(
            self,
            "Confirmar actualización",
            f"¿Seguro que quieres actualizar estos datos?\n\n"
            f"Nombre: {nuevo_nombre}\n"
            f"Email: {nuevo_email}\n"
            f"DNI: {dni}",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            # Si el usuario confirma, actualizar en la base de datos
            if respuesta == QMessageBox.StandardButton.Yes:
                baseLocal.update_cliente(nuevo_nombre, nuevo_email, dni, correo,)
                usuario_actualizado = baseLocal.obtenerUsuarioPorCorreo(correo)
                id, nombre, password, email, apellido, dni = usuario_actualizado
                self.manager.usuario = Cliente(id, nombre, password, email, apellido, dni)
                QMessageBox.information(self, "Actualización", "Datos actualizados con éxito.")

            #si no informa que el propio usuario lo ha cancelado
            else:
                QMessageBox.information(self, "Acción cancelada por el usuario", "No se han actualizado los datos.")
        else:
                #lanzamos un error debido que el dni no cumple el formato especificado
                QMessageBox.critical(self, 'Error', "El dni no es cumple el formato.")
    
    #eliminamos el usuario del nuestro firebase y base local 
    def eliminarusuario(self):
        import pyrebase
        import requests
        respuesta = QMessageBox.question(
        self,
        "Confirmar eliminacion PERMANENTE",
        f"¿Seguro que quiere eliminar tu cuenta de la plataforma?\n\n",
        QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)
        # Si el usuario confirma, actualizar en la base de datos
        if respuesta == QMessageBox.StandardButton.Yes:
            self.firebaseConfig = {
            "apiKey": "AIzaSyDtWlIUbITDQtvTI6pi4k0WxxOlimBIXxY",
            "authDomain": "prueba1-79b1f.firebaseapp.com",
            "databaseURL": "https://prueba1-79b1f-default-rtdb.firebaseio.com/", 
            "projectId": "prueba1-79b1f",
            "storageBucket": "prueba1-79b1f.appspot.com",
            "messagingSenderId": "827606316467",
            "appId": "1:827606316467:web:7cd3fcc0d0d4af6edec7c6"
            }

            # Inicializar Firebase
            self.firebase = pyrebase.initialize_app(self.firebaseConfig)
            auth = self.firebase.auth()

            try:

                # Hacer la solicitud a la API de Firebase para eliminar la cuenta
                url = f"https://identitytoolkit.googleapis.com/v1/accounts:delete?key={self.firebaseConfig['apiKey']}"
                response = requests.post(url, json={"idToken": self.manager.token})

                if response.status_code == 200:
                    baseLocal.eliminarClientePorCorreo(self.manager.usuario.email)
                    print("✅ Usuario eliminado correctamente de Firebase")
                    # una vez eliminado de firebase, podemos eliminarlo de la base de datos y lo regresamos al login
                    self.cerrarSesion()
                else:
                    #en caso de error lo logeamos a la consola
                    print("❌ Error al eliminar el usuario:", response.json())

            #en caso de error lo logeamos a la consola
            except requests.exceptions.RequestException as e:
                print("❌ Error de conexión:", e)

            except Exception as e:
                print("❌ Error general:", e)
        else:
            #le informamos al usuario que el mismo esta cancelando esa accion
            QMessageBox.information(self, "Acción cancelada por el usuario", "No se ha eliminado la cuenta.")

    def pdf(self):
        fecha = self.manager.managerPDF.generar_fecha_actual()
        ruta_pdf = 'PDFs/usuario' + fecha + '.pdf'

        try:
            resultados = glob.glob("**/informacionUsuario.md", recursive=True)

            if resultados:
                ruta_txt = resultados[0]  # Tomamos la primera coincidencia
            else:
                # No encontrado
                QMessageBox.warning(self, 'Error', '¡No se encontró informacionUsuario.md!')
                return 

            with open(ruta_txt, "r", encoding="utf-8") as file:
                contenido_md = file.read()

            contenido_html = markdown2.markdown(contenido_md)

            pdf = PDF4()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", "", 12)

            for linea in contenido_html.split("\n"):
                if "<h1>" in linea:
                    pdf.set_font("Arial", "B", 16)
                    pdf.multi_cell(0, 10, linea.replace("<h1>", "").replace("</h1>", ""))
                elif "<h2>" in linea:
                    if "<em>" in linea:
                        pdf.set_font("Arial", "B", 12)
                        pdf.multi_cell(0, 10, linea.replace("<em>", "_").replace("</em>", "_").replace("<h2>", "").replace("</h2>", ""))
                    else:
                        pdf.set_font("Arial", "B", 14)
                        pdf.multi_cell(0, 10, linea.replace("<h2>", "").replace("</h2>", ""))   
                elif "<h3>" in linea:
                    pdf.set_font("Arial", "B", 12)
                    pdf.multi_cell(0, 10, linea.replace("<h3>", "").replace("</h3>", ""))
                elif "<ul>" in linea or "<ol>" in linea:
                    # Aquí solo marcamos que estamos en una lista, pero no agregamos nada aún
                    lista_nueva = True
                elif "<li>" in linea:
                    if lista_nueva:
                        pdf.set_font("Arial", "", 12)
                        lista_nueva = False
                    if "<em>" in linea:
                        pdf.set_font("Arial", "", 12)
                        pdf.multi_cell(0, 10, linea.replace("<em>", "_").replace("</em>", "_").replace("<li>", "").replace("</li>", ""))
                    else:
                        pdf.multi_cell(0, 8, "* " + linea.replace("<li>", "").replace("</li>", ""))
                elif "</ul>" in linea or "</ol>" in linea:
                    lista_nueva = False  # Fin de la lista
                elif "<p>" in linea or "</p>" in linea:
                    pdf.set_font("Arial", "", 12)
                    pdf.multi_cell(0, 10, linea.replace("<p>", "").replace("</p>", ""))
                elif "<hr />" in linea:
                    pdf.ln(5)  # Añadimos un espacio después de la línea <hr>
                    pdf.set_font("Arial", "", 10) 
                    pdf.multi_cell(0, 2, "------------------------------------------------------------------------------------------------------------------------")
                    pdf.ln(5)  # Añadimos un espacio después de la línea de separación
                else:
                    pdf.set_font("Arial", "", 12)
                    pdf.multi_cell(0, 6, linea.strip())



            pdf.output(ruta_pdf, 'F')
            QMessageBox.information(self,'Información', '¡Informe 1 creado con éxito!') 

        except FileNotFoundError:
            QMessageBox.warning(self, 'Error', '¡No se encontró MisViajesInfo.txt!')