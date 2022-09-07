from utility.FileLoader import FileLoader

class TablesIronswornPrompts:
    def __init__(self):
        self.path = "json/ironsworn_prompts.json"
        self.data = FileLoader(self.path).load_file()

    def get_ironsworn_prompt_action(self):
        return self.data["Oracles"][0]["Oracle Table"]

    def get_ironsworn_prompt_theme(self):
        return self.data["Oracles"][1]["Oracle Table"]

    def get_ironsworn_prompt_feature_aspect(self):
        return self.data["Oracles"][2]["Oracles"][0]["Oracle Table"]

    def get_ironsworn_prompt_feature_focus(self):
        return self.data["Oracles"][2]["Oracles"][1]["Oracle Table"]

    def get_ironsworn_prompt_trap_event(self):
        return self.data["Oracles"][3]["Oracles"][0]["Oracle Table"]

    def get_ironsworn_prompt_trap_component(self):
        return self.data["Oracles"][3]["Oracles"][1]["Oracle Table"]

    def get_ironsworn_prompt_combat_method(self):
        return self.data["Oracles"][4]["Oracles"][0]["Oracle Table"]

    def get_ironsworn_prompt_combat_target(self):
        return self.data["Oracles"][4]["Oracles"][1]["Oracle Table"]
