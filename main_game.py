import pygame, label, buttons
import sys 
def clear(color):
	button_rec = pygame.Rect(0,0,500,500)
	button_sq = pygame.Surface([500, 500])
	button_sq.fill(color)
	main_screen.blit(button_sq,button_rec)


if __name__ == "__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((500,500))
	main_screen.fill((255,255,255))
	a = buttons.button((110,60),(360,255),(255,151,153))
	a.draw(main_screen)
<<<<<<< HEAD
	

	
=======
>>>>>>> 370acca7f811c98797131d4d8aa90bd0056a465b
	b = label.Label((370,270) , (75,30) , (232,32,61) , "None", 40, "Female")
	b.draw(main_screen)
	c = buttons.button((110,60),(70,255),(255,151,153))
	c.draw(main_screen)
	d = label.Label((95,270) , (75,30) , (232,23,61) , "None", 40, "Male")
	d.draw(main_screen)
	e = label.Label((180,150) , (60,60) , (232,14,33) , "None", 50, "Welcome !")
	e.draw(main_screen)

<<<<<<< HEAD
	while True:
		ev = pygame.event.poll()

		#CODE...
		pygame.display.flip()

		pygame.display.flip()
		
=======

	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos	
			if c.rec.collidepoint(x,y):
				clear((255,255,255))	
			if a.rec.collidepoint(x,y):
				clear((255,255,255))	
		pygame.display.flip()



>>>>>>> 370acca7f811c98797131d4d8aa90bd0056a465b
