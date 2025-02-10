# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(901, 619)
        self.horizontalLayout = QHBoxLayout(Main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Main)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);border: 0;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 200))
        self.frame_4.setStyleSheet(u"border: 0;")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 30))
        self.frame_6.setStyleSheet(u"border: 0;")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #4B4B4B;\n"
"font-size: 20pt;")
        self.label.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"border: 0;")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setKerning(False)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"text-align: left; color: #333;")
        icon = QIcon()
        icon.addFile(u":/Icons/images/icons/icons8-import_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"text-align: left; color: #333;")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/images/icons/icons8-record_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"text-align: left; color: #333;")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/images/icons/icons8-run-command_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"text-align: left; color: #333;")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/images/icons/icons8-export-pdf_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"text-align: left; color: #333;")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/images/icons/icons8-setting_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.pushButton_5)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border: 0;")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 30))
        self.frame_9.setStyleSheet(u"border: 0;")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #4B4B4B;\n"
"font-size: 20pt;")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: #D9D9D9;\n"
"border-radius: 8px; padding-top: 1px;")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frame_8)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_8)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 174, 397))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_10 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 70))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 0, 0, 0)
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: #333;")

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setItalic(False)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: #858585;")

        self.verticalLayout_6.addWidget(self.label_4)


        self.verticalLayout_8.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 70))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 0, 0, 0)
        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: #333;")

        self.verticalLayout_7.addWidget(self.label_6)

        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setFamilies([u"Poppins"])
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: #858585;")

        self.verticalLayout_7.addWidget(self.label_5)


        self.verticalLayout_8.addWidget(self.frame_11)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 0, 0, 0)
        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color: #333;")

        self.verticalLayout_9.addWidget(self.label_9)

        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")
        font5 = QFont()
        font5.setFamilies([u"Poppins"])
        font5.setBold(False)
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: #858585;")

        self.verticalLayout_9.addWidget(self.label_8)


        self.verticalLayout_8.addWidget(self.frame_13)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame)

        self.line = QFrame(Main)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.frame_2 = QFrame(Main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(400, 0))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);border: 0;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_14 = QVBoxLayout(self.frame_2)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 65))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_15)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.frame_23.setStyleSheet(u"background-color: #2B2B2B;\n"
"border-radius: 10px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(30, 30))
        self.frame_25.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_25)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_25)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/images/icons/icons8-audiomaster_red.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon5)

        self.verticalLayout_15.addWidget(self.pushButton_6)


        self.horizontalLayout_5.addWidget(self.frame_25)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_24)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_2)

        self.label_11 = QLabel(self.frame_24)
        self.label_11.setObjectName(u"label_11")
        font6 = QFont()
        font6.setFamilies([u"Poppins"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.label_11.setFont(font6)
        self.label_11.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_16.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_24)
        self.label_12.setObjectName(u"label_12")
        font7 = QFont()
        font7.setFamilies([u"Poppins"])
        font7.setPointSize(10)
        self.label_12.setFont(font7)
        self.label_12.setStyleSheet(u"color: #FFF;")
        self.label_12.setIndent(0)

        self.verticalLayout_16.addWidget(self.label_12)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addWidget(self.frame_24)


        self.horizontalLayout_4.addWidget(self.frame_23)

        self.frame_22 = QFrame(self.frame_15)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.frame_22.setStyleSheet(u"background-color: #2B2B2B;\n"
"border-radius: 10px;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_27 = QFrame(self.frame_22)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(30, 30))
        self.frame_27.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_27)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_27)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon5)

        self.verticalLayout_17.addWidget(self.pushButton_7)


        self.horizontalLayout_6.addWidget(self.frame_27)

        self.frame_26 = QFrame(self.frame_22)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_26)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(5, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_4)

        self.label_13 = QLabel(self.frame_26)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_20.addWidget(self.label_13)

        self.label_10 = QLabel(self.frame_26)
        self.label_10.setObjectName(u"label_10")
        font8 = QFont()
        font8.setFamilies([u"Poppins"])
        font8.setPointSize(11)
        self.label_10.setFont(font8)
        self.label_10.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_20.addWidget(self.label_10)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_5)


        self.horizontalLayout_6.addWidget(self.frame_26)


        self.horizontalLayout_4.addWidget(self.frame_22)

        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.frame_19.setStyleSheet(u"background-color: #2B2B2B;\n"
"border-radius: 10px;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_29 = QFrame(self.frame_19)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(30, 30))
        self.frame_29.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_29)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.frame_29)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setIcon(icon5)

        self.verticalLayout_18.addWidget(self.pushButton_8)


        self.horizontalLayout_7.addWidget(self.frame_29)

        self.frame_28 = QFrame(self.frame_19)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_28)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_6)

        self.label_14 = QLabel(self.frame_28)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font6)
        self.label_14.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_21.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_28)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font8)
        self.label_15.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_21.addWidget(self.label_15)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_7)


        self.horizontalLayout_7.addWidget(self.frame_28)


        self.horizontalLayout_4.addWidget(self.frame_19)

        self.frame_21 = QFrame(self.frame_15)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.frame_21.setStyleSheet(u"background-color: #2B2B2B;\n"
"border-radius: 10px;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_31 = QFrame(self.frame_21)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(30, 30))
        self.frame_31.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_31)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.frame_31)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setIcon(icon5)

        self.verticalLayout_19.addWidget(self.pushButton_9)


        self.horizontalLayout_8.addWidget(self.frame_31)

        self.frame_30 = QFrame(self.frame_21)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_30)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 0, 0, 0)
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_8)

        self.label_16 = QLabel(self.frame_30)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font6)
        self.label_16.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_22.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_30)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font8)
        self.label_17.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_22.addWidget(self.label_17)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_9)


        self.horizontalLayout_8.addWidget(self.frame_30)


        self.horizontalLayout_4.addWidget(self.frame_21)


        self.verticalLayout_14.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 160))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_16)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_16)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(16777215, 90))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 5, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_34)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_34)
        self.label_19.setObjectName(u"label_19")
        font9 = QFont()
        font9.setFamilies([u"Poppins"])
        font9.setPointSize(18)
        font9.setBold(True)
        self.label_19.setFont(font9)
        self.label_19.setStyleSheet(u"color: #000;")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_34)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font4)
        self.label_20.setStyleSheet(u"color: #858585;")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_20)


        self.horizontalLayout_9.addWidget(self.frame_34)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.verticalLayout_23.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_16)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(16777215, 70))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_10 = QPushButton(self.frame_33)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/images/icons/icons8-play_red.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon6)
        self.pushButton_10.setIconSize(QSize(35, 35))

        self.horizontalLayout_10.addWidget(self.pushButton_10)

        self.horizontalSlider = QSlider(self.frame_33)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #333;\n"
