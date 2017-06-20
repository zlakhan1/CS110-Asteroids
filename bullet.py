import math
import ship
class bullet():
	def __init__(self, x, y, angle): 
		#ship.__init__(self,x,y,angle) 
		self.x = x
		self.y = y
		self.angle = angle
	def move(self):
		angler = math.radians(self.angle)
		print("angler:",angler)  
		print("cos:",(math.cos(angler) * 10), "sin:",(math.sin(angler) * 10))  
		self.x += (math.cos(angler) * 10) 
		self.y += (math.sin(angler) * 10)	
		print(self.x,self.y) 
		
