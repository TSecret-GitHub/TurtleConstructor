from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QFileDialog, QAction)
from turtle_class import Invader
import py_design.design_three
import importlib
import site

imported = True
var_class = None

class consoleApp(QtWidgets.QMainWindow, py_design.design_three.Ui_MainWindow):
    def __init__(self, invader):
        super().__init__()
        self.setupUi(self)

        self.invader = invader

        self.commandLinkButton.clicked.connect(self.console_run)
        self.commandLinkButton_2.clicked.connect(self.import_button)

        self.msg = QMessageBox()
        self.msg.setWindowTitle("Message")
        self.msg.setIcon(QMessageBox.Critical)

    def console_run(self):
        text = self.textEdit.toPlainText()
        if text[:8] == 'specific' and imported:
            print('specific')
            exec(text[9:])
            return

        try:
            self.invader.command(text)
        except:
            self.msg.setText('Неправильный ввод!')
            self.msg.exec_()

    def import_button(self):
        global var_class
        
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)")
        if fileName:
            print(fileName[-3:])
            if fileName[-3:] == '.py':
                index = fileName.rfind('/')
                site.addsitedir(fileName[:index])
                index += 1 
                index = fileName[index:-3]
                exec(f'import {index}')
                imported = True
                self.invader.command('hideturtle()')
                exec(f'{index}.art()')

            else:
                self.msg.setText('НЕТ, нужен Python(.py) файл!')
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.openFileNameDialog()
        self.openFileNamesDialog()
        self.saveFileDialog()
        
        self.show()