#!/usr/bin/env python
import os, sys
from inc.config import Config
from PySide.QtGui import QApplication
from ui.mainwindow import MainWindow

config = Config()
config.load()

# Create tmp directory if it doesn't exist
if not os.path.exists(os.path.join(os.getcwd(), 'tmp')):
	os.mkdir(os.path.join(os.getcwd(), 'tmp'))
	os.chmod(os.path.join(os.getcwd(), 'tmp'), 0777)

# The app
if __name__ == '__main__':
	# Create app
	app = QApplication(sys.argv)
	app.setApplicationName('LMMS Theme Installer')

	# Configuration wizard
	if config.get('Wizard', 'firstrun') == 'True':
		from ui.firstrunwizard import FirstRunWizardWindow
		wizard = FirstRunWizardWindow()
		wizard.show()

	# Show window
	window = MainWindow()
	window.show()

	# Closed connection
	app.lastWindowClosed.connect(app.quit)

	# Run it
	sys.exit(app.exec_())