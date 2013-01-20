import os, shutil, sys, urlparse
from PySide.QtWebKit import QWebPage
from inc.config import Config
from ..module import Module, ModuleWindow

# Config
global config
config = Config()
config.load()

class PresetsWindow(ModuleWindow):

	def __init__(self, ui):
		super(PresetsWindow, self).__init__(ui)
		self.module = Presets()

		self.ui.presetDescriptionWebView.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
		self.ui.presetDescriptionWebView.show()

		# Widget slots
		self.ui.presetListWidget.clicked.connect(self.preset_list_widget_clicked)
		self.ui.presetDescriptionWebView.linkClicked.connect(self.event_link_clicked)

	def load_window(self):
		if self.ui.presetListWidget.item(0) is None:
			self.preset_list = self.module.get_list('Presets')

			for preset in self.preset_list:
				self.ui.presetListWidget.addItem(preset['name'])

	def preset_list_widget_clicked(self, item):
		preset_name = self.ui.presetListWidget.itemFromIndex(item).text()

		for preset in self.preset_list:
			if preset_name == preset['name']:
				preset_id = preset['id']
				break

		if preset_id is not None:
			self.module.preset_id = preset_id
			self.ui.presetDescriptionWebView.setHtml(self.module.generate_html(preset_id))

class Presets(Module):
	def __init__(self):
		super(Presets, self).__init__('presets')

	def install(self, preset):
		cat = self.get_info(self.preset_id)['cat']

		# Install preset
		if not os.path.exists(os.path.join(self.directory, cat, preset)):
			os.makedirs(os.path.join(self.directory, cat))
		else:
			os.unlink(os.path.join(self.directory, cat, preset))

		shutil.copy(os.path.join(config.get('Directories', 'tmp'), preset), os.path.join(self.directory, cat, preset))

		# Cleanup time
		self._clear_tmp()