import os
from PyQt6 import QtWidgets, uic, QtGui
import sys
from PyQt6.QtWidgets import *
from recursos_rc import *
import BD.basedatos as baseLocal
from PyQt6.QtGui import QIcon
import glob
import markdown2
from managerPDF.ManagerPDF import PDF5
class Menu(QtWidgets.QMainWindow):
    def __init__(self,manager):
        super(Menu, self).__init__()
        
        #cargamos la interfaz grafica
        file_log = "menu.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)
        uic.loadUi(full_path_lo,self)
        self.setWindowIcon(QIcon("recursos/iconos/icon.ico"))
        
        #cargamos los datos del destino
        self.cargarDatos()
        
        #este es nuestro navigation
        self.manager = manager

        #revisamo si el usuario ya se ha logeado
        if self.manager.usuario is not None:
            #cargamos los viajes del usuario
            self.cargarDatosLista()
            self.QLNombre.setText(self.manager.usuario.nombre)
            self.QLCorreo.setText(self.manager.usuario.email)
        
        #conectamos los diferentes  elementos
        self.QLabelUsuario.setPixmap(QtGui.QPixmap(":/icons/recursos/iconos/usuario.png"))
        self.QLabelConfiguracion.setPixmap(QtGui.QPixmap(":/icons/recursos/iconos/engranaje.png"))
        self.QTMisViajes.itemClicked.connect(self.irAMisViajes)
        self.BMisViajes.clicked.connect(self.irAMisViajes)
        self.QTTredingsTopicsTabla.cellClicked.connect(self.irACompras)
        self.QLabelConfiguracion.mousePressEvent= self.mousePressEventLabel
        self.BtodoViajes.clicked.connect(self.pdf)

    #cargamos los datos al a tabla del desinger 
    def cargarDatos(self):

        #esta funcion nos regresa todas los nombre de los destinos disponible
        destinos = baseLocal.obtenerSoloElNombreDelDestinoParaLaPantallaMenu()

        # Configurar la tabla con una sola columna llamada "Destinos"
        self.QTTredingsTopicsTabla.setColumnCount(1)
        self.QTTredingsTopicsTabla.setHorizontalHeaderLabels(["Destinos"])

        # Limpiar filas anteriores
        self.QTTredingsTopicsTabla.setRowCount(0)

        # Insertar los datos en la tabla
        for row_idx, row_data in enumerate(destinos):
            self.QTTredingsTopicsTabla.insertRow(row_idx)
            for col_idx, data in enumerate(row_data):
                self.QTTredingsTopicsTabla.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(data)))
    
    #cargamos los viajes que tenga el usuario vigente en la lista
    def cargarDatosLista(self):
        #recuperamos todos los destinos de la base de datos
        viajes = baseLocal.obtenerSoloElNombreDelViajeParaLaPantallaMenu(self.manager.usuario.email)
        if not viajes:
            print("No se encontraron viajes para este email.")

        #limpiamos la lista antes de meter contenido
        self.QTMisViajes.clear()

        #agregamos la informacion en la lista
        for viaje in viajes:
            self.QTMisViajes.addItem(viaje[0]) 

    #navegamos a la pestaña mis viajes
    def irAMisViajes(self):
        self.manager.mostrarVentana("misviajes")

    #navegamos a la pestaña ir a comprar vuelos
    def irACompras(self,row):
        self.manager.destino=self.QTTredingsTopicsTabla.item(row,0).text()
        self.manager.mostrarVentana("vuelos")

    #si le pulsa al engranage viajamos a la pestaña configuracion
    def mousePressEventLabel(self, event):
        self.irAConfiguracion()

    #navegamos a la pestaña configuracion
    def irAConfiguracion(self):
        self.manager.mostrarVentana("configuracion")





    def pdf(self):

        fecha = self.manager.managerPDF.generar_fecha_actual()
        ruta_pdf = 'PDFs/Destinos' + fecha + '.pdf'
        viajes = baseLocal.obtenerSoloElNombreDelViajeParaLaPantallaMenu(self.manager.usuario.email)

        try:
            resultados = glob.glob("**/destinosVigentes.md", recursive=True)

            if resultados:
                ruta_txt = resultados[0]  # Tomamos la primera coincidencia
            else:
               # No encontrado
                QMessageBox.warning(self, 'Error', '¡No se encontró destinosVigentes.md!')
                return 

            with open(ruta_txt, "r", encoding="utf-8") as file:
                contenido_md = file.read()

            contenido_html = markdown2.markdown(contenido_md)
            pdf = PDF5()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", "", 12)
            pdf.multi_cell(0, 10, f"Informe de destinos vigentes a fecha de hoy:{fecha}")
            pdf.ln(5)
            pdf.set_font("Arial", "B", 12)
            pdf.multi_cell(0, 10, "Viajes vigentes:")
            for dato in viajes:
                pdf.set_font("Arial", "", 12)
                pdf.multi_cell(0, 10, f"    Origen: España")
                pdf.set_font("Arial", "", 12)
                pdf.multi_cell(0, 10, f"    Destino: {dato[0]}")
                pdf.ln(5)
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