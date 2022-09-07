from utility.FileLoader import FileLoader

class TablesIronswornTurningPoint:
    def __init__(self):
        self.path = "json/ironsworn_oracles_turning_point.json"
        self.data = FileLoader(self.path).load_file()

    def get_ironsworn_challenge_rank(self):
        return self.data["Oracles"][0]["Oracle Table"]
