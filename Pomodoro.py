# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pomodoro.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import os
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPropertyAnimation, QTimer
from pygame import mixer

class Pomodoro(QMainWindow):
    
    def __init__(self):
        ruta = os.path.dirname ( os.path.abspath ( __file__ ) ) + r"\Pomodoro.ui"
        QMainWindow.__init__(self)
        uic.loadUi(ruta,self)
        
        '''self.ui = Ui_MainWindow()
        self.ui.setupUi(self)'''
        
        #Ocultar la barra por defecto
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        #Funcionalidad de los botones de la barra superior
        self.btnCerrarPom.clicked.connect(self.close)
        self.btnMinimizarPom.clicked.connect(self.showMinimized)
        self.btnExpandirPom.clicked.connect(self.toggleMaximizeRestore)
        
        #Implementando menu desplegable
        self.btnMenuPom.clicked.connect(self.mover_menu)
        
        #iniciando pomodoro trabajo
        self.btnIniciarPom.clicked.connect(self.start_timer)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer_trabajo)
        self.time_remaining = 0
        
        self.btnPausarPom.clicked.connect(self.detener)
        self.btnReanudarPom.clicked.connect(self.reanudar)
        
        #iniciando pomodoro descanso
        self.btnRestaurarPom.clicked.connect(self.startDescanso)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer_descanso)
        mixer.init()
    
    def detener(self):
        self.timer.stop()
    
    def reanudar(self):
        self.timer.start(1000)
    
    def start_timer(self):
        minutes = int(self.cbMinutosTrabajoPom.currentText())
        self.time_remaining = minutes * 60
        self.timer.start(1000)
        
    def update_timer_trabajo(self):
        if self.time_remaining > 0:
            self.time_remaining -= 1
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            time_str = f"{minutes:02d}:{seconds:02d}"
            self.lcdConteoRegresivoPom.display(time_str)
        else:
            self.timer.stop()
            mixer.music.load("sound.mp3")
            mixer.music.play()
    
    def toggleMaximizeRestore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    
    def startDescanso(self):
        minutes = int(self.cbMinDescansoPom.currentText())
        self.time_remaining = minutes * 60
        self.timer.start(1000)
    
    def update_timer_descanso(self):
        if self.time_remaining > 0:
            self.time_remaining -= 1
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            time_str = f"{minutes:02d}:{seconds:02d}"
            self.lcdConteoRegresivoPom.display(time_str)
        else:
            self.timer.stop()
            mixer.music.load("sound.mp3")
            mixer.music.play()
    
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
        self.btnMenuPom = QtWidgets.QPushButton(self.frmArriba)
        self.btnMenuPom.setMinimumSize(QtCore.QSize(200, 0))
        self.btnMenuPom.setMaximumSize(QtCore.QSize(200, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/barra-de-menus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMenuPom.setIcon(icon)
        self.btnMenuPom.setIconSize(QtCore.QSize(145, 40))
        self.btnMenuPom.setObjectName("btnMenuPom")
        self.horizontalLayout.addWidget(self.btnMenuPom)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnMinimizarPom = QtWidgets.QPushButton(self.frmArriba)
        self.btnMinimizarPom.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/minimizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMinimizarPom.setIcon(icon1)
        self.btnMinimizarPom.setIconSize(QtCore.QSize(40, 40))
        self.btnMinimizarPom.setObjectName("btnMinimizarPom")
        self.horizontalLayout.addWidget(self.btnMinimizarPom)
        self.btnExpandirPom = QtWidgets.QPushButton(self.frmArriba)
        self.btnExpandirPom.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/maximizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExpandirPom.setIcon(icon2)
        self.btnExpandirPom.setIconSize(QtCore.QSize(40, 40))
        self.btnExpandirPom.setObjectName("btnExpandirPom")
        self.horizontalLayout.addWidget(self.btnExpandirPom)
        self.btnCerrarPom = QtWidgets.QPushButton(self.frmArriba)
        self.btnCerrarPom.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/cerrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCerrarPom.setIcon(icon3)
        self.btnCerrarPom.setIconSize(QtCore.QSize(40, 40))
        self.btnCerrarPom.setObjectName("btnCerrarPom")
        self.horizontalLayout.addWidget(self.btnCerrarPom)
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
        self.frame = QtWidgets.QFrame(self.frmAbajo)
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setStyleSheet("QFrame{\n"
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
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.btnInicioPom = QtWidgets.QPushButton(self.frame)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/timemaster-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInicioPom.setIcon(icon4)
        self.btnInicioPom.setIconSize(QtCore.QSize(50, 50))
        self.btnInicioPom.setObjectName("btnInicioPom")
        self.verticalLayout_2.addWidget(self.btnInicioPom)
        self.btnAlarmaPom = QtWidgets.QPushButton(self.frame)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/alarma-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlarmaPom.setIcon(icon5)
        self.btnAlarmaPom.setIconSize(QtCore.QSize(40, 40))
        self.btnAlarmaPom.setObjectName("btnAlarmaPom")
        self.verticalLayout_2.addWidget(self.btnAlarmaPom)
        self.btnCronometroPom = QtWidgets.QPushButton(self.frame)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/temporizador.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCronometroPom.setIcon(icon6)
        self.btnCronometroPom.setIconSize(QtCore.QSize(40, 40))
        self.btnCronometroPom.setObjectName("btnCronometroPom")
        self.verticalLayout_2.addWidget(self.btnCronometroPom)
        self.btnPomodoroPom = QtWidgets.QPushButton(self.frame)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/pomodoro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPomodoroPom.setIcon(icon7)
        self.btnPomodoroPom.setIconSize(QtCore.QSize(40, 40))
        self.btnPomodoroPom.setObjectName("btnPomodoroPom")
        self.verticalLayout_2.addWidget(self.btnPomodoroPom)
        self.btnHistorialPom = QtWidgets.QPushButton(self.frame)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/historial.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHistorialPom.setIcon(icon8)
        self.btnHistorialPom.setIconSize(QtCore.QSize(50, 50))
        self.btnHistorialPom.setObjectName("btnHistorialPom")
        self.verticalLayout_2.addWidget(self.btnHistorialPom)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font: italic 15pt \"Vivaldi\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.frmAbajo)
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color: #cc9900\n"
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
        self.label_2.setGeometry(QtCore.QRect(40, 40, 201, 31))
        self.label_2.setStyleSheet("font: italic 16pt \"Vivaldi\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 211, 16))
        self.label_3.setStyleSheet("font: italic 16pt \"Vivaldi\";")
        self.label_3.setObjectName("label_3")
        self.cbMinutosTrabajoPom = QtWidgets.QComboBox(self.frame_2)
        self.cbMinutosTrabajoPom.setGeometry(QtCore.QRect(280, 50, 121, 22))
        self.cbMinutosTrabajoPom.setObjectName("cbMinutosTrabajoPom")
        self.cbMinDescansoPom = QtWidgets.QComboBox(self.frame_2)
        self.cbMinDescansoPom.setGeometry(QtCore.QRect(280, 90, 121, 22))
        self.cbMinDescansoPom.setObjectName("cbMinDescansoPom")
        self.lcdConteoRegresivoPom = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdConteoRegresivoPom.setGeometry(QtCore.QRect(180, 150, 131, 41))
        self.lcdConteoRegresivoPom.setObjectName("lcdConteoRegresivoPom")
        self.btnIniciarPom = QtWidgets.QPushButton(self.frame_2)
        self.btnIniciarPom.setGeometry(QtCore.QRect(50, 260, 75, 23))
        self.btnIniciarPom.setStyleSheet("QPushButton{\n"
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
        self.btnIniciarPom.setObjectName("btnIniciarPom")
        self.btnPausarPom = QtWidgets.QPushButton(self.frame_2)
        self.btnPausarPom.setGeometry(QtCore.QRect(170, 260, 75, 23))
        self.btnPausarPom.setObjectName("btnPausarPom")
        self.btnReanudarPom = QtWidgets.QPushButton(self.frame_2)
        self.btnReanudarPom.setGeometry(QtCore.QRect(290, 260, 75, 23))
        self.btnReanudarPom.setObjectName("btnReanudarPom")
        self.btnRestaurarPom = QtWidgets.QPushButton(self.frame_2)
        self.btnRestaurarPom.setGeometry(QtCore.QRect(410, 260, 75, 23))
        self.btnRestaurarPom.setObjectName("btnRestaurarPom")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frmArriba.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.verticalLayout.addWidget(self.frmAbajo)
        windowPomodoro.setCentralWidget(self.centralwidget)

        self.retranslateUi(windowPomodoro)
        QtCore.QMetaObject.connectSlotsByName(windowPomodoro)

    def retranslateUi(self, windowPomodoro):
        _translate = QtCore.QCoreApplication.translate
        windowPomodoro.setWindowTitle(_translate("windowPomodoro", "MainWindow"))
        self.btnMenuPom.setText(_translate("windowPomodoro", "Menu"))
        self.btnInicioPom.setText(_translate("windowPomodoro", "Inicio         "))
        self.btnAlarmaPom.setText(_translate("windowPomodoro", "Alarma       "))
        self.btnCronometroPom.setText(_translate("windowPomodoro", "Cronometro"))
        self.btnPomodoroPom.setText(_translate("windowPomodoro", "Pomodoro"))
        self.btnHistorialPom.setText(_translate("windowPomodoro", "Historial  "))
        self.label.setText(_translate("windowPomodoro", "Pomodoro"))
        self.label_2.setText(_translate("windowPomodoro", "Ingrese minutos de trabajo:"))
        self.label_3.setText(_translate("windowPomodoro", "Ingrese minutos de Descanso:"))
        self.btnIniciarPom.setText(_translate("windowPomodoro", "Iniciar"))
        self.btnPausarPom.setText(_translate("windowPomodoro", "Pausar"))
        self.btnReanudarPom.setText(_translate("windowPomodoro", "Reanudar"))
        self.btnRestaurarPom.setText(_translate("windowPomodoro", "Restaurar"))
#import conjunto_rc
