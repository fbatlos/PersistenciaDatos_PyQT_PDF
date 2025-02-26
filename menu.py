import os
from PyQt6 import QtWidgets, uic, QtGui
import sys
from PyQt6.QtWidgets import *
from recursos_rc import *

class Menu(QtWidgets.QMainWindow):
    def __init__(self,manager):
        super(Menu, self).__init__()
        file_log = "menu.ui"
        full_path_lo = os.path.join(os.path.dirname(__file__), file_log)
        uic.loadUi(full_path_lo,self)
        self.QLabelUsuario.setPixmap(QtGui.QPixmap(":/icons/recursos/iconos/usuario.png"))
        self.QLabelConfiguracion.setPixmap(QtGui.QPixmap(":/icons/recursos/iconos/engranaje.png"))
        self.manager = manager
        self.BMisViajes.clicked.connect(self.cargar_viajes)
        self.BViajes.clicked.connect(self.cargar_viajes)
        self.QLabelConfiguracion.mousePressEvent= self.mousePressEventLabel

    def cargar_viajes(self):
        conn = 3
        print("emmanuel")

    def mousePressEventLabel(self, event):
        self.irAConfiguracion()

    def irAConfiguracion(self):
        self.manager.mostrarVentana("configuracion")