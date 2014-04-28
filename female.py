import img, label, buttons
class female(object):
	def __init__(self):
		self.hair = 0
		self.eye = 0
		self.nose = 0
		self.mouth = 0
		self.eyes_list = ["eyes7.jpeg", "eyes11.jpeg", "eyes9.jpeg", "eyes1.jpeg" , "eyes2.jpeg"]
		self.nose_list = ["m1.jpg", "m2.jpg", "nose1.jpeg" , "nose.jpeg" ]
		self.mouth_list = ["mouth6.jpeg", "mouth2.jpeg", "n1.jpeg" , "mouth3.jpeg" ]
		self.hair_list = [["girlheads1.jpeg",(500,650),(25,23)], ["girlheads2.jpeg",(300,600),(97,0)], ["girlheads3.jpeg",(470,585),(-13,-12)]]
	def draw(self, choose_screen):
		#self.pic_face = img.img((300,600),(90,0),"boyheads2.jpeg")
		#self.pic_face.draw(choose_screen)
		self.pic_hair = img.img(self.hair_list[self.hair][1],self.hair_list[self.hair][2],self.hair_list[self.hair][0])
		self.pic_hair.draw(choose_screen)
		self.pic_mouth = img.img((100,80),(200,320),self.mouth_list[self.mouth])
		self.pic_mouth.draw(choose_screen)
		f = buttons.button((170,65),(325,435),(255,151,153))
		f.draw(choose_screen)
		g = label.Label((333,440),(70,70),(232,23,61), "None" , 45, "Play Again")
		g.draw(choose_screen)
		self.pic_nose = img.img((60,58),(220,260),self.nose_list[self.nose])
		self.pic_nose.draw(choose_screen)
		self.pic_eyes = img.img((140,53),(175,206),self.eyes_list[self.eye])
		self.pic_eyes.draw(choose_screen)
		next1 = img.img((50,50),(420,70),"next.png")
		next1.draw(choose_screen)
		pre1 = img.img((50,50),(40,70),"pre.png")
		pre1.draw(choose_screen)
		next2 = img.img((50,50),(420,160),"next.png")
		next2.draw(choose_screen)
		pre2 = img.img((50,50),(40,160),"pre.png")
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
		f2 = buttons.button((170,65),(0,435),(255,151,153))
		f2.draw(choose_screen)
		g2 = label.Label((10,440),(70,70),(232,23,61), "None" , 45, "Play game")
		g2.draw(choose_screen)
	def change_hair(self, num):
		self.hair +=num
		self.hair = self.hair%len(self.hair_list)
	def change_eye(self, num):
		self.eye +=num
		self.eye = self.eye%len(self.eyes_list)
	def change_nose(self, num):
		self.nose +=num
		self.nose = self.nose%len(self.nose_list)
	def change_mouth(self, num):
		self.mouth +=num
		self.mouth = self.mouth%len(self.mouth_list)


