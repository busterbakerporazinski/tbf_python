#! /usr/bin/env python3

#Enemy Class

#Buster Baker-Porazinski 

class enemy(object):
	
	def _init_(self, punchd, kickd, grapd, puncho, kicko, grapo, hp, speed, name, appid): 

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
		return "%s is an enemy." % (self.name)



