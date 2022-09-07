from utility.FileLoader import FileLoader

class TablesDelveDomain:
    def __init__(self):
        self.path = "json/delve_domains.json"
        self.data = FileLoader(self.path).load_file()

    def get_delve_domain_barrow(self):
        data = self.data["Domains"][0]

        domain_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return domain_details

    def get_delve_domain_cavern(self):
        data = self.data["Domains"][1]

        domain_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return domain_details

    def get_delve_domain_frozen_cavern(self):
        data = self.data["Domains"][2]

        domain_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return domain_details

    def get_delve_domain_icereach(self):
        data = self.data["Domains"][3]

        domain_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return domain_details

    def get_delve_domain_mine(self):
        data = self.data["Domains"][4]

        domain_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return domain_details

    def get_delve_domain_pass(self):
        data = self.data["Domains"][5]

        domain_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return domain_details

    def get_delve_domain_ruin(self):
        data = self.data["Domains"][6]

        domain_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return domain_details

    def get_delve_domain_sea_cave(self):
        data = self.data["Domains"][7]

        domain_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return domain_details

    def get_delve_domain_shadowfen(self):
        data = self.data["Domains"][8]

        domain_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return domain_details

    def get_delve_domain_stronghold(self):
        data = self.data["Domains"][9]

        domain_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return domain_details

    def get_delve_domain_tanglewood(self):
        data = self.data["Domains"][10]

        domain_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return domain_details

    def get_delve_domain_underkeep(self):
        data = self.data["Domains"][11]

        domain_details = {
            "name": data["Name"],
            "summary": data["Summary"],
            "description": data["Description"],
            "features_table": data["Features"],
            "dangers_table": data["Dangers"]
        }

        return domain_details


        