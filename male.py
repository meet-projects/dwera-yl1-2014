import img, label, buttons
class male(object):
	def __init__(self):
		self.hair = 0
		self.eye = 0
		self.nose = 0
		self.mouth = 0
		self.eyes_list = ["images.jpeg", "eyes1.jpeg", "eyes2.jpeg", "eyes.jpeg"]
		self.nose_list = ["nose1.jpeg", "nose.jpeg", "nose2.jpeg"]
		self.mouth_list = ["mouth.jpeg", "mouth9.jpeg", "mouth2.jpeg", "mouth4.jpeg"]
		self.hair_list = [["boyheads1.jpeg",(300,600),(80,0)], ["boyheads2.jpeg",(300,600),(90,0)], ["boyheads3.jpeg",(300,600),(90,0)]]
	def draw(self, choose_screen):
		#self.pic_face = img.img((300,600),(90,0),"boyheads2.jpeg")
		#self.pic_face.draw(choose_screen)
		self.pic_hair = img.img(self.hair_list[self.hair][1],self.hair_list[self.hair][2],self.hair_list[self.hair][0])
		self.pic_hair.draw(choose_screen)
		self.pic_mouth = img.img((100,80),(200,300),self.mouth_list[self.mouth])
		self.pic_mouth.draw(choose_screen)
		f = buttons.button((170,65),(325,435),(255,151,153))
		f.draw(choose_screen)
		g = label.Label((333,440),(70,70),(232,23,61), "None" , 45, "Play Again")
		g.draw(choose_screen)
		self.pic_nose = img.img((60,50),(220,240),self.nose_list[self.nose])
		self.pic_nose.draw(choose_screen)
		self.pic_eyes = img.img((140,50),(180,170),self.eyes_list[self.eye])
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

#(300,600),(90,0)
