from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from secondWindow import secondApp
from turtle import *
import sys
import design
import design_two

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.twoWindow = None

        self.confirmButton.clicked.connect(self.confirm_clicked)
    
    def confirm_clicked(self):
        text = self.confirmTextEdit.toPlainText()

        msg = QMessageBox()
        msg.setWindowTitle("Message")

        if text == 'Я хочу просто потратить ваше время в пустую заставляя вас писать этот текст :)':
            msg.setIcon(QMessageBox.Information)
            msg.setText("Мне удалось потратить твое время!")
            msg.setInformativeText('Открываю окно управления...')
            msg.exec_()
            
            self.close()
            self.twoWindow = secondApp()
            self.twoWindow.show()
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Неправильно!")
            msg.exec_()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
