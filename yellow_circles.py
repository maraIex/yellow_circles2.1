import sys
import random

from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from yellow_circles1 import Ui_MainWindow


class DisplayWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.btn.clicked.connect(self.b_event)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_figure(qp)
            qp.end()

    def b_event(self):
        self.paint()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_figure(self, qp):
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        qp.setBrush(QColor(color[0], color[1], color[2]))
        d = random.randint(0, 500)
        a = random.randint(0, 800)
        b = random.randint(0, 600)
        qp.drawEllipse(a, b, d, d)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DisplayWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())