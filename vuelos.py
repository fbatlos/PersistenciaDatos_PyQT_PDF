import sys
import os
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic  # Librería para trabajar con el archivo de la interfaz
import BD.basedatos as baseLocal
import sqlite3
from compra import Compra
from PyQt6.QtGui import QIcon
import glob
import markdown2
from managerPDF.ManagerPDF import PDF3

# Clase que muestra los vuelos disponibles
class Vuelos(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        file_log = "vuelos.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)
        uic.loadUi(full_path_lo, self)
        # Cargamos las variables de la clase y los componente de la interfaz
        self.manager = manager
        self.destino = self.manager.destino
        self.te_titulo.setText(f"Vuelos a {self.destino}")
        self.pasajero = self.manager.usuario
        self.orden = 0
        self.cargar_vuelos()
        self.comboBox.currentIndexChanged.connect(self.update_tabla_vuelos)
        self.tabla_vuelos.cellClicked.connect(self.ir_a_comprar)
        self.bt_volver.clicked.connect(self.volver)
        self.bt_descargar.clicked.connect(self.pdfVuelos)
        self.setWindowIcon(QIcon("recursos/iconos/icon.ico")) # Se le pone el icon a la aplicación

    # Método que carga los vuelos disponibles
    def cargar_vuelos(self):
        aviones = baseLocal.obtener_vuelos(self.destino, self.orden)
        aviones.sort(key=lambda x: x[self.orden])
        self.cargar_tabla(aviones)

    # Método que carga la tabla con los vuelos disponibles
    def cargar_tabla(self, aviones):
        #Definimos las columnas de la tabla
        self.tabla_vuelos.setColumnCount(5)
        self.tabla_vuelos.setHorizontalHeaderLabels(["Modelo", "Categoria", "Precio", "Asientos", "ID"])
        self.tabla_vuelos.setRowCount(0)

        #Añadimos los datos a la tabla
        for row_idx, row_data in enumerate(aviones):
            self.tabla_vuelos.insertRow(row_idx)
            for col_idx, data in enumerate(row_data):
                self.tabla_vuelos.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))
        #Ajustamos el tamaño de las columnas
        self.tabla_vuelos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    # Método que actualiza el orden de la tabla de vuelos
    def update_tabla_vuelos(self):
        # Obtenemos el orden seleccionado
        if self.comboBox.currentText() == "Modelo":
            self.orden = 0
        elif self.comboBox.currentText() == "Categoria":
            self.orden = 1
        elif self.comboBox.currentText() == "Precio":
            self.orden = 2
        # Limpiamos la tabla y cargamos los vuelos ordenados
        self.tabla_vuelos.setRowCount(0)
        # Cargamos los vuelos ordenados
        self.cargar_vuelos()

    # Método que lleva a la ventana de compra
    def ir_a_comprar(self, row):
        # Obtenemos los datos del vuelo seleccionado
        modelo = self.tabla_vuelos.item(row, 0).text()
        precio = self.tabla_vuelos.item(row, 2).text()
        asientos = self.tabla_vuelos.item(row, 3).text()
        id_vuelo = self.tabla_vuelos.item(row, 4).text()
        # Guardamos los datos del vuelo seleccionado
        self.manager.vuelo = [modelo, precio, asientos, id_vuelo, self.destino]
        # Mostramos la ventana de compra
        self.manager.mostrarVentana("compra")

    # Método que lleva a la ventana de menu
    def volver(self):
        self.manager.mostrarVentana("menu")

    def pdfVuelos(self):
        fecha = self.manager.managerPDF.generar_fecha_actual()
        ruta_pdf = 'PDFs/informeVuelos' + fecha + '.pdf'
        self.grab().save('recursos/informe1.png')

        try:
            resultados = glob.glob("**/VuelosInfo.md", recursive=True)
            if resultados:
                ruta_txt = resultados[0]  # Tomamos la primera coincidencia
            else:
                QMessageBox.warning(self, 'Error', '¡No se encontró MisViajesInfo.txt!')
                return
            
            with open(ruta_txt, "r", encoding="utf-8") as file:
                contenido_md = file.read()
            
            contenido_html = markdown2.markdown(contenido_md)
            pdf = PDF3('L')
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.image("recursos/informe1.png", x= 10, y=30, w= 270, h= 155)
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
            QMessageBox.information(self,'Información', '¡Informe creado con éxito!') 
        except FileNotFoundError:
            QMessageBox.warning(self, 'Error', '¡No se encontró VuelosInfo.md!')