import math
import random 
import pygame
import os,sys
def load_image(name, colorkey=None):
	fullname = os.path.join("assets", name) 
	image = pygame.image.load(fullname) 
	image = image.convert() 
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
	return image, image.get_rect() 
	 

	return image, image.get_rect()
class asteriod(pygame.sprite.Sprite):
	'''Asteriod needs some more work just a rough idea of what is needed'''
	def __init__(self,x,y,angle):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('asteriod.png', -1) 
		self.image = pygame.transform.scale(self.image, (200, 200))
		self.rect.x = x
		self.rect.y =y 
		self.angle = angle 
	def move(self):
		'''Asteriod moves based on angle depending on the random value the asteriods will move at diffrent angles'''
		print(self.angle)
		angler = math.radians(self.angle)
		moverx = random.randrange(0,21) 
		movery = random.randrange(0,21)
		self.rect.x += (math.cos(angler) * moverx) 
		self.rect.y += (math.sin(angler) * movery)
		if self.rect.x >600 or self.rect.y<0:
			self.rect.x -= 600
			self.rect.y += 600
		if self.rect.x<0 or self.rect.y>600:
			self.rect.x += 600
			self.rect.y -= 600
		x = random.randrange(0,11)
		angleOne = random.randrange(0,361)
		angleTwo = random.randrange(0,361) 
		if x % 2 == 0:
			self.angle += angleOne
		else:
			self.angle -= angleTwo
		if self.angle>=360 or self.angle<=-360:
			self.angle = 0
			
	def health(self, level):
		'''Sets the asteriods health, it will do more later'''
		y = random.randrange(0,2)
		if y == 1 :
			self.level = 1
		else:
			self.level = 0 

