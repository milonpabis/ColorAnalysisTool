# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 400)
        Form.setMinimumSize(QSize(600, 400))
        Form.setMaximumSize(QSize(600, 400))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(170, 0, 255);\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.head = QFrame(Form)
        self.head.setObjectName(u"head")
        self.head.setMinimumSize(QSize(600, 80))
        self.head.setMaximumSize(QSize(600, 80))
        self.head.setStyleSheet(u"border-top: 2px solid black;\n"
"border-right: 2px solid black;\n"
"border-left: 2px solid black;")
        self.head.setFrameShape(QFrame.NoFrame)
        self.head.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.head)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.l_title = QLabel(self.head)
        self.l_title.setObjectName(u"l_title")
        self.l_title.setMaximumSize(QSize(300, 50))
        font = QFont()
        font.setFamilies([u"Lato Semibold"])
        font.setPointSize(14)
        font.setBold(True)
        self.l_title.setFont(font)
        self.l_title.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border: 2px solid black;\n"
"")
        self.l_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.l_title)


        self.verticalLayout.addWidget(self.head)

        self.body = QFrame(Form)
        self.body.setObjectName(u"body")
        self.body.setFrameShape(QFrame.NoFrame)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.body)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 0))
        self.frame.setMaximumSize(QSize(100, 16777215))
        self.frame.setStyleSheet(u"\n"
"border-left: 2px solid black;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.body)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(500, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(5)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.l_photo = QLabel(self.frame_2)
        self.l_photo.setObjectName(u"l_photo")
        self.l_photo.setMaximumSize(QSize(350, 200))
        self.l_photo.setAcceptDrops(False)
        self.l_photo.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.l_photo.setFrameShape(QFrame.Panel)
        self.l_photo.setFrameShadow(QFrame.Raised)
        self.l_photo.setLineWidth(5)
        self.l_photo.setMidLineWidth(0)
        self.l_photo.setPixmap(QPixmap(u"UI/images/insert_image.png"))
        self.l_photo.setScaledContents(False)
        self.l_photo.setAlignment(Qt.AlignCenter)
        self.l_photo.setWordWrap(False)
        self.l_photo.setMargin(0)
        self.l_photo.setIndent(-1)
        self.l_photo.setOpenExternalLinks(False)

        self.horizontalLayout_4.addWidget(self.l_photo)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.body)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setMaximumSize(QSize(100, 16777215))
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet(u"border-right: 2px solid black;")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.body)

        self.foot = QFrame(Form)
        self.foot.setObjectName(u"foot")
        self.foot.setMinimumSize(QSize(600, 80))
        self.foot.setMaximumSize(QSize(600, 80))
        self.foot.setAutoFillBackground(False)
        self.foot.setStyleSheet(u"border-bottom: 2px solid black;\n"
"border-right: 2px solid black;\n"
"border-left: 2px solid black;")
        self.foot.setFrameShape(QFrame.NoFrame)
        self.foot.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.foot)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bt_start = QPushButton(self.foot)
        self.bt_start.setObjectName(u"bt_start")
        self.bt_start.setMaximumSize(QSize(120, 25))
        font1 = QFont()
        font1.setFamilies([u"Lato Semibold"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.bt_start.setFont(font1)
        self.bt_start.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"")

        self.horizontalLayout_2.addWidget(self.bt_start)


        self.verticalLayout.addWidget(self.foot)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.l_title.setText(QCoreApplication.translate("Form", u"COLOR ANALYSIS TOOL", None))
        self.l_photo.setText("")
        self.bt_start.setText(QCoreApplication.translate("Form", u"START ANALYSIS", None))
    # retranslateUi

