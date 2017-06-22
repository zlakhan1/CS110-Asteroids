import math
import pygame
import os,sys
import ship
def load_image(name, colorkey=None):
	fullname = os.path.join("assets", name) 
	image = pygame.image.load(fullname) 
	image = image.convert() 
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
	return image, image.get_rect() 
class bullet(pygame.sprite.Sprite):
	def __init__(self,x,y,angle):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('laser.png', -1)  
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.rect.x = x
		self.rect.y = y
		self.angle = angle
	def move(self):
		'''The bullet is called then appears on the ships current x,y and with the ships current angle it then travels forward''' 
		print(self.angle)
		angler = math.radians(self.angle) 
		self.rect.x +=(math.cos(angler) * 10) 
		self.rect.y +=(math.sin(angler) * 10)	
		print(self.rect.x,self.rect.y) 
	def update(self):
		print("updating") 
