import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap

app = QApplication(sys.argv)
label = QLabel()
screen = app.desktop().screenGeometry()
label.setGeometry(screen)
pixmap = QPixmap("image.jpg")
label.setPixmap(pixmap)
label.setScaledContents(True)
label.show()
sys.exit(app.exec_())