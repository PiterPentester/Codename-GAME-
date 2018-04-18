import pygame, random
from pygame.sprite import Sprite

class Meteors(Sprite):
	
	def __init__(self, game_settings, screen):
	
		super().__init__()
		self.screen = screen
		self.game_settings = game_settings
		# 
		self.image = pygame.image.load("images/meteor1.png")
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		# 
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# 
		self.y = float(self.rect.y)
	def blitme(self):
	
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		self.y +=  self.game_settings.meteors_speed_factor
		self.rect.y = self.y
		if self.rect.top >= self.screen_rect.bottom:
			self.kill()
