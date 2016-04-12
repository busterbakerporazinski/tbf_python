#! /usr/env/python
# Buster Baker-Porazinski
# 041116 Enemy ID Storage

import random

enemyid = {}


def newenemy (self, name, tier, level): #generates and stores enemies.
	self.name = name
	self.tier = tier
	self.level = level

	currentn = 000 

	if self.name = y: #if desired, a random name will be generated and assigned to the stats provided. 

		namelist =['Bono', 'Milo', 'Cecil', 'Pax', 'Khan', 'Elder', 'Pumba', 'Sonic', 'Washi', 'Guru']
		tutilelist =["The Wild", "The Feirce", "The Swift", "The Hidden", "The Wise", "Strong-Fisted", "Heavy-Legged", "The Wizard", "The Harbringer", "The Brawler" ]

		rand1 = random.randint(0,9)
		rand1 = random.randint(0,9)

		firstn = namelist[rand1]
		titlen = titlelist[rand2]
		together = firstn + titlen
		
		currentn == (currentn + 1)

		other = currentn + self.tier + 'E' + self.level

		enemyid[together] = other

		return (firstn, titlen)

	elif 

		currentn == (currentn + 1)

		other = currentn + self.tier + 'E' + self.level

		enemyid['Fighter The Challenger'] = other

		return ("Fighter The Challenger") #returns a default name if no name is desired.


