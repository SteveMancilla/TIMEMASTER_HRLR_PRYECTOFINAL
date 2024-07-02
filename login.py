# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import os, sys
from PyQt5 import uic

class Ui_MainWindow(QMainWindow):
    
    def __init__(self):
        ruta = os.path.dirname ( os.path.abspath ( __file__ ) ) + r"\login.ui"
        QMainWindow.__init__(self)
        uic.loadUi(ruta,self)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(349, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 351, 461))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/fondoLogin.jpg"))
        self.label.setObjectName("label")
        self.lblNombre = QtWidgets.QLabel(self.centralwidget)
        self.lblNombre.setGeometry(QtCore.QRect(50, 240, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
        self.lblContrasea = QtWidgets.QLabel(self.centralwidget)
        self.lblContrasea.setGeometry(QtCore.QRect(50, 290, 101, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblContrasea.setFont(font)
        self.lblContrasea.setObjectName("lblContrasea")
        self.txtInputNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtInputNombre.setGeometry(QtCore.QRect(160, 240, 131, 21))
        self.txtInputNombre.setObjectName("txtInputNombre")
        self.txtInputDNI = QtWidgets.QLineEdit(self.centralwidget)
        self.txtInputDNI.setGeometry(QtCore.QRect(160, 290, 131, 20))
        self.txtInputDNI.setObjectName("txtInputDNI")
        self.btnIngresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnIngresar.setGeometry(QtCore.QRect(120, 370, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnIngresar.setFont(font)
        self.btnIngresar.setMouseTracking(False)
        self.btnIngresar.setAcceptDrops(False)
        self.btnIngresar.setObjectName("btnIngresar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 349, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblNombre.setText(_translate("MainWindow", "Nombre:"))
        self.lblContrasea.setText(_translate("MainWindow", "DNI:"))
        self.btnIngresar.setText(_translate("MainWindow", "Ingresar"))
