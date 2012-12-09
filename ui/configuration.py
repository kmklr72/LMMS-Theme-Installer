import os
from inc.functions import *
from PySide.QtCore import QDir
from PySide.QtGui import QLineEdit, QMainWindow
from ui.configuration import Ui_Configuration

class ConfigurationWindow(QMainWindow):
	def __init__(self):
		super(ConfigurationWindow, self).__init__()
		self.ui = Ui_Configuration()
		self.ui.setupUi(self)
		self.populateConfig()

		# Slots
		self.ui.configButtonBox.rejected.connect(self.close)
		self.ui.configButtonBox.accepted.connect(self.saveConfig)
		self.ui.themeDirAutoGenPushButton.clicked.connect(self.autoGenThemeDir)

	def populateConfig(self):
		# General group
		self.ui.lspLineEdit.setText(config.get('General', 'lsp'))
		self.ui.tmpDirLineEdit.setText(config.get('General', 'tmp'))
		self.ui.themeDirLineEdit.setText(config.get('General', 'theme_dir'))

	def autoGenThemeDir(self):
		self.ui.themeDirLineEdit.setText(generate_theme_dir())

	def saveConfig(self):
		# General group
		config.set('General', 'lsp', self.ui.lspLineEdit.text())
		config.set('General', 'tmp', os.path.normpath(self.ui.tmpDirLineEdit.text()))
		config.set('General', 'theme_dir', os.path.normpath(self.ui.themeDirLineEdit.text()))
		config.save()

		self.close()