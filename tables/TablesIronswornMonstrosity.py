from utility.FileLoader import FileLoader

class TablesIronswornMonstrosity:
    def __init__(self):
        self.path = "json/ironsworn_monstrosity_oracles.json"
        self.data = FileLoader(self.path).load_file()

    def get_ironsworn_monstrosity_size(self):
        return self.data["Oracles"][0]["Oracle Table"]

    def get_ironsworn_monstrosity_form(self):
        return self.data["Oracles"][1]["Oracle Table"]

    def get_ironsworn_monstrosity_characteristics(self):
        return self.data["Oracles"][2]["Oracle Table"]

    def get_ironsworn_monstrosity_abilities(self):
        return self.data["Oracles"][3]["Oracle Table"]
