# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 244, 251);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.centralwidget.setMaximumSize(QSize(800, 600))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(700, 550))
        self.groupBox.setMaximumSize(QSize(16777215, 550))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(18)
        font.setBold(False)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(255, 233, 252);")
        self.groupBox.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(150, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 34, -1, -1)
        self.l_first_hash = QLabel(self.frame_6)
        self.l_first_hash.setObjectName(u"l_first_hash")
        self.l_first_hash.setMaximumSize(QSize(100, 110))
        font1 = QFont()
        font1.setFamilies([u"Lato Semibold"])
        font1.setPointSize(28)
        font1.setBold(True)
        self.l_first_hash.setFont(font1)
        self.l_first_hash.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(230, 187, 255, 255), stop:0.883333 rgba(139, 69, 200, 255));\n"
"color: rgb(244, 210, 255);\n"
"border-radius: 10px;")
        self.l_first_hash.setFrameShape(QFrame.WinPanel)
        self.l_first_hash.setFrameShadow(QFrame.Raised)
        self.l_first_hash.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_6.addWidget(self.l_first_hash)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(140, 150))
        self.frame_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(230, 187, 255, 255), stop:0.883333 rgba(139, 69, 200, 255));\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QFrame.WinPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.l_first_color = QLabel(self.frame_7)
        self.l_first_color.setObjectName(u"l_first_color")
        self.l_first_color.setMinimumSize(QSize(100, 100))
        self.l_first_color.setMaximumSize(QSize(100, 100))
        self.l_first_color.setStyleSheet(u"background-color: rgb(255, 0, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"")
        self.l_first_color.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.l_first_color)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, -1, 34)
        self.l_first_hex = QLabel(self.frame_8)
        self.l_first_hex.setObjectName(u"l_first_hex")
        self.l_first_hex.setMaximumSize(QSize(100, 110))
        font2 = QFont()
        font2.setFamilies([u"Lato Semibold"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.l_first_hex.setFont(font2)
        self.l_first_hex.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(139, 69, 200, 255), stop:0.883333 rgba(230, 187, 255, 255));\n"
"color: rgb(244, 210, 255);\n"
"border-radius: 10px;\n"
"")
        self.l_first_hex.setFrameShape(QFrame.WinPanel)
        self.l_first_hex.setFrameShadow(QFrame.Raised)
        self.l_first_hex.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.l_first_hex.setMargin(5)

        self.horizontalLayout_13.addWidget(self.l_first_hex)


        self.verticalLayout.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(135, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(125, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 56, -1, -1)
        self.l_second_hash = QLabel(self.frame_9)
        self.l_second_hash.setObjectName(u"l_second_hash")
        self.l_second_hash.setMinimumSize(QSize(80, 90))
        self.l_second_hash.setMaximumSize(QSize(85, 95))
        font3 = QFont()
        font3.setFamilies([u"Lato Semibold"])
        font3.setPointSize(24)
        font3.setBold(True)
        self.l_second_hash.setFont(font3)
        self.l_second_hash.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(230, 187, 255, 255), stop:0.883333 rgba(139, 69, 200, 255));\n"
"color: rgb(244, 210, 255);\n"
"border-radius: 10px;")
        self.l_second_hash.setFrameShape(QFrame.WinPanel)
        self.l_second_hash.setFrameShadow(QFrame.Raised)
        self.l_second_hash.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_7.addWidget(self.l_second_hash)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(125, 135))
        self.frame_10.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(230, 187, 255, 255), stop:0.883333 rgba(139, 69, 200, 255));\n"
