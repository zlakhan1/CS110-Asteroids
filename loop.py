import ship
import pygame
import bullet
import asteriod
import random
import score  
		

def main():
	
	pygame.init()
	pygame.mixer.pre_init()
	player = score.score()
	#pygame.mixer.music.load('betsky.ogg')
	#pygame.mixer.music.play(loops = 15, start = 0.0)
	screen = pygame.display.set_mode((600,600))
	background = pygame.Surface(screen.get_size()) 
	background = background.convert()
	nimbus = ship.ship(100.0,100.0,90)
	#pewpew = bullet.bullet(nimbus.rect.x,nimbus.rect.y,nimbus.angle)
	aster = asteriod.asteriod(100,100,90) 
	background.fill((0,0,0)) 
	white = (250, 250,250)
	screen.blit(background,(0,0)) 
	laser = bullet.bullet(10,10,0) 
	#pygame.transform.scale(aster, (20, 20))
	#pygame.transform.scale(pewpew, (5, 5))
	pygame.display.flip() 
	randx = random.randrange(300)
	randy = random.randrange(300)
	allsprites = pygame.sprite.Group((aster))
	shp = pygame.sprite.Group((nimbus,laser))
	clock = pygame.time.Clock() 
	pygame.key.set_repeat(1,10) 
	start_screen = True
	game_screen = False 
	end_screen = False 
	#TM = pygame.USEREVENT+1
	#evnt = pygame.event.Event(TM, asteroid) 
	#tmr = pygame.time.set_timer(pygame.USEREVENT +1, 4000)	
	while start_screen == True:
		myfont = pygame.font.SysFont("Britannic Bold", 40)
		intro = myfont.render("Welcome, press enter to start", 1,white) 
		game_over = myfont.render(" G A M E  O V E R", 4,white)
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
					return 
			keys = pygame.key.get_pressed()
			if keys[pygame.K_KP_ENTER ]:
				print("test") 
				start_screen = False
				game_screen = True 
		screen.blit(intro,(100,100)) 
		pygame.display.flip() 

	while game_screen == True:
		screen.blit(background,(0,0))
		clock.tick(160) 
		for event in pygame.event.get():
			#if event.type == evnt:
				#return
			crash = pygame.sprite.collide_rect(aster, nimbus)
			counter = 0			
			if crash:
				nimbus.rect.x =(300)
				nimbus.rect.y =(300)	
				counter += 1
				print('cross')
				print(counter)
			if counter == 1:
				screen.blit(game_over,(100,100))			

			nimbus.score = 0			
			shot = pygame.sprite.spritecollide(laser,allsprites,True)			
			if shot:
				allsprites.add(aster)
				aster.rect.x =random.randrange(250)
				aster.rect.y =random.randrange(250)
				laser.rect.x = 6000
				laser.rect.y = 6000
				pygame.display.flip()
				nimbus.score +=50
				print('hit')
			
			keys = pygame.key.get_pressed()
			nimbus.move(keys) 
			nimbus.shoot(keys) 
			if keys[pygame.K_e]:
				coor = nimbus.shoot(keys)
				laser.setCoor(coor[0] + 30,coor[1],coor[2]) 
		#if event.type == pygame.event.Event(crash)+1:
		#	allsprites.add(aster)
				#allsprites.add(laser) 
		currentscore = str(player.current())
		pygame.display.set_caption(currentscore)   
		laser.update()
		allsprites.draw(screen)
		shp.draw(screen)
		screen.blit(nimbus.image,nimbus.rect)
		screen.blit(laser.image,laser.rect)
		pygame.display.flip() 

	#quit()
	while end_screen == True:
		playerscore = player.player() 
		playerscore = 'High Score' + ':' + str(up) 
		print("up", up) 
		myfont = pygame.font.SysFont("Britannic Bold", 40)
		intro = myfont.render("Gameover, press enter to continue", 1,white)
		scorer = myfont.render(up, 0 , white) 		
		myfont = pygame.font.SysFont("Britannic Bold", 40)
		intro = myfont.render("Gameover, press enter to continue", 1,white) 
		scorer = myfont.render(up, 0 , white)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					return 
			keys = pygame.key.get_pressed()
			if keys[pygame.K_KP_ENTER ]:
				print("test") 
				end_screen = False
				start_screen = True 
		screen.blit(intro,(100,100)) 
		pygame.display.flip() 
main() 

