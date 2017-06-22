import ship
import pygame
import bullet
import asteriod

  
		

def main(): 
	pygame.init()
	screen = pygame.display.set_mode((600,600))
	background = pygame.Surface(screen.get_size()) 
	background = background.convert()
	nimbus = ship.ship(300.0,300.0,90)
	#pewpew = bullet.bullet(nimbus.rect.x,nimbus.rect.y,nimbus.angle)
	aster = asteriod.asteriod(300,300,90) 
	background.fill((0,0,0)) 
	screen.blit(background,(0,0)) 
	#pygame.transform.scale(aster, (20, 20))
	#pygame.transform.scale(pewpew, (5, 5))
	pygame.display.flip() 
	allsprites = pygame.sprite.Group((nimbus))
	clock = pygame.time.Clock() 
	pygame.key.set_repeat(1,10) 
	while True:
		
		clock.tick(30) 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
			keys = pygame.key.get_pressed()
			#if keys[pygame.K_e]:
				#laser = bullet.bullet() 
				#laser.rect.x = nimbus.rect.x
				#laser.rect.y = nimbus.rect.y
				#laser.angle = nimbus.angle
				#allsprites.add(laser) 
				#laser.move(laser.rect.x,laser.rect.y,laser.angle)
			nimbus.move(keys)
		#aster.move()  
		allsprites.draw(screen)
		pygame.display.flip() 
main() 
