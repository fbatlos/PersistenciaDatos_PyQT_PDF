from PyQt6 import QtWidgets
from PyQt6 import QtWidgets, uic
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import * 
from managerPDF.ManagerPDF import PDF2
import BD.basedatos as baseLocal
from datetime import datetime
from PyQt6.QtGui import QIcon
import glob
import markdown2

#Clase de La ventana
class MisViajes(QtWidgets.QMainWindow):
    def __init__(self, manager):
        super().__init__()
        file_log = "misviajes.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)
        uic.loadUi(full_path_lo, self) 
        self.setWindowIcon(QIcon("recursos/iconos/icon.ico"))
        #añadimos la instancia del manager al self y comprobamos que existe.
        self.manager = manager
        if self.manager.usuario is not None:
            #añadimostodos los datos necesarios a nuestra pantalla 
            self.email = self.manager.usuario.email
            self.boton_actualizar.clicked.connect(self.actualizar_viaje)
            self.boton_eliminar.clicked.connect(self.eliminar_viaje)
            self.boton_volver_menu.clicked.connect(self.volverMenu)
            self.boton_pdf.clicked.connect(self.pdfMisViajes)
            self.cargar_viajes()
    #Clase usada para cargar todos los viajes
    def cargar_viajes(self):
        #Llamamos a la bd y obtenemos los datos.
        self.viajes = baseLocal.getMisViajes(self.email)
        print(f"Viajes encontrados: {self.viajes}") 

        #Creamos la tabla con los headers correspondientes 
        self.tabla_viajes.setColumnCount(4)
        self.tabla_viajes.setHorizontalHeaderLabels(["Destino", "Fecha de Salida", "Fecha de Regreso", "Precio"])
        self.tabla_viajes.setRowCount(0) 
        self.tabla_viajes.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        #Añadimos los datos a su celda
        for viaje in self.viajes:
            destino = viaje[2]
            fecha_salida = viaje[3]  
            fecha_regreso = viaje[4]  
            precio = viaje[5]  

            row_position = self.tabla_viajes.rowCount()
            self.tabla_viajes.insertRow(row_position)

            self.tabla_viajes.setItem(row_position, 0, QtWidgets.QTableWidgetItem(destino))
            self.tabla_viajes.setItem(row_position, 1, QtWidgets.QTableWidgetItem(fecha_salida))
            self.tabla_viajes.setItem(row_position, 2, QtWidgets.QTableWidgetItem(fecha_regreso))
            self.tabla_viajes.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(precio)))
         
       
        
    #Actualizamos las fechas ya que es lo unico que va ha poder actualizar.
    def actualizar_viaje(self):
        #Miramos la fila seleccionada.
        selected = self.tabla_viajes.currentRow()
        if selected < 0:
            QtWidgets.QMessageBox.warning(self, "Error", "Selecciona un viaje para actualizar")
            return
        #obtenemos el id
        viaje_id = int(self.viajes[selected][0])

        #Obtenemos la fechas
        nueva_fecha_salida = self.tabla_viajes.item(selected, 1).text() 
        nueva_fecha_regreso = self.tabla_viajes.item(selected, 2).text()
        #Le damos el formato desado, ya que lo necesitamos en un formato concreto
        formato_fecha = "%Y-%m-%d"
        try:
            #Ponemos los diferentes datos en su formato
            fecha_salida = datetime.strptime(nueva_fecha_salida, formato_fecha)
            fecha_regreso = datetime.strptime(nueva_fecha_regreso, formato_fecha)
            fecha_actual = datetime.today()
            #Comprobamos los datos entre sí
            if fecha_salida < fecha_actual:
                QtWidgets.QMessageBox.warning(self, "Error", "La fecha de salida no puede ser en el pasado.")
                self.cargar_viajes()
                return

            if fecha_regreso < fecha_salida:
                QtWidgets.QMessageBox.warning(self, "Error", "La fecha de regreso no puede ser anterior a la de salida.")
                self.cargar_viajes()
                return
        #Excepción para posible error del formato
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Formato de fecha inválido.")
            self.cargar_viajes()
            return
        #Cargamos en la bd
        baseLocal.putMisViajes(nueva_fecha_salida, nueva_fecha_regreso,viaje_id)
        #Recargamos la ventana para ver el cambio
        self.cargar_viajes()

    #Eliminamos los viajes
    def eliminar_viaje(self):
        #Seleccionamos la fila
        selected = self.tabla_viajes.currentRow()
        if selected < 0:
            QtWidgets.QMessageBox.warning(self, "Error", "Selecciona un viaje para eliminar")
            return
        #Obtenemos el id
        viaje_id = int(self.viajes[selected][0])
        #Confirmamos la orden ya que se eliminarán datos
        respuesta = QtWidgets.QMessageBox.question(
            self, "Confirmar Eliminación", "¿Estás seguro de eliminar este viaje?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        #En caso de afirmación se elimina y recargamos la ventana.
        if respuesta == QtWidgets.QMessageBox.StandardButton.Yes:
            baseLocal.delMisViajes(viaje_id)
            self.cargar_viajes()
    

    def pdfMisViajes(self):
    

        fecha = self.manager.managerPDF.generar_fecha_actual()
        ruta_pdf = 'PDFs/informeMisViajes' + fecha + '.pdf'

        try:
            resultados = glob.glob("**/MisviajesInfo.md", recursive=True)

            if resultados:
                ruta_txt = resultados[0]  # Tomamos la primera coincidencia
            else:
               # No encontrado
                QMessageBox.warning(self, 'Error', '¡No se encontró MisViajesInfo.txt!')
                return

            with open(ruta_txt, "r", encoding="utf-8") as file:
                contenido_md = file.read()

            contenido_html = markdown2.markdown(contenido_md)

            pdf = PDF2()
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

        

    #Volvemos al menu.
    def volverMenu(self):
        self.manager.mostrarVentana("menu")