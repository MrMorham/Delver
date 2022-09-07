from utility.FileLoader import FileLoader

class TablesDelveTheme:
    def __init__(self):
        self.path = "json/delve_themes.json"
        self.data = FileLoader(self.path).load_file()

    def get_delve_theme_ancient(self):
        data = self.data["Themes"][0]

        theme_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return theme_details

    def get_delve_theme_corrupted(self):
        data = self.data["Themes"][1]

        theme_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return theme_details

    def get_delve_theme_fortified(self):
        data = self.data["Themes"][2]

        theme_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return theme_details

    def get_delve_theme_hallowed(self):
        data = self.data["Themes"][3]

        theme_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return theme_details

    def get_delve_theme_haunted(self):
        data = self.data["Themes"][4]

        theme_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return theme_details

    def get_delve_theme_infested(self):
        data = self.data["Themes"][5]

        theme_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return theme_details

    def get_delve_theme_ravaged(self):
        data = self.data["Themes"][6]

        theme_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return theme_details

    def get_delve_theme_wild(self):
        data = self.data["Themes"][7]

        theme_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return theme_details

