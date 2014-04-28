import pygame, label, buttons, img, male, main_game, female, time, random
def setup(man, main_screen):
	main_game.clear((255,255,255),main_screen)
	man.pic_hair = img.img(man.hair_list[man.hair][1],man.hair_list[man.hair][2],man.hair_list[man.hair][0])
	man.pic_hair.draw(main_screen)
	man.pic_mouth = img.img((100,80),(200,300),man.mouth_list[man.mouth])
	man.pic_mouth.draw(main_screen)
	man.pic_nose = img.img((60,50),(220,240),man.nose_list[man.nose])
	man.pic_nose.draw(main_screen)
	man.pic_eyes = img.img((140,50),(180,170),man.eyes_list[man.eye])
	man.pic_eyes.draw(main_screen)
	pygame.image.save(main_screen, "screenshot.jpeg")
def update(main_screen, pos, place, points):
	main_game.clear((255,255,255),main_screen)
	apple = img.img((100,100),(place[0],place[1]),"apple.jpg")
	apple.location = place
	apple.draw(main_screen)
	player = img.img((100,100),pos,"screenshot.jpeg")
	player.draw(main_screen)
	f = buttons.button((170,65),(325,435),(255,151,153))
	f.draw(main_screen)
	g = label.Label((333,440),(70,70),(232,23,61), "None" , 45, str(points) + " points")
	g.draw(main_screen)
	return apple
def run(main_screen, man):
	setup(man, main_screen)
	main_game.clear((255,255,255),main_screen)
	pos = [0,0]
	player = img.img((100,100),pos,"screenshot.jpeg")
	player.draw(main_screen)
	place = [random.randint(0,400),random.randint(0,400)]
	apple = img.img((100,100),(place[0],place[1]),"apple.jpg")
	apple.draw(main_screen)
	points = 0
	while True:
		ev = pygame.event.poll()
		pygame.display.flip()
		if (apple.pic.collidepoint(pos)):
			points+=1
			place = [random.randint(0,400),random.randint(0,400)]
			apple = update(main_screen, pos, place, points)

		if ev.type == pygame.KEYDOWN:
			if ev.key == pygame.K_DOWN:
				pos[1] = pos[1]+15
				update(main_screen, pos, place, points)
			if ev.key == pygame.K_UP:
				pos[1] = pos[1]-15
				update(main_screen, pos, place, points)
			if ev.key == pygame.K_LEFT:
				pos[0] = pos[0]-15
				update(main_screen, pos, place, points)
			if ev.key == pygame.K_RIGHT:
				pos[0] = pos[0]+15
				update(main_screen, pos, place, points)
			

