"""Arena: hosts single fight for every fights"""

from Enemy_class import *

class Arena(object):
    def __init__(player_1, player_2):
        self.p1 = player_1
        self.p2 = player_2
        self.result = [] #not available, need to be pre-created or make some
                            # creating method in this class
                            # should content p1, p2 names in the first cell

    def fight_auto_defend(self, attacker, defender, att_type):
        """
        Known attack type from attacker, auto generate defend type from defender
        """
        def_type, def_damage = defender.getDef()
        print(def_type)
        att_damage = attacker.getAtt_damage(att_type)
        if att_type == def_type:
            self.flag = 0
            defender.setFlag(0)
        elif att_type == "hammer" and def_type == "sword":
            self.flag = 1
            defender.setFlag(2)
            defender.loseHp(att_damage)
        elif att_type == "sword" and def_type == "shield":
            self.flag = 1
            defender.setFlag(2)
            defender.loseHp(att_damage)
        elif att_type == "shield" and def_type == "hammer":
            self.flag = 1
            defender.setFlag(2)
            defender.loseHp(att_damage)
        else:
            self.flag = 2
            defender.setFlag(1)

    def fight_auto_attack(self, attacker, defender, def_type):
        """
        Known defend type from attacker, auto generate attack type from defender
        """
        att_type, att_damage = attacker.getAtt()
        print(att_type)
        def_damage = defender.getAtt_damage(def_type)
        if att_type == def_type:
            self.flag = 0
            defender.setFlag(0)
        elif att_type == "hammer" and def_type == "sword":
            self.flag = 1
            defender.setFlag(2)
            defender.loseHp(att_damage)
        elif att_type == "sword" and def_type == "shield":
            self.flag = 1
            defender.setFlag(2)
            defender.loseHp(att_damage)
        elif att_type == "shield" and def_type == "hammer":
            self.flag = 1
            defender.setFlag(2)
            defender.loseHp(att_damage)
        else:
            self.flag = 2
            defender.setFlag(1)

    def fight_auto(self, attacker, defender):
        """
        Auto-generate all types
        """
        att_type, att_damage = attacker.getAtt()
        print(att_type)
        def_type, def_damage = defender.getDef()
        print(def_type)
        if att_type == def_type:
            self.flag = 0
            defender.setFlag(0)
        elif att_type == "hammer" and def_type == "sword":
            self.flag = 1
            defender.setFlag(2)
            defender.loseHp(att_damage)
        elif att_type == "sword" and def_type == "shield":
            self.flag = 1
            defender.setFlag(2)
            defender.loseHp(att_damage)
        elif att_type == "shield" and def_type == "hammer":
            self.flag = 1
            defender.setFlag(2)
            defender.loseHp(att_damage)
        else:
            self.flag = 2
            defender.setFlag(1)