"height: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: #F00;\n"
"width: 10px;\n"
"height: 2px;\n"
"margin: -5px -1px;\n"
"border-radius: 5px;\n"
"border: 1px solid #FF3333;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #333;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: #FF0000;\n"
"}")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.horizontalSlider)

        self.label_22 = QLabel(self.frame_33)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"color: #000;")

        self.horizontalLayout_10.addWidget(self.label_22)


        self.verticalLayout_23.addWidget(self.frame_33)


        self.verticalLayout_14.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_17)
        self.verticalLayout_25.setSpacing(8)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.frame_17)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"background-color: #D9D9D9;\n"
"border-radius: 15px")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_35)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(12, 0, 12, 12)
        self.scrollArea_3 = QScrollArea(self.frame_35)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 352, 355))
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 12, 0, 0)
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_10)

        self.frame_37 = QFrame(self.scrollAreaWidgetContents)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"background-color: #575757;\n"
"border-radius: 10px;")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_37)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_27 = QLabel(self.frame_37)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"color: #FFF;")
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_31.addWidget(self.label_27)


        self.verticalLayout_27.addWidget(self.frame_37)

        self.frame_40 = QFrame(self.scrollAreaWidgetContents)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"background-color: #868686;\n"
"border-radius: 10px;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_40)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_26 = QLabel(self.frame_40)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_30.addWidget(self.label_26)


        self.verticalLayout_27.addWidget(self.frame_40)

        self.frame_39 = QFrame(self.scrollAreaWidgetContents)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"background-color: #575757;\n"
"border-radius: 10px;")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_39)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_25 = QLabel(self.frame_39)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"color: #FFF;")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_29.addWidget(self.label_25)


        self.verticalLayout_27.addWidget(self.frame_39)

        self.frame_38 = QFrame(self.scrollAreaWidgetContents)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"background-color: #868686;\n"
"border-radius: 10px;")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_38)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_24 = QLabel(self.frame_38)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_28.addWidget(self.label_24)


        self.verticalLayout_27.addWidget(self.frame_38)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_26.addWidget(self.scrollArea_3)


        self.verticalLayout_25.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_17)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(16777215, 50))
        self.frame_36.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: #333;\n"
"border-radius: 13px;\n"
"color: #000;\n"
"padding: 5px;")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.frame_36.setLineWidth(1)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.frame_36)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"border: None;")

        self.horizontalLayout_11.addWidget(self.textEdit)

        self.pushButton_11 = QPushButton(self.frame_36)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"border: none;")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/images/icons/icons8-send_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon7)
        self.pushButton_11.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.pushButton_11)


        self.verticalLayout_25.addWidget(self.frame_36)


        self.verticalLayout_14.addWidget(self.frame_17)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 0))
        self.frame_3.setMaximumSize(QSize(400, 16777215))
        self.frame_3.setStyleSheet(u"background-color: #333333;border: 0;")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(12, -1, -1, -1)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        font10 = QFont()
        font10.setPointSize(20)
        self.label_7.setFont(font10)
        self.label_7.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_5.addWidget(self.label_7)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: #D9D9D9;\n"
