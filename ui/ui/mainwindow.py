# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\DO NOT MOVE\Desktop\LMMS Theme Installer\ui\ui\mainwindow.ui'
#
# Created: Sun Dec 02 19:44:43 2012
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(673, 395)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_4 = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.themeListWidget = QtGui.QListWidget(self.centralWidget)
        self.themeListWidget.setObjectName("themeListWidget")
        self.gridLayout_4.addWidget(self.themeListWidget, 0, 0, 1, 1)
        self.descriptionWebView = QtWebKit.QWebView(self.centralWidget)
        self.descriptionWebView.setUrl(QtCore.QUrl("about:blank"))
        self.descriptionWebView.setObjectName("descriptionWebView")
        self.gridLayout_4.addWidget(self.descriptionWebView, 0, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 3)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 673, 21))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setObjectName("menuBar")
        self.menu_File = QtGui.QMenu(self.menuBar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtGui.QMenu(self.menuBar)
        self.menu_Edit.setEnabled(True)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Help = QtGui.QMenu(self.menuBar)
        self.menu_Help.setEnabled(False)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOptions = QtGui.QAction(MainWindow)
        self.actionOptions.setEnabled(True)
        self.actionOptions.setObjectName("actionOptions")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu_File.addAction(self.actionExit)
        self.menu_Edit.addAction(self.actionOptions)
        self.menu_Help.addAction(self.actionAbout)
        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menu_Edit.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "LMMS Theme Installer", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOptions.setText(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
