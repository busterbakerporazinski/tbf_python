#! /usr/bin/env python3

#Player Class

#Buster Baker-Porazinski 


class Player(object):
	
	def __init__(self, punchd, kickd, grapd, puncho, kicko, grapo, hp, speed, name, appid, wealth, itemset, move): 

		self.punchd = punchd
		self.kickd = kickd
		self.grapd = grapd

		self.puncho = puncho
		self.kicko = kicko
		self.grapo = grapo 

		self.hp = hp
		self.speed = speed
		self.name = name
		self.appid = appid

		self.wealth = wealth
		self.itemset = itemset
		self.move = move

	def getPunchd(self):
		return self.punchd

	def getKickd(self):
		return self.kickd

	def getGrapd(self):
		return self.grapd



	def getPuncho(self):
		return self.puncho

	def getKicko(self):
		return self.kicko

	def getGrapo(self):
		return self.grapo



	def getHp(self):
		return self.hp

	def getSpeed(self):
		return self.speed

	def getName(self):
		return self.name

	def getAppid(self):
		return self.appid



	def __str__ (self):
		return "Hello %s" % (self.name)
