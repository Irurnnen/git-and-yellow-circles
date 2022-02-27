import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 470, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Кнопка"))


class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        # if self.do_paint:
        painter = QPainter()
        painter.begin(self)
        self.paint_circles(painter)
        painter.end()
        # Имя элемента совпадает с objectName в QTDesigner

    def paint_circles(self, painter):
        painter.setPen(QPen(Qt.white,  8, Qt.SolidLine))

        for _ in range(3):
            temp = randint(0, 250), randint(0, 250), randint(100, 300)
            if self.do_paint:
                painter.setPen(QPen(QColor(randint(0, 255), randint(
                    0, 255), randint(0, 255)),  8, Qt.SolidLine))
            else:
                painter.setPen(QPen(Qt.white,  8, Qt.SolidLine))
            painter.drawEllipse(temp[0], temp[1], temp[2], temp[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec_())
