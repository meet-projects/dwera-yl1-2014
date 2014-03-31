import pygame
class img(object):
	def __init__(self,size,location,url):
		self.size = size
		self.location = location
		self.url = url
	def draw(self,main_screen):
		self.pic  = pygame.Rect(self.location[0],self.location[1],self.size[0],self.size[1])
		img = pygame.image.load(self.url)
		img =  pygame.transform.scale(img, (self.size[0], self.size[1]))
		main_screen.blit(img, self.pic)
