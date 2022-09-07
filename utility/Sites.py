from itertools import count
from tables.TablesDelveSite import TablesDelveSite
from tables.TablesDelveTheme import TablesDelveTheme
from tables.TablesDelveDomain import TablesDelveDomain
from tables.TablesIronswornMove import TablesIronswornMove
from tables.TablesIronswornPrompts import TablesIronswornPrompts
from utility.Monster import Monster
from utility.Roll import Roll

class Sites:
    def __init__(self):
        
        self.delve_site_tables = TablesDelveSite()
        self.delve_theme_tables = TablesDelveTheme()
        self.delve_domain_tables = TablesDelveDomain()
        self.ironsworn_move_tables = TablesIronswornMove()
        self.ironsworn_prompts_tables = TablesIronswornPrompts()
        self.monster_factory = Monster()

        self.dice = Roll()

        self.site_theme_map = {
            "ancient": self.delve_theme_tables.get_delve_theme_ancient,
            "corrupted": self.delve_theme_tables.get_delve_theme_corrupted,
            "fortified": self.delve_theme_tables.get_delve_theme_fortified,
            "hallowed": self.delve_theme_tables.get_delve_theme_hallowed,
            "haunted": self.delve_theme_tables.get_delve_theme_haunted,
            "infested": self.delve_theme_tables.get_delve_theme_infested,
            "ravaged": self.delve_theme_tables.get_delve_theme_ravaged,
            "wild": self.delve_theme_tables.get_delve_theme_wild
        }

        self.site_domain_map = {
            "barrow": {"domain": self.delve_domain_tables.get_delve_domain_barrow, "place": self.delve_site_tables.get_site_place_barrow},
            "cavern": {"domain": self.delve_domain_tables.get_delve_domain_cavern, "place": self.delve_site_tables.get_site_place_cavern},
            "frozen_cavern": {"domain": self.delve_domain_tables.get_delve_domain_frozen_cavern, "place": self.delve_site_tables.get_site_place_frozen_cavern},
            "icereach": {"domain": self.delve_domain_tables.get_delve_domain_icereach, "place": self.delve_site_tables.get_site_place_icereach},
            "mine": {"domain": self.delve_domain_tables.get_delve_domain_mine, "place": self.delve_site_tables.get_site_place_mine},
            "pass": {"domain": self.delve_domain_tables.get_delve_domain_pass, "place": self.delve_site_tables.get_site_place_pass},
            "ruin": {"domain": self.delve_domain_tables.get_delve_domain_ruin, "place": self.delve_site_tables.get_site_place_ruin},
            "sea_cave": {"domain": self.delve_domain_tables.get_delve_domain_sea_cave, "place": self.delve_site_tables.get_site_place_sea_cave},
            "shadowfen": {"domain": self.delve_domain_tables.get_delve_domain_shadowfen, "place": self.delve_site_tables.get_site_place_shadowfen},
            "stronghold": {"domain": self.delve_domain_tables.get_delve_domain_stronghold, "place": self.delve_site_tables.get_site_place_stronghold},
            "tanglewood": {"domain": self.delve_domain_tables.get_delve_domain_tanglewood, "place": self.delve_site_tables.get_site_place_tanglewood},
            "underkeep": {"domain": self.delve_domain_tables.get_delve_domain_underkeep, "place": self.delve_site_tables.get_site_place_underkeep}
        }

        self.site_move_map = {
            "reveal_a_danger": self.ironsworn_move_tables.get_ironsworn_move_reveal_a_danger
        }

    def get_theme(self):
        return self.dice.roll_on_table(self.delve_site_tables.get_site_theme(), self.dice.roll(100))
        
    def get_domain(self):
        return self.dice.roll_on_table(self.delve_site_tables.get_site_domain(), self.dice.roll(100))

    def create_site(self, size):
        theme_display = self.get_theme()
        theme = theme_display.lower()
        domain_display = self.get_domain()
        domain = domain_display.lower().replace(" ", "_")

        site_name = self.create_site_name(domain)

        return {
            "name": site_name,
            "theme_display": theme_display,
            "theme": theme,
            "domain_display": domain_display,
            "domain": domain,
            "map": self.create_map(theme, domain, size)
        }

    def create_map(self, theme, domain, size):        
        map = {}
        danger_increments = 100 / size
        
        for n in range(0, size):
            theme_details = self.site_theme_map[theme]()
            domain_details = self.site_domain_map[domain]["domain"]()

            danger_level = (n + 1) * danger_increments

            new_area = self.create_area(theme_details, domain_details, danger_level)

            theme = new_area["theme"].lower()
            domain = new_area["domain"].lower().replace(" ", "_")

            map["Area {}".format(n)] = new_area

        return map

    def get_feature_table(self, theme_details, domain_details):
        return theme_details["features_table"] + domain_details["features_table"]
    
    def get_danger_table(self, theme_details, domain_details):
        default_dangers = self.site_move_map["reveal_a_danger"]()["table"][2:]

        return theme_details["dangers_table"] + domain_details["dangers_table"] + default_dangers

    def create_site_name(self, domain):
        name = self.dice.roll_on_table(self.delve_site_tables.get_site_name_format(), self.dice.roll(100))

        name = name.replace("[Description]", self.dice.roll_on_table(self.delve_site_tables.get_site_description(), self.dice.roll(100)))
        name = name.replace("{Place}", self.get_domain_place(domain))
        name = name.replace("[Detail]", self.dice.roll_on_table(self.delve_site_tables.get_site_detail(), self.dice.roll(100)))
        name = name.replace("[Namesake]", self.dice.roll_on_table(self.delve_site_tables.get_site_namesake(), self.dice.roll(100)))

        return name

    def get_domain_place(self, domain):
        return self.dice.roll_on_table(self.site_domain_map[domain]["place"](), self.dice.roll(100))

    def create_area(self, theme_details, domain_details, danger_level):
        feature_table = self.get_feature_table(theme_details, domain_details) 
        danger_table = self.get_danger_table(theme_details, domain_details)

        feature = self.get_feature(feature_table)
        danger = self.get_danger(danger_table, danger_level)

        if (feature["description"].lower().count("you transition into a new theme")):
            theme = self.get_theme()
            feature["description"] += ": [{}]".format(theme)
        else:
            theme = theme_details["name"]

        if (feature["description"].lower().count("you transition into a new domain")):
            domain = self.get_domain()
            feature["description"] += ": [{}]".format(domain)
        else:
            domain = domain_details["name"]

        area = {
            "theme": theme,
            "domain": domain, 
            "feature": feature,
            "danger": danger
        }
        
        return area
        
    def get_feature(self, feature_table):
        aspect_table = self.ironsworn_prompts_tables.get_ironsworn_prompt_feature_aspect()
        focus_table = self.ironsworn_prompts_tables.get_ironsworn_prompt_feature_focus()

        feature = {
            "description": self.dice.roll_on_table(feature_table, self.dice.roll(100)),
            "aspect": self.dice.roll_on_table(aspect_table, self.dice.roll(100)),
            "focus": self.dice.roll_on_table(focus_table, self.dice.roll(100))
        }

        return feature
    
    def get_danger(self, danger_table, danger_level):
        danger = {}

        original_danger = self.dice.roll(100)

        if (original_danger > 94):
            first_danger = self.dice.roll(100)
            second_danger = self.dice.roll(100)

            while (first_danger > 94 or second_danger > 94):
                first_danger = self.dice.roll(100)
                second_danger = self.dice.roll(100)

            danger["description"] = "{} Also {}".format(
                self.dice.roll_on_table(danger_table, first_danger),
                self.dice.roll_on_table(danger_table, second_danger)
                )
        else:
            danger["description"] = self.dice.roll_on_table(danger_table, original_danger)

        if (danger["description"].lower().count("denizen") > 0):
            danger["denizen"] = self.get_denizen(danger_level)
        else:
            danger["denizen"] = {}

        return danger
    
    def get_denizen(self, danger_level):
        return self.monster_factory.get_monster(danger_level)