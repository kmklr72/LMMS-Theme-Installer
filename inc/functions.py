#import os, re, shutil, stat, tarfile, urllib, urlparse
import os, re
from bs4 import BeautifulSoup
from inc.config import Config

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