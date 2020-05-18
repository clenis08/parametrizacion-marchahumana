# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1424, 786)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(188, 188, 188);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 500, 461, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Import_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Import_Button.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0, 51, 102);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.Import_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/icons8-importar-csv-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Import_Button.setIcon(icon)
        self.Import_Button.setIconSize(QtCore.QSize(80, 80))
        self.Import_Button.setObjectName("Import_Button")
        self.horizontalLayout.addWidget(self.Import_Button)
        self.Connect_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Connect_Button.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0, 51, 102);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.Connect_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/icons8-vuelva-a-introducir-el-código-pin-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Connect_Button.setIcon(icon1)
        self.Connect_Button.setIconSize(QtCore.QSize(80, 80))
        self.Connect_Button.setObjectName("Connect_Button")
        self.horizontalLayout.addWidget(self.Connect_Button)
        self.Graph_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Graph_Button.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0, 51, 102);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.Graph_Button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/icons8-cuenta-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Graph_Button.setIcon(icon2)
        self.Graph_Button.setIconSize(QtCore.QSize(80, 80))
        self.Graph_Button.setObjectName("Graph_Button")
        self.horizontalLayout.addWidget(self.Graph_Button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Guess = QtWidgets.QToolButton(self.centralwidget)
        self.Guess.setGeometry(QtCore.QRect(50, 630, 391, 31))
        self.Guess.setObjectName("Guess")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(480, 70, 931, 221))
        self.MplWidget.setObjectName("MplWidget")
        self.MplWidget_2 = MplWidget(self.centralwidget)
        self.MplWidget_2.setGeometry(QtCore.QRect(480, 300, 931, 221))
        self.MplWidget_2.setObjectName("MplWidget_2")
        self.MxConfusion = MplWidget(self.centralwidget)
        self.MxConfusion.setGeometry(QtCore.QRect(10, 70, 461, 421))
        self.MxConfusion.setObjectName("MxConfusion")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(479, 529, 931, 131))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.StanUp_Lbl = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.StanUp_Lbl.setStyleSheet("border-image: url(:/SU/StandUp_Green.png);\n"
"border-image: url(:/SU/StanUp_Red.png);")
        self.StanUp_Lbl.setText("")
        self.StanUp_Lbl.setObjectName("StanUp_Lbl")
        self.horizontalLayout_2.addWidget(self.StanUp_Lbl)
        self.Walking_Lbl = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Walking_Lbl.setStyleSheet("border-image: url(:/Wk/Walking_Green.png);\n"
"border-image: url(:/Wk/Walking_Red.png);")
        self.Walking_Lbl.setText("")
        self.Walking_Lbl.setObjectName("Walking_Lbl")
        self.horizontalLayout_2.addWidget(self.Walking_Lbl)
        self.Laying_Lbl = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Laying_Lbl.setStyleSheet("border-image: url(:/La/Laying_Green.png);\n"
"border-image: url(:/La/Laying_Red.png);")
        self.Laying_Lbl.setText("")
        self.Laying_Lbl.setObjectName("Laying_Lbl")
        self.horizontalLayout_2.addWidget(self.Laying_Lbl)
        self.SitDown_Lbl = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.SitDown_Lbl.setStyleSheet("border-image: url(:/SD/SitDown_Green.png);\n"
"border-image: url(:/SD/SitDown_Red.png);")
        self.SitDown_Lbl.setText("")
        self.SitDown_Lbl.setObjectName("SitDown_Lbl")
        self.horizontalLayout_2.addWidget(self.SitDown_Lbl)
        self.UpStairs_Lbl = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.UpStairs_Lbl.setStyleSheet("border-image: url(:/US/UpStairs_Green.png);\n"
"border-image: url(:/US/UpStairs_Red.png);")
        self.UpStairs_Lbl.setText("")
        self.UpStairs_Lbl.setObjectName("UpStairs_Lbl")
        self.horizontalLayout_2.addWidget(self.UpStairs_Lbl)
        self.DownStair_Lbl = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.DownStair_Lbl.setStyleSheet("border-image: url(:/DS/DownStairs_Green.png);\n"
"border-image: url(:/DS/DownStairs_Red.png);")
        self.DownStair_Lbl.setText("")
        self.DownStair_Lbl.setObjectName("DownStair_Lbl")
        self.horizontalLayout_2.addWidget(self.DownStair_Lbl)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 1401, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.Title = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Title.setObjectName("Title")
        self.horizontalLayout_3.addWidget(self.Title)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1424, 21))
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
        self.Guess.setText(_translate("MainWindow", "Guess"))
        self.Title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; font-style:italic;\">Human Gait Recognition</span></p></body></html>"))
from mplwidget import MplWidget
import DownStairs_rc
import Laying_rc
import SitDown_rc
import StandUp_rc
import UpStairs_rc
import Walking_rc
