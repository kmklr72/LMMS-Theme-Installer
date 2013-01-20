import ConfigParser, os, re, shutil, stat, sys, urllib, urlparse
from bs4 import BeautifulSoup
from PySide.QtCore import Qt
from PySide.QtGui import QDesktopServices, QMessageBox
from inc.functions import *
from inc.config import Config
from inc.cache import cache

# Config
global config
config = Config()
config.load()

class ModuleWindow(object):
	module = None

	def __init__(self, ui):
		self.ui = ui

	def event_link_clicked(self, url):
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
			package = self.module.download('http://localhost/test/download.php?file=2800&name=Fat-flat.xpf')
			#package = self.module.download(url_string)
			try:
				self.module.install(package)
				msgbox.close()

				complete_msgbox = QMessageBox()
				complete_msgbox.setWindowTitle('Complete')
				complete_msgbox.setText('Install complete.')
				complete_msgbox.setStandardButtons(QMessageBox.Ok)
				complete_msgbox.setAttribute(Qt.WA_DeleteOnClose)
				complete_msgbox.exec_()
			except:
				msgbox.close()
				print "Unexpected error:", sys.exc_info()[:2]

				failed_msgbox = QMessageBox()
				failed_msgbox.setWindowTitle('Failed')
				failed_msgbox.setText('Install failed. Please try again later.')
				failed_msgbox.setStandardButtons(QMessageBox.Ok)
				failed_msgbox.setAttribute(Qt.WA_DeleteOnClose)
				failed_msgbox.exec_()
		else:
			QDesktopServices.openUrl(url)

