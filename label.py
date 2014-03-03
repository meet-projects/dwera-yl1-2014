class Label(object):
	def __init__(self, place , size , color , font, font_size, text):
		self.p = place
		self.s = size
		self.c = color
		self.f = font
		self.fs = font_size
		self.t = text
		label_rec = pygame.Rect(self.p[0], self.p[1], self.s[0], self.s[1])
		orderlabel = pygame.font.Font(self.f, self.fs)
		label = orderlabel.render(self.t , 1, self.c , (255,255,255))
		main_screen.blit(label, button_rec)	
