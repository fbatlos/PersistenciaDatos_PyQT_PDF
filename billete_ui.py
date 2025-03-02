# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'billete.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import recursos_rc

class Ui_GestionViajes(object):
    def setupUi(self, GestionViajes):
        if not GestionViajes.objectName():
            GestionViajes.setObjectName(u"GestionViajes")
        GestionViajes.resize(1000, 494)
        GestionViajes.setMinimumSize(QSize(1000, 494))
        GestionViajes.setMaximumSize(QSize(1000, 494))
        self.principal = QWidget(GestionViajes)
        self.principal.setObjectName(u"principal")
        self.principal.setEnabled(True)
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
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setAutoFillBackground(True)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setMaximumSize(QSize(1200, 900))
        self.widget1.setAutoFillBackground(False)
        self.widget1.setStyleSheet(u"QWidget#widget {\n"
"    border: 0px;\n"
"    border-bottom:1px solid black; /* Borde negro en la parte inferior */\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout_7.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_7.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout_7.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout_7.setHorizontalSpacing(6)
        self.emailLabel = QLabel(self.widget1)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.emailLabel)

        self.lt_email = QLineEdit(self.widget1)
        self.lt_email.setObjectName(u"lt_email")
        self.lt_email.setStyleSheet(u"QLineEdit {\n"
"    background: transparent;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"}")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.lt_email)


        self.horizontalLayout.addLayout(self.formLayout_7)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_2.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_2.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_2.setHorizontalSpacing(13)
        self.formLayout_2.setContentsMargins(-1, -1, 29, -1)
        self.QLabel = QLabel(self.widget1)
        self.QLabel.setObjectName(u"QLabel")
        self.QLabel.setMaximumSize(QSize(1200, 900))
        font = QFont()
        font.setPointSize(20)
        self.QLabel.setFont(font)
        self.QLabel.setTextFormat(Qt.AutoText)
        self.QLabel.setWordWrap(False)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.QLabel)

        self.te_precio = QLabel(self.widget1)
        self.te_precio.setObjectName(u"te_precio")
        self.te_precio.setMaximumSize(QSize(1200, 900))
        self.te_precio.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.te_precio)


        self.horizontalLayout.addLayout(self.formLayout_2)


        self.verticalLayout.addWidget(self.widget1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(40)
        self.formLayout.setContentsMargins(0, 40, 0, 40)
        self.nombreDelPasajeroLabel = QLabel(self.widget)
        self.nombreDelPasajeroLabel.setObjectName(u"nombreDelPasajeroLabel")
        font1 = QFont()
        font1.setPointSize(16)
        self.nombreDelPasajeroLabel.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nombreDelPasajeroLabel)

        self.te_nombre = QLineEdit(self.widget)
        self.te_nombre.setObjectName(u"te_nombre")
        self.te_nombre.setFont(font1)
        self.te_nombre.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.te_nombre)

        self.apellidoDelPasajeroLabel = QLabel(self.widget)
        self.apellidoDelPasajeroLabel.setObjectName(u"apellidoDelPasajeroLabel")
        self.apellidoDelPasajeroLabel.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.apellidoDelPasajeroLabel)

        self.te_apellido = QLineEdit(self.widget)
        self.te_apellido.setObjectName(u"te_apellido")
        self.te_apellido.setFont(font1)
        self.te_apellido.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.te_apellido)

        self.dNIDelPasajeroLabel = QLabel(self.widget)
        self.dNIDelPasajeroLabel.setObjectName(u"dNIDelPasajeroLabel")
        self.dNIDelPasajeroLabel.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.dNIDelPasajeroLabel)

        self.te_dni = QLineEdit(self.widget)
        self.te_dni.setObjectName(u"te_dni")
        self.te_dni.setFont(font1)
        self.te_dni.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.te_dni)

        self.nMeroDeAsientosLabel = QLabel(self.widget)
        self.nMeroDeAsientosLabel.setObjectName(u"nMeroDeAsientosLabel")
        self.nMeroDeAsientosLabel.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.nMeroDeAsientosLabel)

        self.te_asientos = QLineEdit(self.widget)
        self.te_asientos.setObjectName(u"te_asientos")
        self.te_asientos.setFont(font1)
        self.te_asientos.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.te_asientos)


        self.horizontalLayout_5.addLayout(self.formLayout)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_6.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_6.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_6.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_6.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_6.setVerticalSpacing(40)
        self.formLayout_6.setContentsMargins(0, 40, -1, 40)
        self.ql_origen = QLabel(self.widget)
        self.ql_origen.setObjectName(u"ql_origen")
        self.ql_origen.setFont(font1)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.ql_origen)

        self.Le_origen = QLineEdit(self.widget)
        self.Le_origen.setObjectName(u"Le_origen")
        self.Le_origen.setFont(font1)
        self.Le_origen.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.Le_origen.setReadOnly(True)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.Le_origen)

        self.destinoLabel = QLabel(self.widget)
        self.destinoLabel.setObjectName(u"destinoLabel")
        self.destinoLabel.setFont(font1)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.destinoLabel)

        self.te_destino = QLineEdit(self.widget)
        self.te_destino.setObjectName(u"te_destino")
        self.te_destino.setFont(font1)
        self.te_destino.setReadOnly(True)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.te_destino)

        self.fechaDeSalidaLabel = QLabel(self.widget)
        self.fechaDeSalidaLabel.setObjectName(u"fechaDeSalidaLabel")
        self.fechaDeSalidaLabel.setFont(font1)

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.fechaDeSalidaLabel)

        self.te_salida = QLineEdit(self.widget)
        self.te_salida.setObjectName(u"te_salida")
        self.te_salida.setFont(font1)
        self.te_salida.setReadOnly(True)

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.te_salida)

        self.fechaDeVueltaLabel = QLabel(self.widget)
        self.fechaDeVueltaLabel.setObjectName(u"fechaDeVueltaLabel")
        self.fechaDeVueltaLabel.setFont(font1)

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.fechaDeVueltaLabel)

        self.te_regreso = QLineEdit(self.widget)
        self.te_regreso.setObjectName(u"te_regreso")
        self.te_regreso.setFont(font1)
        self.te_regreso.setReadOnly(True)

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.te_regreso)


        self.horizontalLayout_5.addLayout(self.formLayout_6)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.widget2 = QWidget(self.widget)
        self.widget2.setObjectName(u"widget2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.bt_aceptar = QPushButton(self.widget2)
        self.bt_aceptar.setObjectName(u"bt_aceptar")

        self.horizontalLayout_2.addWidget(self.bt_aceptar)

        self.bt_descargar = QPushButton(self.widget2)
        self.bt_descargar.setObjectName(u"bt_descargar")

        self.horizontalLayout_2.addWidget(self.bt_descargar)


        self.verticalLayout.addWidget(self.widget2)


        self.verticalLayout_3.addWidget(self.widget)

        GestionViajes.setCentralWidget(self.principal)

        self.retranslateUi(GestionViajes)

        QMetaObject.connectSlotsByName(GestionViajes)
    # setupUi

    def retranslateUi(self, GestionViajes):
        GestionViajes.setWindowTitle(QCoreApplication.translate("GestionViajes", u"Vuelos App", None))
        self.emailLabel.setText("")
        self.lt_email.setText(QCoreApplication.translate("GestionViajes", u"prueba1@gmail.com", None))
        self.QLabel.setText(QCoreApplication.translate("GestionViajes", u"Precio:", None))
        self.te_precio.setText(QCoreApplication.translate("GestionViajes", u"0", None))
        self.nombreDelPasajeroLabel.setText(QCoreApplication.translate("GestionViajes", u"Nombre del pasajero:", None))
        self.apellidoDelPasajeroLabel.setText(QCoreApplication.translate("GestionViajes", u"Apellido del pasajero:", None))
        self.dNIDelPasajeroLabel.setText(QCoreApplication.translate("GestionViajes", u"DNI del pasajero:", None))
        self.nMeroDeAsientosLabel.setText(QCoreApplication.translate("GestionViajes", u"N\u00famero de asientos:", None))
        self.ql_origen.setText(QCoreApplication.translate("GestionViajes", u"Origen:", None))
        self.Le_origen.setText(QCoreApplication.translate("GestionViajes", u"Espa\u00f1a", None))
        self.destinoLabel.setText(QCoreApplication.translate("GestionViajes", u"Destino:", None))
        self.fechaDeSalidaLabel.setText(QCoreApplication.translate("GestionViajes", u"Fecha de salida:", None))
        self.fechaDeVueltaLabel.setText(QCoreApplication.translate("GestionViajes", u"Fecha de vuelta:", None))
        self.bt_aceptar.setText(QCoreApplication.translate("GestionViajes", u"Aceptar", None))
        self.bt_descargar.setText(QCoreApplication.translate("GestionViajes", u"Descargar PDF", None))
    # retranslateUi

