import sys
import os
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic  # Librería para trabajar con el archivo de la interfaz
from PyQt6.QtCore import QDate
import BD.basedatos as baseLocal
from PyQt6.QtGui import QIcon
import glob
import markdown2
from managerPDF.ManagerPDF import PDF1

# Clase que muestra la ventana de compra
class Compra(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        file_log = "compras.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)
        uic.loadUi(full_path_lo, self)
        self.setWindowIcon(QIcon("recursos/iconos/icon.ico"))
        # Cargamos las variables de la clase y los componentes de la interfaz
        self.manager = manager
        if self.manager.usuario is not None:
            self.vuelo = self.manager.vuelo
            self.pasajero = self.manager.usuario
            self.fecha_salida = ""
            self.fecha_regreso = ""
            self.cantidad_asientos = 1
            self.cargar_datos()
            self.fc_salida.dateChanged.connect(self.set_fecha_salida)
            self.fc_vuelta.dateChanged.connect(self.set_fecha_regreso)
            self.bt_cantidad.valueChanged.connect(self.set_cantidad_asientos)
            self.boton_comprar.clicked.connect(self.comprar)

    # Método que carga los datos del pasajero y del vuelo
    def cargar_datos(self):
        self.te_nombre.setText(self.pasajero.nombre)
        self.te_apellido.setText(self.pasajero.apellido)
        self.te_dni.setText(self.pasajero.dni)
        self.pt_destino.setText(self.vuelo[4])
        self.pt_vuelo.setText(self.vuelo[0])
        self.fc_salida.setDate(QDate.currentDate())
        self.fc_vuelta.setDate(QDate.currentDate())
        self.set_fecha_regreso(QDate.currentDate())
        self.set_fecha_salida(QDate.currentDate())
        self.bt_volver.clicked.connect(self.volver)

    # Método que establece la cantidad de asientos
    def set_cantidad_asientos(self, cantidad):
        self.cantidad_asientos = cantidad

    # Método que establece la fecha de salida
    def set_fecha_salida(self, fecha):
        self.fecha_salida = fecha.toString("yyyy-MM-dd")

    # Método que establece la fecha de regreso
    def set_fecha_regreso(self, fecha):
        self.fecha_regreso = fecha.toString("yyyy-MM-dd")

    # Método que realiza la compra del vuelo
    def comprar(self):
        # Comprobamos si hay suficientes asientos
        if self.cantidad_asientos > int(self.vuelo[3]):
            QMessageBox.critical(self, "Error", "No hay suficientes asientos disponibles")
            return
        
        if self.fecha_anterior_a_hoy():
            QMessageBox.critical(self, "Error", "La fecha de salida debe ser posterior a la actual")
            return

        # Comprobamos si la fecha de regreso es posterior a la de salida
        if self.comprobar_fechas():
            # Insertamos el viaje en la base de datos
            baseLocal.insertar_viaje(self.pasajero.email, self.vuelo[3], self.fecha_salida, self.fecha_regreso, self.vuelo[1])
            self.actualizar_asientos()
            # Guardamos los datos del viaje y mostramos la ventana del billete
            self.manager.viaje = [id, self.pasajero.email, self.vuelo[3], self.fecha_salida, self.fecha_regreso, self.vuelo[1], self.cantidad_asientos]
            self.manager.mostrarVentana("billete")
        else:
            # Mostramos un mensaje de error
            QMessageBox.critical(self, "Error", "La fecha de regreso debe ser posterior a la de salida")

    # Método que actualiza la cantidad de asientos
    def actualizar_asientos(self):
        baseLocal.actualizar_asientos(self.cantidad_asientos, self.vuelo[3])

    # Método que comprueba si la fecha de salida es anterior a la actual
    def fecha_anterior_a_hoy(self):
        hoy = QDate.currentDate()
        # Convertimos la fecha de salida a QDate
        fecha_salida_qdate = QDate.fromString(self.fecha_salida, "yyyy-MM-dd")
        # Comprobamos si la fecha de salida es anterior a la actual
        if fecha_salida_qdate < hoy:
            return True
        return False

    # Método que comprueba si la fecha de regreso es posterior a la de salida
    def comprobar_fechas(self):
        if self.fecha_salida <= self.fecha_regreso:
            return True
        return False

    # Método que lleva a la ventana de vuelos
    def volver(self):
        self.manager.mostrarVentana("vuelos")


# Clase que muestra la ventana del billete
class Billete(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        # Cargamos las variables de la clase y los componentes de la interfaz
        file_log = "billete.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)
        uic.loadUi(full_path_lo, self)
        self.manager = manager
        self.viaje = manager.viaje
        self.cliente = self.manager.usuario
        self.cargar_datos()
        self.bt_aceptar.clicked.connect(self.aceptar)
        self.bt_descargar.clicked.connect(self.crea_informe1)
        self.setWindowIcon(QIcon("recursos/iconos/icon.ico"))

    # Método que carga los datos del cliente y del viaje
    def cargar_datos(self):
        if self.cliente is not None:
            self.te_nombre.setText(self.cliente.nombre)
            self.te_apellido.setText(self.cliente.apellido)
            self.te_dni.setText(self.cliente.dni)
            self.lt_email.setText(self.cliente.email)
        if self.viaje is not None:
            self.te_salida.setText(self.viaje[3])
            self.te_regreso.setText(self.viaje[4])
            self.te_precio.setText(self.viaje[5])
            self.te_asientos.setText(str(self.viaje[6]))
            destino = baseLocal.obtener_destinos_y_aviones(self.viaje[2])
            if destino is not None:
                self.te_destino.setText(destino[0][0])
        
    def crea_informe1(self):
        fecha = self.manager.managerPDF.generar_fecha_actual()
        ruta_pdf = 'PDFs/Billete' + fecha + '.pdf'
        self.grab().save('PDFs/informe1.png')

        try:
            resultados = glob.glob("**/BilleteInfo.md", recursive=True)
            if resultados:
                ruta_txt = resultados[0]  # Tomamos la primera coincidencia
            else:
                QMessageBox.warning(self, 'Error', '¡No se encontró BilleteInfo.md!')
                return
            
            with open(ruta_txt, "r", encoding="utf-8") as file:
                contenido_md = file.read()
            
            contenido_html = markdown2.markdown(contenido_md)
            pdf = PDF1('L')
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.image("PDFs/informe1.png", x= 10, y=30, w= 270, h= 155)
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
            os.remove("PDFs/informe1.png")
        except FileNotFoundError:
            QMessageBox.warning(self, 'Error', '¡No se encontró BilleteInfo.md!')
    # Método que lleva a la ventana de vuelos
    def aceptar(self):
        self.manager.mostrarVentana("menu")