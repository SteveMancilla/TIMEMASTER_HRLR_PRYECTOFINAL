# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaInteractiva.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

'''import sys
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import os
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPropertyAnimation
from Pomodoro import Pomodoro
from Cronometro import Cronometro
from Alarma import Alarma

class ventanaInteractiva(QMainWindow):
    
    def __init__(self):
        ruta = os.path.dirname ( os.path.abspath ( __file__ ) ) + r"\ventanaInteractiva.ui"
        QMainWindow.__init__(self)
        uic.loadUi(ruta,self)
        
        '''self.ui = Ui_MainWindow()
        self.ui.setupUi(self)'''
        
        #Ocultar la barra por defecto
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        #Funcionalidad de los botones de la barra superior
        self.btnCerrar.clicked.connect(self.close)
        self.btnMinimizar.clicked.connect(self.showMinimized)
        self.btnMaximizar.clicked.connect(self.toggleMaximizeRestore)
        
        #Implementando menu desplegable
        self.btnMenu.clicked.connect(self.mover_menu)
        
        #Funciones de los botnos pomodoro, alarma, cronometro
        #POMODORO
        self.btnPomodoro.clicked.connect(self.Open_Pomodoro)
        self.btnPomodoro.clicked.connect(self.close)
        
        #cronometro
        self.btnCronometro.clicked.connect(self.Open_Cronometro)
        self.btnCronometro.clicked.connect(self.close)
        
        #Alarma
        self.btnAlarma.clicked.connect(self.Open_Alarma)
        self.btnAlarma.clicked.connect(self.close)

    def Open_Pomodoro(self):
        self.pom = Pomodoro()
        self.pom.show()
    
    def Open_Cronometro(self):
        self.crono = Cronometro()
        self.crono.show()
        
    def Open_Alarma(self):
        self.crono = Alarma()
        self.crono.show()
    
    def toggleMaximizeRestore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    
    def mover_menu(self):
        
        width = self.frmLateral.width()
        normal = 0
        if width==0:
            extender = 200
        else:
            extender = normal
        
        self.animacion = QPropertyAnimation(self.frmLateral, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frmSuperior = QtWidgets.QFrame(self.centralwidget)
        self.frmSuperior.setMinimumSize(QtCore.QSize(0, 80))
        self.frmSuperior.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frmSuperior.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.frmSuperior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmSuperior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmSuperior.setObjectName("frmSuperior")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frmSuperior)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnMenu = QtWidgets.QPushButton(self.frmSuperior)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnMenu.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/barra-de-menus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMenu.setIcon(icon)
        self.btnMenu.setIconSize(QtCore.QSize(145, 30))
        self.btnMenu.setObjectName("btnMenu")
        self.horizontalLayout_2.addWidget(self.btnMenu)
        spacerItem = QtWidgets.QSpacerItem(281, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnMinimizar = QtWidgets.QPushButton(self.frmSuperior)
        self.btnMinimizar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/minimizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMinimizar.setIcon(icon1)
        self.btnMinimizar.setIconSize(QtCore.QSize(40, 40))
        self.btnMinimizar.setObjectName("btnMinimizar")
        self.horizontalLayout_2.addWidget(self.btnMinimizar)
        self.btnRestaurar = QtWidgets.QPushButton(self.frmSuperior)
        self.btnRestaurar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/restaurar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRestaurar.setIcon(icon2)
        self.btnRestaurar.setIconSize(QtCore.QSize(40, 40))
        self.btnRestaurar.setObjectName("btnRestaurar")
        self.horizontalLayout_2.addWidget(self.btnRestaurar)
        self.btnMaximizar = QtWidgets.QPushButton(self.frmSuperior)
        self.btnMaximizar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/maximizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMaximizar.setIcon(icon3)
        self.btnMaximizar.setIconSize(QtCore.QSize(40, 40))
        self.btnMaximizar.setObjectName("btnMaximizar")
        self.horizontalLayout_2.addWidget(self.btnMaximizar)
        self.btnCerrar = QtWidgets.QPushButton(self.frmSuperior)
        self.btnCerrar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/cerrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCerrar.setIcon(icon4)
        self.btnCerrar.setIconSize(QtCore.QSize(40, 40))
        self.btnCerrar.setObjectName("btnCerrar")
        self.horizontalLayout_2.addWidget(self.btnCerrar)
        self.verticalLayout.addWidget(self.frmSuperior)
        self.frmInferior = QtWidgets.QFrame(self.centralwidget)
        self.frmInferior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmInferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmInferior.setObjectName("frmInferior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frmInferior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frmLateral = QtWidgets.QFrame(self.frmInferior)
        self.frmLateral.setMinimumSize(QtCore.QSize(200, 0))
        self.frmLateral.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frmLateral.setStyleSheet("QFrame{\n"
"background-color: #87cefa\n"
"}\n"
"\n"
"QPushButton{\n"
"bakcground-color: #aa55ff;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}")
        self.frmLateral.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmLateral.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmLateral.setObjectName("frmLateral")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frmLateral)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.frmLateral)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/timemaster-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.btnAlarma = QtWidgets.QPushButton(self.frmLateral)
        self.btnAlarma.setMinimumSize(QtCore.QSize(0, 40))
        self.btnAlarma.setMaximumSize(QtCore.QSize(16777215, 40))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/alarma-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlarma.setIcon(icon6)
        self.btnAlarma.setIconSize(QtCore.QSize(50, 50))
        self.btnAlarma.setObjectName("btnAlarma")
        self.verticalLayout_3.addWidget(self.btnAlarma)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.btnCronometro = QtWidgets.QPushButton(self.frmLateral)
        self.btnCronometro.setMinimumSize(QtCore.QSize(0, 40))
        self.btnCronometro.setMaximumSize(QtCore.QSize(16777215, 40))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/temporizador.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCronometro.setIcon(icon7)
        self.btnCronometro.setIconSize(QtCore.QSize(40, 40))
        self.btnCronometro.setObjectName("btnCronometro")
        self.verticalLayout_3.addWidget(self.btnCronometro)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.btnPomodoro = QtWidgets.QPushButton(self.frmLateral)
        self.btnPomodoro.setMinimumSize(QtCore.QSize(0, 40))
        self.btnPomodoro.setMaximumSize(QtCore.QSize(16777215, 40))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/pomodoro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPomodoro.setIcon(icon8)
        self.btnPomodoro.setIconSize(QtCore.QSize(40, 40))
        self.btnPomodoro.setObjectName("btnPomodoro")
        self.verticalLayout_3.addWidget(self.btnPomodoro)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.btnHistorial = QtWidgets.QPushButton(self.frmLateral)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/historial.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHistorial.setIcon(icon9)
        self.btnHistorial.setIconSize(QtCore.QSize(50, 50))
        self.btnHistorial.setObjectName("btnHistorial")
        self.verticalLayout_3.addWidget(self.btnHistorial)
        spacerItem6 = QtWidgets.QSpacerItem(20, 118, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.label = QtWidgets.QLabel(self.frmLateral)
        self.label.setStyleSheet("font: italic 15pt \"Vivaldi\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frmLateral)
        self.frmContenedor = QtWidgets.QFrame(self.frmInferior)
        self.frmContenedor.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.frmContenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmContenedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmContenedor.setObjectName("frmContenedor")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frmContenedor)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frmContenedor)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 501, 451))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/fondoInicio.jpeg"))
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.frmContenedor)
        self.verticalLayout.addWidget(self.frmInferior)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnMenu.setText(_translate("MainWindow", "Menu"))
        self.pushButton.setText(_translate("MainWindow", "Inicio          "))
        self.btnAlarma.setText(_translate("MainWindow", "Alarma       "))
        self.btnCronometro.setText(_translate("MainWindow", "Cronometro"))
        self.btnPomodoro.setText(_translate("MainWindow", "Pomodoro"))
        self.btnHistorial.setText(_translate("MainWindow", "Historial     "))
        self.label.setText(_translate("MainWindow", "Construcción de Software"))
