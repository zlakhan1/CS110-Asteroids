import math
class bullet:
	def __init__(self, x, y, angle): 
		self.x = x
		self. y = y
		self.angle = angle
	def move(self):
	'''The bullet is called then appears on the ships current x,y and with the ships current angle it then travels forward''' 
		print(self.angle)
		angler = math.radians(self.angle) 
		self.x = self.x + (math.cos(angler) * 10) 
		self.y = self.y + (math.sin(angler) * 10)	
		print(self.x,self.y) 
		