class Module(object):
	def __init__(self, module):
		self.directory = config.get('Directories', module)
		if not isinstance(self.directory, str):
			self.directory = os.path.join(config.get('Directories', 'data'), module)

	def download(self, url):
		# Get filename from URL
		filename = urlparse.parse_qs(urlparse.urlparse(url).query)['name'][0]

		# Download file
		urllib.urlretrieve(url, os.path.join(config.get('Directories', 'tmp'), filename))

		if os.path.exists(os.path.join(config.get('Directories', 'tmp'), filename)):
			return filename
		else:
			return False

	@cache.cache('page_source')
	def get_source(self, url):
		source = urllib.urlopen(url)
		html = source.read()
		source.close()
		return html

	def get_list(self, category):
		html = BeautifulSoup(self.get_source(config.get('General', 'lsp') + '?action=browse&category=' + category))
		modules = self._build_list(html)

		return modules

	def get_info(self, id):
		html = BeautifulSoup(self.get_source(config.get('General', 'lsp') + '?action=show&file=' + str(id)))
		module = self._build_info(html)

		return module

	def generate_head(self):
		return '''<style type="text/css">
		body {
			font: 0.8em 'Open Sans', 'Segoe UI', Ubuntu, sans-serif;
		}

		h2 {
			margin: 0;
			padding: 0;
		}

		#downloadbtn {
			color: #0a0;
			font-size:12pt;
			font-weight: bold;
			display:block;
			border: 1px solid #888;
			background: #ddd;
			padding: 4px;
			width:160px;
			text-align:center;
		}

		#downloadbtn:hover {
			background: #bbb;
		}
		</style>'''

	def generate_html(self, content):
		if '<' in content:
			# Assume it's HTML
			info = self._build_info(content)
		else:
			# Get the info from the server
			info = self.get_info(content)

		html = '''<!DOCTYPE html>
		<html>
		<head>
		''' + self.generate_head() + '''
		</head>
		<body>

		<div style="display:block">
			<div style="float:left;">
				<h2>''' + info['name'] + '''</h2>
				by ''' + info['user'] + '''
			</div>

			<div style="float:right;">
				<a href="''' + info['download_url'] + '''" id="downloadbtn"><img src="''' + config.get('General', 'lsp') + '''download.png" alt="" style="border:0px; vertical-align:middle; padding-right:5px;" />Install</a>
			</div>

			<div style="clear:both;"></div>
		</div>

		<table style="border:none;">
			<tr>
				<td>
					<b>Size:</b> ''' + info['size'] + '''<br />
					<b>License:</b> ''' + info['license'] + '''<br />
					<b>Rating:</b> ''' + info['rating'] + '''
				</td>
				<td style="width:20px;"></td>
				<td>
					<b>Submitted:</b> ''' + info['dates']['submitted'] + '''<br />
					<b>Updated:</b> ''' + info['dates']['updated'] + '''<br />
					<b>Downloads:</b> ''' + info['downloads'] + '''
				</td>
			</tr>
		</table>
		<hr />
		<p>Description:<br />''' + info['description'] + '''</p>

		</body>
		</html>'''

		return html

	# Private methods
	def _build_list(self, html):
		list = []

		for element in html.find_all('tr', 'file'):
			item = {}
			for anchor in element.find_all('a', href=True):
				if 'file' in anchor['href']:
					item['name'] = anchor.string
					item['id'] = urlparse.parse_qs(urlparse.urlparse(anchor['href']).query)['file'][0]
				elif 'subcategory' in anchor['href']:
					item['cat'] = anchor.string
				elif 'user' in anchor['href']:
					item['user'] = get_username(anchor.string)

			list.append(item)

		return list

	def _build_info(self, html):
		info = {}

		# Get the name and category
		h2 = html.find('h2')
		list = re.split('<img.*?/>', str(h2))
		info['name'] = re.sub('<.*?>', '', list[-1])
		info['cat'] = re.sub('<.*?>', '', list[-2])

		# Get other info
		header = html.find('tr', 'file')
		info['user'] = get_username(header.find('a').string)

		info['download_url'] = config.get('General', 'lsp') + html.find('a', id='downloadbtn')['href']

		for td in html.find('tr', 'file').find_all('td'):
			td = str(td)
			td.replace('<br />', '<br/>')

			if '<br/>' not in td:
				continue

			for line in td.split('<br/>'):
				if '<b>' not in line:
					continue

				# Check for dates line
				if '<div class="nobr">' in line:
					if 'dates' not in info:
						info['dates'] = {}

					dates = line.split('</div>')
					submitted = strip_tags(dates[0])
					info['dates']['submitted'] = submitted.split(':', 1)[1].strip(' ')

					updated = strip_tags(dates[1])
					info['dates']['updated'] = updated.split(':', 1)[1].strip(' ')

					continue

				# The rest of the info
				line_info = strip_tags(line)
				info_list = line_info.split(':')
				info_list[1] = info_list[1].strip(' ')

				if 'Rating' in info_list[0]:
					info['rating'] = info_list[1]
				elif 'Size' in info_list[0]:
					info['size'] = info_list[1]
				elif 'License' in info_list[0]:
					info['license'] = info_list[1]

		# Extras
		extras = html.find('div', id='filedetails')
		remove_tag_tree(extras, 'table')
		extras = str(extras)
		for line in extras.split('<b>'):
			line_list = line.split(':', 1)

			if 'Description' not in line_list[0]:
				line = strip_tags(br2nl(line))

			if 'Downloads' in line_list[0]:
				info['downloads'] = strip_tags(line_list[1]).strip()
			elif 'Description' in line_list[0]:
				info['description'] = unicode(nl2br(br2nl(line_list[1].replace('\n', '').replace('</b>', '', 1)).strip('\n')), 'utf-8')

		return info

	def _clear_tmp(self):
		for item in os.listdir(config.get('Directories', 'tmp')):
			item_path = os.path.join(config.get('Directories', 'tmp'), item)
			os.chmod(item_path, stat.S_IWUSR)
			if os.path.isfile(item_path):
				os.unlink(item_path)
			else:
				shutil.rmtree(item_path)