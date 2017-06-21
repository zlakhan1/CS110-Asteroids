import pygame 
import math
import bullet
import os,sys 

	 

class ship(pygame.sprite.Sprite):
	'''This is the ship object it can go forward, backward, change its angle, and shoot'''
	def __init__(self, x , y, angle):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('spaceshipmod.png', -1) 
		self. image = pygame.transform.scale(self.image, (100, 100))
		self.rect.x = x
		self.rect.y = y
		self.angle = angle
	def rotater(image,angle):
		"""rotate an image while keeping its center and size"""
		orig_rect = image.get_rect()
		rot_image = pygame.transform.rotate(image, angle)
		rot_rect = orig_rect.copy()
		rot_rect.center = rot_image.get_rect().center
		rot_image = rot_image.subsurface(rot_rect).copy()
		return rot_image
	def move(self,direction):
		print("move gets called") 
		print(self.rect.x, self.rect.y)  
		pygame.key.get_pressed
		if direction[pygame.K_UP]:
			print("up") 
			self.angle += 10
			if self.angle >360:
				self.angle = 0 
			
		elif direction[pygame.K_LEFT]:
			print(self.angle)
			if 0<self.angle<90:
				self.rect.x += (math.cos(math.radians(self.angle)) * 2) 
				self.rect.y -= (math.sin(math.radians(self.angle)) * 2)	
			if self.angle == 90:
				self.rect.x += (math.cos(math.radians(self.angle)) * 2)
				self.rect.y -= (math.sin(math.radians(self.angle)) * 2)	 
			if 90<self.angle<180:
				self.rect.x += (math.cos(math.radians(self.angle)) * 2)
				self.rect.y -= (math.sin(math.radians(self.angle)) * 2)	
			if self.angle == 180:
				self.rect.x += (math.cos(math.radians(self.angle)) * 2)
				self.rect.y += (math.sin(math.radians(self.angle)) * 2)	
			if 180<self.angle<270:
				self.rect.x += (math.cos(math.radians(self.angle)) * 2)
				self.rect.y -= (math.sin(math.radians(self.angle)) * 2)
			if self.angle == 270:
				self.rect.x += (math.cos(math.radians(self.angle)) * 2)
				self.rect.y -= (math.sin(math.radians(self.angle)) * 2)
			if 270<self.angle<360:
				self.rect.x += (math.cos(math.radians(self.angle)) * 2)
				self.rect.y -= (math.sin(math.radians(self.angle)) * 2)
			if self.angle == 0 or self.angle ==360:
				self.rect.x += (math.cos(math.radians(self.angle)) * 2)
				self.rect.y += (math.sin(math.radians(self.angle)) * 2)
			if self.rect.y < 0 or self.rect.x <0: 
				self.rect.y += 600
				self.rect.x += 600
			if self.rect.y > 600 or self.rect.x>600:
				self.rect.y -= 600 
				self.rect.x -= 600
		elif direction[pygame.K_DOWN]:
			print("down") 
			self.angle -= 10
			if self.angle<0:
				self.angle = 360
			
		elif direction[pygame.K_RIGHT]: 
			if 0<self.angle<90:
				self.rect.x -= (math.cos(math.radians(self.angle)) * 2) 
				self.rect.y += (math.sin(math.radians(self.angle)) * 2)	
			if self.angle == 90:
				self.rect.x -= (math.cos(math.radians(self.angle)) * 2)
				self.rect.y += (math.sin(math.radians(self.angle)) * 2)	 
			if 90<self.angle<180:
				self.rect.x -= (math.cos(math.radians(self.angle)) * 2)
				self.rect.y += (math.sin(math.radians(self.angle)) * 2)	
			if self.angle == 180:
				self.rect.x -= (math.cos(math.radians(self.angle)) * 2)
				self.rect.y -= (math.sin(math.radians(self.angle)) * 2)	
			if 180<self.angle<270:
				self.rect.x -= (math.cos(math.radians(self.angle)) * 2)
				self.rect.y += (math.sin(math.radians(self.angle)) * 2)
			if self.angle == 270:
				self.rect.x -= (math.cos(math.radians(self.angle)) * 2)
				self.rect.y += (math.sin(math.radians(self.angle)) * 2)
			if 270<self.angle<360:
				self.rect.x -= (math.cos(math.radians(self.angle)) * 2)
				self.rect.y += (math.sin(math.radians(self.angle)) * 2)
			if self.angle == 0 or self.angle ==360:
				self.rect.x -= (math.cos(math.radians(self.angle)) * 2)
				self.rect.y -= (math.sin(math.radians(self.angle)) * 2)
			
	def shoot(self,angle):
		'''Calls the bullet object'''
		bill = bullet.bullet(self.x, self.y, self.angle)
		bill.move()
	def update(self):
		print("Updating") 


