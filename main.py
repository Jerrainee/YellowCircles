from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from random import randint
from PyQt5 import uic
import sys

from UI import Ui_MainWindow


class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1280, 720)

        self.flag = False
        self.generate_button.clicked.connect(self.paint)

    def paint(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0,255), randint(0,  255), randint(0, 255)))
            self.generate_circle(qp)
            qp.end()

    def generate_circle(self, qp):
        r = randint(10, 500)
        x = randint(0, 1280)
        y = randint(0, 720)
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec_())

