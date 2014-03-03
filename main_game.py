import pygame
def clear(color):
	button_rec = pygame.Rect(0,0,500,500)
	button_sq = pygame.Surface([500, 500])
	button_sq.fill(color)
	main_screen.blit(button_sq,button_rec)
if __name__ == "__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((500,500))
	main_screen.fill((255,255,255))
	while True:
		ev = pygame.event.poll()

		#CODE...
		pygame.display.flip()
		
