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
		self.populate_config()

		# Slots
		self.ui.configButtonBox.rejected.connect(self.close)
		self.ui.configButtonBox.accepted.connect(self.save_config)
		self.ui.dataDirAutoGenPushButton.clicked.connect(self.auto_gen_data_dir)

	def populate_config(self):
		# General group
		self.ui.lspLineEdit.setText(config.get('General', 'lsp'))
		self.ui.tmpDirLineEdit.setText(config.get('Directories', 'tmp'))
		self.ui.dataDirLineEdit.setText(config.get('Directories', 'data'))
		self.ui.themeDirLineEdit.setText(config.get('Directories', 'themes'))
		self.ui.presetDirLineEdit.setText(config.get('Directories', 'presets'))

	def auto_gen_data_dir(self):
		self.ui.dataDirLineEdit.setText(generate_data_dir())

	def save_config(self):
		# General group
		config.set('General', 'lsp', self.ui.lspLineEdit.text())
		config.set('Directories', 'tmp', os.path.normpath(self.ui.tmpDirLineEdit.text()))
		config.set('Directories', 'data', os.path.normpath(self.ui.dataDirLineEdit.text()))
		config.set('Directories', 'themes', os.path.normpath(self.ui.themeDirLineEdit.text()))
		config.set('Directories', 'presets', os.path.normpath(self.ui.presetDirLineEdit.text()))
		config.save()

		self.close()