import pygame 
import math
import bullet
class ship:
	'''This is the ship object it can go forward, backward, change its angle, and shoot'''
	def __init__(self, x , y, angle):
		self.x = x
		self.y = y
		self.angle = angle
	def check(self):
	'''Just checks the ships current position and heading'''
		return(str(self.x,self.y,self.angle)) 
	def forward(self,angle):
	'''The ships goes forward based on its current angle,cannot go beyond the screen ''' 
		print("worked angle", self.angle)
		angler = math.radians(self.angle) 
		self.x = self.x + (math.cos(angler) * 1) 
		self.y = self.y + (math.sin(angler) * 1)	
		print(self.x,self.y)
		if self.x >= 270: #just a placeholder for the screen size
			self.x = -270
		if self.y>= 270:
			self.y = -270
	def backward(self,angle):
	'''The ship goes backward based on its current angle,cannot go beyond the screen'''
		angle = math.radians(self.angle)
		self.x = self.x + (math.cos(angle) *-1)
		self.y = self.y + (math.sin(angle) *-1) 
		print(self.x,self.y)
		if self.x >= -270: #placeholder value for screen size
			self.x = 270
		if self.y>= -270:
			self.y = 270
	def changeAngle(self,angle):
	'''Changes the current angle of the ship, postively can't go above 360 or it resets to zero'''
		print("Change is working") 
		self.angle += 10
		print(self.angle) 
		if self.angle>= 360: 
			self.angle = 0
	def shoot(self,angle):
	'''Calls the bullet object'''
		bill = bullet.bullet(self.x, self.y, self.angle)
		bill.move()
		
