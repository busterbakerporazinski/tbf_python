#! usr/env/bin python3
#Buster Baker-Porazinski
#TBF 
#040616 Exp + Loot Calc

import random

class ExpAndLootCalc(object):

	def __init__ (self, current_elevel, Loot_tier):

		self.current_elevel = current_elevel
		self.Loot_tier = Loot_tier



	def DetermineTier (self, elevel):


		if elevel => 5:
			self.Loot_tier = 1
			return Lootlist(1)

		elif elevel => 10:
			self.Loot_tier = 2
			 return LootList(2)

		elif elevel => 15:
			self.Loot_tier = 3 
			return LootList(3)


	def LootList (self, Loot_tier):

		if Loot_tier == 1:
			num1 = random.randint(1,10)
			return tieroneloot[num1]


		elif Loot_tier == 2:
			num2 = random.randint(1,10)
			return tiertwoloot[num2]

		elif Loot_tier == 3:
			num3 = random.randint(1,10)
			return tierthreeloot[num3]


		tieroneloot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

		tiertwoloot = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

		tierthreeloot = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


	def DetermineExp (self, current_elevel):

		expgained = (self.current_elevel) * (self.Loot_tier)
		return expgained





