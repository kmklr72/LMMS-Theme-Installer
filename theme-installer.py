import sys
from inc.functions import *
from PySide.QtGui import QApplication, QPixmap, QSplashScreen

from ui.mainwindow import MainWindow

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