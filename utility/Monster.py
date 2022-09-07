from tables.TablesIronswornMonstrosity import TablesIronswornMonstrosity
from tables.TablesIronswornTurningPoint import TablesIronswornTurningPoint
from utility.Roll import Roll

class Monster:
    def __init__(self):
        self.monster_tables = TablesIronswornMonstrosity()
        self.challenge_rank_table = TablesIronswornTurningPoint().get_ironsworn_challenge_rank()
        self.dice = Roll()
    
    def get_monster(self, danger_level):
        challenge_rank = self.get_challenge_rank(danger_level)

        denizen = {
            "challenge": challenge_rank,
            "size": self.get_monster_size(),
            "form": self.get_monster_form(),
            "features": self.get_monster_characteristics(challenge_rank),
            "abilities": self.get_monster_abilities(challenge_rank)
        }

        return denizen 
    
    def get_challenge_rank(self, danger_level):
        return self.dice.roll_on_table(self.challenge_rank_table, self.dice.roll(danger_level))

    def get_monster_size(self):
        return self.dice.roll_on_table(self.monster_tables.get_ironsworn_monstrosity_size(), self.dice.roll(100))
    
    def get_monster_form(self):
        dice_roll = self.dice.roll(100)

        if (dice_roll <= 80):
            return self.dice.roll_on_table(self.monster_tables.get_ironsworn_monstrosity_form(), dice_roll)
        else:
            return self.get_monster_hybrid_form()
            
    def get_monster_hybrid_form(self):
        hybrid_roll_one = self.dice.roll(100)
        hybrid_roll_two = self.dice.roll(100)

        while(hybrid_roll_one > 80 or hybrid_roll_two > 80):
            if (hybrid_roll_one > 80):
                hybrid_roll_one = self.dice.roll(100)
            
            if (hybrid_roll_two > 80):
                hybrid_roll_two = self.dice.roll(100)
        
        hybrid = """Hybrid {} and {}""".format(
            self.dice.roll_on_table(self.monster_tables.get_ironsworn_monstrosity_form(), hybrid_roll_one), 
            self.dice.roll_on_table(self.monster_tables.get_ironsworn_monstrosity_form(), hybrid_roll_two)
        )
        
        return hybrid
    
    def get_monster_characteristics(self, challenge):
        number_of_characteristics = 0

        if (challenge == "Troublesome"):
            number_of_characteristics = self.dice.roll(1)
        elif (challenge == "Dangerous"):
            number_of_characteristics = self.dice.roll(2)
        elif (challenge == "Formidable"):
            number_of_characteristics = self.dice.roll(3)
        elif (challenge == "Extreme"):
            number_of_characteristics = self.dice.roll(4)
        else:
            number_of_characteristics = self.dice.roll(5)
        
        characteristics = []

        for n in range(0, number_of_characteristics):
            characteristics.append(self.get_monster_characteristic())
        
        return characteristics

    def get_monster_abilities(self, challenge):
        number_of_abilities = 0

        if (challenge == "Troublesome"):
            number_of_abilities = self.dice.roll(1)
        elif (challenge == "Dangerous"):
            number_of_abilities = self.dice.roll(2)
        elif (challenge == "Formidable"):
            number_of_abilities = self.dice.roll(3)
        elif (challenge == "Extreme"):
            number_of_abilities = self.dice.roll(4)
        else:
            number_of_abilities = self.dice.roll(5)
        
        abilities = []

        for n in range(0, number_of_abilities):
            abilities.append(self.get_monster_ability())
        
        return abilities

    def get_monster_characteristic(self):
        return self.dice.roll_on_table(self.monster_tables.get_ironsworn_monstrosity_characteristics(), self.dice.roll(100))

    def get_monster_ability(self):
        return self.dice.roll_on_table(self.monster_tables.get_ironsworn_monstrosity_abilities(), self.dice.roll(100))


