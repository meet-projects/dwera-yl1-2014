class button(object):
	def __init__(self,size,location,color):
		button_rec = pygame.Rect(location[0], location[1], size[0], size[1])
		button_sq = pygame.Surface([size[0],size[1] ])
		main_screen.blit(button_sq, button_rec)
