import math
import random 

class asteriod:
	'''Asteriod needs some more work just a rough idea of what is needed'''
	def __init__(self,x,y,angle):
		self.x = x
		self.y =y 
		self.angle = angle 
	def move(self):
	'''Asteriod moves based on angle depending on the random value the asteriods will move at diffrent angles'''
		print(self.angle)
		angler = math.radians(self.angle) 
		self.x = self.x + (math.cos(angler) * 2) 
		self.y = self.y + (math.sin(angler) * 2)	
		print(self.x,self.y) 
	def angle(self):
		x = random.randrange(0,11):
			if x % 2 == 0:
				self.angle += 30
			else:
				self.angle -=15
		if self.angle>=360 or self.angle<=-360:
			self.angle = 0
			
	def health(self, level):
	'''Sets the asteriods health, it will do more later'''
		y = random.randrange(0,2)
			if y == 1 :
				self.level = 1
			else:
				self.level = 0 

