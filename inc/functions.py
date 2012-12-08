from bs4 import BeautifulSoup
from inc.config import Config
import os, re, shutil, stat, tarfile, urllib, urlparse

# Config
global config
config = Config()
config.load()

def get_source(url):
	source = urllib.urlopen(url)
	html = source.read()
	source.close()
	return html

def remote_get_themes():
	# Parse HTML
	html = BeautifulSoup(get_source(config.get('General', 'lsp') + '?action=browse&category=UI%20themes'))
	themes = get_themes(html)

	return themes

def get_themes(html):
	themes = []

	for element in html.find_all('tr', 'file'):
		theme = {}
		for anchor in element.find_all('a', href=True):
			if 'file' in anchor['href']:
				theme['name'] = anchor.string
				theme['id'] = urlparse.parse_qs(urlparse.urlparse(anchor['href']).query)['file'][0]
			elif 'subcategory' in anchor['href']:
				theme['cat'] = anchor.string
			elif 'user' in anchor['href']:
				theme['user'] = get_username(anchor.string)

		themes.append(theme)

	return themes

def remote_get_theme_info(id):
	html = BeautifulSoup(get_source(config.get('General', 'lsp') + '?action=show&file=' + str(id)))
	theme = get_theme_info(html)

	return theme

def get_theme_info(html):
	theme = {}

	# Get the name
	h2 = html.find('h2')
	list = re.split('<img.*?/>', str(h2))
	theme['name'] = re.sub('<.*?>', '', list[-1])

	# Get other info
	header = html.find('tr', 'file')
	theme['user'] = get_username(header.find('a').string)

	theme['download_url'] = config.get('General', 'lsp') + html.find('a', id='downloadbtn')['href']

	for td in html.find('tr', 'file').find_all('td'):
		td = str(td)
		td.replace('<br />', '<br/>')

		if '<br/>' not in td:
			continue

		for line in td.split('<br/>'):
			#print line
			if '<b>' not in line:
				continue

			# Check for dates line
			if '<div class="nobr">' in line:
				if 'dates' not in theme:
					theme['dates'] = {}

				dates = line.split('</div>')
				submitted = strip_tags(dates[0])
				theme['dates']['submitted'] = submitted.split(':', 1)[1].strip(' ')

				updated = strip_tags(dates[1])
				theme['dates']['updated'] = updated.split(':', 1)[1].strip(' ')

				continue

			# The rest of the info
			info = strip_tags(line)
			info_list = info.split(':')
			info_list[1] = info_list[1].strip(' ')

			if 'Rating' in info_list[0]:
				theme['rating'] = info_list[1]
			elif 'Size' in info_list[0]:
				theme['size'] = info_list[1]
			elif 'License' in info_list[0]:
				theme['license'] = info_list[1]

	# Extras
	extras = html.find('div', id='filedetails')
	remove_tag_tree(extras, 'table')
	extras = str(extras)
	for line in extras.split('<b>'):
		line_list = line.split(':', 1)

		if 'Description' not in line_list[0]:
			line = strip_tags(br2nl(line))

		if 'Downloads' in line_list[0]:
			theme['downloads'] = strip_tags(line_list[1]).strip()
		elif 'Description' in line_list[0]:
			theme['description'] = unicode(nl2br(br2nl(line_list[1].replace('\n', '').replace('</b>', '', 1)).strip('\n')), 'utf-8')

	return theme

def generate_theme_html(content):
	if '<' in content:
		# Assume it's HTML
		theme = get_theme_info(content)
	else:
		# Get the theme info from the server
		theme = remote_get_theme_info(content)

	html_header = '''<!DOCTYPE html>
	<html>
	<head>
	<style type="text/css">
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
	</style>
	</head>
	<body>'''

	html_body = '''
	<div style="display:block">
		<div style="float:left;">
			<h2>''' + theme['name'] + '''</h2>
			by ''' + theme['user'] + '''
		</div>

		<div style="float:right;">
			<a href="''' + theme['download_url'] + '''" id="downloadbtn"><img src="''' + config.get('General', 'lsp') + '''download.png" alt="" style="border:0px; vertical-align:middle; padding-right:5px;" />Install</a>
		</div>

		<div style="clear:both;"></div>
	</div>

	<table style="border:none;">
		<tr>
			<td>
				<b>Size:</b> ''' + theme['size'] + '''<br />
				<b>License:</b> ''' + theme['license'] + '''<br />
				<b>Rating:</b> ''' + theme['rating'] + '''
			</td>
			<td style="width:20px;"></td>
			<td>
				<b>Submitted:</b> ''' + theme['dates']['submitted'] + '''<br />
				<b>Updated:</b> ''' + theme['dates']['updated'] + '''<br />
				<b>Downloads:</b> ''' + theme['downloads'] + '''
			</td>
		</tr>
	</table>
	<hr />
	<p>Description:<br />''' + theme['description'] + '''</p>
	'''

	html_footer = '''</body>
	</html>'''

	return html_header + html_body + html_footer

def download_theme(url):
	# Get theme name from url
	filename = urlparse.parse_qs(urlparse.urlparse(url).query)['name'][0]

	# Download theme
	urllib.urlretrieve(url, os.path.join(config.get('General', 'tmp'), filename))

	if os.path.exists(os.path.join(config.get('General', 'tmp'), filename)):
		return filename
	else:
		return False

def install_theme(tarball):
	tar = tarfile.open(os.path.join(config.get('General', 'tmp'), tarball), 'r')
	theme_name = tarball.split('.')[0]
	tar.extractall(os.path.join(config.get('General', 'tmp'), theme_name))
	tar.close()

	# Get to the actual theme directory
	for path, dirs, files in os.walk(os.path.join(config.get('General', 'tmp'), theme_name)):
		if 'style.css' in files:
			theme_tmp_dir = path
			break

	# Install theme
	if not os.path.isdir(os.path.join(config.get('General', 'theme_dir'), theme_name)):
		os.mkdir(os.path.join(config.get('General', 'theme_dir'), theme_name))

	for filename in os.listdir(theme_tmp_dir):
		abspath = os.path.join(theme_tmp_dir, filename)
		shutil.copy(abspath, os.path.join(config.get('General', 'theme_dir'), theme_name, filename))

	# Cleanup time
	for item in os.listdir(config.get('General', 'tmp')):
		item_path = os.path.join(config.get('General', 'tmp'), item)
		os.chmod(item_path, stat.S_IWUSR)
		if os.path.isfile(item_path):
			os.unlink(item_path)
		else:
			shutil.rmtree(item_path)

def strip_tags(html):
	regex = re.compile('<[^<]+?>')
	return regex.sub('', html)

def remove_tag_tree(soup, tagname):
	for tag in soup.find_all(tagname):
		contents = tag.contents
		parent = tag.parent
		tag.extract()

def nl2br(string):
	return string.replace('\n', '<br/>')

def br2nl(string):
	return string.replace('<br/>', '\n')

def get_username(string):
	try:
		string = unicode(string, 'utf-8')
	except:
		pass

	return string