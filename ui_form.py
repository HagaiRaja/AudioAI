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
        self.left_container = QFrame(Main)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMinimumSize(QSize(200, 0))
        self.left_container.setMaximumSize(QSize(300, 16777215))
        self.left_container.setStyleSheet(u"background-color: rgb(255, 255, 255);border: 0;")
        self.left_container.setFrameShape(QFrame.NoFrame)
        self.left_container.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.left_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.menu_container = QFrame(self.left_container)
        self.menu_container.setObjectName(u"menu_container")
        self.menu_container.setMaximumSize(QSize(16777215, 200))
        self.menu_container.setStyleSheet(u"border: 0;")
        self.menu_container.setFrameShape(QFrame.NoFrame)
        self.menu_container.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.menu_container)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_container_label = QFrame(self.menu_container)
        self.menu_container_label.setObjectName(u"menu_container_label")
        self.menu_container_label.setMaximumSize(QSize(16777215, 30))
        self.menu_container_label.setStyleSheet(u"border: 0;")
        self.menu_container_label.setFrameShape(QFrame.NoFrame)
        self.menu_container_label.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.menu_container_label)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.menu_label = QLabel(self.menu_container_label)
        self.menu_label.setObjectName(u"menu_label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.menu_label.setFont(font)
        self.menu_label.setStyleSheet(u"color: #4B4B4B;\n"
"font-size: 20pt;")
        self.menu_label.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.menu_label)


        self.verticalLayout_2.addWidget(self.menu_container_label)

        self.menu_container_option = QFrame(self.menu_container)
        self.menu_container_option.setObjectName(u"menu_container_option")
        self.menu_container_option.setStyleSheet(u"border: 0;")
        self.menu_container_option.setFrameShape(QFrame.NoFrame)
        self.menu_container_option.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.menu_container_option)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu_import_button = QPushButton(self.menu_container_option)
        self.menu_import_button.setObjectName(u"menu_import_button")
        font1 = QFont()
        font1.setKerning(False)
        self.menu_import_button.setFont(font1)
        self.menu_import_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menu_import_button.setStyleSheet(u"text-align: left; color: #333;")
        icon = QIcon()
        icon.addFile(u":/Icons/images/icons/icons8-import_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_import_button.setIcon(icon)
        self.menu_import_button.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.menu_import_button)

        self.menu_record_button = QPushButton(self.menu_container_option)
        self.menu_record_button.setObjectName(u"menu_record_button")
        self.menu_record_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menu_record_button.setStyleSheet(u"text-align: left; color: #333;")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/images/icons/icons8-record_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_record_button.setIcon(icon1)
        self.menu_record_button.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.menu_record_button)

        self.menu_action_button = QPushButton(self.menu_container_option)
        self.menu_action_button.setObjectName(u"menu_action_button")
        self.menu_action_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menu_action_button.setStyleSheet(u"text-align: left; color: #333;")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/images/icons/icons8-run-command_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_action_button.setIcon(icon2)
        self.menu_action_button.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.menu_action_button)

        self.menu_export_button = QPushButton(self.menu_container_option)
        self.menu_export_button.setObjectName(u"menu_export_button")
        self.menu_export_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menu_export_button.setStyleSheet(u"text-align: left; color: #333;")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/images/icons/icons8-export-pdf_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_export_button.setIcon(icon3)
        self.menu_export_button.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.menu_export_button)

        self.menu_settings_button = QPushButton(self.menu_container_option)
        self.menu_settings_button.setObjectName(u"menu_settings_button")
        self.menu_settings_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menu_settings_button.setStyleSheet(u"text-align: left; color: #333;")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/images/icons/icons8-setting_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_settings_button.setIcon(icon4)
        self.menu_settings_button.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.menu_settings_button)


        self.verticalLayout_2.addWidget(self.menu_container_option)


        self.verticalLayout.addWidget(self.menu_container)

        self.recording_container = QFrame(self.left_container)
        self.recording_container.setObjectName(u"recording_container")
        self.recording_container.setStyleSheet(u"border: 0;")
        self.recording_container.setFrameShape(QFrame.NoFrame)
        self.recording_container.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.recording_container)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.recording_container_label = QFrame(self.recording_container)
        self.recording_container_label.setObjectName(u"recording_container_label")
        self.recording_container_label.setMaximumSize(QSize(16777215, 30))
        self.recording_container_label.setStyleSheet(u"border: 0;")
        self.recording_container_label.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.recording_container_label)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.recording_label = QLabel(self.recording_container_label)
        self.recording_label.setObjectName(u"recording_label")
        self.recording_label.setFont(font)
        self.recording_label.setStyleSheet(u"color: #4B4B4B;\n"
"font-size: 20pt;")

        self.horizontalLayout_3.addWidget(self.recording_label)


        self.verticalLayout_3.addWidget(self.recording_container_label)

        self.recording_container_list = QFrame(self.recording_container)
        self.recording_container_list.setObjectName(u"recording_container_list")
        self.recording_container_list.setStyleSheet(u"background-color: #D9D9D9;\n"
"border-radius: 8px; padding-top: 1px;")
        self.recording_container_list.setFrameShape(QFrame.NoFrame)
        self.recording_container_list.setLineWidth(0)
        self.gridLayout = QGridLayout(self.recording_container_list)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.recording_container_scrollArea = QScrollArea(self.recording_container_list)
        self.recording_container_scrollArea.setObjectName(u"recording_container_scrollArea")
        self.recording_container_scrollArea.setWidgetResizable(True)
        self.recording_container_frame = QWidget()
        self.recording_container_frame.setObjectName(u"recording_container_frame")
        self.recording_container_frame.setGeometry(QRect(0, 0, 174, 397))
        self.verticalLayout_8 = QVBoxLayout(self.recording_container_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.recording1_frame = QFrame(self.recording_container_frame)
        self.recording1_frame.setObjectName(u"recording1_frame")
        self.recording1_frame.setMaximumSize(QSize(16777215, 70))
        self.recording1_frame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.recording1_frame.setStyleSheet(u"QFrame{background-color:#FFC9C9}\n"
"QFrame:hover {color:#FFC9C9}")
        self.recording1_frame.setFrameShape(QFrame.StyledPanel)
        self.recording1_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.recording1_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 0, 0, 0)
        self.recording1_title = QLabel(self.recording1_frame)
        self.recording1_title.setObjectName(u"recording1_title")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setBold(True)
        self.recording1_title.setFont(font2)
        self.recording1_title.setStyleSheet(u"color: #333;")

        self.verticalLayout_6.addWidget(self.recording1_title)

        self.recording1_datetime = QLabel(self.recording1_frame)
        self.recording1_datetime.setObjectName(u"recording1_datetime")
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setItalic(False)
        self.recording1_datetime.setFont(font3)
        self.recording1_datetime.setStyleSheet(u"color: #858585;")

        self.verticalLayout_6.addWidget(self.recording1_datetime)


        self.verticalLayout_8.addWidget(self.recording1_frame)

        self.recording2_frame = QFrame(self.recording_container_frame)
        self.recording2_frame.setObjectName(u"recording2_frame")
        self.recording2_frame.setMaximumSize(QSize(16777215, 70))
        self.recording2_frame.setFrameShape(QFrame.StyledPanel)
        self.recording2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.recording2_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 0, 0, 0)
        self.recording2_title = QLabel(self.recording2_frame)
        self.recording2_title.setObjectName(u"recording2_title")
        self.recording2_title.setFont(font2)
        self.recording2_title.setStyleSheet(u"color: #333;")

        self.verticalLayout_7.addWidget(self.recording2_title)

        self.recording2_datetime = QLabel(self.recording2_frame)
        self.recording2_datetime.setObjectName(u"recording2_datetime")
        font4 = QFont()
        font4.setFamilies([u"Poppins"])
        self.recording2_datetime.setFont(font4)
        self.recording2_datetime.setStyleSheet(u"color: #858585;")

        self.verticalLayout_7.addWidget(self.recording2_datetime)


        self.verticalLayout_8.addWidget(self.recording2_frame)

        self.recording3_frame = QFrame(self.recording_container_frame)
        self.recording3_frame.setObjectName(u"recording3_frame")
        self.recording3_frame.setFrameShape(QFrame.StyledPanel)
        self.recording3_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.recording3_frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 0, 0, 0)
        self.recording3_title = QLabel(self.recording3_frame)
        self.recording3_title.setObjectName(u"recording3_title")
        self.recording3_title.setFont(font2)
        self.recording3_title.setStyleSheet(u"color: #333;")

        self.verticalLayout_9.addWidget(self.recording3_title)

        self.recording3_datetime = QLabel(self.recording3_frame)
        self.recording3_datetime.setObjectName(u"recording3_datetime")
        font5 = QFont()
        font5.setFamilies([u"Poppins"])
        font5.setBold(False)
        self.recording3_datetime.setFont(font5)
        self.recording3_datetime.setStyleSheet(u"color: #858585;")

        self.verticalLayout_9.addWidget(self.recording3_datetime)


        self.verticalLayout_8.addWidget(self.recording3_frame)

        self.recording_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.recording_verticalSpacer)

        self.recording_container_scrollArea.setWidget(self.recording_container_frame)

        self.gridLayout.addWidget(self.recording_container_scrollArea, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.recording_container_list)


        self.verticalLayout.addWidget(self.recording_container)


        self.horizontalLayout.addWidget(self.left_container)

        self.left_center_divider = QFrame(Main)
        self.left_center_divider.setObjectName(u"left_center_divider")
        self.left_center_divider.setLineWidth(2)
        self.left_center_divider.setFrameShape(QFrame.Shape.VLine)
        self.left_center_divider.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.left_center_divider)

        self.center_container = QFrame(Main)
        self.center_container.setObjectName(u"center_container")
        self.center_container.setMinimumSize(QSize(400, 0))
        self.center_container.setStyleSheet(u"background-color: rgb(255, 255, 255);border: 0;")
        self.center_container.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_14 = QVBoxLayout(self.center_container)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.model_buttons = QFrame(self.center_container)
        self.model_buttons.setObjectName(u"model_buttons")
        self.model_buttons.setMaximumSize(QSize(16777215, 65))
        self.model_buttons.setFrameShape(QFrame.StyledPanel)
        self.model_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.model_buttons)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.transcribe_container = QFrame(self.model_buttons)
        self.transcribe_container.setObjectName(u"transcribe_container")
        self.transcribe_container.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.transcribe_container.setStyleSheet(u"background-color: #2B2B2B;\n"
"border-radius: 10px;")
        self.transcribe_container.setFrameShape(QFrame.StyledPanel)
        self.transcribe_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.transcribe_container)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.transcribe_container_icon = QFrame(self.transcribe_container)
        self.transcribe_container_icon.setObjectName(u"transcribe_container_icon")
        self.transcribe_container_icon.setMaximumSize(QSize(30, 30))
        self.transcribe_container_icon.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;")
        self.transcribe_container_icon.setFrameShape(QFrame.StyledPanel)
        self.transcribe_container_icon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.transcribe_container_icon)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.transcribe_icon = QPushButton(self.transcribe_container_icon)
        self.transcribe_icon.setObjectName(u"transcribe_icon")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/images/icons/icons8-audiomaster_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.transcribe_icon.setIcon(icon5)

        self.verticalLayout_15.addWidget(self.transcribe_icon)


        self.horizontalLayout_5.addWidget(self.transcribe_container_icon)

        self.transcribe_container_content = QFrame(self.transcribe_container)
        self.transcribe_container_content.setObjectName(u"transcribe_container_content")
        self.transcribe_container_content.setStyleSheet(u"")
        self.transcribe_container_content.setFrameShape(QFrame.StyledPanel)
        self.transcribe_container_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.transcribe_container_content)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 0, 0, 0)
        self.transcribe_verticalSpacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.transcribe_verticalSpacer_top)

        self.transcribe_label = QLabel(self.transcribe_container_content)
        self.transcribe_label.setObjectName(u"transcribe_label")
        font6 = QFont()
        font6.setFamilies([u"Poppins"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.transcribe_label.setFont(font6)
        self.transcribe_label.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_16.addWidget(self.transcribe_label)

        self.transcribe_model = QLabel(self.transcribe_container_content)
        self.transcribe_model.setObjectName(u"transcribe_model")
        font7 = QFont()
        font7.setFamilies([u"Poppins"])
        font7.setPointSize(10)
        self.transcribe_model.setFont(font7)
        self.transcribe_model.setStyleSheet(u"color: #FFF;")
        self.transcribe_model.setIndent(0)

        self.verticalLayout_16.addWidget(self.transcribe_model)

        self.transcribe_verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.transcribe_verticalSpacer_bottom)


        self.horizontalLayout_5.addWidget(self.transcribe_container_content)


        self.horizontalLayout_4.addWidget(self.transcribe_container)

        self.alignment_container = QFrame(self.model_buttons)
        self.alignment_container.setObjectName(u"alignment_container")
        self.alignment_container.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.alignment_container.setStyleSheet(u"background-color: #2B2B2B;\n"
"border-radius: 10px;")
        self.alignment_container.setFrameShape(QFrame.StyledPanel)
        self.alignment_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.alignment_container)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.alignment_container_icon = QFrame(self.alignment_container)
        self.alignment_container_icon.setObjectName(u"alignment_container_icon")
        self.alignment_container_icon.setMaximumSize(QSize(30, 30))
        self.alignment_container_icon.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;")
        self.alignment_container_icon.setFrameShape(QFrame.StyledPanel)
        self.alignment_container_icon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.alignment_container_icon)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.alignment_icon = QPushButton(self.alignment_container_icon)
        self.alignment_icon.setObjectName(u"alignment_icon")
        self.alignment_icon.setIcon(icon5)

        self.verticalLayout_17.addWidget(self.alignment_icon)


        self.horizontalLayout_6.addWidget(self.alignment_container_icon)

        self.alignment_container_content = QFrame(self.alignment_container)
        self.alignment_container_content.setObjectName(u"alignment_container_content")
        self.alignment_container_content.setFrameShape(QFrame.StyledPanel)
        self.alignment_container_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.alignment_container_content)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(5, 0, 0, 0)
        self.alignment_verticalSpacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.alignment_verticalSpacer_top)

        self.alignment_label = QLabel(self.alignment_container_content)
        self.alignment_label.setObjectName(u"alignment_label")
        self.alignment_label.setFont(font6)
        self.alignment_label.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_20.addWidget(self.alignment_label)

        self.alignment_model = QLabel(self.alignment_container_content)
        self.alignment_model.setObjectName(u"alignment_model")
        font8 = QFont()
        font8.setFamilies([u"Poppins"])
        font8.setPointSize(11)
        self.alignment_model.setFont(font8)
        self.alignment_model.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_20.addWidget(self.alignment_model)

        self.alignment_verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.alignment_verticalSpacer_bottom)


        self.horizontalLayout_6.addWidget(self.alignment_container_content)


        self.horizontalLayout_4.addWidget(self.alignment_container)

        self.diarization_container = QFrame(self.model_buttons)
        self.diarization_container.setObjectName(u"diarization_container")
        self.diarization_container.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.diarization_container.setStyleSheet(u"background-color: #2B2B2B;\n"
"border-radius: 10px;")
        self.diarization_container.setFrameShape(QFrame.StyledPanel)
        self.diarization_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.diarization_container)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.diarization_container_icon = QFrame(self.diarization_container)
        self.diarization_container_icon.setObjectName(u"diarization_container_icon")
        self.diarization_container_icon.setMaximumSize(QSize(30, 30))
        self.diarization_container_icon.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;")
        self.diarization_container_icon.setFrameShape(QFrame.StyledPanel)
        self.diarization_container_icon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.diarization_container_icon)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.diarization_icon = QPushButton(self.diarization_container_icon)
        self.diarization_icon.setObjectName(u"diarization_icon")
        self.diarization_icon.setIcon(icon5)

        self.verticalLayout_18.addWidget(self.diarization_icon)


        self.horizontalLayout_7.addWidget(self.diarization_container_icon)

        self.diarization_container_content = QFrame(self.diarization_container)
        self.diarization_container_content.setObjectName(u"diarization_container_content")
        self.diarization_container_content.setFrameShape(QFrame.StyledPanel)
        self.diarization_container_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.diarization_container_content)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 0, 0, 0)
        self.diarization_verticalSpacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.diarization_verticalSpacer_top)

        self.diarization_label = QLabel(self.diarization_container_content)
        self.diarization_label.setObjectName(u"diarization_label")
        self.diarization_label.setFont(font6)
        self.diarization_label.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_21.addWidget(self.diarization_label)

        self.diarization_model = QLabel(self.diarization_container_content)
        self.diarization_model.setObjectName(u"diarization_model")
        self.diarization_model.setFont(font8)
        self.diarization_model.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_21.addWidget(self.diarization_model)

        self.diarization_verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.diarization_verticalSpacer_bottom)


        self.horizontalLayout_7.addWidget(self.diarization_container_content)


        self.horizontalLayout_4.addWidget(self.diarization_container)

        self.rag_container = QFrame(self.model_buttons)
        self.rag_container.setObjectName(u"rag_container")
        self.rag_container.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.rag_container.setStyleSheet(u"background-color: #2B2B2B;\n"
"border-radius: 10px;")
        self.rag_container.setFrameShape(QFrame.StyledPanel)
        self.rag_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.rag_container)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.rag_container_icon = QFrame(self.rag_container)
        self.rag_container_icon.setObjectName(u"rag_container_icon")
        self.rag_container_icon.setMaximumSize(QSize(30, 30))
        self.rag_container_icon.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;")
        self.rag_container_icon.setFrameShape(QFrame.StyledPanel)
        self.rag_container_icon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.rag_container_icon)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.rag_icon = QPushButton(self.rag_container_icon)
        self.rag_icon.setObjectName(u"rag_icon")
        self.rag_icon.setIcon(icon5)

        self.verticalLayout_19.addWidget(self.rag_icon)


        self.horizontalLayout_8.addWidget(self.rag_container_icon)

        self.rag_container_content = QFrame(self.rag_container)
        self.rag_container_content.setObjectName(u"rag_container_content")
        self.rag_container_content.setFrameShape(QFrame.StyledPanel)
        self.rag_container_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.rag_container_content)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 0, 0, 0)
        self.rag_verticalSpacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.rag_verticalSpacer_top)

        self.rag_label = QLabel(self.rag_container_content)
        self.rag_label.setObjectName(u"rag_label")
        self.rag_label.setFont(font6)
        self.rag_label.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_22.addWidget(self.rag_label)

        self.rag_model = QLabel(self.rag_container_content)
        self.rag_model.setObjectName(u"rag_model")
        self.rag_model.setFont(font8)
        self.rag_model.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_22.addWidget(self.rag_model)

        self.rag_verticalSpacer_botom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.rag_verticalSpacer_botom)


        self.horizontalLayout_8.addWidget(self.rag_container_content)


        self.horizontalLayout_4.addWidget(self.rag_container)


        self.verticalLayout_14.addWidget(self.model_buttons)

        self.audio_player = QFrame(self.center_container)
        self.audio_player.setObjectName(u"audio_player")
        self.audio_player.setMaximumSize(QSize(16777215, 160))
        self.audio_player.setFrameShape(QFrame.StyledPanel)
        self.audio_player.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.audio_player)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.audio_player_now_playing = QFrame(self.audio_player)
        self.audio_player_now_playing.setObjectName(u"audio_player_now_playing")
        self.audio_player_now_playing.setMaximumSize(QSize(16777215, 90))
        self.audio_player_now_playing.setFrameShape(QFrame.StyledPanel)
        self.audio_player_now_playing.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.audio_player_now_playing)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 5, 0, 0)
        self.audio_player_horizontalSpacer_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.audio_player_horizontalSpacer_left)

        self.audio_player_container = QFrame(self.audio_player_now_playing)
        self.audio_player_container.setObjectName(u"audio_player_container")
        self.audio_player_container.setFrameShape(QFrame.StyledPanel)
        self.audio_player_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.audio_player_container)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.audio_player_title = QLabel(self.audio_player_container)
        self.audio_player_title.setObjectName(u"audio_player_title")
        font9 = QFont()
        font9.setFamilies([u"Poppins"])
        font9.setPointSize(18)
        font9.setBold(True)
        self.audio_player_title.setFont(font9)
        self.audio_player_title.setStyleSheet(u"color: #000;")
        self.audio_player_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.audio_player_title)

        self.audio_player_desc = QLabel(self.audio_player_container)
        self.audio_player_desc.setObjectName(u"audio_player_desc")
        self.audio_player_desc.setFont(font4)
        self.audio_player_desc.setStyleSheet(u"color: #858585;")
        self.audio_player_desc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.audio_player_desc)


        self.horizontalLayout_9.addWidget(self.audio_player_container)

        self.audio_player_horizontalSpacer_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.audio_player_horizontalSpacer_right)


        self.verticalLayout_23.addWidget(self.audio_player_now_playing)

        self.audio_player_progress = QFrame(self.audio_player)
        self.audio_player_progress.setObjectName(u"audio_player_progress")
        self.audio_player_progress.setMaximumSize(QSize(16777215, 70))
        self.audio_player_progress.setFrameShape(QFrame.StyledPanel)
        self.audio_player_progress.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.audio_player_progress)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.audio_player_current_time = QLabel(self.audio_player_progress)
        self.audio_player_current_time.setObjectName(u"audio_player_current_time")
        self.audio_player_current_time.setStyleSheet(u"color: #000;")

        self.horizontalLayout_10.addWidget(self.audio_player_current_time)

        self.audio_player_slider = QSlider(self.audio_player_progress)
        self.audio_player_slider.setObjectName(u"audio_player_slider")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audio_player_slider.sizePolicy().hasHeightForWidth())
        self.audio_player_slider.setSizePolicy(sizePolicy)
        self.audio_player_slider.setMinimumSize(QSize(270, 0))
        self.audio_player_slider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.audio_player_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"                border: 1px solid #333;\n"
