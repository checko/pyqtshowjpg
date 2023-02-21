import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap
from PIL import Image

class MyLabel(QLabel):
    def __init__(self):
        super().__init__()
        screen = app.desktop().screenGeometry()
        self.setGeometry(screen)
        pixmap = QPixmap("image.jpg")
        self.setPixmap(pixmap)
        self.setScaledContents(True)
        
    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        pil_image = Image.fromqpixmap(self.pixmap())
        rgb = pil_image.getpixel((x, y))
        msg = QMessageBox()
        msg.setText(f"R: {rgb[0]}, G: {rgb[1]}, B: {rgb[2]}")
        msg.exec_()

app = QApplication(sys.argv)
label = MyLabel()
label.show()
sys.exit(app.exec_())