# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_two.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 459)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 10, 311, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 411, 76))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hideturtle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hideturtle.setObjectName("hideturtle")
        self.verticalLayout.addWidget(self.hideturtle)
        self.console = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(90, 420, 341, 41))
        self.console.setObjectName("console")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 150, 431, 241))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.color = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.color.setObjectName("color")
        self.horizontalLayout.addWidget(self.color)
        self.left = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.left.setObjectName("left")
        self.horizontalLayout.addWidget(self.left)
        self.forward = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.forward.setObjectName("forward")
        self.horizontalLayout.addWidget(self.forward)
        self.right = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.right.setObjectName("right")
        self.horizontalLayout.addWidget(self.right)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.goto_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.goto_2.setObjectName("goto_2")
        self.horizontalLayout_3.addWidget(self.goto_2)
        self.end_fill = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.end_fill.setObjectName("end_fill")
        self.horizontalLayout_3.addWidget(self.end_fill)
        self.begin_fill = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.begin_fill.setObjectName("begin_fill")
        self.horizontalLayout_3.addWidget(self.begin_fill)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pendown = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pendown.setObjectName("pendown")
        self.horizontalLayout_2.addWidget(self.pendown)
        self.penup = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.penup.setObjectName("penup")
        self.horizontalLayout_2.addWidget(self.penup)
        self.pencolor = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pencolor.setObjectName("pencolor")
        self.horizontalLayout_2.addWidget(self.pencolor)
        self.pensize = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pensize.setObjectName("pensize")
        self.horizontalLayout_2.addWidget(self.pensize)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.circle = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.circle.setObjectName("circle")
        self.horizontalLayout_4.addWidget(self.circle)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Итак</span><span style=\" font-size:14pt;\">, это консоль управления!</span></p></body></html>"))
        self.hideturtle.setText(_translate("MainWindow", "hideturtle"))
        self.console.setText(_translate("MainWindow", "Использовать консоль для ручного ввода..."))
        self.color.setText(_translate("MainWindow", "color"))
        self.left.setText(_translate("MainWindow", "left"))
        self.forward.setText(_translate("MainWindow", "forward"))
        self.right.setText(_translate("MainWindow", "right"))
        self.goto_2.setText(_translate("MainWindow", "goto"))
        self.end_fill.setText(_translate("MainWindow", "end_fill"))
        self.begin_fill.setText(_translate("MainWindow", "begin_fill"))
        self.pendown.setText(_translate("MainWindow", "pendown"))
        self.penup.setText(_translate("MainWindow", "penup"))
        self.pencolor.setText(_translate("MainWindow", "pencolor"))
        self.pensize.setText(_translate("MainWindow", "pensize"))
        self.circle.setText(_translate("MainWindow", "circle"))
