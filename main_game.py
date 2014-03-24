import pygame, label, buttons
def clear(color):
	button_rec = pygame.Rect(0,0,500,500)
	button_sq = pygame.Surface([500, 500])
	button_sq.fill(color)
	main_screen.blit(button_sq,button_rec)
if __name__ == "__main__":
	pygame.init()
	'''main_screen = pygame.display.set_mode((500,500))
	main_screen.fill((255,255,255))
	a = buttons.button((110,60),(360,255),(255,151,153))
	a.draw(main_screen)
<<<<<<< HEAD
	b = buttons.button((200,20),(300,30),(0,234,0))
	b.draw(main_screen)'''
	

	choose_screen = pygame.display.set_mode((500,500))
	choose_screen.fill(255,255,255)
	eyes = buttons.button((20,20),(200,100)),(255,0,0))
	noses = buttons.button((20,220),(200,100),(255,0,0))
	mouths = buttons.button((120,20),(200,100),(255,0,0))
	hair = buttons.button((120,220),(200,100),(255,0,0))
	
=======
	b = label.Label((370,270) , (75,30) , (232,32,61) , "None", 40, "Female")
	b.draw(main_screen)
	c = buttons.button((110,60),(70,255),(255,151,153))
	c.draw(main_screen)
	d = label.Label((95,270) , (75,30) , (232,23,61) , "None", 40, "Male")
	d.draw(main_screen)
	e = label.Label((180,150) , (60,60) , (232,14,33) , "None", 50, "Welcome !")
	e.draw(main_screen)

>>>>>>> 36555160eb342a3f3bdb7578f77869b2e7897c26
	while True:
		ev = pygame.event.poll()

		#CODE...
<<<<<<< HEAD
		pygame.display.flip()
=======
	wq	pygame.display.flip()
		
>>>>>>> 36555160eb342a3f3bdb7578f77869b2e7897c26
