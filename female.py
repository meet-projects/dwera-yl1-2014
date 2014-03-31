import img
class female(object):
	def __init__(self):
		self.hair = 0
		self.eye = 0
		self.nose = 0
		self.mouth = 0
		self.eyes_list = ["images.jpeg", "eyes1.jpeg", "eyes2.jpeg", "eyes.jpeg"]
		self.nose_list = ["nose1.jpeg", "nose.jpeg", "nose2.jpeg"]
		self.mouth_list = ["mouth.jpeg", "mouth9.jpeg", "mouth2.jpeg", "mouth6.jpeg"]
		self.hair_list = ["hair2boy.jpeg", "hairboys.jpeg"]
	def draw(self, choose_screen):
		self.pic_face = img.img((300,400),(100,60),"face.png")
		self.pic_face.draw(choose_screen)
		self.pic_hair = img.img((200,100),(153,60),self.hair_list[self.hair])
		self.pic_hair.draw(choose_screen)
		self.pic_mouth = img.img((100,80),(200,300),self.mouth_list[self.mouth])
		self.pic_mouth.draw(choose_screen)
		self.pic_nose = img.img((60,50),(220,220),self.nose_list[self.nose])
		self.pic_nose.draw(choose_screen)
		self.pic_eyes = img.img((150,50),(180,120),self.eyes_list[self.eye])
		self.pic_eyes.draw(choose_screen)
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
