import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QResizeEvent
from PyQt5.QtCore import Qt, QRectF, QSize, QEvent


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.image_label = QLabel(self)
        self.mouse_pos_label = QLabel(self)
        self.mouse_pos_label.move(10, 10)
        self.image = QImage('image.jpg')
        screen = QApplication(sys.argv)
        screen_rect = app.desktop().screenGeometry()
        image_rect = QRectF(0, 0, self.image.width(), self.image.height())
        if image_rect.width() > screen_rect.width() or image_rect.height() > screen_rect.height():
            self.image = self.image.scaledToWidth(screen_rect.width(), Qt.SmoothTransformation)
            if self.image.height() > screen_rect.height():
                self.image = self.image.scaledToHeight(screen_rect.height(), Qt.SmoothTransformation)
        self.image_label.setPixmap(QPixmap.fromImage(self.image))
        self.image_label.mouseMoveEvent = self.mouse_move_event
        self.setMouseTracking(True)

    def resizeEvent(self, event: QResizeEvent):
        self.image_label.resize(event.size())

    def mouse_move_event(self, event):
        x = event.x()
        y = event.y()
        color = self.image.pixelColor(x, y)
        r = color.red()
        g = color.green()
        b = color.blue()
        self.mouse_pos_label.setText(f"Mouse position: ({x}, {y}) RGB: ({r}, {g}, {b})")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Image Viewer')
        self.viewer_widget = QWidget(self)
        self.viewer_layout = QVBoxLayout(self.viewer_widget)
        self.image_viewer = ImageViewer()
        self.viewer_layout.addWidget(self.image_viewer)
        self.setFixedSize(self.image_viewer.image.size())
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
