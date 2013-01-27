import os
from inc.functions import *
from PySide.QtGui import QWizard
from ui.firstrunwizard import Ui_FirstRunWizard

class FirstRunWizardWindow(QWizard):
	def __init__(self):
		super(FirstRunWizardWindow, self).__init__()
		self.ui = Ui_FirstRunWizard()
		self.ui.setupUi(self)
		self.populateConfig()

		# Slots
		self.finished.connect(self.saveConfig)

	def populateConfig(self):
		# General group
		self.ui.themeDirLineEdit.setText(generate_data_dir())

	def saveConfig(self):
		# Directories group
		config.set('Directories', 'data', os.path.normpath(self.ui.themeDirLineEdit.text()))

		# Wizard group
		config.set('Wizard', 'firstrun', 'False')

		config.save()