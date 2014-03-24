import pygame, label, buttons
def clear(color):
	button_rec = pygame.Rect(0,0,500,500)
	button_sq = pygame.Surface([500, 500])
	button_sq.fill(color)
	main_screen.blit(button_sq,button_rec)
if __name__ == "__main__":
	pygame.init()
	choose_screen = pygame.display.set_mode((500,500))
	choose_screen.fill((255,255,255))
	eyes = buttons.button((200,100),(20,20),(255,0,0))
	eyes.draw(choose_screen)
	eyesl = label.Label(((200,100),(20,20),(0,0,0),	
	noses = buttons.button((200,100),(20,130),(0,0,0))
	noses.draw(choose_screen)
	mouths = buttons.button((200,100),(230,20),(0,255,0))
	mouths.draw(choose_screen)
	hair = buttons.button((200,100),(230,130),(0,0,255))
	hair.draw(choose_screen)
	
	while True:
		ev = pygame.event.poll()

		#CODE...
		pygame.display.flip()
