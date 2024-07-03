# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cronometro.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import os, sys
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPropertyAnimation, QTimer, QTime
from pygame import mixer
from Pomodoro import Pomodoro

class Cronometro(QMainWindow):
    
    def __init__(self):
        ruta = os.path.dirname ( os.path.abspath ( __file__ ) ) + r"\Cronometro.ui"
        QMainWindow.__init__(self)
        uic.loadUi(ruta,self)
        
        #Ocultar la barra por defecto
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        #Funcionalidad de los botones superiores
        self.btnCerrarCrono.clicked.connect(self.close)
        self.btnMinimizarCrono.clicked.connect(self.showMinimized)
        self.btnExpandirCrono.clicked.connect(self.toggleMaximizeRestore)
        
        
        #implementacion desplegable
        self.btnMenuCrono.clicked.connect(self.mover_menu)
        self.btnPomodoroCrono.clicked.connect(self.OpenPomodoro)
        
        
        #Mostrando hora actual
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mostrarHoraActual)
        self.timer.start(1000)
        self.mostrarHoraActual()
        
        #iniciar cronometro min
        self.btnIniciarCronoMin.clicked.connect(self.start_cronometroMin)
        self.tim = QTimer(self)
        self.tim.timeout.connect(self.update_CronometroMin)
        self.time_remaining = 0
        
        #Iniciar cronometro seg
        self.btnIniciarCronoSeg.clicked.connect(self.start_cronometroSeg)
        self.timSeg = QTimer(self)
        self.timSeg.timeout.connect(self.update_CronometroSeg)
        
        #pausando y reanudando
        self.btnPausarCrono.clicked.connect(self.detener)
        self.btnReanudarCrono.clicked.connect(self.reanudar)
        
        # Flags de pausa
        self.is_paused_min = False
        self.is_paused_seg = False
        
        mixer.init()
    
    def OpenPomodoro(self):
        self.pom = Pomodoro()
        self.pom.show()
    
    def detener(self):
        if self.tim.isActive():
            self.tim.stop()
            self.is_paused_min = True
        if self.timSeg.isActive():
            self.timSeg.stop()
            self.is_paused_seg = True

    def reanudar(self):
        if self.time_remaining > 0:
            if self.is_paused_min:
                self.tim.start(1000)
                self.is_paused_min = False
            if self.is_paused_seg:
                self.timSeg.start(1000)
                self.is_paused_seg = False
    
    def start_cronometroMin(self):
        minutes = int(self.cbMinutosTrabajoCrono.currentText())
        self.time_remaining = minutes * 60
        self.tim.start(1000)
        self.is_paused_min = False
    
    def update_CronometroMin(self):
        if self.time_remaining > 0:
            self.time_remaining -= 1
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            time_str = f"{minutes:02d}:{seconds:02d}"
            self.lcdConteoRegresivoCrono.display(time_str)
        else:
            self.tim.stop()
            mixer.music.load("sound.mp3")
            mixer.music.play(loops=1)
    
    def start_cronometroSeg(self):
        seconds = int(self.cbMinDescansoCrono.currentText())
        self.time_remaining = seconds
        self.timSeg.start(1000)
        self.is_paused_seg = False
    
    def update_CronometroSeg(self):
        if self.time_remaining > 0:
            self.time_remaining -= 1
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            time_str = f"{minutes:02d}:{seconds:02d}"
            self.lcdConteoRegresivoCrono.display(time_str)
        else:
            self.timSeg.stop()
            mixer.music.load("sound.mp3")
            mixer.music.play(loops=1)
    
    def mostrarHoraActual(self):
        current_time = QTime.currentTime()
        time_str = current_time.toString('HH:mm:ss')
        self.lcdNumberHoraActual.setText(time_str)
    
    def toggleMaximizeRestore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    
    def mover_menu(self):
        
        width = self.frmLateralPomodoro.width()
        normal = 0
        if width==0:
            extender = 200
        else:
            extender = normal
        
        self.animacion = QPropertyAnimation(self.frmLateralPomodoro, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()
    
    def setupUi(self, windowPomodoro):
        windowPomodoro.setObjectName("windowPomodoro")
        windowPomodoro.resize(729, 485)
        self.centralwidget = QtWidgets.QWidget(windowPomodoro)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frmArriba = QtWidgets.QFrame(self.centralwidget)
        self.frmArriba.setMinimumSize(QtCore.QSize(100, 80))
        self.frmArriba.setMaximumSize(QtCore.QSize(5000000, 100))
        self.frmArriba.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"background-image: url(:/new/other.jpg);")
        self.frmArriba.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmArriba.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmArriba.setObjectName("frmArriba")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frmArriba)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnMenuCrono = QtWidgets.QPushButton(self.frmArriba)
        self.btnMenuCrono.setMinimumSize(QtCore.QSize(200, 0))
        self.btnMenuCrono.setMaximumSize(QtCore.QSize(200, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/barra-de-menus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMenuCrono.setIcon(icon)
        self.btnMenuCrono.setIconSize(QtCore.QSize(145, 40))
        self.btnMenuCrono.setObjectName("btnMenuCrono")
        self.horizontalLayout.addWidget(self.btnMenuCrono)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnMinimizarCrono = QtWidgets.QPushButton(self.frmArriba)
        self.btnMinimizarCrono.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/minimizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMinimizarCrono.setIcon(icon1)
        self.btnMinimizarCrono.setIconSize(QtCore.QSize(40, 40))
        self.btnMinimizarCrono.setObjectName("btnMinimizarCrono")
        self.horizontalLayout.addWidget(self.btnMinimizarCrono)
        self.btnExpandirCrono = QtWidgets.QPushButton(self.frmArriba)
        self.btnExpandirCrono.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/maximizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExpandirCrono.setIcon(icon2)
        self.btnExpandirCrono.setIconSize(QtCore.QSize(40, 40))
        self.btnExpandirCrono.setObjectName("btnExpandirCrono")
        self.horizontalLayout.addWidget(self.btnExpandirCrono)
        self.btnCerrarCrono = QtWidgets.QPushButton(self.frmArriba)
        self.btnCerrarCrono.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/cerrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCerrarCrono.setIcon(icon3)
        self.btnCerrarCrono.setIconSize(QtCore.QSize(40, 40))
        self.btnCerrarCrono.setObjectName("btnCerrarCrono")
        self.horizontalLayout.addWidget(self.btnCerrarCrono)
        self.verticalLayout.addWidget(self.frmArriba)
        self.frmAbajo = QtWidgets.QFrame(self.centralwidget)
        self.frmAbajo.setStyleSheet("background-color: rgb(157, 196, 255);")
        self.frmAbajo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmAbajo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmAbajo.setObjectName("frmAbajo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frmAbajo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frmLateralPomodoro = QtWidgets.QFrame(self.frmAbajo)
        self.frmLateralPomodoro.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frmLateralPomodoro.setStyleSheet("QFrame{\n"
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
        self.frmLateralPomodoro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmLateralPomodoro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmLateralPomodoro.setObjectName("frmLateralPomodoro")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frmLateralPomodoro)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.btnInicioCrono = QtWidgets.QPushButton(self.frmLateralPomodoro)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/timemaster-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInicioCrono.setIcon(icon4)
        self.btnInicioCrono.setIconSize(QtCore.QSize(50, 50))
        self.btnInicioCrono.setObjectName("btnInicioCrono")
        self.verticalLayout_2.addWidget(self.btnInicioCrono)
        self.btnAlarmaCrono = QtWidgets.QPushButton(self.frmLateralPomodoro)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/alarma-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlarmaCrono.setIcon(icon5)
        self.btnAlarmaCrono.setIconSize(QtCore.QSize(40, 40))
        self.btnAlarmaCrono.setObjectName("btnAlarmaCrono")
        self.verticalLayout_2.addWidget(self.btnAlarmaCrono)
        self.btnCronometroCrono = QtWidgets.QPushButton(self.frmLateralPomodoro)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/temporizador.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCronometroCrono.setIcon(icon6)
        self.btnCronometroCrono.setIconSize(QtCore.QSize(40, 40))
        self.btnCronometroCrono.setObjectName("btnCronometroCrono")
        self.verticalLayout_2.addWidget(self.btnCronometroCrono)
        self.btnPomodoroCrono = QtWidgets.QPushButton(self.frmLateralPomodoro)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/pomodoro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPomodoroCrono.setIcon(icon7)
        self.btnPomodoroCrono.setIconSize(QtCore.QSize(40, 40))
        self.btnPomodoroCrono.setObjectName("btnPomodoroCrono")
        self.verticalLayout_2.addWidget(self.btnPomodoroCrono)
        self.btnHistorialCrono = QtWidgets.QPushButton(self.frmLateralPomodoro)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/historial.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHistorialCrono.setIcon(icon8)
        self.btnHistorialCrono.setIconSize(QtCore.QSize(50, 50))
        self.btnHistorialCrono.setObjectName("btnHistorialCrono")
        self.verticalLayout_2.addWidget(self.btnHistorialCrono)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.frmLateralPomodoro)
        self.label.setStyleSheet("font: italic 15pt \"Vivaldi\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.frmLateralPomodoro)
        self.frame_2 = QtWidgets.QFrame(self.frmAbajo)
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color: #00cc00\n"
"}\n"
"\n"
"QPushButton{\n"
"bakcground-color: #0000cc;\n"
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
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 201, 31))
        self.label_2.setStyleSheet("font: italic 16pt \"Vivaldi\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 211, 16))
        self.label_3.setStyleSheet("font: italic 16pt \"Vivaldi\";")
        self.label_3.setObjectName("label_3")
        self.cbMinutosTrabajoPom = QtWidgets.QComboBox(self.frame_2)
        self.cbMinutosTrabajoPom.setGeometry(QtCore.QRect(310, 90, 121, 22))
        self.cbMinutosTrabajoPom.setObjectName("cbMinutosTrabajoPom")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinutosTrabajoPom.addItem("")
        self.cbMinDescansoPom = QtWidgets.QComboBox(self.frame_2)
        self.cbMinDescansoPom.setGeometry(QtCore.QRect(310, 130, 121, 22))
        self.cbMinDescansoPom.setObjectName("cbMinDescansoPom")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.cbMinDescansoPom.addItem("")
        self.lcdConteoRegresivoCrono = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdConteoRegresivoCrono.setGeometry(QtCore.QRect(190, 190, 131, 41))
        self.lcdConteoRegresivoCrono.setObjectName("lcdConteoRegresivoCrono")
        self.btnIniciarCrono = QtWidgets.QPushButton(self.frame_2)
        self.btnIniciarCrono.setGeometry(QtCore.QRect(50, 300, 111, 23))
        self.btnIniciarCrono.setStyleSheet("QPushButton{\n"
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
        self.btnIniciarCrono.setObjectName("btnIniciarCrono")
        self.btnPausarPom = QtWidgets.QPushButton(self.frame_2)
        self.btnPausarPom.setGeometry(QtCore.QRect(200, 300, 121, 23))
        self.btnPausarPom.setObjectName("btnPausarPom")
        self.btnReanudarPom = QtWidgets.QPushButton(self.frame_2)
        self.btnReanudarPom.setGeometry(QtCore.QRect(360, 300, 131, 23))
        self.btnReanudarPom.setObjectName("btnReanudarPom")
        self.lcdNumberHoraActual = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdNumberHoraActual.setGeometry(QtCore.QRect(190, 20, 141, 41))
        self.lcdNumberHoraActual.setObjectName("lcdNumberHoraActual")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frmAbajo)
        windowPomodoro.setCentralWidget(self.centralwidget)

        self.retranslateUi(windowPomodoro)
        QtCore.QMetaObject.connectSlotsByName(windowPomodoro)

    def retranslateUi(self, windowPomodoro):
        _translate = QtCore.QCoreApplication.translate
        windowPomodoro.setWindowTitle(_translate("windowPomodoro", "MainWindow"))
        self.btnMenuCrono.setText(_translate("windowPomodoro", "Menu"))
        self.btnInicioCrono.setText(_translate("windowPomodoro", "Inicio         "))
        self.btnAlarmaCrono.setText(_translate("windowPomodoro", "Alarma       "))
        self.btnCronometroCrono.setText(_translate("windowPomodoro", "Cronometro"))
        self.btnPomodoroCrono.setText(_translate("windowPomodoro", "Pomodoro"))
        self.btnHistorialCrono.setText(_translate("windowPomodoro", "Historial  "))
        self.label.setText(_translate("windowPomodoro", "Cronometro"))
        self.label_2.setText(_translate("windowPomodoro", "Ingrese tiempo minutos:"))
        self.label_3.setText(_translate("windowPomodoro", "Ingrese tiempo segundos:"))
        self.cbMinutosTrabajoPom.setItemText(0, _translate("windowPomodoro", "0"))
        self.cbMinutosTrabajoPom.setItemText(1, _translate("windowPomodoro", "1"))
        self.cbMinutosTrabajoPom.setItemText(2, _translate("windowPomodoro", "2"))
        self.cbMinutosTrabajoPom.setItemText(3, _translate("windowPomodoro", "3"))
        self.cbMinutosTrabajoPom.setItemText(4, _translate("windowPomodoro", "4"))
        self.cbMinutosTrabajoPom.setItemText(5, _translate("windowPomodoro", "5"))
        self.cbMinutosTrabajoPom.setItemText(6, _translate("windowPomodoro", "6"))
        self.cbMinutosTrabajoPom.setItemText(7, _translate("windowPomodoro", "7"))
        self.cbMinutosTrabajoPom.setItemText(8, _translate("windowPomodoro", "8"))
        self.cbMinutosTrabajoPom.setItemText(9, _translate("windowPomodoro", "9"))
        self.cbMinutosTrabajoPom.setItemText(10, _translate("windowPomodoro", "10"))
        self.cbMinutosTrabajoPom.setItemText(11, _translate("windowPomodoro", "11"))
        self.cbMinutosTrabajoPom.setItemText(12, _translate("windowPomodoro", "12"))
        self.cbMinutosTrabajoPom.setItemText(13, _translate("windowPomodoro", "13"))
        self.cbMinutosTrabajoPom.setItemText(14, _translate("windowPomodoro", "14"))
        self.cbMinutosTrabajoPom.setItemText(15, _translate("windowPomodoro", "15"))
        self.cbMinutosTrabajoPom.setItemText(16, _translate("windowPomodoro", "16"))
        self.cbMinutosTrabajoPom.setItemText(17, _translate("windowPomodoro", "17"))
        self.cbMinutosTrabajoPom.setItemText(18, _translate("windowPomodoro", "18"))
        self.cbMinutosTrabajoPom.setItemText(19, _translate("windowPomodoro", "19"))
        self.cbMinutosTrabajoPom.setItemText(20, _translate("windowPomodoro", "20"))
        self.cbMinutosTrabajoPom.setItemText(21, _translate("windowPomodoro", "21"))
        self.cbMinutosTrabajoPom.setItemText(22, _translate("windowPomodoro", "22"))
        self.cbMinutosTrabajoPom.setItemText(23, _translate("windowPomodoro", "23"))
        self.cbMinutosTrabajoPom.setItemText(24, _translate("windowPomodoro", "24"))
        self.cbMinutosTrabajoPom.setItemText(25, _translate("windowPomodoro", "25"))
        self.cbMinutosTrabajoPom.setItemText(26, _translate("windowPomodoro", "26"))
        self.cbMinutosTrabajoPom.setItemText(27, _translate("windowPomodoro", "27"))
        self.cbMinutosTrabajoPom.setItemText(28, _translate("windowPomodoro", "28"))
        self.cbMinutosTrabajoPom.setItemText(29, _translate("windowPomodoro", "29"))
        self.cbMinutosTrabajoPom.setItemText(30, _translate("windowPomodoro", "30"))
        self.cbMinutosTrabajoPom.setItemText(31, _translate("windowPomodoro", "31"))
        self.cbMinutosTrabajoPom.setItemText(32, _translate("windowPomodoro", "32"))
        self.cbMinutosTrabajoPom.setItemText(33, _translate("windowPomodoro", "33"))
        self.cbMinutosTrabajoPom.setItemText(34, _translate("windowPomodoro", "34"))
        self.cbMinutosTrabajoPom.setItemText(35, _translate("windowPomodoro", "35"))
        self.cbMinutosTrabajoPom.setItemText(36, _translate("windowPomodoro", "36"))
        self.cbMinutosTrabajoPom.setItemText(37, _translate("windowPomodoro", "37"))
        self.cbMinutosTrabajoPom.setItemText(38, _translate("windowPomodoro", "38"))
        self.cbMinutosTrabajoPom.setItemText(39, _translate("windowPomodoro", "39"))
        self.cbMinutosTrabajoPom.setItemText(40, _translate("windowPomodoro", "40"))
        self.cbMinutosTrabajoPom.setItemText(41, _translate("windowPomodoro", "41"))
        self.cbMinutosTrabajoPom.setItemText(42, _translate("windowPomodoro", "42"))
        self.cbMinutosTrabajoPom.setItemText(43, _translate("windowPomodoro", "43"))
        self.cbMinutosTrabajoPom.setItemText(44, _translate("windowPomodoro", "44"))
        self.cbMinutosTrabajoPom.setItemText(45, _translate("windowPomodoro", "45"))
        self.cbMinutosTrabajoPom.setItemText(46, _translate("windowPomodoro", "46"))
        self.cbMinutosTrabajoPom.setItemText(47, _translate("windowPomodoro", "47"))
        self.cbMinutosTrabajoPom.setItemText(48, _translate("windowPomodoro", "48"))
        self.cbMinutosTrabajoPom.setItemText(49, _translate("windowPomodoro", "49"))
        self.cbMinutosTrabajoPom.setItemText(50, _translate("windowPomodoro", "50"))
        self.cbMinutosTrabajoPom.setItemText(51, _translate("windowPomodoro", "51"))
        self.cbMinutosTrabajoPom.setItemText(52, _translate("windowPomodoro", "52"))
        self.cbMinutosTrabajoPom.setItemText(53, _translate("windowPomodoro", "53"))
        self.cbMinutosTrabajoPom.setItemText(54, _translate("windowPomodoro", "54"))
        self.cbMinutosTrabajoPom.setItemText(55, _translate("windowPomodoro", "55"))
        self.cbMinutosTrabajoPom.setItemText(56, _translate("windowPomodoro", "56"))
        self.cbMinutosTrabajoPom.setItemText(57, _translate("windowPomodoro", "57"))
        self.cbMinutosTrabajoPom.setItemText(58, _translate("windowPomodoro", "58"))
        self.cbMinutosTrabajoPom.setItemText(59, _translate("windowPomodoro", "59"))
        self.cbMinDescansoPom.setItemText(0, _translate("windowPomodoro", "0"))
        self.cbMinDescansoPom.setItemText(1, _translate("windowPomodoro", "1"))
        self.cbMinDescansoPom.setItemText(2, _translate("windowPomodoro", "2"))
        self.cbMinDescansoPom.setItemText(3, _translate("windowPomodoro", "3"))
        self.cbMinDescansoPom.setItemText(4, _translate("windowPomodoro", "4"))
        self.cbMinDescansoPom.setItemText(5, _translate("windowPomodoro", "5"))
        self.cbMinDescansoPom.setItemText(6, _translate("windowPomodoro", "6"))
        self.cbMinDescansoPom.setItemText(7, _translate("windowPomodoro", "7"))
        self.cbMinDescansoPom.setItemText(8, _translate("windowPomodoro", "8"))
        self.cbMinDescansoPom.setItemText(9, _translate("windowPomodoro", "9"))
        self.cbMinDescansoPom.setItemText(10, _translate("windowPomodoro", "10"))
        self.cbMinDescansoPom.setItemText(11, _translate("windowPomodoro", "11"))
        self.cbMinDescansoPom.setItemText(12, _translate("windowPomodoro", "12"))
        self.cbMinDescansoPom.setItemText(13, _translate("windowPomodoro", "13"))
        self.cbMinDescansoPom.setItemText(14, _translate("windowPomodoro", "14"))
        self.cbMinDescansoPom.setItemText(15, _translate("windowPomodoro", "15"))
        self.cbMinDescansoPom.setItemText(16, _translate("windowPomodoro", "16"))
        self.cbMinDescansoPom.setItemText(17, _translate("windowPomodoro", "17"))
        self.cbMinDescansoPom.setItemText(18, _translate("windowPomodoro", "18"))
        self.cbMinDescansoPom.setItemText(19, _translate("windowPomodoro", "19"))
        self.cbMinDescansoPom.setItemText(20, _translate("windowPomodoro", "20"))
        self.cbMinDescansoPom.setItemText(21, _translate("windowPomodoro", "21"))
        self.cbMinDescansoPom.setItemText(22, _translate("windowPomodoro", "22"))
        self.cbMinDescansoPom.setItemText(23, _translate("windowPomodoro", "23"))
        self.cbMinDescansoPom.setItemText(24, _translate("windowPomodoro", "24"))
        self.cbMinDescansoPom.setItemText(25, _translate("windowPomodoro", "25"))
        self.cbMinDescansoPom.setItemText(26, _translate("windowPomodoro", "26"))
        self.cbMinDescansoPom.setItemText(27, _translate("windowPomodoro", "27"))
        self.cbMinDescansoPom.setItemText(28, _translate("windowPomodoro", "28"))
        self.cbMinDescansoPom.setItemText(29, _translate("windowPomodoro", "29"))
        self.cbMinDescansoPom.setItemText(30, _translate("windowPomodoro", "30"))
        self.cbMinDescansoPom.setItemText(31, _translate("windowPomodoro", "31"))
        self.cbMinDescansoPom.setItemText(32, _translate("windowPomodoro", "32"))
        self.cbMinDescansoPom.setItemText(33, _translate("windowPomodoro", "33"))
        self.cbMinDescansoPom.setItemText(34, _translate("windowPomodoro", "34"))
        self.cbMinDescansoPom.setItemText(35, _translate("windowPomodoro", "35"))
        self.cbMinDescansoPom.setItemText(36, _translate("windowPomodoro", "36"))
        self.cbMinDescansoPom.setItemText(37, _translate("windowPomodoro", "37"))
        self.cbMinDescansoPom.setItemText(38, _translate("windowPomodoro", "38"))
        self.cbMinDescansoPom.setItemText(39, _translate("windowPomodoro", "39"))
        self.cbMinDescansoPom.setItemText(40, _translate("windowPomodoro", "40"))
        self.cbMinDescansoPom.setItemText(41, _translate("windowPomodoro", "41"))
        self.cbMinDescansoPom.setItemText(42, _translate("windowPomodoro", "42"))
        self.cbMinDescansoPom.setItemText(43, _translate("windowPomodoro", "43"))
        self.cbMinDescansoPom.setItemText(44, _translate("windowPomodoro", "44"))
        self.cbMinDescansoPom.setItemText(45, _translate("windowPomodoro", "45"))
        self.cbMinDescansoPom.setItemText(46, _translate("windowPomodoro", "46"))
        self.cbMinDescansoPom.setItemText(47, _translate("windowPomodoro", "47"))
        self.cbMinDescansoPom.setItemText(48, _translate("windowPomodoro", "48"))
        self.cbMinDescansoPom.setItemText(49, _translate("windowPomodoro", "49"))
        self.cbMinDescansoPom.setItemText(50, _translate("windowPomodoro", "50"))
        self.cbMinDescansoPom.setItemText(51, _translate("windowPomodoro", "51"))
        self.cbMinDescansoPom.setItemText(52, _translate("windowPomodoro", "52"))
        self.cbMinDescansoPom.setItemText(53, _translate("windowPomodoro", "53"))
        self.cbMinDescansoPom.setItemText(54, _translate("windowPomodoro", "54"))
        self.cbMinDescansoPom.setItemText(55, _translate("windowPomodoro", "55"))
        self.cbMinDescansoPom.setItemText(56, _translate("windowPomodoro", "56"))
        self.cbMinDescansoPom.setItemText(57, _translate("windowPomodoro", "57"))
        self.cbMinDescansoPom.setItemText(58, _translate("windowPomodoro", "58"))
        self.cbMinDescansoPom.setItemText(59, _translate("windowPomodoro", "59"))
        self.btnIniciarCrono.setText(_translate("windowPomodoro", "Iniciar Cronometro"))
        self.btnPausarPom.setText(_translate("windowPomodoro", "Pausar Cronometro"))
        self.btnReanudarPom.setText(_translate("windowPomodoro", "Reanudar Cronometro"))
#import conjunto_rc
