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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(805, 415)
        self.horizontalLayout = QHBoxLayout(Main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Main)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);border: 0;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border: 0;")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
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
        self.pushButton.setStyleSheet(u"text-align: left;\n"
"color: #333;")
        icon = QIcon()
        icon.addFile(u":/Icons/images/icons/icons8-import_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"text-align: left; color: #333; cursor: pointer;")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/images/icons/icons8-record_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"text-align: left; color: #333; cursor: pointer;")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/images/icons/icons8-run-command_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"text-align: left; color: #333; cursor: pointer;")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/images/icons/icons8-export-pdf_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"text-align: left; color: #333; cursor: pointer;")
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
        self.verticalLayout_3.setSpacing(0)
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
"border-radius: 8px;")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setLineWidth(0)

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
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);border: 0;")
        self.frame_2.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(400, 16777215))
        self.frame_3.setStyleSheet(u"background-color: #333333;border: 0;")
        self.frame_3.setFrameShape(QFrame.NoFrame)

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
    # retranslateUi

