from utility.FileLoader import FileLoader

class TablesDelveSite():
	def __init__(self):
		self.path = "json/delve_sites.json"
		self.data = FileLoader(self.path).load_file()
	
	def get_site_name_format(self):
		return self.data["Categories"][0]["Oracles"][0]["Oracle Table"]

	def get_site_description(self):		
		return self.data["Categories"][0]["Oracles"][1]["Oracle Table"]

	def get_site_detail(self):
		return self.data["Categories"][0]["Oracles"][2]["Oracle Table"]

	def get_site_namesake(self):
		return self.data["Categories"][0]["Oracles"][3]["Oracle Table"]

	def get_site_theme(self):
		return self.data["Categories"][1]["Oracles"][0]["Oracle Table"]
	
	def get_site_domain(self):
		return self.data["Categories"][1]["Oracles"][1]["Oracle Table"]

	def get_site_place_barrow(self):
		return self.data["Categories"][0]["Oracles"][4]["Oracles"][0]["Oracle Table"]

	def get_site_place_cavern(self):
		return self.data["Categories"][0]["Oracles"][4]["Oracles"][1]["Oracle Table"]

	def get_site_place_frozen_cavern(self):
		return self.data["Categories"][0]["Oracles"][4]["Oracles"][2]["Oracle Table"]

	def get_site_place_icereach(self):
		return self.data["Categories"][0]["Oracles"][4]["Oracles"][3]["Oracle Table"]

	def get_site_place_mine(self):
		return self.data["Categories"][0]["Oracles"][4]["Oracles"][4]["Oracle Table"]

	def get_site_place_pass(self):
		return self.data["Categories"][0]["Oracles"][4]["Oracles"][5]["Oracle Table"]

	def get_site_place_ruin(self):
		return self.data["Categories"][0]["Oracles"][4]["Oracles"][6]["Oracle Table"]

	def get_site_place_sea_cave(self):
		return self.data["Categories"][0]["Oracles"][4]["Oracles"][7]["Oracle Table"]

	def get_site_place_shadowfen(self):
		return self.data["Categories"][0]["Oracles"][4]["Oracles"][8]["Oracle Table"]

	def get_site_place_stronghold(self):
		return self.data["Categories"][0]["Oracles"][4]["Oracles"][9]["Oracle Table"]

	def get_site_place_tanglewood(self):
		return self.data["Categories"][0]["Oracles"][4]["Oracles"][10]["Oracle Table"]

	def get_site_place_underkeep(self):
		return self.data["Categories"][0]["Oracles"][4]["Oracles"][11]["Oracle Table"]
