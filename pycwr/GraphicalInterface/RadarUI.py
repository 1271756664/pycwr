# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeatherRadar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import matplotlib
# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import cartopy.crs as ccrs

# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def get_fig_ax(self):
        self.ax = self.fig.add_axes([0.035, 0.06, 0.88, 0.88])
        self.cax = self.fig.add_axes([0.9, 0.06, 0.028, 0.88])
        return self.fig, self.ax, self.cax

    def get_fig_ax_map(self):
        self.ax = self.fig.add_axes([0.06, 0.025, 0.82, 0.95], projection=ccrs.PlateCarree())
        self.cax = self.fig.add_axes([0.91, 0.1, 0.028, 0.8])
        return self.fig, self.ax, self.cax


# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)  # Inherit from QWidget
        self.canvas = MplCanvas()  # Create canvas object
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.vbl = QtWidgets.QVBoxLayout()  # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.ntb)
        self.setLayout(self.vbl)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1148, 909)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/icon/icons8-gps-antenna-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MplWidget = MplWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.MplWidget.sizePolicy().hasHeightForWidth())
        self.MplWidget.setSizePolicy(sizePolicy)
        self.MplWidget.setMinimumSize(QtCore.QSize(550, 550))
        self.MplWidget.setObjectName("MplWidget")
        self.horizontalLayout_2.addWidget(self.MplWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(20, 10))
        font = QtGui.QFont()
        font.setFamily("????????????")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setToolTipDuration(-1)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_15 = QtWidgets.QRadioButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_15.sizePolicy().hasHeightForWidth())
        self.radioButton_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_15.setFont(font)
        self.radioButton_15.setObjectName("radioButton_15")
        self.gridLayout_2.addWidget(self.radioButton_15, 2, 1, 1, 1)
        self.radioButton_12 = QtWidgets.QRadioButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_12.sizePolicy().hasHeightForWidth())
        self.radioButton_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_12.setFont(font)
        self.radioButton_12.setObjectName("radioButton_12")
        self.gridLayout_2.addWidget(self.radioButton_12, 2, 0, 1, 1)
        self.radioButton_14 = QtWidgets.QRadioButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_14.sizePolicy().hasHeightForWidth())
        self.radioButton_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_14.setFont(font)
        self.radioButton_14.setObjectName("radioButton_14")
        self.gridLayout_2.addWidget(self.radioButton_14, 1, 1, 1, 1)
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_10.sizePolicy().hasHeightForWidth())
        self.radioButton_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("????????????")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setChecked(True)
        self.radioButton_10.setObjectName("radioButton_10")
        self.gridLayout_2.addWidget(self.radioButton_10, 0, 0, 1, 1)
        self.radioButton_13 = QtWidgets.QRadioButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_13.sizePolicy().hasHeightForWidth())
        self.radioButton_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_13.setFont(font)
        self.radioButton_13.setObjectName("radioButton_13")
        self.gridLayout_2.addWidget(self.radioButton_13, 0, 1, 1, 1)
        self.radioButton_11 = QtWidgets.QRadioButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_11.sizePolicy().hasHeightForWidth())
        self.radioButton_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_11.setFont(font)
        self.radioButton_11.setObjectName("radioButton_11")
        self.gridLayout_2.addWidget(self.radioButton_11, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(20, 10))
        font = QtGui.QFont()
        font.setFamily("????????????")
        self.groupBox.setFont(font)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("????????????")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 0, 1, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_4.sizePolicy().hasHeightForWidth())
        self.radioButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("????????????")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 1, 0, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_5.sizePolicy().hasHeightForWidth())
        self.radioButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("????????????")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 1, 1, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("????????????")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 0, 2, 1, 1)
        self.radioButton_1 = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_1.sizePolicy().hasHeightForWidth())
        self.radioButton_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("????????????")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")
        self.gridLayout.addWidget(self.radioButton_1, 0, 0, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_7.sizePolicy().hasHeightForWidth())
        self.radioButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("????????????")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout.addWidget(self.radioButton_7, 2, 0, 1, 1)
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_8.sizePolicy().hasHeightForWidth())
        self.radioButton_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("????????????")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout.addWidget(self.radioButton_8, 2, 1, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_6.sizePolicy().hasHeightForWidth())
        self.radioButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("????????????")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout.addWidget(self.radioButton_6, 1, 2, 1, 1)
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.radioButton_9.sizePolicy().hasHeightForWidth())
        self.radioButton_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("????????????")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setObjectName("radioButton_9")
        self.gridLayout.addWidget(self.radioButton_9, 2, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 50))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("????????????")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("????????????")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("????????????")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 20)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.setStretch(0, 6)
        self.verticalLayout_3.setStretch(1, 11)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.setStretch(0, 20)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1148, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu3D = QtWidgets.QMenu(self.menu_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/res/icon/icons8-virtualbox-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu3D.setIcon(icon1)
        self.menu3D.setObjectName("menu3D")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menuBar)
        self.menu_4.setObjectName("menu_4")
        self.menu_6 = QtWidgets.QMenu(self.menu_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/res/icon/icons8-support-60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_6.setIcon(icon2)
        self.menu_6.setObjectName("menu_6")
        self.menu_5 = QtWidgets.QMenu(self.menuBar)
        self.menu_5.setObjectName("menu_5")
        self.menu_7 = QtWidgets.QMenu(self.menuBar)
        self.menu_7.setObjectName("menu_7")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/res/icon/icons8-opened-folder-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionopen.setIcon(icon3)
        self.actionopen.setObjectName("actionopen")
        self.actionquit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/res/icon/icons8-exit-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionquit.setIcon(icon4)
        self.actionquit.setObjectName("actionquit")
        self.actionVVP = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/res/icon/icons8-wind-turbines-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVVP.setIcon(icon5)
        self.actionVVP.setObjectName("actionVVP")
        self.actionVAD = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/res/icon/icons8-wind-turbine-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVAD.setIcon(icon6)
        self.actionVAD.setObjectName("actionVAD")
        self.actionLWC = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/res/icon/icons8-water-steam-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLWC.setIcon(icon7)
        self.actionLWC.setObjectName("actionLWC")
        self.actionCLOUD_TOP = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/res/icon/icons8-storm-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCLOUD_TOP.setIcon(icon8)
        self.actionCLOUD_TOP.setObjectName("actionCLOUD_TOP")
        self.actionstorm_Identification = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/res/icon/icons8-lightning-bolt-40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionstorm_Identification.setIcon(icon9)
        self.actionstorm_Identification.setObjectName("actionstorm_Identification")
        self.actionCentroid_height = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/res/icon/icons8-heaven-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCentroid_height.setIcon(icon10)
        self.actionCentroid_height.setObjectName("actionCentroid_height")
        self.actionstation = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/res/icon/icons8-services-60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionstation.setIcon(icon11)
        self.actionstation.setObjectName("actionstation")
        self.actionabout_this_program = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/res/icon/icons8-dashed-cloud-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionabout_this_program.setIcon(icon12)
        self.actionabout_this_program.setObjectName("actionabout_this_program")
        self.actionabout_us = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/res/icon/icons8-people-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionabout_us.setIcon(icon13)
        self.actionabout_us.setObjectName("actionabout_us")
        self.actioncontact_us = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/res/icon/icons8-contacts-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncontact_us.setIcon(icon14)
        self.actioncontact_us.setObjectName("actioncontact_us")
        self.actionstorm_track = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/res/icon/icons8-radar-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionstorm_track.setIcon(icon15)
        self.actionstorm_track.setObjectName("actionstorm_track")
        self.actionR = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/res/icon/icons8-storm-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionR.setIcon(icon16)
        self.actionR.setObjectName("actionR")
        self.actionW = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/res/icon/icons8-soundcloud-48 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionW.setIcon(icon17)
        self.actionW.setObjectName("actionW")
        self.actionV = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/res/icon/icons8-happy-cloud-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionV.setIcon(icon18)
        self.actionV.setObjectName("actionV")
        self.actionNETCDF = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/res/icon/icons8-save-as-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNETCDF.setIcon(icon19)
        self.actionNETCDF.setObjectName("actionNETCDF")
        self.actionabout_data_format = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/res/icon/icons8-toolbox-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionabout_data_format.setIcon(icon20)
        self.actionabout_data_format.setObjectName("actionabout_data_format")
        self.actionVVP_2 = QtWidgets.QAction(MainWindow)
        self.actionVVP_2.setIcon(icon5)
        self.actionVVP_2.setObjectName("actionVVP_2")
        self.actionVAD_2 = QtWidgets.QAction(MainWindow)
        self.actionVAD_2.setIcon(icon6)
        self.actionVAD_2.setObjectName("actionVAD_2")
        self.actionLWC_2 = QtWidgets.QAction(MainWindow)
        self.actionLWC_2.setIcon(icon7)
        self.actionLWC_2.setObjectName("actionLWC_2")
        self.actionCAPPI = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/res/icon/icons8-windy-weather-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCAPPI.setIcon(icon21)
        self.actionCAPPI.setObjectName("actionCAPPI")
        self.actionCR = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/res/icon/icons8-windy-weather-64 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCR.setIcon(icon22)
        self.actionCR.setObjectName("actionCR")
        self.actioncappi = QtWidgets.QAction(MainWindow)
        self.actioncappi.setIcon(icon21)
        self.actioncappi.setObjectName("actioncappi")
        self.actioncr = QtWidgets.QAction(MainWindow)
        self.actioncr.setIcon(icon22)
        self.actioncr.setObjectName("actioncr")
        self.actiontop = QtWidgets.QAction(MainWindow)
        self.actiontop.setIcon(icon8)
        self.actiontop.setObjectName("actiontop")
        self.actionIdentification = QtWidgets.QAction(MainWindow)
        self.actionIdentification.setIcon(icon9)
        self.actionIdentification.setObjectName("actionIdentification")
        self.actiontrack = QtWidgets.QAction(MainWindow)
        self.actiontrack.setIcon(icon15)
        self.actiontrack.setObjectName("actiontrack")
        self.actionheight = QtWidgets.QAction(MainWindow)
        self.actionheight.setIcon(icon10)
        self.actionheight.setObjectName("actionheight")
        self.actionsavedir = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/res/icon/icons8-add-folder-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionsavedir.setIcon(icon23)
        self.actionsavedir.setObjectName("actionsavedir")
        self.actionopendir = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/res/icon/icons8-opened-folder-480.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionopendir.setIcon(icon24)
        self.actionopendir.setObjectName("actionopendir")
        self.actionr = QtWidgets.QAction(MainWindow)
        self.actionr.setIcon(icon16)
        self.actionr.setObjectName("actionr")
        self.actionv = QtWidgets.QAction(MainWindow)
        self.actionv.setIcon(icon18)
        self.actionv.setObjectName("actionv")
        self.actionw = QtWidgets.QAction(MainWindow)
        self.actionw.setIcon(icon17)
        self.actionw.setObjectName("actionw")
        self.actionvertical = QtWidgets.QAction(MainWindow)
        self.actionvertical.setCheckable(True)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/res/icon/icons8-soundcloud-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionvertical.setIcon(icon25)
        self.actionvertical.setObjectName("actionvertical")
        self.actionopen_2 = QtWidgets.QAction(MainWindow)
        self.actionopen_2.setIcon(icon3)
        self.actionopen_2.setObjectName("actionopen_2")
        self.actionopendir_2 = QtWidgets.QAction(MainWindow)
        self.actionopendir_2.setIcon(icon24)
        self.actionopendir_2.setObjectName("actionopendir_2")
        self.actionquit_2 = QtWidgets.QAction(MainWindow)
        self.actionquit_2.setIcon(icon4)
        self.actionquit_2.setObjectName("actionquit_2")
        self.actionwithmap = QtWidgets.QAction(MainWindow)
        self.actionwithmap.setCheckable(True)
        self.actionwithmap.setChecked(False)
        self.actionwithmap.setEnabled(True)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/res/icon/icons8-radar-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionwithmap.setIcon(icon26)
        #self.actionwithmap.setShortcutVisibleInContextMenu(False)
        self.actionwithmap.setObjectName("actionwithmap")
        self.actioncontinuous = QtWidgets.QAction(MainWindow)
        self.actioncontinuous.setCheckable(True)
        self.actioncontinuous.setChecked(False)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/res/icon/icons8-barometer-40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncontinuous.setIcon(icon27)
        self.actioncontinuous.setObjectName("actioncontinuous")
        self.menu3D.addAction(self.actionr)
        self.menu3D.addAction(self.actionv)
        self.menu3D.addAction(self.actionw)
        self.menu_2.addAction(self.actioncappi)
        self.menu_2.addAction(self.actioncr)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionVVP)
        self.menu_2.addAction(self.actionVAD)
        self.menu_2.addAction(self.actionCentroid_height)
        self.menu_2.addAction(self.actionLWC)
        self.menu_2.addAction(self.actionCLOUD_TOP)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionstorm_Identification)
        self.menu_2.addAction(self.actionstorm_track)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.menu3D.menuAction())
        self.menu_3.addAction(self.actionCAPPI)
        self.menu_3.addAction(self.actionCR)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionVVP_2)
        self.menu_3.addAction(self.actionVAD_2)
        self.menu_3.addAction(self.actionheight)
        self.menu_3.addAction(self.actionLWC_2)
        self.menu_3.addAction(self.actiontop)
        self.menu_3.addAction(self.actionIdentification)
        self.menu_3.addAction(self.actiontrack)
        self.menu_6.addAction(self.actionwithmap)
        self.menu_6.addAction(self.actioncontinuous)
        self.menu_4.addAction(self.actionsavedir)
        self.menu_4.addAction(self.menu_6.menuAction())
        self.menu_4.addAction(self.actionstation)
        self.menu_5.addAction(self.actionabout_data_format)
        self.menu_5.addSeparator()
        self.menu_5.addAction(self.actionabout_this_program)
        self.menu_5.addAction(self.actionabout_us)
        self.menu_5.addAction(self.actioncontact_us)
        self.menu_7.addAction(self.actionvertical)
        self.menu.addAction(self.actionopen_2)
        self.menu.addAction(self.actionopendir_2)
        self.menu.addSeparator()
        self.menu.addAction(self.actionquit_2)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu_7.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())
        self.menuBar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????????????????????????????????????"))
        self.MplWidget.setStatusTip(_translate("MainWindow", "????????????????????????"))
        self.groupBox_2.setStatusTip(_translate("MainWindow", "?????????????????????"))
        self.groupBox_2.setTitle(_translate("MainWindow", "????????????"))
        self.radioButton_15.setText(_translate("MainWindow", "????????????"))
        self.radioButton_12.setText(_translate("MainWindow", "??????"))
        self.radioButton_14.setText(_translate("MainWindow", "???????????????"))
        self.radioButton_10.setText(_translate("MainWindow", "???????????????"))
        self.radioButton_13.setText(_translate("MainWindow", "???????????????"))
        self.radioButton_11.setText(_translate("MainWindow", "????????????"))
        self.groupBox.setStatusTip(_translate("MainWindow", "????????????????????????"))
        self.groupBox.setTitle(_translate("MainWindow", "VCP21"))
        self.radioButton_2.setText(_translate("MainWindow", "???2???"))
        self.radioButton_4.setText(_translate("MainWindow", "???4???"))
        self.radioButton_5.setText(_translate("MainWindow", "???5???"))
        self.radioButton_3.setText(_translate("MainWindow", "???3???"))
        self.radioButton_1.setText(_translate("MainWindow", "???1???"))
        self.radioButton_7.setText(_translate("MainWindow", "???7???"))
        self.radioButton_8.setText(_translate("MainWindow", "???8???"))
        self.radioButton_6.setText(_translate("MainWindow", "???6???"))
        self.radioButton_9.setText(_translate("MainWindow", "???9???"))
        self.listWidget.setStatusTip(_translate("MainWindow", "?????????????????????"))
        self.pushButton.setText(_translate("MainWindow", "?????????"))
        self.pushButton_2.setText(_translate("MainWindow", "????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "?????????"))
        self.menu_2.setTitle(_translate("MainWindow", "??????"))
        self.menu3D.setTitle(_translate("MainWindow", "3D??????"))
        self.menu_3.setTitle(_translate("MainWindow", "??????"))
        self.menu_4.setTitle(_translate("MainWindow", "??????"))
        self.menu_6.setTitle(_translate("MainWindow", "????????????"))
        self.menu_5.setTitle(_translate("MainWindow", "??????"))
        self.menu_7.setTitle(_translate("MainWindow", "??????"))
        self.menu.setTitle(_translate("MainWindow", "??????"))
        self.actionopen.setText(_translate("MainWindow", "????????????"))
        self.actionopen.setStatusTip(_translate("MainWindow", "?????????????????????????????????"))
        self.actionquit.setText(_translate("MainWindow", "??????"))
        self.actionquit.setStatusTip(_translate("MainWindow", "????????????"))
        self.actionVVP.setText(_translate("MainWindow", "????????????"))
        self.actionVAD.setText(_translate("MainWindow", "????????????"))
        self.actionLWC.setText(_translate("MainWindow", "???????????????"))
        self.actionCLOUD_TOP.setText(_translate("MainWindow", "???????????????"))
        self.actionstorm_Identification.setText(_translate("MainWindow", "????????????"))
        self.actionCentroid_height.setText(_translate("MainWindow", "????????????"))
        self.actionstation.setText(_translate("MainWindow", "??????????????????"))
        self.actionabout_this_program.setText(_translate("MainWindow", "???????????????"))
        self.actionabout_us.setText(_translate("MainWindow", "????????????"))
        self.actioncontact_us.setText(_translate("MainWindow", "????????????"))
        self.actionstorm_track.setText(_translate("MainWindow", "????????????"))
        self.actionR.setText(_translate("MainWindow", "???????????????"))
        self.actionW.setText(_translate("MainWindow", "??????"))
        self.actionV.setText(_translate("MainWindow", "????????????"))
        self.actionNETCDF.setText(_translate("MainWindow", "????????????"))
        self.actionabout_data_format.setText(_translate("MainWindow", "????????????????????????"))
        self.actionVVP_2.setText(_translate("MainWindow", "????????????"))
        self.actionVAD_2.setText(_translate("MainWindow", "????????????"))
        self.actionLWC_2.setText(_translate("MainWindow", "???????????????"))
        self.actionCAPPI.setText(_translate("MainWindow", "CAPPI"))
        self.actionCR.setText(_translate("MainWindow", "?????????????????????"))
        self.actioncappi.setText(_translate("MainWindow", "CAPPI"))
        self.actioncr.setText(_translate("MainWindow", "?????????????????????"))
        self.actiontop.setText(_translate("MainWindow", "???????????????"))
        self.actionIdentification.setText(_translate("MainWindow", "????????????"))
        self.actiontrack.setText(_translate("MainWindow", "????????????"))
        self.actionheight.setText(_translate("MainWindow", "????????????"))
        self.actionsavedir.setText(_translate("MainWindow", "????????????"))
        self.actionopendir.setText(_translate("MainWindow", "???????????????"))
        self.actionopendir.setStatusTip(_translate("MainWindow", "????????????????????????????????????"))
        self.actionr.setText(_translate("MainWindow", "???????????????"))
        self.actionv.setText(_translate("MainWindow", "????????????"))
        self.actionw.setText(_translate("MainWindow", "??????"))
        self.actionvertical.setText(_translate("MainWindow", "????????????"))
        self.actionopen_2.setText(_translate("MainWindow", "????????????"))
        self.actionopen_2.setStatusTip(_translate("MainWindow", "????????????"))
        self.actionopendir_2.setText(_translate("MainWindow", "???????????????"))
        self.actionquit_2.setText(_translate("MainWindow", "??????"))
        self.actionwithmap.setText(_translate("MainWindow", "????????????"))
        self.actioncontinuous.setText(_translate("MainWindow", "????????????"))

