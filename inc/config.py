import ConfigParser, os

class Config(ConfigParser.ConfigParser, object):
	def __init__(self):
		super(Config, self).__init__()

	def get(self, section, option, raw = False, vars = None):
		value = super(Config, self).get(section, option, raw, vars)

		if '%cd%' in value:
			value = value.replace('%cd%', os.getcwd())

		return value