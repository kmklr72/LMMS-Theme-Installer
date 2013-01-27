#import os, re, shutil, stat, tarfile, urllib, urlparse
import os, re
from bs4 import BeautifulSoup
from inc.config import Config
from PySide.QtCore import QDir

# Config
global config
config = Config()
config.load()

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

def generate_data_dir():
	lmms_rc_file = os.path.join(QDir.home().absolutePath(), '.lmmsrc.xml')

	xml = BeautifulSoup(open(lmms_rc_file).read())
	return os.path.normpath(os.path.split(os.path.split(xml.paths['artwork'].rstrip('/\\'))[0])[0])