"                height: 2px;\n"
"                }\n"
"\n"
"                QSlider::handle:horizontal {\n"
"                background: #F00;\n"
"                width: 10px;\n"
"                height: 2px;\n"
"                margin: -5px -1px;\n"
"                border-radius: 5px;\n"
"                border: 1px solid #FF3333;\n"
"                }\n"
"\n"
"                QSlider::add-page:horizontal {\n"
"                background: #333;\n"
"                }\n"
"\n"
"                QSlider::sub-page:horizontal {\n"
"                background: #FF0000;\n"
"                }")
        self.audio_player_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.audio_player_slider)

        self.audio_player_duration = QLabel(self.audio_player_progress)
        self.audio_player_duration.setObjectName(u"audio_player_duration")
        self.audio_player_duration.setStyleSheet(u"color: #000;")

        self.horizontalLayout_10.addWidget(self.audio_player_duration)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)


        self.verticalLayout_23.addWidget(self.audio_player_progress)

        self.audio_player_toolbar = QFrame(self.audio_player)
        self.audio_player_toolbar.setObjectName(u"audio_player_toolbar")
        self.audio_player_toolbar.setFrameShape(QFrame.StyledPanel)
        self.audio_player_toolbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.audio_player_toolbar)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.audio_player_toolbar_horizontalSpacer_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.audio_player_toolbar_horizontalSpacer_left)

        self.backward_button = QPushButton(self.audio_player_toolbar)
        self.backward_button.setObjectName(u"backward_button")
        self.backward_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/images/icons/icons8-replay_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backward_button.setIcon(icon6)
        self.backward_button.setIconSize(QSize(35, 35))

        self.horizontalLayout_12.addWidget(self.backward_button)

        self.play_button = QPushButton(self.audio_player_toolbar)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/images/icons/icons8-play_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_button.setIcon(icon7)
        self.play_button.setIconSize(QSize(35, 35))

        self.horizontalLayout_12.addWidget(self.play_button)

        self.forward_button = QPushButton(self.audio_player_toolbar)
        self.forward_button.setObjectName(u"forward_button")
        self.forward_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/Icons/images/icons/icons8-forward_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.forward_button.setIcon(icon8)
        self.forward_button.setIconSize(QSize(35, 35))

        self.horizontalLayout_12.addWidget(self.forward_button)

        self.audio_player_toolbar_horizontalSpacer_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.audio_player_toolbar_horizontalSpacer_right)


        self.verticalLayout_23.addWidget(self.audio_player_toolbar)


        self.verticalLayout_14.addWidget(self.audio_player)

        self.ai_chatbox_container = QFrame(self.center_container)
        self.ai_chatbox_container.setObjectName(u"ai_chatbox_container")
        self.ai_chatbox_container.setFrameShape(QFrame.StyledPanel)
        self.ai_chatbox_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.ai_chatbox_container)
        self.verticalLayout_25.setSpacing(8)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.ai_chatbox_history_container = QFrame(self.ai_chatbox_container)
        self.ai_chatbox_history_container.setObjectName(u"ai_chatbox_history_container")
        self.ai_chatbox_history_container.setStyleSheet(u"background-color: #D9D9D9;\n"
"border-radius: 15px")
        self.ai_chatbox_history_container.setFrameShape(QFrame.StyledPanel)
        self.ai_chatbox_history_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.ai_chatbox_history_container)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(12, 12, 12, 12)
        self.cleat_chat_container = QFrame(self.ai_chatbox_history_container)
        self.cleat_chat_container.setObjectName(u"cleat_chat_container")
        self.cleat_chat_container.setFrameShape(QFrame.StyledPanel)
        self.cleat_chat_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.cleat_chat_container)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 5)
        self.clear_chat_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.clear_chat_horizontalSpacer)

        self.clear_chat_button = QPushButton(self.cleat_chat_container)
        self.clear_chat_button.setObjectName(u"clear_chat_button")
        self.clear_chat_button.setMinimumSize(QSize(80, 20))
        self.clear_chat_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clear_chat_button.setStyleSheet(u"color: \"#FFF\";\n"
"background-color: #0D0404;\n"
"border-radius: 10px;")

        self.horizontalLayout_13.addWidget(self.clear_chat_button)


        self.verticalLayout_26.addWidget(self.cleat_chat_container)

        self.ai_chatbox_history_scrollArea = QScrollArea(self.ai_chatbox_history_container)
        self.ai_chatbox_history_scrollArea.setObjectName(u"ai_chatbox_history_scrollArea")
        self.ai_chatbox_history_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 352, 298))
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 12, 0, 0)
        self.ai_chatbox_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.ai_chatbox_verticalSpacer)

        self.ai_chatbox_human1 = QFrame(self.scrollAreaWidgetContents)
        self.ai_chatbox_human1.setObjectName(u"ai_chatbox_human1")
        self.ai_chatbox_human1.setStyleSheet(u"background-color: #575757;\n"
"border-radius: 10px;")
        self.ai_chatbox_human1.setFrameShape(QFrame.StyledPanel)
        self.ai_chatbox_human1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.ai_chatbox_human1)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.ai_chatbox_human1_label = QLabel(self.ai_chatbox_human1)
        self.ai_chatbox_human1_label.setObjectName(u"ai_chatbox_human1_label")
        self.ai_chatbox_human1_label.setStyleSheet(u"color: #FFF;")
        self.ai_chatbox_human1_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_31.addWidget(self.ai_chatbox_human1_label)


        self.verticalLayout_27.addWidget(self.ai_chatbox_human1)

        self.ai_chatbox_bot1 = QFrame(self.scrollAreaWidgetContents)
        self.ai_chatbox_bot1.setObjectName(u"ai_chatbox_bot1")
        self.ai_chatbox_bot1.setStyleSheet(u"background-color: #868686;\n"
"border-radius: 10px;")
        self.ai_chatbox_bot1.setFrameShape(QFrame.StyledPanel)
        self.ai_chatbox_bot1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.ai_chatbox_bot1)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.ai_chatbox_bot1_label = QLabel(self.ai_chatbox_bot1)
        self.ai_chatbox_bot1_label.setObjectName(u"ai_chatbox_bot1_label")
        self.ai_chatbox_bot1_label.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_30.addWidget(self.ai_chatbox_bot1_label)


        self.verticalLayout_27.addWidget(self.ai_chatbox_bot1)

        self.ai_chatbox_human2 = QFrame(self.scrollAreaWidgetContents)
        self.ai_chatbox_human2.setObjectName(u"ai_chatbox_human2")
        self.ai_chatbox_human2.setStyleSheet(u"background-color: #575757;\n"
"border-radius: 10px;")
        self.ai_chatbox_human2.setFrameShape(QFrame.StyledPanel)
        self.ai_chatbox_human2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.ai_chatbox_human2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.ai_chatbox_human2_label = QLabel(self.ai_chatbox_human2)
        self.ai_chatbox_human2_label.setObjectName(u"ai_chatbox_human2_label")
        self.ai_chatbox_human2_label.setStyleSheet(u"color: #FFF;")
        self.ai_chatbox_human2_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_29.addWidget(self.ai_chatbox_human2_label)


        self.verticalLayout_27.addWidget(self.ai_chatbox_human2)

        self.ai_chatbox_bot2 = QFrame(self.scrollAreaWidgetContents)
        self.ai_chatbox_bot2.setObjectName(u"ai_chatbox_bot2")
        self.ai_chatbox_bot2.setStyleSheet(u"background-color: #868686;\n"
"border-radius: 10px;")
        self.ai_chatbox_bot2.setFrameShape(QFrame.StyledPanel)
        self.ai_chatbox_bot2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.ai_chatbox_bot2)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.ai_chatbox_bot2_label = QLabel(self.ai_chatbox_bot2)
        self.ai_chatbox_bot2_label.setObjectName(u"ai_chatbox_bot2_label")
        self.ai_chatbox_bot2_label.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_28.addWidget(self.ai_chatbox_bot2_label)


        self.verticalLayout_27.addWidget(self.ai_chatbox_bot2)

        self.ai_chatbox_history_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_26.addWidget(self.ai_chatbox_history_scrollArea)


        self.verticalLayout_25.addWidget(self.ai_chatbox_history_container)

        self.ai_chatbox_input_container = QFrame(self.ai_chatbox_container)
        self.ai_chatbox_input_container.setObjectName(u"ai_chatbox_input_container")
        self.ai_chatbox_input_container.setMaximumSize(QSize(16777215, 50))
        self.ai_chatbox_input_container.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: #333;\n"
