#!/usr/bin/env python3
# Jay Chawla 
# 032416 CURRENCY
#Creates wallet; stored object. Storage that can hold an amount and remembers the last amount

class Currency(object):

	def __init__(self, moneypool, lastadd, lastsub, fiveper, tenper):
		self.moneypool = moneypool
		self.lastadd = lastadd
		self.lastsub = lastsub
		self.fiveper = fiveper
		self.tenper = tenper

	def getPool(self):
		return self.moneypool #returns moneypool total.


	def getLAdd(self, avalue): #adds an amount and returns that amount too money pool.

		self.avalue = avalue
		self.moneypool = (self.avalue + self.moneypool)

		self.lastadd = self.avalue

		return self.lastadd


	def getLSub(self, svalue): #subtracts an amount and returns that amount from money pool.

		self.svalue = svalue
		self.moneypool = (self.svalue - self.moneypool)

		self.lastsub = self.svalue

		return self.lastsub


	def fivePercentIt(self):
		sel.fiveper = self.lastadd * (0.5) #takes the last add value and returns 5% of value.
		return self.fiveper

	def tenPercentIt(self):
		self.tenper = self.lastadd * (.1) #takes the last add value and returns 10% of value.
		return self.tenper

	def __str__ (self):
		return "Pool: %s | Last Add: %s |" % (self.moneypool, self.lastadd)
