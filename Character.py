import random
class Character(object):
    def __init__(self, punchd , kickd, grapd, puncho, kicko, grapo,
                 hp, speed, name, appid, gold): 
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
            self.gold = gold

            """Recent result from a fight"""
            self.flag = 0 #0=tie, 1=win, 2=win
    
    def getPunchd(self):
        return self.punchd

    def getKickd(self):
        return self.kickd

    def getGrapd(self):
        return self.grapd

    """getDefends return randomly one of the three defense alements"""
    def getDef_auto(self):
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
    def getAtt_auto(self):
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
            self.grapo
        return method, damage

    def getAtt_damage(self, att_type):
        dmg = 0
        if att_type == "hammer":
            dmg = self.puncho
        elif att_type == "sword":
            dmg = self.kicko
        elif att_type == "shield":
            dmg = self.grapo
        return dmg

    def getHp(self):
            return self.hp
        
    def setHp(self, val):
        self.hp = val

    def loseHp(self, val):
        self.hp -= val

    def gainHp(self, val):
        self.hp += val

    def getSpeed(self):
            return self.speed

    def setSpeed(self, val):
        self.speed = val

    def getName(self):
        return self.name

    def getAppid(self):
        return self.appid

    def getGold(self):
        return self.gold

    def setGold(self):
        self.gold = gold

    def setFlag(self, val):
        self.flag = val

    def getFlag(self):
        return self.flag

    def fight_auto(self, enemy):
        att_type, att_damage = self.getAtt()
        def_type, det_damage = enemy.getDef()
        moo = 0
        if att_type == def_type:
            print('tie')
        elif att_type == "hammer" and def_type == "sword":
            print (self.name)
            enemy.loseHp(att_damage)
        elif att_type == "sword" and def_type == "shield":
            print (self.name)
            enemy.loseHp(att_damage)
        elif att_type == "shield" and def_type == "hammer":
            print (self.name)
            enemy.loseHp(att_damage)
        else:
            print (enemy.getName())
            moo = 1

    def fight(self, att_type, enemy):
        def_type, det_damage = enemy.getDef()
        print(def_type)
        att_damage = self.getAtt_damage(att_type)
        if att_type == def_type:
            self.flag = 0
            enemy.setFlag(0)
        elif att_type == "hammer" and def_type == "sword":
            self.flag = 1
            enemy.setFlag(2)
            enemy.loseHp(att_damage)
        elif att_type == "sword" and def_type == "shield":
            self.flag = 1
            enemy.setFlag(2)
            enemy.loseHp(att_damage)
        elif att_type == "shield" and def_type == "hammer":
            self.flag = 1
            enemy.setFlag(2)
            enemy.loseHp(att_damage)
        else:
            self.flag = 2
            enemy.setFlag(1)
            moo = 1

    def __str__ (self):
            return "%s is an enemy." % (self.name)
