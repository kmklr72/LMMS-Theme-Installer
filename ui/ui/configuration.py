# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\DO NOT MOVE\My Documents\GitHub\LMMS-Theme-Installer\ui\ui\configuration.ui'
#
# Created: Fri Dec 07 21:38:28 2012
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Configuration(object):
    def setupUi(self, Configuration):
        Configuration.setObjectName("Configuration")
        Configuration.resize(342, 184)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Configuration.sizePolicy().hasHeightForWidth())
        Configuration.setSizePolicy(sizePolicy)
        Configuration.setMinimumSize(QtCore.QSize(342, 102))
        Configuration.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralWidget = QtGui.QWidget(Configuration)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.generalGroupBox = QtGui.QGroupBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generalGroupBox.sizePolicy().hasHeightForWidth())
        self.generalGroupBox.setSizePolicy(sizePolicy)
        self.generalGroupBox.setObjectName("generalGroupBox")
        self.formLayout = QtGui.QFormLayout(self.generalGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.lspLabel = QtGui.QLabel(self.generalGroupBox)
        self.lspLabel.setObjectName("lspLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lspLabel)
        self.lspLineEdit = QtGui.QLineEdit(self.generalGroupBox)
        self.lspLineEdit.setObjectName("lspLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lspLineEdit)
        self.tmpDirLabel = QtGui.QLabel(self.generalGroupBox)
        self.tmpDirLabel.setObjectName("tmpDirLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.tmpDirLabel)
        self.tmpDirLineEdit = QtGui.QLineEdit(self.generalGroupBox)
        self.tmpDirLineEdit.setObjectName("tmpDirLineEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.tmpDirLineEdit)
        self.themeDirLabel = QtGui.QLabel(self.generalGroupBox)
        self.themeDirLabel.setObjectName("themeDirLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.themeDirLabel)
        self.themeDirLineEdit = QtGui.QLineEdit(self.generalGroupBox)
        self.themeDirLineEdit.setObjectName("themeDirLineEdit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.themeDirLineEdit)
        self.themeDirAutoGenPushButton = QtGui.QPushButton(self.generalGroupBox)
        self.themeDirAutoGenPushButton.setObjectName("themeDirAutoGenPushButton")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.themeDirAutoGenPushButton)
        self.gridLayout.addWidget(self.generalGroupBox, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.configButtonBox = QtGui.QDialogButtonBox(self.centralWidget)
        self.configButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.configButtonBox.setObjectName("configButtonBox")
        self.horizontalLayout_2.addWidget(self.configButtonBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        Configuration.setCentralWidget(self.centralWidget)
        self.actionExit = QtGui.QAction(Configuration)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(Configuration)
        QtCore.QMetaObject.connectSlotsByName(Configuration)

    def retranslateUi(self, Configuration):
        Configuration.setWindowTitle(QtGui.QApplication.translate("Configuration", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.generalGroupBox.setTitle(QtGui.QApplication.translate("Configuration", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.lspLabel.setText(QtGui.QApplication.translate("Configuration", "LMMS SP URL", None, QtGui.QApplication.UnicodeUTF8))
        self.tmpDirLabel.setText(QtGui.QApplication.translate("Configuration", "Temp Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.themeDirLabel.setText(QtGui.QApplication.translate("Configuration", "Theme Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.themeDirAutoGenPushButton.setText(QtGui.QApplication.translate("Configuration", "Auto Generate Theme Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("Configuration", "Exit", None, QtGui.QApplication.UnicodeUTF8))

