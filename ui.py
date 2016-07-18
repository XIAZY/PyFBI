# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/bill/Desktop/ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 326)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_port = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_port.setMaximum(10000)
        self.spinBox_port.setProperty("value", 5000)
        self.spinBox_port.setObjectName("spinBox_port")
        self.gridLayout.addWidget(self.spinBox_port, 1, 5, 1, 1)
        self.label_divider = QtWidgets.QLabel(self.centralwidget)
        self.label_divider.setObjectName("label_divider")
        self.gridLayout.addWidget(self.label_divider, 1, 4, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 2, 1, 1, 1)
        self.label_right = QtWidgets.QLabel(self.centralwidget)
        self.label_right.setObjectName("label_right")
        self.gridLayout.addWidget(self.label_right, 0, 2, 1, 4)
        self.lineEdit_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.gridLayout.addWidget(self.lineEdit_ip, 1, 2, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.label_left = QtWidgets.QLabel(self.centralwidget)
        self.label_left.setObjectName("label_left")
        self.gridLayout.addWidget(self.label_left, 0, 0, 1, 2)
        self.pushButton_install = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_install.setObjectName("pushButton_install")
        self.gridLayout.addWidget(self.pushButton_install, 2, 5, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyFBI"))
        self.label_divider.setText(_translate("MainWindow", ":"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.label_right.setText(_translate("MainWindow", "Target 3DS IP address:"))
        self.label_left.setText(_translate("MainWindow", "CIAs to be sent:"))
        self.pushButton_install.setText(_translate("MainWindow", "Install"))
        self.lineEdit_ip.setFocus()
