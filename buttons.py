import pygame
class button(object):
	def __init__(self,size,location,color):
		self.size = size
		self.location = location
		self.color = color
	def draw(self,main_screen):
		button_rec = pygame.Rect(self.location[0], self.location[1], self.size[0], self.size[1])
		button_sq = pygame.Surface([self.size[0],self.size[1] ])
		button_sq.fill(self.color)
		main_screen.blit(button_sq, button_rec)
