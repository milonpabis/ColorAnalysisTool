from UI.StartWindow import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from PySide6.QtCore import Qt, QSize, Signal, QTimer
from PySide6.QtGui import QIcon, QFont, QColor, QPixmap, QImage
from UI.MainWindow import Ui_MainWindow


class StartWindow(QWidget, Ui_Form):

    start_analysis = Signal()

    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("CAT")
        self.bt_start.pressed.connect(self.analyse_button)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout)

        self.main = main

    def analyse_button(self):
        image = QImage("testimage.jpg")
        h_i, w_i = image.height(), image.width()
        w = self.l_photo.height() / h_i * w_i
        pixmap = QPixmap().fromImage(image)
        self.l_photo.setPixmap(pixmap)
        self.l_photo.setFixedSize(QSize(w, self.l_photo.height()))
        self.l_photo.setScaledContents(True)
        self.timer.start(3000)

    def timeout(self):
        self.timer.stop()
        self.main.show()
        self.hide()









class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_win = StartWindow(self)
        self.start_win.show()





