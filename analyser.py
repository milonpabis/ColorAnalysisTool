from PySide6.QtCore import Qt, QSize, Signal, QTimer, QPoint, QThread
from PySide6.QtGui import QIcon, QFont, QColor, QPixmap, QImage
from PySide6.QtWidgets import QLabel


class Analyser:

    def __init__(self, pixmap: QPixmap):
        self.pixmap = pixmap
        self.original_height = self.pixmap.height()
        self.original_width = self.pixmap.width()
        self.image = self.pixmap.toImage()
        self.colors = []


    def retrieve_colors(self):
        for i in range(self.original_width):
            for j in range(self.original_height):
                color = self.image.pixelColor(QPoint(i, j))
                self.colors.append(color)
        return self.colors



class ThreadRun(QThread):

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.result = []

    def run(self):
        self.result = Analyser(self.image).retrieve_colors()



