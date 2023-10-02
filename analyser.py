from PySide6.QtCore import Qt, QSize, Signal, QTimer, QPoint, QThread
from PySide6.QtGui import QIcon, QFont, QColor, QPixmap, QImage
from PySide6.QtWidgets import QLabel
import math

DISTANCE = 90
DISTANCE_LVL1 = 10
DISTANCE_LVL2 = 20
DISTANCE_LVL3 = 30
DISTANCE_LVL4 = 40
DISTANCE_LVL5 = 50
DISTANCE_LVL6 = 60
DISTANCE_LVL7 = 70
DISTANCE_LVL8 = 80
DISTANCE_LVL9 = 90

# scheme = {'counter': 0, 'colors': [{'first': (r, g, b, h), 'rest': [], 'counter': 0},
# #                {'first': (r, g, b, h), 'rest': [{'first': (r,g,b,h), 'counter': 0},
#                                                   {'first': (r,g,b,h), 'counter': 0}], 'counter': 0}] }


class Analyser:

    def __init__(self, pixmap: QPixmap):
        self.pixmap = pixmap
        self.original_height = self.pixmap.height()
        self.original_width = self.pixmap.width()
        self.image = self.pixmap.toImage()
        self.colors = []
        self.groups = {'counter': 0, 'colors': []}




    def retrieve_colors(self):          # change not to QColor
        for i in range(self.original_width):
            for j in range(self.original_height):
                color = self.image.pixelColor(QPoint(i, j))
                self.compare_colors(color)
            #print(i, j)
        print(self.groups)
        return self.find_top_interior()



    def compare_colors(self, color: QColor):
        r1, g1, b1, _ = color.getRgb()
        h1 = color.name()
        gate = False
        for i in range(len(self.groups['colors'])):
            r2, g2, b2, _ = self.groups['colors'][i]['first']
            distance = self.calc_distance((r1, g1, b1), (r2, g2, b2))
            if distance <= DISTANCE:
                self.groups['colors'][i]['rest'].append((r1, g1, b1, h1))
                self.groups['colors'][i]['counter'] += 1
                gate = True
                break

        if not gate:
            self.groups['colors'].append({'first': (r1, g1, b1, h1), 'rest': []})
            self.groups['colors'][self.groups['counter']]['counter'] = 1
            self.groups["counter"] += 1


    def find_top_interior(self):
        top_5 = []
        for i in self.groups['colors']:
            temp_tops = [{'first': None, 'counter': 0} for _ in range(10)]
            try:
                first = i['rest'][0]
            except IndexError:
                continue
            r1, g1, b1, h1 = first
            for color in i['rest'][1:]:
                r2, g2, b2, h2 = color
                distance = self.calc_distance((r1, g1, b1), (r2, g2, b2))
                if distance <= DISTANCE_LVL1:
                    temp_tops[0]['first'] = color
                    temp_tops[0]['counter'] += 1
                elif distance <= DISTANCE_LVL2:
                    temp_tops[1]['first'] = color
                    temp_tops[1]['counter'] += 1
                elif distance <= DISTANCE_LVL3:
                    temp_tops[2]['first'] = color
                    temp_tops[2]['counter'] += 1
                elif distance <= DISTANCE_LVL4:
                    temp_tops[3]['first'] = color
                    temp_tops[3]['counter'] += 1
                elif distance <= DISTANCE_LVL5:
                    temp_tops[4]['first'] = color
                    temp_tops[4]['counter'] += 1
                elif distance <= DISTANCE_LVL6:
                    temp_tops[5]['first'] = color
                    temp_tops[5]['counter'] += 1
                elif distance <= DISTANCE_LVL7:
                    temp_tops[6]['first'] = color
                    temp_tops[6]['counter'] += 1
                elif distance <= DISTANCE_LVL8:
                    temp_tops[7]['first'] = color
                    temp_tops[7]['counter'] += 1
                elif distance <= DISTANCE_LVL9:
                    temp_tops[8]['first'] = color
                    temp_tops[8]['counter'] += 1
                else:
                    temp_tops[9]['first'] = color
                    temp_tops[9]['counter'] += 1

            temp_tops = self.sort_interior(temp_tops, 1)
            top_5.append(temp_tops[0])
        top_5 = self.find_top(top_5, 5)
        print("TOP5:")
        print(top_5)
        return top_5






    def calc_distance(self, c1: tuple, c2: tuple):
        r1, g1, b1 = c1
        r2, g2, b2 = c2
        return math.sqrt((r2 - r1)**2 + (g2 - g1)**2 + (b2 - b1)**2)


    def find_top(self, data, top):

        result = sorted(data, key=lambda x: x['counter'], reverse=True)
        to_return = [item['first'] for item in result[:top]]
        return to_return

    def sort_interior(self, data, top):

        result = sorted(data, key=lambda x: x['counter'], reverse=True)
        to_return = [item for item in result[:top]]

        return to_return






class ThreadRun(QThread):

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.result = []

    def run(self):
        self.result = Analyser(self.image).retrieve_colors()



