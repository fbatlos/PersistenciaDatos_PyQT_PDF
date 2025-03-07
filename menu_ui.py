# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(775, 485)
        MainWindow.setMinimumSize(QSize(775, 485))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionCerrar_sesion = QAction(MainWindow)
        self.actionCerrar_sesion.setObjectName(u"actionCerrar_sesion")
        self.actionSalir_del_programa = QAction(MainWindow)
        self.actionSalir_del_programa.setObjectName(u"actionSalir_del_programa")
        self.actionver_viajes = QAction(MainWindow)
        self.actionver_viajes.setObjectName(u"actionver_viajes")
        self.actioncomprar_viaje = QAction(MainWindow)
        self.actioncomprar_viaje.setObjectName(u"actioncomprar_viaje")
        self.actionconfiguracion = QAction(MainWindow)
        self.actionconfiguracion.setObjectName(u"actionconfiguracion")
        self.actionacerca_de_mi = QAction(MainWindow)
        self.actionacerca_de_mi.setObjectName(u"actionacerca_de_mi")
        self.principal = QWidget(MainWindow)
        self.principal.setObjectName(u"principal")
        self.principal.setAcceptDrops(False)
        self.principal.setAutoFillBackground(False)
        self.principal.setStyleSheet(u"#principal{\n"
"background-image: url(:/icons/recursos/media/fondo.jpg);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-attachment: fixed;\n"
"}\n"
"#QTMisViajes {\n"
"background-color: rgba(255, 255, 255, 150); /* Fondo blanco con 150 de opacidad (0-255) */\n"
"color: black; \n"
"border: 1px solid #555; /* Borde gris */\n"
"padding: 5px; /* Espaciado interno */\n"
"}\n"
"#QTMisViajes::item {\n"
"padding: 5px; /* Espaciado interno en cada item */\n"
"color: black; \n"
"margin: 5px; /* Espaciado externo en cada item */\n"
"}\n"
"#QTMisViajes::item:selected {\n"
"background-color: rgba(100, 100, 255, 200); /* Fondo azul al seleccionar un item */\n"
"color: black; /* Color del texto al seleccionar */\n"
"}\n"
"\n"
"#QTTredingsTopicsTabla {\n"
"background-color: rgba(255, 255, 255, 150); /* Fondo blanco con 150 de opacidad (0-255) */\n"
"color: black; \n"
"border: 1px solid #555; /* Borde gris */\n"
"padding: 5px; /* Espaciado interno */\n"
"}\n"
"#QTTredingsTopicsTabla::item {\n"
""
                        "padding: 15px; /* Espaciado interno en cada item */\n"
"color: black; \n"
"margin: 15px; /* Espaciado externo en cada item */\n"
"}\n"
"#QTTredingsTopicsTabla::item:selected {\n"
"background-color: rgba(100, 100, 255, 200); /* Fondo azul al seleccionar un item */\n"
"color: black; /* Color del texto al seleccionar */\n"
"}\n"
"#QTTredingsTopicsTabla QTableCornerButton::section {\n"
"        background-color: rgba(255, 255, 255, 50); /* Fondo semitransparente para las cabeceras */\n"
"        color: black; /* Color del texto en las cabeceras */\n"
"        border: 1px solid black; /* Borde negro */\n"
"    }\n"
"\n"
"    #QTTredingsTopicsTabla::horizontalHeader {\n"
"        background-color: rgba(255, 255, 255, 50); /* Fondo semitransparente para las cabeceras horizontales */\n"
"        color: black; /* Color del texto en las cabeceras */\n"
"        border: 1px solid black; /* Borde negro */\n"
"}\n"
"QPushButton {\n"
"background-color: rgba(255, 255, 255, 150); /* Fondo semitransparente para los botones */\n"
""
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
        self.QWGridCabecera = QWidget(self.principal)
        self.QWGridCabecera.setObjectName(u"QWGridCabecera")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.QWGridCabecera.sizePolicy().hasHeightForWidth())
        self.QWGridCabecera.setSizePolicy(sizePolicy)
        self.QWGridCabecera.setStyleSheet(u"background-color: rgb(238, 247, 255);")
        self.horizontalLayout = QHBoxLayout(self.QWGridCabecera)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.QLabelUsuario = QLabel(self.QWGridCabecera)
        self.QLabelUsuario.setObjectName(u"QLabelUsuario")
        self.QLabelUsuario.setMaximumSize(QSize(85, 85))
        self.QLabelUsuario.setPixmap(QPixmap(u":/icons/recursos/iconos/usuario.png"))
        self.QLabelUsuario.setScaledContents(True)
        self.QLabelUsuario.setWordWrap(False)

        self.horizontalLayout.addWidget(self.QLabelUsuario)

        self.QWGirdDatosUsuarios = QWidget(self.QWGridCabecera)
        self.QWGirdDatosUsuarios.setObjectName(u"QWGirdDatosUsuarios")
        self.verticalLayout_2 = QVBoxLayout(self.QWGirdDatosUsuarios)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.QLNombre = QLabel(self.QWGirdDatosUsuarios)
        self.QLNombre.setObjectName(u"QLNombre")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(238, 247, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.QLNombre.setPalette(palette)
        font = QFont()
        font.setPointSize(20)
        font.setWeight(QFont.ExtraBold)
        self.QLNombre.setFont(font)

        self.verticalLayout_2.addWidget(self.QLNombre)

        self.QLCorreo = QLabel(self.QWGirdDatosUsuarios)
        self.QLCorreo.setObjectName(u"QLCorreo")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.QLCorreo.setPalette(palette1)
        font1 = QFont()
        font1.setPointSize(15)
        font1.setWeight(QFont.ExtraBold)
        self.QLCorreo.setFont(font1)

        self.verticalLayout_2.addWidget(self.QLCorreo)


        self.horizontalLayout.addWidget(self.QWGirdDatosUsuarios)

        self.QLNombreApp = QLabel(self.QWGridCabecera)
        self.QLNombreApp.setObjectName(u"QLNombreApp")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.QLNombreApp.setPalette(palette2)
        font2 = QFont()
        font2.setPointSize(24)
        font2.setWeight(QFont.Black)
        font2.setUnderline(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        font2.setHintingPreference(QFont.PreferDefaultHinting)
        self.QLNombreApp.setFont(font2)

        self.horizontalLayout.addWidget(self.QLNombreApp)

        self.QLabelConfiguracion = QLabel(self.QWGridCabecera)
        self.QLabelConfiguracion.setObjectName(u"QLabelConfiguracion")
        self.QLabelConfiguracion.setMaximumSize(QSize(80, 80))
        self.QLabelConfiguracion.setPixmap(QPixmap(u":/icons/recursos/iconos/engranaje.png"))
        self.QLabelConfiguracion.setScaledContents(True)
        self.QLabelConfiguracion.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.QLabelConfiguracion)


        self.verticalLayout.addWidget(self.QWGridCabecera)

        self.QWGridMenus = QWidget(self.principal)
        self.QWGridMenus.setObjectName(u"QWGridMenus")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(90)
        sizePolicy1.setHeightForWidth(self.QWGridMenus.sizePolicy().hasHeightForWidth())
        self.QWGridMenus.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.QWGridMenus)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.QWMenus = QWidget(self.QWGridMenus)
        self.QWMenus.setObjectName(u"QWMenus")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.QWMenus.sizePolicy().hasHeightForWidth())
        self.QWMenus.setSizePolicy(sizePolicy2)
        self.QWMenus.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.QWMenus)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.QFMisViajes = QWidget(self.QWMenus)
        self.QFMisViajes.setObjectName(u"QFMisViajes")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.QFMisViajes.sizePolicy().hasHeightForWidth())
        self.QFMisViajes.setSizePolicy(sizePolicy3)
        self.verticalLayout_4 = QVBoxLayout(self.QFMisViajes)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.QLMisViajes = QLabel(self.QFMisViajes)
        self.QLMisViajes.setObjectName(u"QLMisViajes")
        self.QLMisViajes.setMaximumSize(QSize(16777215, 22))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setWeight(QFont.ExtraBold)
        self.QLMisViajes.setFont(font3)
        self.QLMisViajes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.QLMisViajes)

        self.checkBox = QCheckBox(self.QFMisViajes)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_4.addWidget(self.checkBox)

        self.widget_2 = QWidget(self.QFMisViajes)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.QTMisViajes = QListWidget(self.widget_2)
        self.QTMisViajes.setObjectName(u"QTMisViajes")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.QTMisViajes.sizePolicy().hasHeightForWidth())
        self.QTMisViajes.setSizePolicy(sizePolicy4)
        self.QTMisViajes.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_4.addWidget(self.QTMisViajes)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.QFMisViajes)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 45))
        self.widget_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.BMisViajes = QPushButton(self.widget_4)
        self.BMisViajes.setObjectName(u"BMisViajes")
        self.BMisViajes.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_5.addWidget(self.BMisViajes)


        self.verticalLayout_4.addWidget(self.widget_4)


        self.horizontalLayout_2.addWidget(self.QFMisViajes)

        self.QFTredingTopics = QWidget(self.QWMenus)
        self.QFTredingTopics.setObjectName(u"QFTredingTopics")
        sizePolicy3.setHeightForWidth(self.QFTredingTopics.sizePolicy().hasHeightForWidth())
        self.QFTredingTopics.setSizePolicy(sizePolicy3)
        self.QFTredingTopics.setAcceptDrops(False)
        self.verticalLayout_5 = QVBoxLayout(self.QFTredingTopics)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.QLTredingTopics = QLabel(self.QFTredingTopics)
        self.QLTredingTopics.setObjectName(u"QLTredingTopics")
        self.QLTredingTopics.setMaximumSize(QSize(16777215, 22))
        self.QLTredingTopics.setFont(font3)
        self.QLTredingTopics.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.QLTredingTopics.setIndent(-1)

        self.verticalLayout_5.addWidget(self.QLTredingTopics)

        self.widget = QWidget(self.QFTredingTopics)
        self.widget.setObjectName(u"widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy5)
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.QTTredingsTopicsTabla = QTableWidget(self.widget)
        if (self.QTTredingsTopicsTabla.columnCount() < 1):
            self.QTTredingsTopicsTabla.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.QTTredingsTopicsTabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.QTTredingsTopicsTabla.rowCount() < 1):
            self.QTTredingsTopicsTabla.setRowCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.QTTredingsTopicsTabla.setItem(0, 0, __qtablewidgetitem1)
        self.QTTredingsTopicsTabla.setObjectName(u"QTTredingsTopicsTabla")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.QTTredingsTopicsTabla.sizePolicy().hasHeightForWidth())
        self.QTTredingsTopicsTabla.setSizePolicy(sizePolicy6)
        self.QTTredingsTopicsTabla.setMinimumSize(QSize(0, 0))
        self.QTTredingsTopicsTabla.setMaximumSize(QSize(350, 16777215))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setItalic(True)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.QTTredingsTopicsTabla.setFont(font4)
        self.QTTredingsTopicsTabla.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.QTTredingsTopicsTabla.setAcceptDrops(False)
        self.QTTredingsTopicsTabla.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.QTTredingsTopicsTabla.setAutoFillBackground(False)
        self.QTTredingsTopicsTabla.setFrameShadow(QFrame.Shadow.Sunken)
        self.QTTredingsTopicsTabla.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.QTTredingsTopicsTabla.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.QTTredingsTopicsTabla.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.QTTredingsTopicsTabla.setAutoScrollMargin(1)
        self.QTTredingsTopicsTabla.setAlternatingRowColors(True)
        self.QTTredingsTopicsTabla.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.QTTredingsTopicsTabla.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.QTTredingsTopicsTabla.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.QTTredingsTopicsTabla.setShowGrid(False)
        self.QTTredingsTopicsTabla.setSortingEnabled(False)
        self.QTTredingsTopicsTabla.setWordWrap(True)
        self.QTTredingsTopicsTabla.setCornerButtonEnabled(True)
        self.QTTredingsTopicsTabla.horizontalHeader().setVisible(False)
        self.QTTredingsTopicsTabla.horizontalHeader().setMinimumSectionSize(32)
        self.QTTredingsTopicsTabla.horizontalHeader().setHighlightSections(True)
        self.QTTredingsTopicsTabla.horizontalHeader().setStretchLastSection(True)
        self.QTTredingsTopicsTabla.verticalHeader().setVisible(False)
        self.QTTredingsTopicsTabla.verticalHeader().setMinimumSectionSize(24)
        self.QTTredingsTopicsTabla.verticalHeader().setDefaultSectionSize(24)
        self.QTTredingsTopicsTabla.verticalHeader().setHighlightSections(True)

        self.verticalLayout_6.addWidget(self.QTTredingsTopicsTabla)

        self.BtodoViajes = QPushButton(self.widget)
        self.BtodoViajes.setObjectName(u"BtodoViajes")
        self.BtodoViajes.setEnabled(False)

        self.verticalLayout_6.addWidget(self.BtodoViajes)


        self.verticalLayout_5.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.QFTredingTopics)


        self.verticalLayout_3.addWidget(self.QWMenus)


        self.verticalLayout.addWidget(self.QWGridMenus)

        MainWindow.setCentralWidget(self.principal)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.actionCerrar_sesion.setText(QCoreApplication.translate("MainWindow", u"Cerrar sesion", None))
        self.actionSalir_del_programa.setText(QCoreApplication.translate("MainWindow", u"Salir del programa", None))
        self.actionver_viajes.setText(QCoreApplication.translate("MainWindow", u"ver viajes", None))
        self.actioncomprar_viaje.setText(QCoreApplication.translate("MainWindow", u"comprar viaje", None))
        self.actionconfiguracion.setText(QCoreApplication.translate("MainWindow", u"configuracion", None))
        self.actionacerca_de_mi.setText(QCoreApplication.translate("MainWindow", u"acerca de mi", None))
#if QT_CONFIG(tooltip)
        self.principal.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.QLabelUsuario.setText("")
        self.QLNombre.setText(QCoreApplication.translate("MainWindow", u"usuario", None))
        self.QLCorreo.setText(QCoreApplication.translate("MainWindow", u"usuario@gmail.com", None))
        self.QLNombreApp.setText(QCoreApplication.translate("MainWindow", u"Skyberia", None))
        self.QLabelConfiguracion.setText("")
        self.QLMisViajes.setText(QCoreApplication.translate("MainWindow", u"Mis viajes", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.BMisViajes.setText(QCoreApplication.translate("MainWindow", u"Mis Viajes", None))
        self.QLTredingTopics.setText(QCoreApplication.translate("MainWindow", u"Destinos vigentes", None))
        ___qtablewidgetitem = self.QTTredingsTopicsTabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Destino", None));

        __sortingEnabled = self.QTTredingsTopicsTabla.isSortingEnabled()
        self.QTTredingsTopicsTabla.setSortingEnabled(False)
        self.QTTredingsTopicsTabla.setSortingEnabled(__sortingEnabled)

        self.BtodoViajes.setText(QCoreApplication.translate("MainWindow", u"Descargar todos los viajes", None))
    # retranslateUi

