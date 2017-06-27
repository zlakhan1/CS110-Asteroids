import pygame 
import math
import bullet
import os,sys 
def load_image(name, colorkey=None):
	'''Loads an image and converts it to use in pygame'''
	fullname = os.path.join("assets", name) 
	image = pygame.image.load(fullname) 
	image = image.convert_alpha() 
	pygame.transform.scale(image,(100,100))
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
		self.image= pygame.transform.scale(self.image, (100, 100))
		self.rect.x = x
		self.rect.y = y
		self.angle = angle
		self.health = 3 
	def rotater(image,angle):
		"""rotate an image while keeping its center and size"""
		orig_rect = image.get_rect()
		rot_image = pygame.transform.rotate(image, angle)
		rot_rect = orig_rect.copy()
		rot_rect.center = rot_image.get_rect().center
		rot_image = rot_image.subsurface(rot_rect).copy()
		return rot_image
	def move(self,direction):
		pygame.key.get_pressed
		if direction[pygame.K_UP]:
			self.angle += 10
			if self.angle > 360:
				self.angle = 0 
			a = ship.rotater(self.image, 10) 
			self.image = a
		elif direction[pygame.K_LEFT]:
			self.rect.x += (math.cos(math.radians(self.angle)) * 2.0) #moves x based on cosine 
			self.rect.y -= (math.sin(math.radians(self.angle)) *2.0) # moves y based on sine 
			'''Checks if the ship is pointing toward first quadrant'''
			if 0<self.angle<90:	
				if self.rect.y<0 or self.rect.x>600:
					self.rect.x -= 600
					if self.rect.x <0:
						self.rect.x = 0
					self.rect.y += 600
					if self.rect.y >600 :
						self.rect.y = 600

			'''Checks if the ship is pointing toward top'''
			if self.angle == 90:
				if self.rect.y < 0:
					self.rect.y = self.rect.y + 600


			'''Checks if the ship is pointing toward the second quadrant'''	  
			if 90<self.angle<180:	
				if self.rect.x<0 or self.rect.y<0:
					self.rect.x += 600
					if self.rect.x>600:
						self.rect.x = 600
					self.rect.y += 600
					if self.rect.y >600 :
						self.rect.y = 600

			'''Checks if the ship is pointing right'''
			if self.angle == 180:
				if self.rect.x<0:
					self.rect.x += 600	


			'''Checks if the ship is point toward the third quadrant'''
			if 180<self.angle<270:
				if self.rect.x<0 or self.rect.y>600:
					self.rect.x += 600
					if self.rect.x>600:
						self.rect.x = 600
					self.rect.y -= 600
					if self.rect.y<0:
						self.rect.y = 0 
			
			'''Checks if the ship is point down'''
			if self.angle == 270:
				if self.rect.y>600:
					self.rect.y -= 600

			'''Checks if the ship is pointing toward the fourth quadrant'''
			if 270<self.angle<360:
				if self.rect.x>600 or self.rect.y>600:
					self.rect.x -=600
					if self.rect.x > 600:
						self.rect.x = 600
					self.rect.y -=600
					if self.rect.y > 600:
						self.rect.y = 600
			
			'''Checks if the ship is pointed left'''		
			if self.angle == 360 or self.angle == 0:
				if self.rect.x > 600:
					self.rect.x -= 600
		elif direction[pygame.K_DOWN]:
			'''Decreases the ships angle by ten'''
			self.angle -= 10
			'''Converts a negative angle 360'''
			if self.angle<0:
				self.angle = 360
			b = ship.rotater(self.image,-10) 
			self.image = b
		elif direction[pygame.K_RIGHT]: 
			'''Moves the ship backwards'''
			self.rect.x -= (math.cos(math.radians(self.angle)) *2)
			self.rect.y += (math.sin(math.radians(self.angle)) *2)

			'''Checks if the ship is pointing tward the second quadrant'''
			if 90<self.angle<180:	
				if self.rect.y>600 or self.rect.x>600:
					self.rect.x -= 600
					if self.rect.x <0:
						self.rect.x = 0
					self.rect.y -= 600
					if self.rect.y <0 :
						self.rect.y = 0

			'''Checks if the ship is pointed up'''
			if self.angle == 90:
				if self.rect.y > 600:
					self.rect.y -= 600	

			'''Checks if the ship is pointed toward the third quadrant'''  
			if 180<self.angle<270:	
				if self.rect.x>600 or self.rect.y<0:
					self.rect.x -= 600
					if self.rect.x<0:
						self.rect.x = 0
					self.rect.y += 600
					if self.rect.y >600 :
						self.rect.y = 600
			'''Checks if the pointed toward the first quadrant'''	
			if 0<self.angle<90:
				if self.rect.x<0 or self.rect.y>600:
					self.rect.x += 600
					if self.rect.x>600:
						self.rect.x = 600
					self.rect.y -= 600
					if self.rect.y<0:
						self.rect.y = 0 
			'''Checks if the ship is pointed down'''
			if self.angle == 270:
				if self.rect.y<0:
					self.rect.y += 600
			'''Checks if the ship is pointed toward the fourth quadrant'''
			if 270<self.angle<360:
				if self.rect.x<0 or self.rect.y<0:
					self.rect.x +=600
					if self.rect.x > 600:
						self.rect.x = 600
					self.rect.y +=600
					if self.rect.y > 600:
						self.rect.y = 600

			'''Checks if the ship is pointed right''' 
			if self.angle == 360 or self.angle == 0:
				if self.rect.x > 600:
					self.rect.x -= 600
	def shoot(self,key):
		if key[pygame.K_e]:
			'''creates and calls the bullet class to shoot'''
			bill = bullet.bullet(self.rect.x, self.rect.y, self.angle)
			bill.move()
			coor = [bill.rect.x, bill.rect.y, bill.angle]
			return coor 
	def livesUpdate(self):
		'''Decreases the number of lives'''
		self.health -= 1 
	def update(self):
		print("Updating") 

