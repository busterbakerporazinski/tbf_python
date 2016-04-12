#!/usr/bin/env python

import pygame
import os

from pygame.locals import *

class Player:

	def __init__(self, screen):
		self.screen = screen

		self.image = pygame.image.load(os.path.join('img', 'logo.png'))

		self.x = 10
		self.y = 10

		self.width = self.image.get_width()
		self.height = slef.image.get_height()

		self.speed = 10 

	def update(self):
		pass

	def draw(self, screen=None):
		if screen is None:
			screen = self.screen

		screen.blit(self.image, (self.x, self.y))
