import ConfigParser, os

class Config(ConfigParser.ConfigParser, object):
	def __init__(self):
		super(Config, self).__init__()

	def get(self, section, option, raw = False, vars = None):
		try:
			value = super(Config, self).get(section, option, raw, vars)
		except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
			value = ''
			if section == 'Directories':
				return

		if '%cd%' in value:
			value = value.replace('%cd%', os.getcwd())

		return value

	def save(self):
		return self.write(open(os.path.join(os.getcwd(), 'config.cfg'), 'wb'))

	def load(self):
		return self.read(os.path.join(os.getcwd(), 'config.cfg'))