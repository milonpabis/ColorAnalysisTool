from PySide6.QtCore import Qt, QSize, Signal, QTimer, QPoint, QThread
from PySide6.QtGui import QIcon, QFont, QColor, QPixmap, QImage
from PySide6.QtWidgets import QLabel
import math

DISTANCE = 100

# scheme = {'counter': 0, 'colors': [{'first': QColor, 'rest': [Qcolor], 'counter': 0},
# #                                  {'first': QColor, 'rest': [QColor], 'counter': 0}] }


class Analyser:

    def __init__(self, pixmap: QPixmap):
        self.pixmap = pixmap
        self.original_height = self.pixmap.height()
        self.original_width = self.pixmap.width()
        self.image = self.pixmap.toImage()
        self.colors = []
        self.groups = {'counter': 0, 'colors': []}
        #print(self.calc_distance(QColor(235, 64, 52), QColor(135, 19, 11)))
        #print(self.calc_distance(QColor(235, 64, 52), QColor(222, 21, 7)))
        #print(self.calc_distance(QColor(235, 64, 52), QColor(30, 194, 21)))
        #print(self.calc_distance(QColor(235, 64, 52), QColor(150, 20, 59)))
        #print(self.calc_distance(QColor(235, 64, 52), QColor(150, 20, 137)))
        #print(self.calc_distance(QColor(150, 20, 59), QColor(150, 20, 137)))
        #print(self.calc_distance(QColor(255, 255, 255), QColor(0, 0, 0)))




    def retrieve_colors(self):
        for i in range(self.original_width):
            for j in range(self.original_height):
                color = self.image.pixelColor(QPoint(i, j))
                self.compare_colors(color)
            print(i, j)
        print(self.groups)
        return self.find_top()
    # ->>>   change image size to make it work faster ( 100 x 100 )


    def compare_colors(self, color: QColor):
        r1, g1, b1, _ = color.getRgb()
        h1 = color.name()
        gate = False
        for i in range(len(self.groups['colors'])):
            r2, g2, b2, _ = self.groups['colors'][i]['first']
            distance = self.calc_distance((r1, g1, b1), (r2, g2, b2))
            if distance <= DISTANCE:
                #self.groups['colors'][i]['rest'].append((r1, g1, b1, h1))
                self.groups['colors'][i]['counter'] += 1
                gate = True
                break
        if not gate:
            self.groups['colors'].append({'first': (r1, g1, b1, h1), 'rest': []})
            self.groups['colors'][self.groups['counter']]['counter'] = 1
            self.groups["counter"] += 1



    def calc_distance(self, c1: tuple, c2: tuple):
        r1, g1, b1 = c1
        r2, g2, b2 = c2
        return math.sqrt((r2 - r1)**2 + (g2 - g1)**2 + (b2 - b1)**2)


    def find_top(self):
        result = sorted(self.groups['colors'], key=lambda x: x['counter'], reverse=True)
        to_return = [item['first'] for item in result[:5]]

        return to_return






class ThreadRun(QThread):

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.result = []

    def run(self):
        self.result = Analyser(self.image).retrieve_colors()



