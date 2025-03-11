from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize,QPoint,Qt
import sys
from configuracion import Configuracion
from login import Ventana
from menu import Menu
from misviajes import MisViajes
from vuelos import Vuelos
from compra import Compra, Billete
from models.cliente import Cliente
from managerPDF.ManagerPDF import ManagerPDF
from PyQt6.QtGui import QIcon

# Para la ejecucíon del comando:
# pyinstaller --windowed --icon=recursos/iconos/icon.ico --add-data="BD/basedatos.py:BD" --add-data="models/cliente.py:models" --add-data="recursos/iconos/engranaje.png:recursos/iconos" --add-data="recursos/iconos/usuario.png:recursos/iconos" --add-data="recursos/media/billete.jpg:recursos/media" --add-data="recursos/media/fondo.jpg:recursos/media" --add-data="billete_ui.py:." --add-data="billete.ui:." --add-data="compra.py:." --add-data="compras_ui.py:." --add-data="compras.ui:." --add-data="configuracion_ui.py:." --add-data="configuracion.py:." --add-data="configuracion.ui:." --add-data="firebase.txt:." --add-data="recursos/iconos/icon.ico:recursos/iconos" --add-data="login_ui.py:." --add-data="login.py:." --add-data="login.ui:." --add-data="menu_ui.py:." --add-data="menu.ui:." --add-data="menu.py:." --add-data="misviajes_ui.py:." --add-data="misviajes.ui:." --add-data="misviajes.ui:." --add-data="recursos_rc.py:." --add-data="recursos.qrc:." --add-data="viajes.db:." --add-data="vuelos_ui.py:." --add-data="vuelos.py:." --add-data="vuelos.ui:." --add-data="managerPDF/recursos/BilleteInfo.md:managerPDF/recursos" --add-data="managerPDF/recursos/destinosVigentes.md:managerPDF/recursos" --add-data="managerPDF/recursos/informacionUsuario.md:managerPDF/recursos" --add-data="managerPDF/recursos/MisViajesInfo.md:managerPDF/recursos" --add-data="managerPDF/recursos/VuelosInfo.md:managerPDF/recursos" --add-data="managerPDF/logo_alberti.png:managerPDF" --add-data="managerPDF/logo.png:managerPDF" --add-data="managerPDF/ManagerPDF.py:managerPDF" --add-data="recursos/informe1.png:recursos" --name "Skyberia" Navigation.py
class WindowManager:
    def __init__(self):
        self.current_window = None  # Almacena la ventana actual dd
        self.token = None # paco aqui quiero que me des el token y lo pases aqui
        self.usuario:Cliente = None # paco o ivan aqui teneis el usuario actual lo guardamos
        self.destino = None
        self.vuelo = None
        self.viaje = None
        self.managerPDF = ManagerPDF()

        self.ventanas = {  #aqui estara todos las ventanas que necesitaremos
            "menu": Menu(self), 
            "login":Ventana(self),
            "configuracion": Configuracion(self),
            "misviajes":MisViajes(self),
            "vuelos":Vuelos(self),
            "compra":Compra(self),
            "billete":Billete(self)
        }

        self.full_screen_state:bool = None # estado de la ventana si esta activa o no
        self.previous_size:QSize = None # tamaño de la ventana
        self.previous_position:QPoint = None # posicion de la ventana

    def mostrarVentana(self, nombre:str):
        if nombre not in self.ventanas:
            print(f"❌ ERROR: La ventana '{nombre}' no está registrada.")
            return

        
        self.cerrarVentana()
        self.mostrarVentanaUi(nombre)

    def mostrarVentanaUi(self, nombre:str):
        self.current_window = self.ventanas[nombre]
        #muestro la pantalla en forma maximizada
        if self.full_screen_state:
            self.current_window.showMaximized()
        #si no le pongo el tamaño y la posicion
        else:
            self.current_window.__init__(self) 
            if self.previous_size:
                self.current_window.resize(self.previous_size)
                self.current_window.move(self.previous_position) 
            #bloqueo la pantalla que se pueda redimensionar debido preferencia del equipo de desarrollo
            self.current_window.setFixedSize(self.current_window.size())
            self.current_window.show()

    def cerrarVentana(self):
        #compruebo si la ventana actual esta ocupada
        if self.current_window:
            self.full_screen_state = self.current_window.isMaximized()
            #si no esta en pantalla completa
            if not self.full_screen_state:
                #cogo el alto y bajo 
                self.previous_size = self.current_window.size()
                #cogo la posicion
                self.previous_position = self.current_window.pos()
            self.current_window.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = WindowManager()
    manager.mostrarVentana("login")
    sys.exit(app.exec())