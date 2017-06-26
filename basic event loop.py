import ship
import pygame
import bullet
import asteriod
import random
  
		

def main():
	
	pygame.init()
	pygame.mixer.pre_init()
	screen = pygame.display.set_mode((600,600))
	background = pygame.Surface(screen.get_size()) 
	background = background.convert()
	nimbus = ship.ship(300.0,300.0,90)
	#pewpew = bullet.bullet(nimbus.rect.x,nimbus.rect.y,nimbus.angle)
	aster = asteriod.asteriod(300,300,90) 
	background.fill((0,0,0)) 
	screen.blit(background,(0,0)) 
	laser = bullet.bullet(10,10,0) 
	#pygame.transform.scale(aster, (20, 20))
	#pygame.transform.scale(pewpew, (5, 5))
	pygame.display.flip() 
	randx = random.randrange(300)
	randy = random.randrange(300)
	allsprites = pygame.sprite.Group((nimbus,aster,))

	clock = pygame.time.Clock() 
	pygame.key.set_repeat(1,10) 
		

	while True:
		screen.blit(background,(0,0))
		clock.tick(120) 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			#pygame.mixer.music.load('theme.mp3') #plays music
			#pygame.mixer.music.play( loops = -1, start = 0.0)	
			if pygame.sprite.collide_rect(aster,nimbus):
				print('cross')
			keys = pygame.key.get_pressed()
			if keys[pygame.K_e]:

				laser.rect.x = nimbus.rect.x
				laser.rect.y = nimbus.rect.y
				laser.angle = nimbus.angle
				allsprites.add(laser) 
				laser.move()
			nimbus.move(keys) 

		allsprites.draw(screen)

		pygame.display.flip() 

	quit() 
main() 
