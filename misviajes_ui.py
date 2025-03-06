# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'misviajes.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import recursos_rc

class Ui_GestionViajes(object):
    def setupUi(self, GestionViajes):
        if not GestionViajes.objectName():
            GestionViajes.setObjectName(u"GestionViajes")
        GestionViajes.resize(755, 485)
        GestionViajes.setMinimumSize(QSize(755, 485))
        self.principal = QWidget(GestionViajes)
        self.principal.setObjectName(u"principal")
        self.principal.setStyleSheet(u"#principal{\n"
"background-image: url(:/icons/recursos/media/fondo.jpg);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-attachment: fixed;\n"
"}\n"
"QTableWidget {\n"
"background-color: rgba(255, 255, 255, 150); /* Fondo blanco con 150 de opacidad (0-255) */\n"
"color: black; \n"
"border: 1px solid #555; /* Borde gris */\n"
"padding: 5px; /* Espaciado interno */\n"
"}\n"
"QTableWidget::item {\n"
"padding: 5px; /* Espaciado interno en cada item */\n"
"color: black; \n"
"margin: 5px; /* Espaciado externo en cada item */\n"
"}\n"
"QTableWidget::item:selected {\n"
"background-color: rgba(100, 100, 255, 200); /* Fondo azul al seleccionar un item */\n"
"color: black; /* Color del texto al seleccionar */\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"background-color: rgba(255, 255, 255, 50); /* Fondo semitransparente para las cabeceras */\n"
"color: black; /* Color del texto en las cabeceras */\n"
"border: 1px solid black; /* Borde negro */\n"
"}\n"
"QTableWidget::horizon"
                        "talHeader {\n"
"background-color: rgba(255, 255, 255, 50); /* Fondo semitransparente para las cabeceras horizontales */\n"
"color: black; /* Color del texto en las cabeceras */\n"
"border: 1px solid black; /* Borde negro */\n"
"}\n"
"QPushButton {\n"
"background-color: rgba(255, 255, 255, 150); /* Fondo semitransparente para los botones */\n"
"color: black; /* Color del texto en los botones */\n"
"border: 1px solid black; /* Borde negro */\n"
"padding: 5px; /* Espaciado interno */\n"
"border-radius: 5px; /* Bordes redondeados */\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(200, 200, 200, 200); /* Fondo m\u00e1s oscuro al pasar el rat\u00f3n */\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(150, 150, 150, 200); /* Fondo a\u00fan m\u00e1s oscuro al presionar */\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.principal)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.principal)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.boton_volver_menu = QPushButton(self.widget1)
        self.boton_volver_menu.setObjectName(u"boton_volver_menu")

        self.horizontalLayout.addWidget(self.boton_volver_menu)

        self.boton_pdf = QPushButton(self.widget1)
        self.boton_pdf.setObjectName(u"boton_pdf")

        self.horizontalLayout.addWidget(self.boton_pdf)


        self.verticalLayout.addWidget(self.widget1)

        self.tabla_viajes = QTableWidget(self.widget)
        self.tabla_viajes.setObjectName(u"tabla_viajes")
        self.tabla_viajes.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgba(255, 255, 255, 180); /* Fondo blanco semi-transparente /\n"
"    border: 1px solid gray; / Borde negro /\n"
"    gridline-color: black; / L\u00edneas de la tabla en negro /\n"
"    font-size: 14px;\n"
"    selection-background-color: rgba(100, 100, 255, 150); / Color al seleccionar fila /\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgba(255, 255, 255, 200); / Fondo blanco para los encabezados /\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    border: none; / Quitar bordes alrededor de los encabezados /\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: rgba(255, 255, 255, 200); / Esquina superior izquierda /\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: rgba(255, 255, 255, 200); / Fondo blanco en los encabezados /\n"
"    font-weight: bold; / Negrita en los encabezados /\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section:disa"
                        "bled {\n"
"    background: rgba(220, 220, 220, 180); / Fondo de encabezados deshabilitados /\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: 1px solid black; / Borde negro /\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader {\n"
"    qproperty-contains: false; / Deshabilitar la interacci\u00f3n con los encabezados */\n"
"}")
        self.tabla_viajes.horizontalHeader().setCascadingSectionResizes(True)
        self.tabla_viajes.horizontalHeader().setDefaultSectionSize(190)
        self.tabla_viajes.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tabla_viajes)

        self.widget2 = QWidget(self.widget)
        self.widget2.setObjectName(u"widget2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.boton_actualizar = QPushButton(self.widget2)
        self.boton_actualizar.setObjectName(u"boton_actualizar")

        self.horizontalLayout_2.addWidget(self.boton_actualizar)

        self.boton_eliminar = QPushButton(self.widget2)
        self.boton_eliminar.setObjectName(u"boton_eliminar")

        self.horizontalLayout_2.addWidget(self.boton_eliminar)


        self.verticalLayout.addWidget(self.widget2)


        self.verticalLayout_3.addWidget(self.widget)

        GestionViajes.setCentralWidget(self.principal)

        self.retranslateUi(GestionViajes)

        QMetaObject.connectSlotsByName(GestionViajes)
    # setupUi

    def retranslateUi(self, GestionViajes):
        GestionViajes.setWindowTitle(QCoreApplication.translate("GestionViajes", u"Gesti\u00f3n de Viajes", None))
        self.boton_volver_menu.setText(QCoreApplication.translate("GestionViajes", u"< Volver al menu", None))
        self.boton_pdf.setText(QCoreApplication.translate("GestionViajes", u"Descargar PDF de los viajes", None))
        self.boton_actualizar.setText(QCoreApplication.translate("GestionViajes", u"Actualizar Viaje", None))
        self.boton_eliminar.setText(QCoreApplication.translate("GestionViajes", u"Eliminar Viaje", None))
    # retranslateUi

