import os
from inc.functions import *
from PySide.QtCore import Signal, QObject
from PySide.QtGui import QLineEdit, QMainWindow
from ui.configuration import Ui_Configuration

# Config
config = Config()
config.read(os.path.join(os.getcwd(), 'config.cfg'))

class ConfigurationWindow(QMainWindow, QObject):
	changed = Signal()

	def __init__(self):
		super(ConfigurationWindow, self).__init__()
		self.ui = Ui_Configuration()
		self.ui.setupUi(self)
		self.populateConfig()

		# Slots
		self.ui.configButtonBox.rejected.connect(self.close)
		self.ui.configButtonBox.accepted.connect(self.saveConfig)

	def populateConfig(self):
		# General group
		self.ui.lspLineEdit.setText(config.get('General', 'lsp'))
		self.ui.tmpDirLineEdit.setText(config.get('General', 'tmp'))
		self.ui.themeDirLineEdit.setText(config.get('General', 'theme_dir'))

	def saveConfig(self):
		# General group
		config.set('General', 'lsp', self.ui.lspLineEdit.text())
		config.set('General', 'tmp', self.ui.tmpDirLineEdit.text())
		config.set('General', 'theme_dir', self.ui.themeDirLineEdit.text())
		config.write(open(os.path.join(os.getcwd(), 'config.cfg'), 'wb'))

		self.changed.emit()
		self.close()