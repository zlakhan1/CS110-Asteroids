import pygame 
import math
import bullet
import os,sys 
def load_image(name, colorkey=None):
	fullname = os.path.join("assets", name) 
	image = pygame.image.load(fullname) 
	image = image.convert() 
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
	return image, image.get_rect() 
def load_sound(name):
	fullname = os.path.join('assets', name)
	sound = pygame.mixer.Sound(fullname)
	return sound 
class ship(pygame.sprite.Sprite):
	'''This is the ship object it can go forward, backward, change its angle, and shoot'''
	def __init__(self, x , y, angle):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('spaceshipmod.png', -1) 
		self. image = pygame.transform.scale(self.image, (100, 100))
		self.rect.x = float(x)
		self.rect.y = float(y)
		self.angle = float(angle)
		print(type(self.rect.x))
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
			a = ship.rotater(self.image, 10) 
			self.image = a
		elif direction[pygame.K_LEFT]:
			print(self.angle)
			self.rect.x += float((math.cos(math.radians(self.angle)) * 2.0))
			self.rect.y -= float((math.sin(math.radians(self.angle)) *2.0))
			print(type(self.rect.x))
			if 0<self.angle<90:	
				if self.rect.y<0 or self.rect.x>600:
					self.rect.x -= float(600)
					if self.rect.x <0:
						self.rect.x = float(0)
					self.rect.y += float(600)
					if self.rect.y >600 :
						self.rect.y = float(600)
			if self.angle == 90:
				if self.rect.y < 0:
					self.rect.y = self.rect.y + 600	  
			if 90<self.angle<180:	
				if self.rect.x<0 or self.rect.y<0:
					self.rect.x += 600
					if self.rect.x>600:
						self.rect.x = 600
					self.rect.y += 600
					if self.rect.y >600 :
						self.rect.y = 600
			if self.angle == 180:
				if self.rect.x<0:
					self.rect.x += 600	
			if 180<self.angle<270:
				if self.rect.x<0 or self.rect.y>600:
					self.rect.x += 600
					if self.rect.x>600:
						self.rect.x = 600
					self.rect.y -= 600
					if self.rect.y<0:
						self.rect.y = 0 
			if self.angle == 270:
				if self.rect.y>600:
					self.rect.y -= 600
			if 270<self.angle<360:
				if self.rect.x>600 or self.rect.y>600:
					self.rect.x -=600
					if self.rect.x > 600:
						self.rect.x = 600
					self.rect.y -=600
					if self.rect.y > 600:
						self.rect.y = 600
			if self.angle == 360 or self.angle == 0:
				if self.rect.x > 600:
					self.rect.x -= 600

		elif direction[pygame.K_DOWN]:
			print("down") 
			self.angle -= 10
			if self.angle<0:
				self.angle = 360
			b = ship.rotater(self.image,-10) 
			self.image = b
		elif direction[pygame.K_RIGHT]: 
			self.rect.x -= float((math.cos(math.radians(self.angle)) *2)) 
			self.rect.y += float((math.sin(math.radians(self.angle)) *2))
			if 90<self.angle<180:	
				if self.rect.y>600 or self.rect.x>600:
					self.rect.x -= 600
					if self.rect.x <0:
						self.rect.x = float(0)
					self.rect.y -= 600
					if self.rect.y <0 :
						self.rect.y = 0
			if self.angle == 90:
				if self.rect.y > 600:
					self.rect.y -= 600	  
			if 180<self.angle<270:	
				if self.rect.x>600 or self.rect.y<0:
					self.rect.x -= 600
					if self.rect.x<0:
						self.rect.x = 0
					self.rect.y += 600
					if self.rect.y >600 :
						self.rect.y = 600
			if self.angle == 0 or self.angle == 360:
				if self.rect.x<0:
					self.rect.x += 600	
			if 0<self.angle<90:
				if self.rect.x<0 or self.rect.y>600:
					self.rect.x += 600
					if self.rect.x>600:
						self.rect.x = 600
					self.rect.y -= 600
					if self.rect.y<0:
						self.rect.y = 0 
			if self.angle == 270:
				if self.rect.y<0:
					self.rect.y += 600
			if 270<self.angle<360:
				if self.rect.x<0 or self.rect.y<0:
					self.rect.x +=600
					if self.rect.x > 600:
						self.rect.x = 600
					self.rect.y +=600
					if self.rect.y > 600:
						self.rect.y = 600
			if self.angle == 360 or self.angle == 0:
				if self.rect.x > 600:
					self.rect.x -= 600
		elif direction[pygame.K_e]:
			load_sound("blast.wav") 
			bill = bullet.bullet(self.rect.x, self.rect.y, self.angle)
			bill.move()
			print("bullet is :",bill.rect.x,bill.rect.y,bill.angle)
	def update(self):
		print("Updating") 


