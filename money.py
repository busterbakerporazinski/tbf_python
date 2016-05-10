! /usr/bin/env python3

#Money Class

#Jay Chawla

#Function that stores amount, returns that amount, & prints it

class Money(object):

    def __init__(self, amount):
        self.amount = amount

    def getAmount(self):
        return self.amount

    def __str__(self):
        return "This is %s amount" % (self.amount)
