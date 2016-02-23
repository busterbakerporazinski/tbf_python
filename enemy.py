#! /usr/bin/env python3

#Enemy Class

#Buster Baker-Porazinski 

import random
class Enemy(object):
    def __init__(self, punchd, kickd, grapd, puncho, kicko, grapo,
                 hp, speed, name, appid): 
            """Defense"""
            self.punchd = punchd
            self.kickd = kickd
            self.grapd = grapd

            """Offense"""
            self.puncho = puncho
            self.kicko = kicko
            self.grapo = grapo 

            """Related stat"""
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

    """getDefends return randomly one of the three defense alements"""
    def getDef(self):
        num = random.randint(0, 2)
        methid, damage = "", 0
        if num == 0:
            method = "hammer"
            damage = self.punchd
        elif num == 1:
            method = "sword"
            damage = self.kickd
        else:
            method = "shield"
            damage = self.grapd
        return method, damage

    def getPuncho(self):
        return self.puncho

    def getKicko(self):
        return self.kicko

    def getGrapo(self):
        return self.grapo

    """getOffends return randomly one of the three offense elements"""
    def getAtt(self):
        num = random.randint(0, 2)
        method, damage = "", 0
        if num == 0:
            method = "hammer"
            damage = self.puncho
        elif num == 1:
            method = "sword"
            damage = self.kicko
        else:
            method = "shield"
            damage = self.grapo
        return method, damage

    def getHp(self):
            return self.hp
        
    def setHp(self, val):
        self.hp = val

    def getSpeed(self):
            return self.speed

    def getName(self):
            return self.name

    def getAppid(self):
            return self.appid

    def __str__ (self):
            return "%s is an enemy." % (self.name)
