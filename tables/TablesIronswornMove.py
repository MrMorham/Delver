from utility.FileLoader import FileLoader

class TablesIronswornMove:
    def __init__(self):
        self.path = "json/ironsworn_move_oracles.json"
        self.data = FileLoader(self.path).load_file()

    def get_ironsworn_move_reveal_a_danger(self):
        data = self.data["Oracles"][7]

        move_details = {
            "name": data["Name"],
            "table": data["Oracle Table"]
        }

        return move_details