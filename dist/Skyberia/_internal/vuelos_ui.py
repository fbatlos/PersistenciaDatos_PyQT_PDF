# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vuelos.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(846, 533)
        MainWindow.setMinimumSize(QSize(755, 485))
        MainWindow.setStyleSheet(u"QWidget#principal {\n"
"    background-image: url(recursos/media/fondo.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-size: cover; /* Ajusta la imagen al tama\u00f1o de la ventana */\n"
"}")
        self.principal = QWidget(MainWindow)
        self.principal.setObjectName(u"principal")
        self.principal.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.principal)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 16, 20, 16)
        self.te_titulo = QLabel(self.principal)
        self.te_titulo.setObjectName(u"te_titulo")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(True)
        self.te_titulo.setFont(font)
        self.te_titulo.setLayoutDirection(Qt.LeftToRight)
        self.te_titulo.setStyleSheet(u"color: black;")
        self.te_titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.te_titulo)

        self.comboBox = QComboBox(self.principal)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: rgba(255, 255, 255, 180); /* Blanco transparente */\n"
"    border: 1px solid black; /* Borde negro */\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"    font-size: 14px; /* Tama\u00f1o del texto */\n"
"    padding: 5px; /* Espaciado interno */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgba(240, 240, 240, 200); /* Blanco m\u00e1s intenso al pasar el mouse */\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: rgba(220, 220, 220, 220); /* Blanco m\u00e1s oscuro al presionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(255, 255, 255, 180); /* Fondo blanco transparente para el desplegable */\n"
"    border: 1px solid black; /* Borde negro */\n"
"    font-size: 14px; /* Tama\u00f1o del texto */\n"
"    selection-background-color: rgba(200, 200, 255, 150); /* Azul claro al seleccionar */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 5px; /* Espaciado interno de los elementos */\n"
"   "
                        " font-weight: normal; /* Texto en normal en los \u00edtems */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none; /* Sin borde para la flecha */\n"
"    background: transparent; /* Fondo transparente para la flecha */\n"
"    width: 20px; /* Ancho de la flecha */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border: none; /* Sin borde para la flecha */\n"
"    width: 12px; /* Ajustamos el tama\u00f1o de la flecha */\n"
"    height: 12px; /* Ajustamos el tama\u00f1o de la flecha */\n"
"    background-color: transparent; /* Fondo transparente para la flecha */\n"
"}\n"
"")
        self.comboBox.setEditable(False)

        self.verticalLayout_2.addWidget(self.comboBox)

        self.tabla_vuelos = QTableWidget(self.principal)
        self.tabla_vuelos.setObjectName(u"tabla_vuelos")
        self.tabla_vuelos.setLayoutDirection(Qt.LeftToRight)
        self.tabla_vuelos.setAutoFillBackground(False)
        self.tabla_vuelos.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgba(255, 255, 255, 180); /* Fondo blanco semi-transparente */\n"
"    border: 1px solid gray; /* Borde negro */\n"
"    gridline-color: black; /* L\u00edneas de la tabla en negro */\n"
"    font-size: 14px;\n"
"    selection-background-color: rgba(100, 100, 255, 150); /* Color al seleccionar fila */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgba(255, 255, 255, 200); /* Fondo blanco para los encabezados */\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    border: none; /* Quitar bordes alrededor de los encabezados */\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: rgba(255, 255, 255, 200); /* Esquina superior izquierda */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: rgba(255, 255, 255, 200); /* Fondo blanco en los encabezados */\n"
"    font-weight: bold; /* Negrita en los encabezados */\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderV"
                        "iew::section:disabled {\n"
"    background: rgba(220, 220, 220, 180); /* Fondo de encabezados deshabilitados */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: 1px solid black; /* Borde negro */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader {\n"
"    qproperty-contains: false; /* Deshabilitar la interacci\u00f3n con los encabezados */\n"
"}")
        self.tabla_vuelos.setFrameShape(QFrame.NoFrame)
        self.tabla_vuelos.setFrameShadow(QFrame.Sunken)
        self.tabla_vuelos.setLineWidth(1)
        self.tabla_vuelos.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabla_vuelos.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tabla_vuelos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_vuelos.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tabla_vuelos.setAlternatingRowColors(False)
        self.tabla_vuelos.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_vuelos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_vuelos.setTextElideMode(Qt.ElideMiddle)
        self.tabla_vuelos.setShowGrid(False)
        self.tabla_vuelos.setGridStyle(Qt.SolidLine)
        self.tabla_vuelos.setSortingEnabled(False)
        self.tabla_vuelos.setCornerButtonEnabled(False)
        self.tabla_vuelos.setRowCount(0)
        self.tabla_vuelos.setColumnCount(0)
        self.tabla_vuelos.horizontalHeader().setVisible(True)
        self.tabla_vuelos.horizontalHeader().setCascadingSectionResizes(True)
        self.tabla_vuelos.horizontalHeader().setDefaultSectionSize(190)
        self.tabla_vuelos.horizontalHeader().setHighlightSections(False)
        self.tabla_vuelos.horizontalHeader().setStretchLastSection(True)
        self.tabla_vuelos.verticalHeader().setVisible(False)
        self.tabla_vuelos.verticalHeader().setHighlightSections(True)

        self.verticalLayout_2.addWidget(self.tabla_vuelos)

        self.bt_descargar = QToolButton(self.principal)
        self.bt_descargar.setObjectName(u"bt_descargar")
        self.bt_descargar.setStyleSheet(u"QToolButton {\n"
"    background-color: rgba(255, 255, 255, 180); /* Blanco transparente */\n"
"    border: 1px solid black; /* Borde negro */\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"    font-size: 14px; /* Tama\u00f1o del texto */\n"
"    padding: 5px; /* Espaciado interno */\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: rgba(240, 240, 240, 200); /* Blanco m\u00e1s intenso al pasar el mouse */\n"
"}")

        self.verticalLayout_2.addWidget(self.bt_descargar)

        self.bt_volver = QPushButton(self.principal)
        self.bt_volver.setObjectName(u"bt_volver")
        self.bt_volver.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 180); /* Fondo blanco semi-transparente */\n"
"    border: 1px solid black;  /* Borde negro */\n"
"    border-radius: 5px;  /* Esquinas redondeadas */\n"
"    font-size: 14px;  /* Tama\u00f1o del texto */\n"
"\n"
"    padding: 5px;  /* Espaciado interno */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(200, 200, 200, 200); /* Cambio de color al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(180, 180, 180, 200); /* Color m\u00e1s oscuro al presionar */\n"
"}")

        self.verticalLayout_2.addWidget(self.bt_volver)

        MainWindow.setCentralWidget(self.principal)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vuelos App", None))
        self.te_titulo.setText(QCoreApplication.translate("MainWindow", u"Vuelos para ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Precio", None))

        self.bt_descargar.setText(QCoreApplication.translate("MainWindow", u"Descargar PDF", None))
        self.bt_volver.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
    # retranslateUi