"border-radius: 12px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_12)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 10, -1, -1)
        self.scrollArea_2 = QScrollArea(self.frame_12)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 264, 537))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 0, 0)
        self.frame_14 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 70))
        self.frame_14.setStyleSheet(u"background-color: #0D0404;\n"
"border-radius: 10px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(10, 5, 5, 5)
        self.label_18 = QLabel(self.frame_14)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font5)
        self.label_18.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_11.addWidget(self.label_18)


        self.verticalLayout_10.addWidget(self.frame_14)

        self.frame_20 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 70))
        self.frame_20.setStyleSheet(u"background-color: #575757;\n"
"border-radius: 10px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_20)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 5, 5, 5)
        self.label_21 = QLabel(self.frame_20)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font5)
        self.label_21.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_12.addWidget(self.label_21)


        self.verticalLayout_10.addWidget(self.frame_20)

        self.frame_18 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background-color: #868686;\n"
"border-radius: 10px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_18)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 5, 5, 5)
        self.label_23 = QLabel(self.frame_18)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font5)
        self.label_23.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_13.addWidget(self.label_23)


        self.verticalLayout_10.addWidget(self.frame_18)

        self.verticalSpacer1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_12)


        self.horizontalLayout.addWidget(self.frame_3)


        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Audio AI", None))
        self.label.setText(QCoreApplication.translate("Main", u"MENU", None))
        self.pushButton.setText(QCoreApplication.translate("Main", u" Load", None))
        self.pushButton_3.setText(QCoreApplication.translate("Main", u" Record", None))
        self.pushButton_4.setText(QCoreApplication.translate("Main", u" Action", None))
        self.pushButton_2.setText(QCoreApplication.translate("Main", u" Export", None))
        self.pushButton_5.setText(QCoreApplication.translate("Main", u" Settings", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"RECORDINGS", None))
        self.label_3.setText(QCoreApplication.translate("Main", u"Bob Keating TIMA", None))
        self.label_4.setText(QCoreApplication.translate("Main", u"31/01/2025 10:55", None))
        self.label_6.setText(QCoreApplication.translate("Main", u"Bob Keating TIMA", None))
        self.label_5.setText(QCoreApplication.translate("Main", u"31/01/2025 10:55", None))
        self.label_9.setText(QCoreApplication.translate("Main", u"Bob Keating TIMA", None))
        self.label_8.setText(QCoreApplication.translate("Main", u"31/01/2025 10:55", None))
        self.pushButton_6.setText("")
        self.label_11.setText(QCoreApplication.translate("Main", u"Transcribe", None))
        self.label_12.setText(QCoreApplication.translate("Main", u"Whisper", None))
        self.pushButton_7.setText("")
        self.label_13.setText(QCoreApplication.translate("Main", u"Alignment", None))
        self.label_10.setText(QCoreApplication.translate("Main", u"Whisper", None))
        self.pushButton_8.setText("")
        self.label_14.setText(QCoreApplication.translate("Main", u"Diarization", None))
        self.label_15.setText(QCoreApplication.translate("Main", u"Whisper", None))
        self.pushButton_9.setText("")
        self.label_16.setText(QCoreApplication.translate("Main", u"RAG", None))
        self.label_17.setText(QCoreApplication.translate("Main", u"R3", None))
        self.label_19.setText(QCoreApplication.translate("Main", u"Bob Keating TIMA", None))
        self.label_20.setText(QCoreApplication.translate("Main", u"31/01/2025 10:55", None))
        self.pushButton_10.setText("")
        self.label_22.setText(QCoreApplication.translate("Main", u"4:18", None))
        self.label_27.setText(QCoreApplication.translate("Main", u"List all Past Medical History of Bob!", None))
        self.label_26.setText(QCoreApplication.translate("Main", u"asdasdasd\n"
"sdasdasd\n"
"asdasdasd", None))
        self.label_25.setText(QCoreApplication.translate("Main", u"List all Past Medical History of Bob!", None))
        self.label_24.setText(QCoreApplication.translate("Main", u"asdasdasd\n"
"sdasdasd\n"
"asdasdasd", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Main", u"Ask anything about the audio content...", None))
        self.pushButton_11.setText("")
        self.label_7.setText(QCoreApplication.translate("Main", u"Transcription", None))
        self.label_18.setText(QCoreApplication.translate("Main", u"asdasdasd\n"
"sdasdasd\n"
"asdasdasd", None))
        self.label_21.setText(QCoreApplication.translate("Main", u"Bob Keating TIMA", None))
        self.label_23.setText(QCoreApplication.translate("Main", u"asdasdasd\n"
"sdasdasd\n"
"asdasdasd", None))
    # retranslateUi