"border-radius: 13px;\n"
"color: #000;\n"
"padding: 5px;")
        self.ai_chatbox_input_container.setFrameShape(QFrame.StyledPanel)
        self.ai_chatbox_input_container.setFrameShadow(QFrame.Raised)
        self.ai_chatbox_input_container.setLineWidth(1)
        self.horizontalLayout_11 = QHBoxLayout(self.ai_chatbox_input_container)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.ai_chatbox_input_textarea = QTextEdit(self.ai_chatbox_input_container)
        self.ai_chatbox_input_textarea.setObjectName(u"ai_chatbox_input_textarea")
        self.ai_chatbox_input_textarea.setStyleSheet(u"border: None;")

        self.horizontalLayout_11.addWidget(self.ai_chatbox_input_textarea)

        self.ai_chatbox_input_button = QPushButton(self.ai_chatbox_input_container)
        self.ai_chatbox_input_button.setObjectName(u"ai_chatbox_input_button")
        self.ai_chatbox_input_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ai_chatbox_input_button.setStyleSheet(u"border: none;")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/images/icons/icons8-send_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ai_chatbox_input_button.setIcon(icon9)
        self.ai_chatbox_input_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.ai_chatbox_input_button)


        self.verticalLayout_25.addWidget(self.ai_chatbox_input_container)


        self.verticalLayout_14.addWidget(self.ai_chatbox_container)


        self.horizontalLayout.addWidget(self.center_container)

        self.right_container = QFrame(Main)
        self.right_container.setObjectName(u"right_container")
        self.right_container.setMinimumSize(QSize(300, 0))
        self.right_container.setMaximumSize(QSize(400, 16777215))
        self.right_container.setStyleSheet(u"background-color: #333333;border: 0;")
        self.right_container.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.right_container)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(12, -1, -1, -1)
        self.transcription_label = QLabel(self.right_container)
        self.transcription_label.setObjectName(u"transcription_label")
        self.transcription_label.setMaximumSize(QSize(16777215, 30))
        font10 = QFont()
        font10.setPointSize(20)
        self.transcription_label.setFont(font10)
        self.transcription_label.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_5.addWidget(self.transcription_label)

        self.transcription_container = QFrame(self.right_container)
        self.transcription_container.setObjectName(u"transcription_container")
        self.transcription_container.setStyleSheet(u"background-color: #D9D9D9;\n"
"border-radius: 12px;")
        self.transcription_container.setFrameShape(QFrame.StyledPanel)
        self.transcription_container.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.transcription_container)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 10, -1, -1)
        self.transcription_scrollArea = QScrollArea(self.transcription_container)
        self.transcription_scrollArea.setObjectName(u"transcription_scrollArea")
        self.transcription_scrollArea.setWidgetResizable(True)
        self.transcription_scrollArea_frame = QWidget()
        self.transcription_scrollArea_frame.setObjectName(u"transcription_scrollArea_frame")
        self.transcription_scrollArea_frame.setGeometry(QRect(0, 0, 264, 537))
        self.verticalLayout_10 = QVBoxLayout(self.transcription_scrollArea_frame)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 0, 0)
        self.transcription_speaker1_1 = QFrame(self.transcription_scrollArea_frame)
        self.transcription_speaker1_1.setObjectName(u"transcription_speaker1_1")
        self.transcription_speaker1_1.setMaximumSize(QSize(16777215, 70))
        self.transcription_speaker1_1.setStyleSheet(u"background-color: #0D0404;\n"
"border-radius: 10px;")
        self.transcription_speaker1_1.setFrameShape(QFrame.StyledPanel)
        self.transcription_speaker1_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.transcription_speaker1_1)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(10, 5, 5, 5)
        self.transcription_speaker1_1_label = QLabel(self.transcription_speaker1_1)
        self.transcription_speaker1_1_label.setObjectName(u"transcription_speaker1_1_label")
        self.transcription_speaker1_1_label.setFont(font5)
        self.transcription_speaker1_1_label.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_11.addWidget(self.transcription_speaker1_1_label)


        self.verticalLayout_10.addWidget(self.transcription_speaker1_1)

        self.transcription_speaker2_1 = QFrame(self.transcription_scrollArea_frame)
        self.transcription_speaker2_1.setObjectName(u"transcription_speaker2_1")
        self.transcription_speaker2_1.setMaximumSize(QSize(16777215, 70))
        self.transcription_speaker2_1.setStyleSheet(u"background-color: #575757;\n"
"border-radius: 10px;")
        self.transcription_speaker2_1.setFrameShape(QFrame.StyledPanel)
        self.transcription_speaker2_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.transcription_speaker2_1)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 5, 5, 5)
        self.transcription_speaker2_1_label = QLabel(self.transcription_speaker2_1)
        self.transcription_speaker2_1_label.setObjectName(u"transcription_speaker2_1_label")
        self.transcription_speaker2_1_label.setFont(font5)
        self.transcription_speaker2_1_label.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_12.addWidget(self.transcription_speaker2_1_label)


        self.verticalLayout_10.addWidget(self.transcription_speaker2_1)

        self.transcription_speaker3_1 = QFrame(self.transcription_scrollArea_frame)
        self.transcription_speaker3_1.setObjectName(u"transcription_speaker3_1")
        self.transcription_speaker3_1.setStyleSheet(u"background-color: #868686;\n"
"border-radius: 10px;")
        self.transcription_speaker3_1.setFrameShape(QFrame.StyledPanel)
        self.transcription_speaker3_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.transcription_speaker3_1)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 5, 5, 5)
        self.transcription_speaker3_1_label = QLabel(self.transcription_speaker3_1)
        self.transcription_speaker3_1_label.setObjectName(u"transcription_speaker3_1_label")
        self.transcription_speaker3_1_label.setFont(font5)
        self.transcription_speaker3_1_label.setStyleSheet(u"color: #FFF;")

        self.verticalLayout_13.addWidget(self.transcription_speaker3_1_label)


        self.verticalLayout_10.addWidget(self.transcription_speaker3_1)

        self.transcription_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.transcription_verticalSpacer)

        self.transcription_scrollArea.setWidget(self.transcription_scrollArea_frame)

        self.gridLayout_2.addWidget(self.transcription_scrollArea, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.transcription_container)


        self.horizontalLayout.addWidget(self.right_container)


        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Audio AI", None))
        self.menu_label.setText(QCoreApplication.translate("Main", u"MENU", None))
        self.menu_import_button.setText(QCoreApplication.translate("Main", u"Import", None))
        self.menu_record_button.setText(QCoreApplication.translate("Main", u" Record", None))
        self.menu_action_button.setText(QCoreApplication.translate("Main", u" Action", None))
        self.menu_export_button.setText(QCoreApplication.translate("Main", u" Export", None))
        self.menu_settings_button.setText(QCoreApplication.translate("Main", u" Settings", None))
        self.recording_label.setText(QCoreApplication.translate("Main", u"RECORDINGS", None))
        self.recording1_title.setText(QCoreApplication.translate("Main", u"Bob Keating TIMA", None))
        self.recording1_datetime.setText(QCoreApplication.translate("Main", u"31/01/2025 10:55", None))
        self.recording2_title.setText(QCoreApplication.translate("Main", u"Bob Keating TIMA", None))
        self.recording2_datetime.setText(QCoreApplication.translate("Main", u"31/01/2025 10:55", None))
        self.recording3_title.setText(QCoreApplication.translate("Main", u"Bob Keating TIMA", None))
        self.recording3_datetime.setText(QCoreApplication.translate("Main", u"31/01/2025 10:55", None))
        self.transcribe_icon.setText("")
        self.transcribe_label.setText(QCoreApplication.translate("Main", u"Transcribe", None))
        self.transcribe_model.setText(QCoreApplication.translate("Main", u"Whisper", None))
        self.alignment_icon.setText("")
        self.alignment_label.setText(QCoreApplication.translate("Main", u"Alignment", None))
        self.alignment_model.setText(QCoreApplication.translate("Main", u"Whisper", None))
        self.diarization_icon.setText("")
        self.diarization_label.setText(QCoreApplication.translate("Main", u"Diarization", None))
        self.diarization_model.setText(QCoreApplication.translate("Main", u"Whisper", None))
        self.rag_icon.setText("")
        self.rag_label.setText(QCoreApplication.translate("Main", u"RAG", None))
        self.rag_model.setText(QCoreApplication.translate("Main", u"R3", None))
        self.audio_player_title.setText(QCoreApplication.translate("Main", u"Welcome to AudioAI", None))
        self.audio_player_desc.setText(QCoreApplication.translate("Main", u"select file from recordings or import", None))
        self.audio_player_current_time.setText(QCoreApplication.translate("Main", u"0:00", None))
        self.audio_player_duration.setText(QCoreApplication.translate("Main", u"0:00", None))
        self.backward_button.setText("")
        self.play_button.setText("")
        self.forward_button.setText("")
        self.clear_chat_button.setText(QCoreApplication.translate("Main", u"Clear Chat", None))
        self.ai_chatbox_human1_label.setText(QCoreApplication.translate("Main", u"List all Past Medical History of Bob!", None))
        self.ai_chatbox_bot1_label.setText(QCoreApplication.translate("Main", u"asdasdasd\n"
"sdasdasd\n"
"asdasdasd", None))
        self.ai_chatbox_human2_label.setText(QCoreApplication.translate("Main", u"List all Past Medical History of Bob!", None))
        self.ai_chatbox_bot2_label.setText(QCoreApplication.translate("Main", u"asdasdasd\n"
"sdasdasd\n"
"asdasdasd", None))
        self.ai_chatbox_input_textarea.setPlaceholderText(QCoreApplication.translate("Main", u"Ask anything about the audio content...", None))
        self.ai_chatbox_input_button.setText("")
        self.transcription_label.setText(QCoreApplication.translate("Main", u"Transcription", None))
        self.transcription_speaker1_1_label.setText(QCoreApplication.translate("Main", u"asdasdasd\n"
"sdasdasd\n"
"asdasdasd", None))
        self.transcription_speaker2_1_label.setText(QCoreApplication.translate("Main", u"Bob Keating TIMA", None))
        self.transcription_speaker3_1_label.setText(QCoreApplication.translate("Main", u"asdasdasd\n"
"sdasdasd\n"
"asdasdasd", None))
    # retranslateUi

