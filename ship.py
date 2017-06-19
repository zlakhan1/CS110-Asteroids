import pygame 
import math
import bullet
import sys 
def load_image():
	fullname = os.path.join("assets", spaceship.png) 
	image = pygame.image.load(fullname) 
	 

	return image, image.get_rect()
class ship(pygame.sprite.Sprite):
	'''This is the ship object it can go forward, backward, change its angle, and shoot'''
	def __init__(self, x , y, angle, img_file):
		load_image(img_file) 
		self.rect.x = x
		self.rect.y = y
		self.angle = angle
	def move(self,angle):
		if direction == pygame.K_UP:
			self.angle += 1  
		elif direction == pygame.K_LEFT:
			self.x -= (math.cos(self.angle) * 1) 
			self.y -= (math.sin(self.angle) * 1)	
		elif direction == pygame.K_DOWN:
			self.angle -= 1
		elif direction == pygame.K_RIGHT: 
		  	self.x += (math.cos(self.angle) * 1) 
			self.y += (math.sin(self.angle) * 1)

	def shoot(self,angle):
	'''Calls the bullet object'''
		bill = bullet.bullet(self.x, self.y, self.angle)
		bill.move()
	def update(self):
		print("Updating") 
def tester(key):
	ship.move(key)
def main():
	key = [pygame.K_UP
		
