from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)
from turtle_class import Invader
import design_three

class consoleApp(QtWidgets.QMainWindow, design_three.Ui_MainWindow):
    def __init__(self, invader):
        super().__init__()
        self.setupUi(self)

        self.invader = invader

        self.commandLinkButton.clicked.connect(self.console_run)
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Message")
        self.msg.setIcon(QMessageBox.Critical)

    def console_run(self):
        text = self.textEdit.toPlainText()

        try:
            self.invader.command(text)
        except:
            self.msg.setText('Неправильный ввод!')
            self.msg.exec_()