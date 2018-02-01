# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(911, 547)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/png/kontrol_24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet("background-color: #FFFFFF;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 1, 911, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setStyleSheet("QTabWidget:pane {\n"
"    background: #ffffff;\n"
"     border: 1px solid transparent;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    background: #ffffff;\n"
"    border: 1px solid transparent;\n"
"     left: 203px;\n"
"}\n"
"\n"
"QTabBar:tab { \n"
"    border: 1px solid transparent; \n"
"    height: 18px;\n"
"    padding: 5px 25px 5px 25px;\n"
"    color: #424242;\n"
"} \n"
"\n"
"QTabBar:tab:selected {\n"
"   border-bottom: 2px solid #1565C0;\n"
"}\n"
"\n"
"QTabBar:tab:hover {\n"
"   background: #EEEEEE;\n"
"}\n"
"\n"
"QSlider::groove:horizontal{\n"
"    height: 2px;\n"
"    background: #BDBDBD;\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    height: 2px;\n"
"    background: #1565C0;\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    height: 2px;\n"
"    background: #BDBDBD;\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1565C0;\n"
"    border: 0px;\n"
"    width: 14px;\n"
"    margin: -6px 0 ;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 0px;\n"
"    background: #ffffff;\n"
"    height: 7px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #E0E0E0;\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #D0D0D0;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background: #C0C0C0;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 0px;\n"
"    background: #E0E0E0;\n"
"    width: 0px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 0px;\n"
"    background: transparent;\n"
"    width: 0px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"      background: none;\n"
"  }\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 0px;\n"
"    background: #ffffff;\n"
"    width: 7px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #E0E0E0;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #D0D0D0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #C0C0C0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: 0px;\n"
"    background: #E0E0E0;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 0px;\n"
"    background: #E0E0E0;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"  }\n"
"\n"
"QComboBox {\n"
"    background-color: transparent;\n"
"    border-radius: 0px;\n"
"    border: 0px;\n"
"    border-bottom: 1px solid #9E9E9E;\n"
"    color: #424242;\n"
"    padding: 0 4px ;\n"
"\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-bottom: 1px solid #1565C0;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: #9E9E9E;\n"
"    border-left-style: solid;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/ui/arrow_drop_down.png)\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 0px;\n"
"\n"
"    color: #424242;\n"
"    position: relative;\n"
"    padding: 4px 4px;\n"
"}\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_indoor = QtWidgets.QWidget()
        self.tab_indoor.setStyleSheet("QLabel{\n"
"  background: #E0E0E0;\n"
"  color: #424242;\n"
"  border-radius: 2px;\n"
"  text-decoration: none;\n"
"}\n"
"")
        self.tab_indoor.setObjectName("tab_indoor")
        self.in_air_spinbox = QtWidgets.QSpinBox(self.tab_indoor)
        self.in_air_spinbox.setGeometry(QtCore.QRect(530, 113, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_air_spinbox.setFont(font)
        self.in_air_spinbox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_air_spinbox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.in_air_spinbox.setStyleSheet("QSpinBox {\n"
"    background: transparent;\n"
"    color: #424242;\n"
"    selection-background-color: transparent;\n"
"    selection-color: #424242;\n"
"    border: 1px solid #9E9E9E;\n"
"    border-radius: 2px;\n"
"    padding: 0 4px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; /* position at the top right corner */\n"
"    width: 18px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"    height:18px;\n"
"    border-left: 1px solid #9E9E9E;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/icons/ui/arrow_drop_up_spin.png);\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off { /* off state when value is max */\n"
"    image: url(:/icons/ui/arrow_drop_up_spin_disabled.png);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; /* position at bottom right corner */\n"
"    width: 18px;\n"
"    height:18px;\n"
"    border-left: 1px solid #9E9E9E;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/icons/ui/arrow_drop_down_spin.png);\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow:disabled,\n"
"QSpinBox::down-arrow:off { /* off state when value in min */\n"
"    image: url(:/icons/ui/arrow_drop_down_spin_disabled.png);\n"
"}\n"
"")
        self.in_air_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.in_air_spinbox.setMinimum(17)
        self.in_air_spinbox.setMaximum(30)
        self.in_air_spinbox.setProperty("value", 21)
        self.in_air_spinbox.setObjectName("in_air_spinbox")
        self.in_light_percentage = QtWidgets.QLabel(self.tab_indoor)
        self.in_light_percentage.setGeometry(QtCore.QRect(105, 135, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.in_light_percentage.setFont(font)
        self.in_light_percentage.setStyleSheet("QLabel{\n"
"  background: #FFFFFF;\n"
"  color: #424242;\n"
"  border-radius: 0px;\n"
"  text-decoration: none;\n"
"}")
        self.in_light_percentage.setTextFormat(QtCore.Qt.PlainText)
        self.in_light_percentage.setAlignment(QtCore.Qt.AlignCenter)
        self.in_light_percentage.setObjectName("in_light_percentage")
        self.in_light_on_button = QtWidgets.QPushButton(self.tab_indoor)
        self.in_light_on_button.setGeometry(QtCore.QRect(40, 65, 40, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_light_on_button.setFont(font)
        self.in_light_on_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_light_on_button.setStyleSheet("QPushButton{\n"
"  background-color: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #2E7D32;\n"
"  color: #2E7D32;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66BB6A;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #81C784;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_light_on_button.setObjectName("in_light_on_button")
        self.indoor_lights = QtWidgets.QLabel(self.tab_indoor)
        self.indoor_lights.setGeometry(QtCore.QRect(40, 20, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.indoor_lights.setFont(font)
        self.indoor_lights.setStyleSheet("")
        self.indoor_lights.setAlignment(QtCore.Qt.AlignCenter)
        self.indoor_lights.setObjectName("indoor_lights")
        self.in_fan_on_button = QtWidgets.QPushButton(self.tab_indoor)
        self.in_fan_on_button.setGeometry(QtCore.QRect(260, 65, 40, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_fan_on_button.setFont(font)
        self.in_fan_on_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_fan_on_button.setStyleSheet("QPushButton{\n"
"  background-color: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #2E7D32;\n"
"  color: #2E7D32;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66BB6A;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #81C784;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_fan_on_button.setObjectName("in_fan_on_button")
        self.in_air_auto_button = QtWidgets.QPushButton(self.tab_indoor)
        self.in_air_auto_button.setGeometry(QtCore.QRect(530, 65, 71, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_air_auto_button.setFont(font)
        self.in_air_auto_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_air_auto_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #1565C0;\n"
"  color: #1565C0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #42A5F5;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #64B5F6;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_air_auto_button.setObjectName("in_air_auto_button")
        self.in_light_off_button = QtWidgets.QPushButton(self.tab_indoor)
        self.in_light_off_button.setGeometry(QtCore.QRect(170, 65, 40, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_light_off_button.setFont(font)
        self.in_light_off_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_light_off_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #C62828;\n"
"  color: #C62828;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #EF5350;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #E57373;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_light_off_button.setDefault(False)
        self.in_light_off_button.setFlat(False)
        self.in_light_off_button.setObjectName("in_light_off_button")
        self.in_curtain_auto_button = QtWidgets.QPushButton(self.tab_indoor)
        self.in_curtain_auto_button.setGeometry(QtCore.QRect(750, 65, 71, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_curtain_auto_button.setFont(font)
        self.in_curtain_auto_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_curtain_auto_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #1565C0;\n"
"  color: #1565C0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #42A5F5;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #64B5F6;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_curtain_auto_button.setObjectName("in_curtain_auto_button")
        self.in_light_slider = QtWidgets.QSlider(self.tab_indoor)
        self.in_light_slider.setGeometry(QtCore.QRect(40, 113, 171, 16))
        self.in_light_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_light_slider.setStyleSheet("")
        self.in_light_slider.setMaximum(100)
        self.in_light_slider.setSingleStep(0)
        self.in_light_slider.setPageStep(0)
        self.in_light_slider.setTracking(True)
        self.in_light_slider.setOrientation(QtCore.Qt.Horizontal)
        self.in_light_slider.setObjectName("in_light_slider")
        self.in_curtain_on_button = QtWidgets.QPushButton(self.tab_indoor)
        self.in_curtain_on_button.setGeometry(QtCore.QRect(700, 65, 40, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_curtain_on_button.setFont(font)
        self.in_curtain_on_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_curtain_on_button.setStyleSheet("QPushButton{\n"
"  background-color: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #2E7D32;\n"
"  color: #2E7D32;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66BB6A;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #81C784;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_curtain_on_button.setObjectName("in_curtain_on_button")
        self.in_air_on_button = QtWidgets.QPushButton(self.tab_indoor)
        self.in_air_on_button.setGeometry(QtCore.QRect(480, 65, 40, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_air_on_button.setFont(font)
        self.in_air_on_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_air_on_button.setStyleSheet("QPushButton{\n"
"  background-color: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #2E7D32;\n"
"  color: #2E7D32;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66BB6A;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #81C784;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_air_on_button.setObjectName("in_air_on_button")
        self.in_air_off_button = QtWidgets.QPushButton(self.tab_indoor)
        self.in_air_off_button.setGeometry(QtCore.QRect(610, 65, 40, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_air_off_button.setFont(font)
        self.in_air_off_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_air_off_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #C62828;\n"
"  color: #C62828;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #EF5350;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #E57373;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_air_off_button.setObjectName("in_air_off_button")
        self.in_light_auto_button = QtWidgets.QPushButton(self.tab_indoor)
        self.in_light_auto_button.setGeometry(QtCore.QRect(90, 65, 71, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_light_auto_button.setFont(font)
        self.in_light_auto_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_light_auto_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #1565C0;\n"
"  color: #1565C0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #42A5F5;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #64B5F6;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_light_auto_button.setObjectName("in_light_auto_button")
        self.indoor_curtains = QtWidgets.QLabel(self.tab_indoor)
        self.indoor_curtains.setGeometry(QtCore.QRect(700, 20, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.indoor_curtains.setFont(font)
        self.indoor_curtains.setAlignment(QtCore.Qt.AlignCenter)
        self.indoor_curtains.setObjectName("indoor_curtains")
        self.indoor_fans = QtWidgets.QLabel(self.tab_indoor)
        self.indoor_fans.setGeometry(QtCore.QRect(260, 20, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.indoor_fans.setFont(font)
        self.indoor_fans.setAlignment(QtCore.Qt.AlignCenter)
        self.indoor_fans.setObjectName("indoor_fans")
        self.in_curtain_off_button = QtWidgets.QPushButton(self.tab_indoor)
        self.in_curtain_off_button.setGeometry(QtCore.QRect(830, 65, 40, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_curtain_off_button.setFont(font)
        self.in_curtain_off_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_curtain_off_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #C62828;\n"
"  color: #C62828;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #EF5350;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #E57373;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_curtain_off_button.setObjectName("in_curtain_off_button")
        self.in_fan_off_button = QtWidgets.QPushButton(self.tab_indoor)
        self.in_fan_off_button.setGeometry(QtCore.QRect(390, 65, 40, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_fan_off_button.setFont(font)
        self.in_fan_off_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_fan_off_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #C62828;\n"
"  color: #C62828;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #EF5350;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #E57373;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_fan_off_button.setObjectName("in_fan_off_button")
        self.in_fan_auto_button = QtWidgets.QPushButton(self.tab_indoor)
        self.in_fan_auto_button.setGeometry(QtCore.QRect(310, 65, 71, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_fan_auto_button.setFont(font)
        self.in_fan_auto_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_fan_auto_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #1565C0;\n"
"  color: #1565C0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #42A5F5;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #64B5F6;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_fan_auto_button.setObjectName("in_fan_auto_button")
        self.in_door_open_button = QtWidgets.QPushButton(self.tab_indoor)
        self.in_door_open_button.setGeometry(QtCore.QRect(40, 220, 81, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_door_open_button.setFont(font)
        self.in_door_open_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_door_open_button.setStyleSheet("QPushButton{\n"
"  background-color: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #2E7D32;\n"
"  color: #2E7D32;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66BB6A;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #81C784;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_door_open_button.setObjectName("in_door_open_button")
        self.indoor_air = QtWidgets.QLabel(self.tab_indoor)
        self.indoor_air.setGeometry(QtCore.QRect(480, 20, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.indoor_air.setFont(font)
        self.indoor_air.setAlignment(QtCore.Qt.AlignCenter)
        self.indoor_air.setObjectName("indoor_air")
        self.in_fan_slider = QtWidgets.QSlider(self.tab_indoor)
        self.in_fan_slider.setGeometry(QtCore.QRect(260, 113, 171, 16))
        self.in_fan_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_fan_slider.setMaximum(100)
        self.in_fan_slider.setSingleStep(0)
        self.in_fan_slider.setPageStep(0)
        self.in_fan_slider.setOrientation(QtCore.Qt.Horizontal)
        self.in_fan_slider.setObjectName("in_fan_slider")
        self.in_fan_percentage = QtWidgets.QLabel(self.tab_indoor)
        self.in_fan_percentage.setGeometry(QtCore.QRect(325, 135, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.in_fan_percentage.setFont(font)
        self.in_fan_percentage.setStyleSheet("QLabel{\n"
"  background: #FFFFFF;\n"
"  color: #424242;\n"
"  border-radius: 0px;\n"
"  text-decoration: none;\n"
"}")
        self.in_fan_percentage.setAlignment(QtCore.Qt.AlignCenter)
        self.in_fan_percentage.setObjectName("in_fan_percentage")
        self.in_door_close_button = QtWidgets.QPushButton(self.tab_indoor)
        self.in_door_close_button.setGeometry(QtCore.QRect(130, 220, 81, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_door_close_button.setFont(font)
        self.in_door_close_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_door_close_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #C62828;\n"
"  color: #C62828;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #EF5350;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #E57373;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_door_close_button.setObjectName("in_door_close_button")
        self.indoor_door = QtWidgets.QLabel(self.tab_indoor)
        self.indoor_door.setGeometry(QtCore.QRect(40, 175, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.indoor_door.setFont(font)
        self.indoor_door.setAlignment(QtCore.Qt.AlignCenter)
        self.indoor_door.setObjectName("indoor_door")
        self.tabWidget.addTab(self.tab_indoor, "")
        self.tab_outdoor = QtWidgets.QWidget()
        self.tab_outdoor.setStyleSheet("QLabel{\n"
"  background: #E0E0E0;\n"
"  color: #424242;\n"
"  border-radius: 2px;\n"
"  text-decoration: none;\n"
"}\n"
"")
        self.tab_outdoor.setObjectName("tab_outdoor")
        self.outdoor_lights = QtWidgets.QLabel(self.tab_outdoor)
        self.outdoor_lights.setGeometry(QtCore.QRect(40, 20, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.outdoor_lights.setFont(font)
        self.outdoor_lights.setAlignment(QtCore.Qt.AlignCenter)
        self.outdoor_lights.setObjectName("outdoor_lights")
        self.out_light_auto_button = QtWidgets.QPushButton(self.tab_outdoor)
        self.out_light_auto_button.setGeometry(QtCore.QRect(90, 65, 71, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.out_light_auto_button.setFont(font)
        self.out_light_auto_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.out_light_auto_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #1565C0;\n"
"  color: #1565C0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #42A5F5;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #64B5F6;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.out_light_auto_button.setObjectName("out_light_auto_button")
        self.out_light_percentage = QtWidgets.QLabel(self.tab_outdoor)
        self.out_light_percentage.setGeometry(QtCore.QRect(105, 135, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.out_light_percentage.setFont(font)
        self.out_light_percentage.setStyleSheet("QLabel{\n"
"  background: #FFFFFF;\n"
"  color: #424242;\n"
"  border-radius: 0px;\n"
"  text-decoration: none;\n"
"}")
        self.out_light_percentage.setTextFormat(QtCore.Qt.PlainText)
        self.out_light_percentage.setAlignment(QtCore.Qt.AlignCenter)
        self.out_light_percentage.setObjectName("out_light_percentage")
        self.out_light_on_button = QtWidgets.QPushButton(self.tab_outdoor)
        self.out_light_on_button.setGeometry(QtCore.QRect(40, 65, 40, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.out_light_on_button.setFont(font)
        self.out_light_on_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.out_light_on_button.setStyleSheet("QPushButton{\n"
"  background-color: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #2E7D32;\n"
"  color: #2E7D32;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66BB6A;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #81C784;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.out_light_on_button.setObjectName("out_light_on_button")
        self.out_light_slider = QtWidgets.QSlider(self.tab_outdoor)
        self.out_light_slider.setGeometry(QtCore.QRect(40, 113, 171, 16))
        self.out_light_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.out_light_slider.setMaximum(100)
        self.out_light_slider.setSingleStep(0)
        self.out_light_slider.setPageStep(0)
        self.out_light_slider.setOrientation(QtCore.Qt.Horizontal)
        self.out_light_slider.setObjectName("out_light_slider")
        self.out_light_off_button = QtWidgets.QPushButton(self.tab_outdoor)
        self.out_light_off_button.setGeometry(QtCore.QRect(170, 65, 40, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.out_light_off_button.setFont(font)
        self.out_light_off_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.out_light_off_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #C62828;\n"
"  color: #C62828;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #EF5350;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #E57373;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.out_light_off_button.setObjectName("out_light_off_button")
        self.out_irri_auto_button = QtWidgets.QPushButton(self.tab_outdoor)
        self.out_irri_auto_button.setGeometry(QtCore.QRect(310, 65, 71, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.out_irri_auto_button.setFont(font)
        self.out_irri_auto_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.out_irri_auto_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #1565C0;\n"
"  color: #1565C0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #42A5F5;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #64B5F6;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.out_irri_auto_button.setObjectName("out_irri_auto_button")
        self.out_irri_on_button = QtWidgets.QPushButton(self.tab_outdoor)
        self.out_irri_on_button.setGeometry(QtCore.QRect(260, 65, 40, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.out_irri_on_button.setFont(font)
        self.out_irri_on_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.out_irri_on_button.setStyleSheet("QPushButton{\n"
"  background-color: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #2E7D32;\n"
"  color: #2E7D32;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66BB6A;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #81C784;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.out_irri_on_button.setObjectName("out_irri_on_button")
        self.outdoor_irrigation = QtWidgets.QLabel(self.tab_outdoor)
        self.outdoor_irrigation.setGeometry(QtCore.QRect(260, 20, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.outdoor_irrigation.setFont(font)
        self.outdoor_irrigation.setAlignment(QtCore.Qt.AlignCenter)
        self.outdoor_irrigation.setObjectName("outdoor_irrigation")
        self.out_irri_off_button = QtWidgets.QPushButton(self.tab_outdoor)
        self.out_irri_off_button.setGeometry(QtCore.QRect(390, 65, 40, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.out_irri_off_button.setFont(font)
        self.out_irri_off_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.out_irri_off_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #C62828;\n"
"  color: #C62828;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #EF5350;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #E57373;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.out_irri_off_button.setObjectName("out_irri_off_button")
        self.out_irri_slider = QtWidgets.QSlider(self.tab_outdoor)
        self.out_irri_slider.setGeometry(QtCore.QRect(260, 113, 171, 16))
        self.out_irri_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.out_irri_slider.setMaximum(100)
        self.out_irri_slider.setSingleStep(0)
        self.out_irri_slider.setPageStep(0)
        self.out_irri_slider.setOrientation(QtCore.Qt.Horizontal)
        self.out_irri_slider.setObjectName("out_irri_slider")
        self.out_irri_percentage = QtWidgets.QLabel(self.tab_outdoor)
        self.out_irri_percentage.setGeometry(QtCore.QRect(325, 135, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.out_irri_percentage.setFont(font)
        self.out_irri_percentage.setStyleSheet("QLabel{\n"
"  background: #FFFFFF;\n"
"  color: #424242;\n"
"  border-radius: 0px;\n"
"  text-decoration: none;\n"
"}")
        self.out_irri_percentage.setTextFormat(QtCore.Qt.PlainText)
        self.out_irri_percentage.setAlignment(QtCore.Qt.AlignCenter)
        self.out_irri_percentage.setObjectName("out_irri_percentage")
        self.tabWidget.addTab(self.tab_outdoor, "")
        self.tab_camera = QtWidgets.QWidget()
        self.tab_camera.setObjectName("tab_camera")
        self.start_stream_button = QtWidgets.QPushButton(self.tab_camera)
        self.start_stream_button.setGeometry(QtCore.QRect(250, 120, 171, 61))
        self.start_stream_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #1565C0;\n"
"  color: #1565C0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #42A5F5;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #64B5F6;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.start_stream_button.setObjectName("start_stream_button")
        self.stop_stream_button = QtWidgets.QPushButton(self.tab_camera)
        self.stop_stream_button.setGeometry(QtCore.QRect(480, 120, 171, 61))
        self.stop_stream_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #C62828;\n"
"  color: #C62828;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #EF5350;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #E57373;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.stop_stream_button.setObjectName("stop_stream_button")
        self.tabWidget.addTab(self.tab_camera, "")
        self.tab_message = QtWidgets.QWidget()
        self.tab_message.setMouseTracking(True)
        self.tab_message.setObjectName("tab_message")
        self.message_send_button = QtWidgets.QPushButton(self.tab_message)
        self.message_send_button.setGeometry(QtCore.QRect(700, 250, 88, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.message_send_button.setFont(font)
        self.message_send_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.message_send_button.setStyleSheet("QPushButton{\n"
"  background-color: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #2E7D32;\n"
"  color: #2E7D32;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66BB6A;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #81C784;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.message_send_button.setObjectName("message_send_button")
        self.message_clear_button = QtWidgets.QPushButton(self.tab_message)
        self.message_clear_button.setGeometry(QtCore.QRect(800, 250, 88, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.message_clear_button.setFont(font)
        self.message_clear_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.message_clear_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #C62828;\n"
"  color: #C62828;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #EF5350;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #E57373;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.message_clear_button.setObjectName("message_clear_button")
        self.message_text = QtWidgets.QTextEdit(self.tab_message)
        self.message_text.setGeometry(QtCore.QRect(17, 30, 875, 205))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.message_text.setFont(font)
        self.message_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.message_text.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.message_text.setStyleSheet("QTextEdit {\n"
"color: #424242;\n"
"padding: 2px;\n"
"border: 1px solid #CCCCCC;\n"
"}\n"
"")
        self.message_text.setTabStopWidth(40)
        self.message_text.setAcceptRichText(False)
        self.message_text.setObjectName("message_text")
        self.tabWidget.addTab(self.tab_message, "")
        self.tab_database = QtWidgets.QWidget()
        self.tab_database.setObjectName("tab_database")
        self.table = QtWidgets.QTableWidget(self.tab_database)
        self.table.setGeometry(QtCore.QRect(8, 60, 893, 231))
        self.table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table.setStyleSheet("QTableView {\n"
"    background-color : none;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    color: #424242;\n"
"}\n"
"")
        self.table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table.setShowGrid(True)
        self.table.setObjectName("table")
        self.table.setColumnCount(10)
        self.table.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table.setItem(1, 3, item)
        self.layoutWidget = QtWidgets.QWidget(self.tab_database)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 5, 461, 46))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.level_combobox = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.level_combobox.sizePolicy().hasHeightForWidth())
        self.level_combobox.setSizePolicy(sizePolicy)
        self.level_combobox.setMinimumSize(QtCore.QSize(107, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.level_combobox.setFont(font)
        self.level_combobox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.level_combobox.setStyleSheet("")
        self.level_combobox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.level_combobox.setFrame(True)
        self.level_combobox.setObjectName("level_combobox")
        self.level_combobox.addItem("")
        self.level_combobox.addItem("")
        self.level_combobox.addItem("")
        self.level_combobox.addItem("")
        self.level_combobox.addItem("")
        self.horizontalLayout.addWidget(self.level_combobox)
        self.section_combobox = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.section_combobox.sizePolicy().hasHeightForWidth())
        self.section_combobox.setSizePolicy(sizePolicy)
        self.section_combobox.setMinimumSize(QtCore.QSize(107, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.section_combobox.setFont(font)
        self.section_combobox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.section_combobox.setStyleSheet("")
        self.section_combobox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.section_combobox.setFrame(True)
        self.section_combobox.setObjectName("section_combobox")
        self.section_combobox.addItem("")
        self.section_combobox.addItem("")
        self.horizontalLayout.addWidget(self.section_combobox)
        self.subject_combobox = QtWidgets.QComboBox(self.layoutWidget)
        self.subject_combobox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subject_combobox.sizePolicy().hasHeightForWidth())
        self.subject_combobox.setSizePolicy(sizePolicy)
        self.subject_combobox.setMinimumSize(QtCore.QSize(0, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.subject_combobox.setFont(font)
        self.subject_combobox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.subject_combobox.setStyleSheet("")
        self.subject_combobox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.subject_combobox.setIconSize(QtCore.QSize(18, 18))
        self.subject_combobox.setFrame(True)
        self.subject_combobox.setObjectName("subject_combobox")
        self.subject_combobox.addItem("")
        self.subject_combobox.addItem("")
        self.subject_combobox.addItem("")
        self.subject_combobox.addItem("")
        self.subject_combobox.addItem("")
        self.horizontalLayout.addWidget(self.subject_combobox)
        self.search_lineedit = QtWidgets.QLineEdit(self.tab_database)
        self.search_lineedit.setGeometry(QtCore.QRect(720, 12, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_lineedit.setFont(font)
        self.search_lineedit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.search_lineedit.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border: 0px;\n"
"        border-bottom: 1px solid #9E9E9E;\n"
"    color: #424242;\n"
"    padding: 0 4px 0 20px;\n"
"    selection-background-color: #42A5F5;\n"
"    selection-color: #ffffff;\n"
"    background-image: url(:/icons/ui/search.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: left;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"        border-bottom: 1px solid #1565C0;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"        border-bottom: 1px solid #1565C0;\n"
"}\n"
"\n"
"")
        self.search_lineedit.setObjectName("search_lineedit")
        self.refresh_button = QtWidgets.QPushButton(self.tab_database)
        self.refresh_button.setGeometry(QtCore.QRect(480, 17, 31, 31))
        self.refresh_button.setMinimumSize(QtCore.QSize(31, 31))
        self.refresh_button.setMaximumSize(QtCore.QSize(31, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.refresh_button.setFont(font)
        self.refresh_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.refresh_button.setStyleSheet("QPushButton{\n"
"    background: transparent;\n"
"    border: 0px;\n"
"    image: url(:/icons/ui/refresh_normal.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    image: url(:/icons/ui/refresh_hover.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    image: url(:/icons/ui/refresh_pressed.png);\n"
"}\n"
"\n"
"")
        self.refresh_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/ui/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_button.setIcon(icon1)
        self.refresh_button.setIconSize(QtCore.QSize(20, 20))
        self.refresh_button.setObjectName("refresh_button")
        self.layoutWidget.raise_()
        self.table.raise_()
        self.search_lineedit.raise_()
        self.refresh_button.raise_()
        self.tabWidget.addTab(self.tab_database, "")
        self.room_frame = QtWidgets.QFrame(self.centralwidget)
        self.room_frame.setGeometry(QtCore.QRect(10, 361, 441, 178))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.room_frame.setFont(font)
        self.room_frame.setStyleSheet("background: #E0E0E0;\n"
"border-radius: 2px;\n"
"color: #424242;")
        self.room_frame.setObjectName("room_frame")
        self.layoutWidget_2 = QtWidgets.QWidget(self.room_frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(90, 20, 61, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.in_light_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_light_label.setFont(font)
        self.in_light_label.setStyleSheet("")
        self.in_light_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_light_label.setObjectName("in_light_label")
        self.verticalLayout_4.addWidget(self.in_light_label)
        self.in_fan_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_fan_label.setFont(font)
        self.in_fan_label.setStyleSheet("")
        self.in_fan_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_fan_label.setObjectName("in_fan_label")
        self.verticalLayout_4.addWidget(self.in_fan_label)
        self.in_air_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_air_label.setFont(font)
        self.in_air_label.setStyleSheet("")
        self.in_air_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_air_label.setObjectName("in_air_label")
        self.verticalLayout_4.addWidget(self.in_air_label)
        self.in_curtain_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_curtain_label.setFont(font)
        self.in_curtain_label.setStyleSheet("")
        self.in_curtain_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_curtain_label.setObjectName("in_curtain_label")
        self.verticalLayout_4.addWidget(self.in_curtain_label)
        self.in_door_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_door_label.setFont(font)
        self.in_door_label.setStyleSheet("")
        self.in_door_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_door_label.setObjectName("in_door_label")
        self.verticalLayout_4.addWidget(self.in_door_label)
        self.layoutWidget_4 = QtWidgets.QWidget(self.room_frame)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 20, 81, 131))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.in_close_button = QtWidgets.QPushButton(self.room_frame)
        self.in_close_button.setGeometry(QtCore.QRect(373, 115, 61, 30))
        self.in_close_button.setMinimumSize(QtCore.QSize(61, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_close_button.setFont(font)
        self.in_close_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_close_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #C62828;\n"
"  color: #C62828;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #EF5350;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #E57373;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_close_button.setObjectName("in_close_button")
        self.in_open_button = QtWidgets.QPushButton(self.room_frame)
        self.in_open_button.setGeometry(QtCore.QRect(373, 35, 61, 30))
        self.in_open_button.setMinimumSize(QtCore.QSize(61, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_open_button.setFont(font)
        self.in_open_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_open_button.setStyleSheet("QPushButton{\n"
"  background-color: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #2E7D32;\n"
"  color: #2E7D32;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66BB6A;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #81C784;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_open_button.setObjectName("in_open_button")
        self.layoutWidget_6 = QtWidgets.QWidget(self.room_frame)
        self.layoutWidget_6.setGeometry(QtCore.QRect(205, 20, 91, 51))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_7.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_7.addWidget(self.label_21)
        self.layoutWidget_9 = QtWidgets.QWidget(self.room_frame)
        self.layoutWidget_9.setGeometry(QtCore.QRect(295, 20, 61, 51))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.in_temp_label = QtWidgets.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_temp_label.setFont(font)
        self.in_temp_label.setStyleSheet("")
        self.in_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_temp_label.setObjectName("in_temp_label")
        self.verticalLayout_10.addWidget(self.in_temp_label)
        self.in_alarm_label = QtWidgets.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_alarm_label.setFont(font)
        self.in_alarm_label.setStyleSheet("")
        self.in_alarm_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_alarm_label.setObjectName("in_alarm_label")
        self.verticalLayout_10.addWidget(self.in_alarm_label)
        self.layoutWidget_3 = QtWidgets.QWidget(self.room_frame)
        self.layoutWidget_3.setGeometry(QtCore.QRect(150, 20, 41, 131))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.layoutWidget_3.setFont(font)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.in_light_level_label = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_light_level_label.setFont(font)
        self.in_light_level_label.setStyleSheet("")
        self.in_light_level_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_light_level_label.setObjectName("in_light_level_label")
        self.verticalLayout_5.addWidget(self.in_light_level_label)
        self.in_fan_level_label = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_fan_level_label.setFont(font)
        self.in_fan_level_label.setStyleSheet("")
        self.in_fan_level_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_fan_level_label.setObjectName("in_fan_level_label")
        self.verticalLayout_5.addWidget(self.in_fan_level_label)
        self.in_air_level_label = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_air_level_label.setFont(font)
        self.in_air_level_label.setStyleSheet("")
        self.in_air_level_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_air_level_label.setObjectName("in_air_level_label")
        self.verticalLayout_5.addWidget(self.in_air_level_label)
        self.in_curtain_level_label = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_curtain_level_label.setFont(font)
        self.in_curtain_level_label.setStyleSheet("")
        self.in_curtain_level_label.setText("")
        self.in_curtain_level_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_curtain_level_label.setObjectName("in_curtain_level_label")
        self.verticalLayout_5.addWidget(self.in_curtain_level_label)
        self.in_door_level_label = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.in_door_level_label.setFont(font)
        self.in_door_level_label.setStyleSheet("")
        self.in_door_level_label.setText("")
        self.in_door_level_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_door_level_label.setObjectName("in_door_level_label")
        self.verticalLayout_5.addWidget(self.in_door_level_label)
        self.in_alarm_button = QtWidgets.QPushButton(self.room_frame)
        self.in_alarm_button.setGeometry(QtCore.QRect(373, 75, 61, 30))
        self.in_alarm_button.setMinimumSize(QtCore.QSize(61, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.in_alarm_button.setFont(font)
        self.in_alarm_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_alarm_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #1565C0;\n"
"  color: #1565C0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #42A5F5;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #64B5F6;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.in_alarm_button.setObjectName("in_alarm_button")
        self.layoutWidget_4.raise_()
        self.layoutWidget_2.raise_()
        self.in_close_button.raise_()
        self.in_open_button.raise_()
        self.layoutWidget_6.raise_()
        self.layoutWidget_9.raise_()
        self.layoutWidget_3.raise_()
        self.in_alarm_button.raise_()
        self.indoor_label = QtWidgets.QLabel(self.centralwidget)
        self.indoor_label.setGeometry(QtCore.QRect(10, 340, 61, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.indoor_label.setFont(font)
        self.indoor_label.setStyleSheet("background: #E0E0E0;\n"
"border-radius: 2px;\n"
"color: #424242;")
        self.indoor_label.setAlignment(QtCore.Qt.AlignCenter)
        self.indoor_label.setObjectName("indoor_label")
        self.outdoor_frame = QtWidgets.QFrame(self.centralwidget)
        self.outdoor_frame.setGeometry(QtCore.QRect(460, 361, 441, 178))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.outdoor_frame.setFont(font)
        self.outdoor_frame.setStyleSheet("background: #E0E0E0;\n"
"border-radius: 2px;\n"
"color: #424242;")
        self.outdoor_frame.setObjectName("outdoor_frame")
        self.layoutWidget_5 = QtWidgets.QWidget(self.outdoor_frame)
        self.layoutWidget_5.setGeometry(QtCore.QRect(80, 20, 51, 51))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.out_light_label = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.out_light_label.setFont(font)
        self.out_light_label.setStyleSheet("")
        self.out_light_label.setAlignment(QtCore.Qt.AlignCenter)
        self.out_light_label.setObjectName("out_light_label")
        self.verticalLayout_6.addWidget(self.out_light_label)
        self.out_irri_label = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.out_irri_label.setFont(font)
        self.out_irri_label.setStyleSheet("")
        self.out_irri_label.setAlignment(QtCore.Qt.AlignCenter)
        self.out_irri_label.setObjectName("out_irri_label")
        self.verticalLayout_6.addWidget(self.out_irri_label)
        self.layoutWidget_7 = QtWidgets.QWidget(self.outdoor_frame)
        self.layoutWidget_7.setGeometry(QtCore.QRect(10, 20, 71, 51))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_8.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_8.addWidget(self.label_19)
        self.layoutWidget_8 = QtWidgets.QWidget(self.outdoor_frame)
        self.layoutWidget_8.setGeometry(QtCore.QRect(130, 20, 41, 51))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.out_light_level_label = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.out_light_level_label.setFont(font)
        self.out_light_level_label.setStyleSheet("  color: #424242;")
        self.out_light_level_label.setAlignment(QtCore.Qt.AlignCenter)
        self.out_light_level_label.setObjectName("out_light_level_label")
        self.verticalLayout_9.addWidget(self.out_light_level_label)
        self.out_irri_level_label = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.out_irri_level_label.setFont(font)
        self.out_irri_level_label.setStyleSheet("  color: #424242;")
        self.out_irri_level_label.setAlignment(QtCore.Qt.AlignCenter)
        self.out_irri_level_label.setObjectName("out_irri_level_label")
        self.verticalLayout_9.addWidget(self.out_irri_level_label)
        self.layoutWidget_10 = QtWidgets.QWidget(self.outdoor_frame)
        self.layoutWidget_10.setGeometry(QtCore.QRect(195, 20, 91, 81))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget_10)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_11.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_11.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_11.addWidget(self.label_24)
        self.layoutWidget_11 = QtWidgets.QWidget(self.outdoor_frame)
        self.layoutWidget_11.setGeometry(QtCore.QRect(285, 20, 61, 81))
        self.layoutWidget_11.setObjectName("layoutWidget_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget_11)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.out_temp_label = QtWidgets.QLabel(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.out_temp_label.setFont(font)
        self.out_temp_label.setStyleSheet("")
        self.out_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.out_temp_label.setObjectName("out_temp_label")
        self.verticalLayout_12.addWidget(self.out_temp_label)
        self.out_hum_label = QtWidgets.QLabel(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.out_hum_label.setFont(font)
        self.out_hum_label.setStyleSheet("")
        self.out_hum_label.setAlignment(QtCore.Qt.AlignCenter)
        self.out_hum_label.setObjectName("out_hum_label")
        self.verticalLayout_12.addWidget(self.out_hum_label)
        self.out_alarm_label = QtWidgets.QLabel(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.out_alarm_label.setFont(font)
        self.out_alarm_label.setStyleSheet("")
        self.out_alarm_label.setAlignment(QtCore.Qt.AlignCenter)
        self.out_alarm_label.setObjectName("out_alarm_label")
        self.verticalLayout_12.addWidget(self.out_alarm_label)
        self.out_alarm_button = QtWidgets.QPushButton(self.outdoor_frame)
        self.out_alarm_button.setGeometry(QtCore.QRect(373, 75, 61, 30))
        self.out_alarm_button.setMinimumSize(QtCore.QSize(61, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.out_alarm_button.setFont(font)
        self.out_alarm_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.out_alarm_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #1565C0;\n"
"  color: #1565C0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #42A5F5;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #64B5F6;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.out_alarm_button.setObjectName("out_alarm_button")
        self.out_close_button = QtWidgets.QPushButton(self.outdoor_frame)
        self.out_close_button.setGeometry(QtCore.QRect(373, 115, 61, 30))
        self.out_close_button.setMinimumSize(QtCore.QSize(61, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.out_close_button.setFont(font)
        self.out_close_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.out_close_button.setStyleSheet("QPushButton{\n"
"  background: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #C62828;\n"
"  color: #C62828;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #EF5350;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #E57373;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.out_close_button.setObjectName("out_close_button")
        self.out_open_button = QtWidgets.QPushButton(self.outdoor_frame)
        self.out_open_button.setGeometry(QtCore.QRect(373, 35, 61, 30))
        self.out_open_button.setMinimumSize(QtCore.QSize(61, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.out_open_button.setFont(font)
        self.out_open_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.out_open_button.setStyleSheet("QPushButton{\n"
"  background-color: transparent;\n"
"  border-radius: 2px;\n"
"  border: 1px solid #2E7D32;\n"
"  color: #2E7D32;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #66BB6A;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #81C784;\n"
"  border-width: 0px;\n"
"  color: #ffffff;\n"
"}")
        self.out_open_button.setObjectName("out_open_button")
        self.outdoor_label = QtWidgets.QLabel(self.centralwidget)
        self.outdoor_label.setGeometry(QtCore.QRect(460, 340, 81, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.outdoor_label.setFont(font)
        self.outdoor_label.setStyleSheet("background: #E0E0E0;\n"
"border-radius: 2px;\n"
"color: #424242;")
        self.outdoor_label.setAlignment(QtCore.Qt.AlignCenter)
        self.outdoor_label.setObjectName("outdoor_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kontrol"))
        self.in_light_percentage.setText(_translate("MainWindow", "0%"))
        self.in_light_on_button.setText(_translate("MainWindow", "ON"))
        self.indoor_lights.setText(_translate("MainWindow", "Lights"))
        self.in_fan_on_button.setText(_translate("MainWindow", "ON"))
        self.in_air_auto_button.setText(_translate("MainWindow", "Auto"))
        self.in_light_off_button.setText(_translate("MainWindow", "OFF"))
        self.in_curtain_auto_button.setText(_translate("MainWindow", "Auto"))
        self.in_curtain_on_button.setText(_translate("MainWindow", "ON"))
        self.in_air_on_button.setText(_translate("MainWindow", "ON"))
        self.in_air_off_button.setText(_translate("MainWindow", "OFF"))
        self.in_light_auto_button.setText(_translate("MainWindow", "Auto"))
        self.indoor_curtains.setText(_translate("MainWindow", "Curtains"))
        self.indoor_fans.setText(_translate("MainWindow", "Fans"))
        self.in_curtain_off_button.setText(_translate("MainWindow", "OFF"))
        self.in_fan_off_button.setText(_translate("MainWindow", "OFF"))
        self.in_fan_auto_button.setText(_translate("MainWindow", "Auto"))
        self.in_door_open_button.setText(_translate("MainWindow", "OPEN"))
        self.indoor_air.setText(_translate("MainWindow", "Air Conditioner"))
        self.in_fan_percentage.setText(_translate("MainWindow", "0%"))
        self.in_door_close_button.setText(_translate("MainWindow", "CLOSE"))
        self.indoor_door.setText(_translate("MainWindow", "Door"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_indoor), _translate("MainWindow", "Indoor"))
        self.outdoor_lights.setText(_translate("MainWindow", "Lights"))
        self.out_light_auto_button.setText(_translate("MainWindow", "Auto"))
        self.out_light_percentage.setText(_translate("MainWindow", "0%"))
        self.out_light_on_button.setText(_translate("MainWindow", "ON"))
        self.out_light_off_button.setText(_translate("MainWindow", "OFF"))
        self.out_irri_auto_button.setText(_translate("MainWindow", "Auto"))
        self.out_irri_on_button.setText(_translate("MainWindow", "ON"))
        self.outdoor_irrigation.setText(_translate("MainWindow", "Irrigation"))
        self.out_irri_off_button.setText(_translate("MainWindow", "OFF"))
        self.out_irri_percentage.setText(_translate("MainWindow", "0%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_outdoor), _translate("MainWindow", "Outdoor"))
        self.start_stream_button.setText(_translate("MainWindow", "START STREAMING"))
        self.stop_stream_button.setText(_translate("MainWindow", "STOP STREAMING"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_camera), _translate("MainWindow", "Camera"))
        self.message_send_button.setText(_translate("MainWindow", "Send"))
        self.message_clear_button.setText(_translate("MainWindow", "Clear"))
        self.message_text.setPlaceholderText(_translate("MainWindow", "Type your message here ..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_message), _translate("MainWindow", "Message"))
        self.table.setSortingEnabled(True)
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Code"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Year"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "UID"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "S1"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "S2"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "S3"))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "S4"))
        item = self.table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "S5"))
        item = self.table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "S6"))
        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        self.table.setSortingEnabled(__sortingEnabled)
        self.level_combobox.setItemText(0, _translate("MainWindow", "Level 1"))
        self.level_combobox.setItemText(1, _translate("MainWindow", "Level 2"))
        self.level_combobox.setItemText(2, _translate("MainWindow", "Level 3"))
        self.level_combobox.setItemText(3, _translate("MainWindow", "Level 4"))
        self.level_combobox.setItemText(4, _translate("MainWindow", "Level 5"))
        self.section_combobox.setItemText(0, _translate("MainWindow", "Section 1"))
        self.section_combobox.setItemText(1, _translate("MainWindow", "Section 2"))
        self.subject_combobox.setItemText(0, _translate("MainWindow", "Antenna"))
        self.subject_combobox.setItemText(1, _translate("MainWindow", "Networks"))
        self.subject_combobox.setItemText(2, _translate("MainWindow", "Communication Systems"))
        self.subject_combobox.setItemText(3, _translate("MainWindow", "Signal Processing"))
        self.subject_combobox.setItemText(4, _translate("MainWindow", "Selective Subjects"))
        self.search_lineedit.setPlaceholderText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_database), _translate("MainWindow", "Database"))
        self.in_light_label.setText(_translate("MainWindow", "-"))
        self.in_fan_label.setText(_translate("MainWindow", "-"))
        self.in_air_label.setText(_translate("MainWindow", "-"))
        self.in_curtain_label.setText(_translate("MainWindow", "-"))
        self.in_door_label.setText(_translate("MainWindow", "-"))
        self.label_8.setText(_translate("MainWindow", "Light"))
        self.label_9.setText(_translate("MainWindow", "Fan"))
        self.label_10.setText(_translate("MainWindow", "Conditioner"))
        self.label_11.setText(_translate("MainWindow", "Curtains"))
        self.label_12.setText(_translate("MainWindow", "Door"))
        self.in_close_button.setText(_translate("MainWindow", "CLOSE"))
        self.in_open_button.setText(_translate("MainWindow", "OPEN"))
        self.label_20.setText(_translate("MainWindow", "Tempreature"))
        self.label_21.setText(_translate("MainWindow", "Alarm Mode"))
        self.in_temp_label.setText(_translate("MainWindow", "-"))
        self.in_alarm_label.setText(_translate("MainWindow", "-"))
        self.in_light_level_label.setText(_translate("MainWindow", "-"))
        self.in_fan_level_label.setText(_translate("MainWindow", "-"))
        self.in_air_level_label.setText(_translate("MainWindow", "-"))
        self.in_alarm_button.setText(_translate("MainWindow", "ALARM"))
        self.indoor_label.setText(_translate("MainWindow", "Indoor"))
        self.out_light_label.setText(_translate("MainWindow", "-"))
        self.out_irri_label.setText(_translate("MainWindow", "-"))
        self.label_18.setText(_translate("MainWindow", "Light"))
        self.label_19.setText(_translate("MainWindow", "Irrigation"))
        self.out_light_level_label.setText(_translate("MainWindow", "-"))
        self.out_irri_level_label.setText(_translate("MainWindow", "-"))
        self.label_22.setText(_translate("MainWindow", "Tempreature"))
        self.label_23.setText(_translate("MainWindow", "Humidity"))
        self.label_24.setText(_translate("MainWindow", "Alarm Mode"))
        self.out_temp_label.setText(_translate("MainWindow", "-"))
        self.out_hum_label.setText(_translate("MainWindow", "-"))
        self.out_alarm_label.setText(_translate("MainWindow", "-"))
        self.out_alarm_button.setText(_translate("MainWindow", "ALARM"))
        self.out_close_button.setText(_translate("MainWindow", "CLOSE"))
        self.out_open_button.setText(_translate("MainWindow", "OPEN"))
        self.outdoor_label.setText(_translate("MainWindow", "Outdoor"))

import resources_rc
