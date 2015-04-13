import mousetrap.plugins.interface as interface
import logging


LOGGER = logging.getLogger(__name__)

class Test(interface.Plugin):
	
	def __init__(self, config):
		self._config = config
		self.counter = 0
		self.data = config[self]['data']


	def run(self, app):
		self.counter += 1
		print(self.data, self.counter)
