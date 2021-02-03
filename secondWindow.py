from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)
from turtle_class import Invader
from turtle import Screen
from consoleWindow import consoleApp
import sys
import py_design.design_two

invader = Invader()
screen = Screen()


class secondApp(QtWidgets.QMainWindow, py_design.design_two.Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.threeWindow = None

        self.msg = QMessageBox()
        self.msg.setWindowTitle("Message")
        self.msg.setIcon(QMessageBox.Critical)

        self.forward.clicked.connect(self.forward_command)
        self.penup.clicked.connect(self.penup_command)
        self.pencolor.clicked.connect(self.pencolor_command)
        self.hideturtle.clicked.connect(self.hideturtle_command)
        self.left.clicked.connect(self.left_command)
        self.right.clicked.connect(self.right_command)
        self.color.clicked.connect(self.color_command)
        self.pendown.clicked.connect(self.pendown_command)
        self.pensize.clicked.connect(self.pensize_command)
        self.goto_2.clicked.connect(self.goto_command)
        self.begin_fill.clicked.connect(self.begin_fill_command)
        self.end_fill.clicked.connect(self.end_fill_command)
        self.circle.clicked.connect(self.circle_command)
        self.console.clicked.connect(self.console_command)
    
    def forward_command(self):
        text, ok = QInputDialog.getText(self, 'Вопрос ввода...', 'Введите количество пикселей:')
        try:
            invader.command('forward(' + text + ')')
        except:
            self.msg.setText('Неправильный ввод!')
            self.msg.exec_()
    
    def penup_command(self):
        invader.command('penup()')

    def pencolor_command(self):
        text, ok = QInputDialog.getText(self, 'Вопрос ввода...', 'Введите цвет черепашки:')
        try:
            invader.command('pencolor("' + text + '")')
        except:
            self.msg.setText('Неправильный ввод!')
            self.msg.exec_()

    def hideturtle_command(self):
        invader.command('hideturtle()')

    def left_command(self):
        text, ok = QInputDialog.getText(self, 'Вопрос ввода...', 'Введите градус поворота:')
        try:
            invader.command('left(' + text + ')')
        except:
            self.msg.setText('Неправильный ввод!')
            self.msg.exec_()

    def right_command(self):
        text, ok = QInputDialog.getText(self, 'Вопрос ввода...', 'Введите градус поворота:')
        try:
            invader.command('right(' + text + ')')
        except:
            self.msg.setText('Неправильный ввод!')
            self.msg.exec_()
    
    def color_command(self):
        text, ok = QInputDialog.getText(self, 'Вопрос ввода...', 'Введите цвет черепашки:')
        try:
            invader.command('color("' + text + '")')
        except:
            self.msg.setText('Неправильный ввод!')
            self.msg.exec_()
    
    def pendown_command(self):
        invader.command('pendown()')
    
    def pensize_command(self):
        text, ok = QInputDialog.getText(self, 'Вопрос ввода...', 'Введите размер черепашки:')
        try:
            invader.command('pensize("' + text + '")')
        except:
            self.msg.setText('Неправильный ввод!')
            self.msg.exec_()

    def goto_command(self):
        text, ok = QInputDialog.getText(self, 'Вопрос ввода...', 'Введите координаты черепашки:')
        try:
            invader.command('goto(' + text + ')')
        except:
            self.msg.setText('Неправильный ввод!')
            self.msg.exec_()

    def begin_fill_command(self):
        invader.command('begin_fill()')
    
    def end_fill_command(self):
        invader.command('end_fill()')

    def circle_command(self):
        text, ok = QInputDialog.getText(self, 'Вопрос ввода...', 'Введите диаметр круга:')
        try:
            invader.command('circle(' + text + ')')
        except:
            self.msg.setText('Неправильный ввод!')
            self.msg.exec_()

    def console_command(self):
        self.threeWindow = consoleApp(invader)
        self.threeWindow.show()