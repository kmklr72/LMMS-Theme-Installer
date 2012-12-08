#!/usr/bin/env python
import os, sys
from PySide.QtGui import QApplication

from ui.mainwindow import MainWindow

# Create tmp directory if it doesn't exist
if not os.path.exists(os.path.join(os.getcwd(), 'tmp')):
	os.mkdir(os.path.join(os.getcwd(), 'tmp'))

# The app
if __name__ == '__main__':
	# Create app
	app = QApplication(sys.argv)
	app.setApplicationName('LMMS Theme Installer')

	# Show window
	window = MainWindow()
	window.show()

	# Closed connection
	app.lastWindowClosed.connect(app.quit)

	# Run it
	sys.exit(app.exec_())