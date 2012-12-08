import os, sys, urlparse
from inc.functions import *
from PySide.QtCore import Qt
from PySide.QtGui import QDesktopServices, QMainWindow, QMessageBox
from PySide.QtWebKit import QWebPage
from ui.mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		# Load window
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.loadWindow()

		self.ui.descriptionWebView.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)

		# Widget slots
		self.ui.themeListWidget.clicked.connect(self.themeListWidgetClicked)
		self.ui.descriptionWebView.linkClicked.connect(self.eventLinkClicked)

		# Menu slots
		self.ui.actionExit.triggered.connect(sys.exit)
		self.ui.actionOptions.triggered.connect(self.optionsTriggered)

	def loadWindow(self):
		global config
		config = Config()
		config.load()

		if self.ui.themeListWidget.item(0) is None:
			self.themes = remote_get_themes()

			for theme in self.themes:
				self.ui.themeListWidget.addItem(theme['name'])

	def themeListWidgetClicked(self, item):
		theme_name = self.ui.themeListWidget.itemFromIndex(item).text()

		for theme in self.themes:
			if theme_name == theme['name']:
				theme_id = theme['id']
				break

		if theme_id is not None:
			self.ui.descriptionWebView.setHtml(generate_theme_html(theme_id))

	def eventLinkClicked(self, url):
		url_string = url.toString()

		if 'file' in urlparse.parse_qs(urlparse.urlparse(url_string).query):
			msgbox = QMessageBox()
			msgbox.setWindowTitle('Installing')
			msgbox.setText('Installing theme. Please wait...')
			msgbox.setStandardButtons(0)
			msgbox.setAttribute(Qt.WA_DeleteOnClose)
			msgbox.setWindowModality(Qt.NonModal)
			msgbox.show()
			msgbox.repaint() # Qt didn't want to show the text so we force a repaint

			# Download and install the theme
			tarball = download_theme(url_string)
			try:
				install_theme(tarball)
				msgbox.close()

				complete_msgbox = QMessageBox()
				complete_msgbox.setWindowTitle('Complete')
				complete_msgbox.setText('Install complete.')
				complete_msgbox.setStandardButtons(QMessageBox.Ok)
				complete_msgbox.setAttribute(Qt.WA_DeleteOnClose)
				complete_msgbox.exec_()
			except:
				msgbox.close()

				failed_msgbox = QMessageBox()
				failed_msgbox.setWindowTitle('Failed')
				failed_msgbox.setText('Install failed. Please try again later.')
				failed_msgbox.setStandardButtons(QMessageBox.Ok)
				failed_msgbox.setAttribute(Qt.WA_DeleteOnClose)
				failed_msgbox.exec_()
		else:
			QDesktopServices.openUrl(url)

	def optionsTriggered(self):
		from configuration import ConfigurationWindow

		self.configWindow = ConfigurationWindow()
		self.configWindow.show()