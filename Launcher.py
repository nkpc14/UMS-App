import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLabel, QPushButton
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import pyqtSlot,Qt
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'University Management System'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 600
        self.initUI()
 
    def initUI(self):

        self.setWindowTitle(self.title)
        self.setFixedSize(800,600)
        self.minimumSize()
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())