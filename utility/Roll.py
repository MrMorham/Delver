import random

class Roll:
	def __init__(self):
		pass

	def roll_on_table(self, data, roll):
		for n in range(len(data)):
			lower_bound = 1 if n-1 < 0 else data[n-1]["Chance"] + 1
			upper_bound = data[n]["Chance"]
			
			if roll >= lower_bound and roll <= upper_bound: return data[n]["Description"]

	def roll(self, number_of_sides):
		return random.randint(1, number_of_sides)
