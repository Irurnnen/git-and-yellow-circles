import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from random import randint


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        #if self.do_paint:
        painter = QPainter()
        painter.begin(self)
        self.paint_circles(painter)
        painter.end()
        # Имя элемента совпадает с objectName в QTDesigner
    
    def paint_circles(self, painter):
        if self.do_paint:
            painter.setPen(QPen(Qt.yellow,  8, Qt.SolidLine))
        else:
            painter.setPen(QPen(Qt.white,  8, Qt.SolidLine))
        for _ in range(3):
            temp = randint(0, 250), randint(0, 250), randint(100, 300)
            
            painter.drawEllipse(temp[0], temp[1], temp[2], temp[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec_())