import math
import random 
import pygame
import os,sys
def load_image(name, colorkey=None):
	'''Loads an image and converts it to use in pygame'''
	fullname = os.path.join("assets", name) 
	image = pygame.image.load(fullname) 
	image = image.convert_alpha() 
	image = pygame.transform.scale(image,(100,100))
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
	return image, image.get_rect() 
	 

	return image, image.get_rect()
class asteriod(pygame.sprite.Sprite):
	'''Asteroidd needs some more work just a rough idea of what is needed'''
	def __init__(self,x,y,angle):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('asteriod.png', -1) 
		self.image = pygame.transform.scale(self.image, (100, 100))
		self.rect.x = x
		self.rect.y =y 
		self.angle = angle 
	def move(self):
		'''Asteriod moves based on angle depending on the random value the asteroids will move at different angles'''
		self.rect.x += (math.cos(math.radians(self.angle)) * 100)
		self.rect.y -= (math.sin(math.radians(self.angle)) * 100)
		'''Checks if the asteriod is pointed toward the first quadarant'''
		if 0<self.angle<90:	
			if self.rect.y<0 or self.rect.x>600:
				self.rect.x -= 600
				if self.rect.x <0:
					self.rect.x = 0
				self.rect.y += 600
				if self.rect.y >600 :
					self.rect.y = 600

		'''Checks if the asteroid is pointed up'''
		if self.angle == 90:
			if self.rect.y < 0:
				self.rect.y = self.rect.y + 600	  

		'''Checks if the asteroid is pointed toward the second quadrant'''
		if 90<self.angle<180:	
			if self.rect.x<0 or self.rect.y<0:
				self.rect.x += 600
				if self.rect.x>600:
						self.rect.x = 600
				self.rect.y += 600
				if self.rect.y >600 :
					self.rect.y = 600

		'''Checks if the asteriod is pointed left'''
		if self.angle == 180:
			if self.rect.x<0:
				self.rect.x += 600
		'''Checks if the asteroid is pointed toward the third quadrant'''	
		if 180<self.angle<270:
			if self.rect.x<0 or self.rect.y>600:
				self.rect.x += 600
				if self.rect.x>600:
					self.rect.x = 600
				self.rect.y -= 600
				if self.rect.y<0:
					self.rect.y = 0 

		'''Checks to see of the asteroid is pointed down'''
		if self.angle == 270:
			if self.rect.y>600:
				self.rect.y -= 600
		'''Checks to see if the asteroid is pointed toward the fourth quadrant'''
		if 270<self.angle<360:
			if self.rect.x>600 or self.rect.y>600:
				self.rect.x -=600
				if self.rect.x > 600:
					self.rect.x = 600
				self.rect.y -=600
				if self.rect.y > 600:
					self.rect.y = 600
		'''Checks to see if the asteroid is pointed to the right''' 
		if self.angle == 360 or self.angle == 0:
			if self.rect.x > 600:
				self.rect.x -= 600
		angler = random.randrange(0,361)
		self.angle = angler
			
	def health(self):
		'''Sets the asteriods health'''
		y = random.randrange(0,2)
		if y == 1 :
			self.level = 1
		else:
			'''If the asteroid is small it will change the image'''
			self.level = 0 
			self.image, self.rect = load_image('littleaster.png', -1) 
	def changeHealth(self):
		'''To be used in a collosion, will decrease the level if it is level 1 ''' 
		if self.level == 1:
			self.level = 0 
