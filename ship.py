#import pygame 
import math
import bullet
import os,sys 
import asteriod 
'''def load_image(name, colorkey=None):
	fullname = os.path.join("assets", name) 
	image = pygame.image.load(fullname) 
	image = image.convert() 
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
	return image, image.get_rect() '''

class ship():#pygame.sprite.Sprite):
	'''This is the ship object it can go forward, backward, change its angle, and shoot'''
	def __init__(self, x , y, angle):
		#pygame.sprite.Sprite.__init__(self)
		#self.image, self.rect = load_image('spaceshipmod.png', -1) 
		#self. image = pygame.transform.scale(self.image, (100, 100))
		#self.rect.x = x
		#self.rect.y = y
		self.x = x
		self.y = y
		self.angle = angle
		self.health = 3 
	def move(self,direction):
		if direction == "w":#direction[pygame.K_UP]:
			print("up") 
			self.angle += 10
			if self.angle >360:
				self.angle = 0 
			#a = ship.rotater(self.image, 10)   
			#self.image = a
		elif direction == "a": #direction[pygame.K_LEFT]:
			print(self.angle)
			if 0<self.angle<90:
				self.x += (math.cos(math.radians(self.angle)) * 2) 
				self.y -= (math.sin(math.radians(self.angle)) * 2)	
			if self.angle == 90:
				self.x += (math.cos(math.radians(self.angle)) * 2)
				self.y -= (math.sin(math.radians(self.angle)) * 2)	 
			if 90<self.angle<180:
				self.x += (math.cos(math.radians(self.angle)) * 2)
				self.y -= (math.sin(math.radians(self.angle)) * 2)	
			if self.angle == 180:
				self.x += (math.cos(math.radians(self.angle)) * 2)
				self.y += (math.sin(math.radians(self.angle)) * 2)	
			if 180<self.angle<270:
				self.x += (math.cos(math.radians(self.angle)) * 2)
				self.y -= (math.sin(math.radians(self.angle)) * 2)
			if self.angle == 270:
				self.x += (math.cos(math.radians(self.angle)) * 2)
				self.y -= (math.sin(math.radians(self.angle)) * 2)
			if 270<self.angle<360:
				self.x += (math.cos(math.radians(self.angle)) * 2)
				self.y -= (math.sin(math.radians(self.angle)) * 2)
			if self.angle == 0 or self.angle ==360:
				self.x += (math.cos(math.radians(self.angle)) * 2)
				self.y += (math.sin(math.radians(self.angle)) * 2)
			#if not 0<self.x<600 or not 0<self.y<600:
			#	self.y -= 600 
			#	self.x -= 600
		elif direction == "s":#direction[pygame.K_DOWN]:
			print("down") 
			self.angle -= 10
			if self.angle<0:
				self.angle = 360
			#b = ship.rotater(self.image,-10) 
			#self.image = b
			
		elif direction == "d":#direction[pygame.K_RIGHT]: 
			if 0<self.angle<90:
				self.x -= (math.cos(math.radians(self.angle)) * 2) 
				self.y += (math.sin(math.radians(self.angle)) * 2)	
			if self.angle == 90:
				self.x -= (math.cos(math.radians(self.angle)) * 2)
				self.y += (math.sin(math.radians(self.angle)) * 2)	 
			if 90<self.angle<180:
				self.x -= (math.cos(math.radians(self.angle)) * 2)
				self.y += (math.sin(math.radians(self.angle)) * 2)	
			if self.angle == 180:
				self.x -= (math.cos(math.radians(self.angle)) * 2)
				self.y -= (math.sin(math.radians(self.angle)) * 2)	
			if 180<self.angle<270:
				self.x -= (math.cos(math.radians(self.angle)) * 2)
				self.y += (math.sin(math.radians(self.angle)) * 2)
			if self.angle == 270:
				self.x -= (math.cos(math.radians(self.angle)) * 2)
				self.y += (math.sin(math.radians(self.angle)) * 2)
			if 270<self.angle<360:
				self.x -= (math.cos(math.radians(self.angle)) * 2)
				self.y += (math.sin(math.radians(self.angle)) * 2)
			if self.angle == 0 or self.angle ==360:
				self.x -= (math.cos(math.radians(self.angle)) * 2)
				self.y -= (math.sin(math.radians(self.angle)) * 2)
			#if self.x>600 or self.y>600:
	
				
	def shoot(self,angle):
		#'''Calls the bullet object'''
		laser = bullet.bullet(self.x, self.y, self.angle)
		laser.move() 
		return laser.x,laser.y,laser.angle
	def collide (self):
		aster = asteriod.asteriod(0,0,0)
		if aster.x == self.rect.x or aster.y == self.rect.y:
			self.health -= 1 
			if self.health == 0:
				print("game over") 
	def update(self):
		print("Updating") 


