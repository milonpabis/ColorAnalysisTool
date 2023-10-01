from UI.StartWindow import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from PySide6.QtCore import Qt, QSize, Signal, QTimer
from PySide6.QtGui import QIcon, QFont, QColor, QPixmap, QImage
from UI.MainWindow import Ui_MainWindow
from analyser import Analyser, ThreadRun


class StartWindow(QWidget, Ui_Form):

    start_analysis = Signal()

    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("CAT")
        self.bt_start.pressed.connect(self.analyse_button)
        self.main = main
        self.change_photo()

    def analyse_button(self):
        pixmap = self.l_photo.pixmap()
        analyser = ThreadRun(pixmap)
        analyser.run()
        result = analyser.result

        self.main.show()
        self.main.get_winners(result[0], result[50000], result[125000], result[300000], result[630000])
        self.hide()


    def change_photo(self):
        image = QImage("testimage.jpg")
        h_i, w_i = image.height(), image.width()
        w = 200 / h_i * w_i
        pixmap = QPixmap().fromImage(image)
        self.l_photo.setPixmap(pixmap)
        self.l_photo.setFixedSize(QSize(w, 200))
        self.l_photo.setScaledContents(True)



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_win = StartWindow(self)
        self.start_win.show()
        self.top_colors = []

    def get_winners(self, first: QColor, second: QColor, third: QColor, fourth: QColor, fifth: QColor):
        r1, g1, b1, _ = first.getRgb()
        self.l_first_color.setStyleSheet(f"background-color: rgb({r1}, {g1}, {b1});"
                                         f"border: 2px solid black;")
        self.l_first_hex.setText(first.name())

        r2, g2, b2, _ = second.getRgb()
        self.l_second_color.setStyleSheet(f"background-color: rgb({r2}, {g2}, {b2});"
                                         f"border: 2px solid black;")
        self.l_second_hex.setText(second.name())

        r3, g3, b3, _ = third.getRgb()
        self.l_third_color.setStyleSheet(f"background-color: rgb({r3}, {g3}, {b3});"
                                         f"border: 2px solid black;")
        self.l_third_hex.setText(third.name())

        r4, g4, b4, _ = fourth.getRgb()
        self.l_fourth_color.setStyleSheet(f"background-color: rgb({r4}, {g4}, {b4});"
                                         f"border: 2px solid black;")
        self.l_fourth_hex.setText(fourth.name())

        r5, g5, b5, _ = fifth.getRgb()
        self.l_fifth_color.setStyleSheet(f"background-color: rgb({r5}, {g5}, {b5});"
                                         f"border: 2px solid black;")
        self.l_fifth_hex.setText(fifth.name())










