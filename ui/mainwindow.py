import os, sys, urlparse
from inc.functions import *
from PySide.QtGui import QMainWindow
from ui.mainwindow import Ui_MainWindow
from inc.modules import themes, presets

class MainWindow(QMainWindow):
	def __init__(self):
		# Load window
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.load_tab(0)

		# TabView slot
		self.ui.tabWidget.currentChanged.connect(self.load_tab)

		# Menu slots
		self.ui.actionExit.triggered.connect(sys.exit)
		self.ui.actionOptions.triggered.connect(self.optionsTriggered)

	def load_tab(self, index):
		module_name = self.ui.tabWidget.tabText(index)

		if module_name == 'Themes':
			if not hasattr(self, 'themesTab'):
				self.themesTab = themes.ThemesWindow(self.ui)
				self.themesTab.load_window()
		elif module_name == 'Presets':
			if not hasattr(self, 'presetsTab'):
				self.presetsTab = presets.PresetsWindow(self.ui)
				self.presetsTab.load_window()

	def optionsTriggered(self):
		from configuration import ConfigurationWindow

		self.configWindow = ConfigurationWindow()
		self.configWindow.show()