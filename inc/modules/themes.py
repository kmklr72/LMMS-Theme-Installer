import os, shutil, urlparse
from PySide.QtWebKit import QWebPage
from inc.config import Config
from ..module import Module, ModuleWindow

# Config
global config
config = Config()
config.load()

class ThemesWindow(ModuleWindow):
	def __init__(self, ui):
		super(ThemesWindow, self).__init__(ui)
		self.module = Themes()
		
		self.ui.themeDescriptionWebView.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
		self.ui.themeDescriptionWebView.show()

		# Widget slots
		self.ui.themeListWidget.clicked.connect(self.theme_list_widget_clicked)
		self.ui.themeDescriptionWebView.linkClicked.connect(self.event_link_clicked)

	def load_window(self):
		if self.ui.themeListWidget.item(0) is None:
			self.theme_list = self.module.get_list('UI%20themes')

			for theme in self.theme_list:
				self.ui.themeListWidget.addItem(theme['name'])

	def theme_list_widget_clicked(self, item):
		theme_name = self.ui.themeListWidget.itemFromIndex(item).text()

		for theme in self.theme_list:
			if theme_name == theme['name']:
				theme_id = theme['id']
				break

		if theme_id is not None:
			self.ui.themeDescriptionWebView.setHtml(self.module.generate_html(theme_id))

class Themes(Module):
	def __init__(self):
		super(Themes, self).__init__('themes')

	def install(self, tarball):
		tar = tarfile.open(os.path.join(config.get('Directories', 'tmp'), tarball), 'r')
		theme_name = tarball.split('.')[0]
		tar.extractall(os.path.join(config.get('Directories', 'tmp'), theme_name))
		tar.close()

		# Get to the actual theme directory
		for path, dirs, files in os.walk(os.path.join(config.get('Directories', 'tmp'), theme_name)):
			if 'style.css' in files:
				theme_tmp_dir = path
				break

		# Install theme
		if not os.path.isdir(os.path.join(self.directory, theme_name)):
			os.mkdir(os.path.join(self.directory, theme_name))

		for filename in os.listdir(theme_tmp_dir):
			abspath = os.path.join(theme_tmp_dir, filename)
			shutil.copy(abspath, os.path.join(self.directory, theme_name, filename))

		# Cleanup time
		self._clear_tmp()