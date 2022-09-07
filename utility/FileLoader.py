from asyncore import read
import json

class FileLoader:
	def __init__(self, path):
		self.path = path

	def load_file(self):
		with open(self.path, "r") as read_file:
			data = json.load(read_file)
		return data    