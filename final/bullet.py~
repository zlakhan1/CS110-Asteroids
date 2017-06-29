import math
import pygame
import os,sys
import ship
def load_image(name, colorkey=None):
	'''Loads an image and converts it to use in pygame'''
	fullname = os.path.join("assets", name) 
	image = pygame.image.load(fullname) 
	image = image.convert_alpha() 
	pygame.transform.scale(image,(75,75))
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
	return image, image.get_rect() 
class bullet(pygame.sprite.Sprite):
	'''Bullet class gets called by the ship'''
	def __init__(self,x,y,angle):
	'''Initalizes the bullet'''
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('laser.png', -1)  
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.rect.x = x
		self.rect.y = y
		self.angle = angle
	def move(self):
		'''The bullet is called then appears on the ships current x,y and with the ships current angle it then travels forward''' 
		angler = math.radians(self.angle) 
		self.rect.x +=(math.cos(angler)) 
		self.rect.y -=(math.sin(angler))	
	def setCoor(self,x,y,angle):
		'''Sets the lasers coordiantes'''
		self.rect.x = x 
		self.rect.y = y 
		self.angle = angle 
	def update(self):
		'''Updates the laser to allow for continous movement'''
		angler = math.radians(self.angle) 
		self.rect.x +=(math.cos(angler) * 20) 
		self.rect.y -=(math.sin(angler) * 20)
