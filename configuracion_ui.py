# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuracion.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(775, 484)
        MainWindow.setMinimumSize(QSize(775, 484))
        self.principal = QWidget(MainWindow)
        self.principal.setObjectName(u"principal")
        self.principal.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.principal.setAcceptDrops(False)
        self.principal.setAutoFillBackground(False)
        self.principal.setStyleSheet(u"#principal{\n"
"background-image: url(:/icons/recursos/media/fondo.jpg);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-attachment: fixed;\n"
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
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.principal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.principal)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.QPBVolver = QPushButton(self.widget)
        self.QPBVolver.setObjectName(u"QPBVolver")
        self.QPBVolver.setMinimumSize(QSize(50, 50))
        self.QPBVolver.setMaximumSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.QPBVolver)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(17)
        self.label_7.setFont(font)

        self.horizontalLayout.addWidget(self.label_7)

        self.BcerrarSesion = QPushButton(self.widget)
        self.BcerrarSesion.setObjectName(u"BcerrarSesion")
        self.BcerrarSesion.setMaximumSize(QSize(100, 50))

        self.horizontalLayout.addWidget(self.BcerrarSesion)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.principal)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(90)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setStyleSheet(u"QFrame {\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-radius: 15px;\n"
"}\n"
"QLabel{ \n"
"min-height: 35px;\n"
"max-height: 35px;\n"
"min-width: 40px;\n"
"max-width: 170px;\n"
"color:black;\n"
"}   \n"
"QTextEdit { \n"
"min-height: 35px;\n"
"max-height: 35px;\n"
"max-width: 170px;\n"
"color:black;\n"
"}\n"
"\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(50)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.widget_4.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(10)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.widget_9, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.widget_4)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(90)
        sizePolicy4.setVerticalStretch(90)
        sizePolicy4.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy4)
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setSizeIncrement(QSize(0, 0))
        self.frame_8.setBaseSize(QSize(0, 0))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_11 = QWidget(self.frame_8)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.widget_11)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.widget_11)

        self.widget1 = QWidget(self.frame_8)
        self.widget1.setObjectName(u"widget1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy5)
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_12 = QWidget(self.widget1)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy6)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget_12)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(170, 35))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.QTENombre = QTextEdit(self.widget_12)
        self.QTENombre.setObjectName(u"QTENombre")
        self.QTENombre.setMinimumSize(QSize(200, 35))
        self.QTENombre.setMaximumSize(QSize(170, 35))

        self.horizontalLayout_3.addWidget(self.QTENombre)


        self.verticalLayout_4.addWidget(self.widget_12)

        self.widget_14 = QWidget(self.widget1)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy6.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy6)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.widget_14)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(170, 35))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.QTEApellido = QTextEdit(self.widget_14)
        self.QTEApellido.setObjectName(u"QTEApellido")
        self.QTEApellido.setMinimumSize(QSize(200, 35))
        self.QTEApellido.setMaximumSize(QSize(170, 35))

        self.horizontalLayout_5.addWidget(self.QTEApellido)


        self.verticalLayout_4.addWidget(self.widget_14)

        self.widget_10 = QWidget(self.widget1)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy6.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy6)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(170, 35))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.QTEDni = QTextEdit(self.widget_10)
        self.QTEDni.setObjectName(u"QTEDni")
        self.QTEDni.setMinimumSize(QSize(200, 35))
        self.QTEDni.setMaximumSize(QSize(170, 35))
        self.QTEDni.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.QTEDni)


        self.verticalLayout_4.addWidget(self.widget_10)

        self.BBActualizarUsuario = QDialogButtonBox(self.widget1)
        self.BBActualizarUsuario.setObjectName(u"BBActualizarUsuario")
        self.BBActualizarUsuario.setStandardButtons(QDialogButtonBox.StandardButton.Apply)
        self.BBActualizarUsuario.setCenterButtons(True)

        self.verticalLayout_4.addWidget(self.BBActualizarUsuario)


        self.verticalLayout_3.addWidget(self.widget1)

        self.PBDescargar = QPushButton(self.frame_8)
        self.PBDescargar.setObjectName(u"PBDescargar")

        self.verticalLayout_3.addWidget(self.PBDescargar)


        self.gridLayout.addWidget(self.frame_8, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.widget_3.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_41 = QWidget(self.widget_3)
        self.widget_41.setObjectName(u"widget_41")
        sizePolicy3.setHeightForWidth(self.widget_41.sizePolicy().hasHeightForWidth())
        self.widget_41.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.widget_41, 0, 0, 1, 1)

        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy3.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.widget_7, 0, 2, 1, 1)

        self.frame_3 = QFrame(self.widget_3)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setStyleSheet(u"\n"
"QLabel{\n"
"color:red;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_6 = QWidget(self.frame_3)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 150))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.label_2.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.frame_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(170, 35))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.label_6.setPalette(palette1)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_6)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_8 = QWidget(self.frame_3)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(90)
        sizePolicy7.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy7)
        self.widget_8.setStyleSheet(u"QDialogButtonBox {\n"
"    background-color: red;  /* Fondo rojo */\n"
"    color: black;  /* Texto negro */\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.buttonBox_2 = QDialogButtonBox(self.widget_8)
        self.buttonBox_2.setObjectName(u"buttonBox_2")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush3 = QBrush(QColor(255, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        brush4 = QBrush(QColor(255, 0, 4, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.buttonBox_2.setPalette(palette2)
        self.buttonBox_2.setStyleSheet(u"")
        self.buttonBox_2.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.buttonBox_2.setStandardButtons(QDialogButtonBox.StandardButton.Apply)
        self.buttonBox_2.setCenterButtons(True)

        self.verticalLayout_5.addWidget(self.buttonBox_2)


        self.verticalLayout_2.addWidget(self.widget_8)


        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.principal)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.QPBVolver.setText(QCoreApplication.translate("MainWindow", u"volver", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACION", None))
        self.BcerrarSesion.setText(QCoreApplication.translate("MainWindow", u"Cerrar sesion", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Actualizar tu cuenta", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" Nombre", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Apellido", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"    DNI    ", None))
        self.PBDescargar.setText(QCoreApplication.translate("MainWindow", u"Descargar mis datos", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Borrar tu cuenta", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u00bfEstas seguro de \n"
"borrar tu cuenta?", None))
    # retranslateUi

