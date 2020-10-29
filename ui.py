# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 562)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Sugar/Desktop/电影视频.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("MainWindow{\n"
"    \n"
"    background-color: rgb(12, 12, 12);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(960, 540))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setEnabled(True)
        self.homeButton.setMinimumSize(QtCore.QSize(0, 0))
        self.homeButton.setMaximumSize(QtCore.QSize(96, 44))
        self.homeButton.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Sugar/Desktop/首页 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon1)
        self.homeButton.setAutoDefault(False)
        self.homeButton.setDefault(False)
        self.homeButton.setFlat(False)
        self.homeButton.setObjectName("homeButton")
        self.gridLayout.addWidget(self.homeButton, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(80, 80))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Sugar/Desktop/u=1592900172,1428334957&fm=26&gp=0.jpg"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.movieButton = QtWidgets.QPushButton(self.centralwidget)
        self.movieButton.setMaximumSize(QtCore.QSize(96, 44))
        self.movieButton.setIcon(icon)
        self.movieButton.setObjectName("movieButton")
        self.gridLayout.addWidget(self.movieButton, 2, 0, 1, 1)
        self.mediaButton = QtWidgets.QPushButton(self.centralwidget)
        self.mediaButton.setMaximumSize(QtCore.QSize(96, 44))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Sugar/Desktop/媒体资源.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mediaButton.setIcon(icon2)
        self.mediaButton.setObjectName("mediaButton")
        self.gridLayout.addWidget(self.mediaButton, 3, 0, 1, 1)
        self.aboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.aboutButton.setMaximumSize(QtCore.QSize(96, 44))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Sugar/Desktop/关于.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutButton.setIcon(icon3)
        self.aboutButton.setObjectName("aboutButton")
        self.gridLayout.addWidget(self.aboutButton, 6, 0, 1, 1)
        self.privateButton = QtWidgets.QPushButton(self.centralwidget)
        self.privateButton.setMaximumSize(QtCore.QSize(96, 44))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/Sugar/Desktop/私人库.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.privateButton.setIcon(icon4)
        self.privateButton.setIconSize(QtCore.QSize(16, 16))
        self.privateButton.setObjectName("privateButton")
        self.gridLayout.addWidget(self.privateButton, 5, 0, 1, 1)
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setMinimumSize(QtCore.QSize(90, 40))
        self.settingsButton.setMaximumSize(QtCore.QSize(96, 44))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/Sugar/Desktop/设 置 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon5)
        self.settingsButton.setObjectName("settingsButton")
        self.gridLayout.addWidget(self.settingsButton, 4, 0, 1, 1)
        self.showLayout = QtWidgets.QGridLayout()
        self.showLayout.setContentsMargins(960, -1, -1, -1)
        self.showLayout.setObjectName("showLayout")
        self.gridLayout.addLayout(self.showLayout, 0, 1, 8, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "影视收藏工具箱"))
        self.homeButton.setText(_translate("MainWindow", "首页"))
        self.movieButton.setText(_translate("MainWindow", "电影"))
        self.mediaButton.setText(_translate("MainWindow", "媒体库"))
        self.aboutButton.setText(_translate("MainWindow", "关于"))
        self.privateButton.setText(_translate("MainWindow", "私人空间"))
        self.settingsButton.setText(_translate("MainWindow", "设置"))

