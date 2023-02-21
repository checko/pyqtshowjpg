import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,  QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Label(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.p = QPixmap()
    def setPixmap(self, p):
        self.p = p
        self.update()
    def paintEvent(self, event):
        if not self.p.isNull():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            painter.drawPixmap(self.rect(), self.p)
class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        lay = QVBoxLayout(self)
        lb = Label(self)
        lb.setPixmap(QPixmap("image.jpg"))
        lay.addWidget(lb)
app = QApplication(sys.argv)
w = Widget()
w.show()
sys.exit(app.exec_())