"border-radius: 10px;")
        self.frame_10.setFrameShape(QFrame.WinPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.l_second_color = QLabel(self.frame_10)
        self.l_second_color.setObjectName(u"l_second_color")
        self.l_second_color.setMinimumSize(QSize(90, 90))
        self.l_second_color.setMaximumSize(QSize(90, 90))
        self.l_second_color.setStyleSheet(u"background-color: rgb(255, 0, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"")
        self.l_second_color.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.l_second_color)


        self.verticalLayout_2.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(125, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, -1, 54)
        self.l_second_hex = QLabel(self.frame_11)
        self.l_second_hex.setObjectName(u"l_second_hex")
        self.l_second_hex.setMaximumSize(QSize(85, 95))
        font4 = QFont()
        font4.setFamilies([u"Lato Semibold"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.l_second_hex.setFont(font4)
        self.l_second_hex.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(139, 69, 200, 255), stop:0.883333 rgba(230, 187, 255, 255));\n"
"color: rgb(244, 210, 255);\n"
"border-radius: 10px;\n"
"")
        self.l_second_hex.setFrameShape(QFrame.WinPanel)
        self.l_second_hex.setFrameShadow(QFrame.Raised)
        self.l_second_hex.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.l_second_hex.setMargin(5)

        self.horizontalLayout_14.addWidget(self.l_second_hex)


        self.verticalLayout_2.addWidget(self.frame_11)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(120, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(110, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 78, -1, -1)
        self.l_third_hash = QLabel(self.frame_12)
        self.l_third_hash.setObjectName(u"l_third_hash")
        self.l_third_hash.setMaximumSize(QSize(70, 80))
        font5 = QFont()
        font5.setFamilies([u"Lato Semibold"])
        font5.setPointSize(20)
        font5.setBold(True)
        self.l_third_hash.setFont(font5)
        self.l_third_hash.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(230, 187, 255, 255), stop:0.883333 rgba(139, 69, 200, 255));\n"
"color: rgb(244, 210, 255);\n"
"border-radius: 10px;")
        self.l_third_hash.setFrameShape(QFrame.WinPanel)
        self.l_third_hash.setFrameShadow(QFrame.Raised)
        self.l_third_hash.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_5.addWidget(self.l_third_hash)


        self.verticalLayout_3.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(110, 120))
        self.frame_13.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(230, 187, 255, 255), stop:0.883333 rgba(139, 69, 200, 255));\n"
"border-radius: 10px;")
        self.frame_13.setFrameShape(QFrame.WinPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.l_third_color = QLabel(self.frame_13)
        self.l_third_color.setObjectName(u"l_third_color")
        self.l_third_color.setMinimumSize(QSize(80, 80))
        self.l_third_color.setMaximumSize(QSize(80, 80))
        self.l_third_color.setStyleSheet(u"background-color: rgb(255, 0, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"")
        self.l_third_color.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.l_third_color)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(110, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 77)
        self.l_third_hex = QLabel(self.frame_14)
        self.l_third_hex.setObjectName(u"l_third_hex")
        self.l_third_hex.setMaximumSize(QSize(70, 80))
        font6 = QFont()
        font6.setFamilies([u"Lato Semibold"])
        font6.setPointSize(11)
        font6.setBold(True)
        self.l_third_hex.setFont(font6)
        self.l_third_hex.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(139, 69, 200, 255), stop:0.883333 rgba(230, 187, 255, 255));\n"
"color: rgb(244, 210, 255);\n"
"border-radius: 10px;\n"
"")
        self.l_third_hex.setFrameShape(QFrame.WinPanel)
        self.l_third_hex.setFrameShadow(QFrame.Raised)
        self.l_third_hex.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.l_third_hex.setMargin(5)

        self.horizontalLayout_15.addWidget(self.l_third_hex)


        self.verticalLayout_3.addWidget(self.frame_14)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(105, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_15 = QFrame(self.frame_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(95, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 101, -1, -1)
        self.l_fourth_hash = QLabel(self.frame_15)
        self.l_fourth_hash.setObjectName(u"l_fourth_hash")
        self.l_fourth_hash.setMaximumSize(QSize(55, 65))
        self.l_fourth_hash.setFont(font2)
        self.l_fourth_hash.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(230, 187, 255, 255), stop:0.883333 rgba(139, 69, 200, 255));\n"
"color: rgb(244, 210, 255);\n"
"border-radius: 10px;")
        self.l_fourth_hash.setFrameShape(QFrame.WinPanel)
        self.l_fourth_hash.setFrameShadow(QFrame.Raised)
        self.l_fourth_hash.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_4.addWidget(self.l_fourth_hash)


        self.verticalLayout_4.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(95, 105))
        self.frame_16.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(230, 187, 255, 255), stop:0.883333 rgba(139, 69, 200, 255));\n"
"border-radius: 10px;")
        self.frame_16.setFrameShape(QFrame.WinPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.l_fourth_color = QLabel(self.frame_16)
        self.l_fourth_color.setObjectName(u"l_fourth_color")
        self.l_fourth_color.setMinimumSize(QSize(70, 70))
        self.l_fourth_color.setMaximumSize(QSize(70, 70))
        self.l_fourth_color.setStyleSheet(u"background-color: rgb(255, 0, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"")
        self.l_fourth_color.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.l_fourth_color)


        self.verticalLayout_4.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(95, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 99)
        self.l_fourth_hex = QLabel(self.frame_17)
        self.l_fourth_hex.setObjectName(u"l_fourth_hex")
        self.l_fourth_hex.setMaximumSize(QSize(55, 65))
        font7 = QFont()
        font7.setFamilies([u"Lato Semibold"])
        font7.setPointSize(8)
        font7.setBold(True)
        self.l_fourth_hex.setFont(font7)
        self.l_fourth_hex.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(139, 69, 200, 255), stop:0.883333 rgba(230, 187, 255, 255));\n"
