import pygame, label, buttons, img, male, main_game
def clear(color, main_screen):
	button_rec = pygame.Rect(0,0,500,500)
	button_sq = pygame.Surface([500, 500])
	button_sq.fill(color)
	main_screen.blit(button_sq,button_rec)
def run(choose_screen, boolean):
	if (boolean):
		man = male.male()
		man.draw(choose_screen)
		next1 = img.img((50,50),(420,70),"next.png")
		next1.draw(choose_screen)
		pre1 = img.img((50,50),(40,70),"pre.png")
		pre1.draw(choose_screen)
		next2 = img.img((50,50),(420,120),"next.png")
		next2.draw(choose_screen)
		pre2 = img.img((50,50),(40,120),"pre.png")
		pre2.draw(choose_screen)
		next3 = img.img((50,50),(420,220),"next.png")
		next3.draw(choose_screen)
		pre3 = img.img((50,50),(40,220),"pre.png")
		pre3.draw(choose_screen)
		next4 = img.img((50,50),(420,320),"next.png")
		next4.draw(choose_screen)
		pre4 = img.img((50,50),(40,320),"pre.png")
		pre4.draw(choose_screen)
		f = buttons.button((170,65),(325,435),(255,151,153))
		f.draw(choose_screen)
		g = label.Label((333,440),(70,70),(232,23,61), "None" , 45, "Play Again")
		g.draw(choose_screen)
		pygame.display.flip()
	else:
		x=0
	while True:
		ev = pygame.event.poll()

		#CODE...
		pygame.display.flip()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos	
			if f.rec.collidepoint(x,y):
				clear((255,255,255), choose_screen)
				main_game.run(choose_screen)
			if next1.pic.collidepoint(x,y):
				man.change_hair(1)
				man.draw(choose_screen)
			if pre1.pic.collidepoint(x,y):
				man.change_hair(-1)
				man.draw(choose_screen)
			if next2.pic.collidepoint(x,y):
				man.change_eye(1)
				man.draw(choose_screen)
			if pre2.pic.collidepoint(x,y):
				man.change_eye(-1)
				man.draw(choose_screen)
			if next3.pic.collidepoint(x,y):
				man.change_nose(1)
				man.draw(choose_screen)
			if pre3.pic.collidepoint(x,y):
				man.change_nose(-1)
				man.draw(choose_screen)
			if next4.pic.collidepoint(x,y):
				man.change_mouth(1)
				man.draw(choose_screen)
			if pre4.pic.collidepoint(x,y):
				man.change_mouth(-1)
				man.draw(choose_screen)
