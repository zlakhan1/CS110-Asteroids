import math
import random 
#import pygame
import os,sys
'''def load_image():#(name, colorkey=None):
	fullname = os.path.join("assets", name) 
	image = pygame.image.load(fullname) 
	image = image.convert() 
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
	return image, image.get_rect() '''
	 

class asteriod():#(pygame.sprite.Sprite):
	'''Asteriod needs some more work just a rough idea of what is needed'''
	def __init__(self,x,y,angle):
		#pygame.sprite.Sprite.__init__(self)
		#self.image, self.rect = load_image('asteriod.png', -1) 
		#self.image = pygame.transform.scale(self.image, (200, 200))
		self.x = x
		self.y =y 
		self.angle = angle 
	def move(self):
		'''Asteriod moves based on angle depending on the random value the asteriods will move at diffrent angles'''
		#print(self.angle)
		angler = math.radians(self.angle) 
		self.x = self.x + (math.cos(angler) * 2) 
		self.y = self.y + (math.sin(angler) * 2)	
		print(self.x,self.y) 
		x = random.randrange(0,11)
		if x % 2 == 0:
			self.angle += 30
		else:
			self.angle -=15
		if self.angle>=360 or self.angle<=-360:
			self.angle = 0
	#def angle(self):
		
			
	def level(self):
		'''Sets the asteriods health'''
		y = random.randrange(0,2)
		if y == 1 :
			self.health = 2
		else:
			self.health = 1 
	
			
		
					
			