"color: rgb(244, 210, 255);\n"
"border-radius: 10px;\n"
"")
        self.l_fourth_hex.setFrameShape(QFrame.WinPanel)
        self.l_fourth_hex.setFrameShadow(QFrame.Raised)
        self.l_fourth_hex.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.l_fourth_hex.setMargin(5)

        self.horizontalLayout_16.addWidget(self.l_fourth_hex)


        self.verticalLayout_4.addWidget(self.frame_17)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.groupBox)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(100, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_18 = QFrame(self.frame_5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(80, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 123, -1, -1)
        self.l_fifth_hash = QLabel(self.frame_18)
        self.l_fifth_hash.setObjectName(u"l_fifth_hash")
        self.l_fifth_hash.setMaximumSize(QSize(45, 50))
        font8 = QFont()
        font8.setFamilies([u"Lato Semibold"])
        font8.setPointSize(12)
        font8.setBold(True)
        self.l_fifth_hash.setFont(font8)
        self.l_fifth_hash.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(230, 187, 255, 255), stop:0.883333 rgba(139, 69, 200, 255));\n"
"color: rgb(244, 210, 255);\n"
"border-radius: 10px;")
        self.l_fifth_hash.setFrameShape(QFrame.WinPanel)
        self.l_fifth_hash.setFrameShadow(QFrame.Raised)
        self.l_fifth_hash.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_3.addWidget(self.l_fifth_hash)


        self.verticalLayout_5.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(80, 90))
        self.frame_19.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(230, 187, 255, 255), stop:0.883333 rgba(139, 69, 200, 255));\n"
"border-radius: 10px;")
        self.frame_19.setFrameShape(QFrame.WinPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.l_fifth_color = QLabel(self.frame_19)
        self.l_fifth_color.setObjectName(u"l_fifth_color")
        self.l_fifth_color.setMinimumSize(QSize(60, 60))
        self.l_fifth_color.setMaximumSize(QSize(60, 60))
        self.l_fifth_color.setStyleSheet(u"background-color: rgb(255, 0, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"")
        self.l_fifth_color.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.l_fifth_color)


        self.verticalLayout_5.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(80, 16777215))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, -1, -1, 122)
        self.l_fifth_hex = QLabel(self.frame_20)
        self.l_fifth_hex.setObjectName(u"l_fifth_hex")
        self.l_fifth_hex.setMaximumSize(QSize(45, 50))
        font9 = QFont()
        font9.setFamilies([u"Lato Semibold"])
        font9.setPointSize(6)
        font9.setBold(True)
        self.l_fifth_hex.setFont(font9)
        self.l_fifth_hex.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(139, 69, 200, 255), stop:0.883333 rgba(230, 187, 255, 255));\n"
"color: rgb(244, 210, 255);\n"
"border-radius: 10px;\n"
"")
        self.l_fifth_hex.setFrameShape(QFrame.WinPanel)
        self.l_fifth_hex.setFrameShadow(QFrame.Raised)
        self.l_fifth_hex.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.l_fifth_hex.setMargin(5)

        self.horizontalLayout_17.addWidget(self.l_fifth_hex)


        self.verticalLayout_5.addWidget(self.frame_20)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"RESULTS", None))
        self.l_first_hash.setText(QCoreApplication.translate("MainWindow", u"#1", None))
        self.l_first_color.setText("")
        self.l_first_hex.setText(QCoreApplication.translate("MainWindow", u"#000000", None))
        self.l_second_hash.setText(QCoreApplication.translate("MainWindow", u"#2", None))
        self.l_second_color.setText("")
        self.l_second_hex.setText(QCoreApplication.translate("MainWindow", u"#000000", None))
        self.l_third_hash.setText(QCoreApplication.translate("MainWindow", u"#3", None))
        self.l_third_color.setText("")
        self.l_third_hex.setText(QCoreApplication.translate("MainWindow", u"#000000", None))
        self.l_fourth_hash.setText(QCoreApplication.translate("MainWindow", u"#4", None))
        self.l_fourth_color.setText("")
        self.l_fourth_hex.setText(QCoreApplication.translate("MainWindow", u"#000000", None))
        self.l_fifth_hash.setText(QCoreApplication.translate("MainWindow", u"#5", None))
        self.l_fifth_color.setText("")
        self.l_fifth_hex.setText(QCoreApplication.translate("MainWindow", u"#000000", None))
    # retranslateUi

