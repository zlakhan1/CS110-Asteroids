import ship
import pygame
import bullet
import asteriod
import random
import score  
		
class Controller:

	def __init__(self,width,height):
		pygame.init()
		self.width = 600
		self.height = 600
		self.screen = pygame.display.set_mode((600,600))
		self.background = pygame.Surface(screen.get_size())  	
		self.ground = background.convert()		
		self.mixinit = pygame.mixer.pre_init()
		self.ship = nimbus.ship(100.0,100.0,90)
		self.asteroid aster.asteriod(100,100,90) 
		
		self.white = (250, 250,250)
		self.screenblit = screen.blit(background,(0,0))	
		self.laser = laser.bullet
		self.mixload = pygame.mixer.music.load('betsky.ogg')
		self.mixplay = pygame.mixer.music.play(loops = 15, start = 0.0)
		self.player = score.score()
		self.flip = pygame.display.flip()
		self.allsprites = pygame.sprite.Group((aster))
		self.shp = pygame.sprite.Group((nimbus,laser))
		self.clock = pygame.time.Clock() 
		start_screen = True
		game_screen = False
		end_screen =False
	
	def mainLoop(self):
		'''This is the Main event Loop of the Game'''
		pygame.key.set_repeat(1,10) 
		while start_screen == True:
			self.backfill = background.fill((0,0,0))
			
		self.intro = pygame.font.SysFont("Britannic Bold", 40)
		intro1 = myfont.render("WELCOME, press enter to start.",1,white) 
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
					return 
			self.keys = pygame.key.get_pressed()
			if keys[pygame.K_KP_ENTER ]:
				print("test") 
				start_screen = False
				game_screen = True 
		screen.blit(intro1,(100,100)) 
		#screen.blit(intro2,(100,100)) 
		#screen.blit(intro3,(100,100)) 
		#screen.blit(intro4,(100,100)) 
		#screen.blit(intro5,(100,100)) 
		pygame.display.flip() 

	while game_screen == True:
		screen.blit(background,(0,0))
		clock.tick(60) 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					return 
			#if event.type == evnt:
				#return
			self.crash = pygame.sprite.collide_rect(aster, nimbus)
			counter = 0			
			if crash:
				nimbus.rect.x =(300)
				nimbus.rect.y =(300)	
				#counter += 1
				nimbus.livesUpdate()
			if nimbus.health<0:
					game_screen = False
					end_screen = True 
				print('health:',nimbus.health)
				print(counter)
			keys = pygame.key.get_pressed()
			nimbus.move(keys) 
			nimbus.shoot(keys) 
			if keys[pygame.K_e]:
				coor = nimbus.shoot(keys)
				laser.setCoor(coor[0] + 30,coor[1],coor[2]) 
		#if event.type == pygame.event.Event(crash)+1:
		#	allsprites.add(aster)
				#allsprites.add(laser) 
		shot = pygame.sprite.spritecollide(laser,allsprites,True)
		if shot:
				allsprites.add(aster)
				aster.rect.x =random.randrange(250)
				aster.rect.y =random.randrange(250)
				laser.rect.x = 6000
				laser.rect.y = 6000
				pygame.display.flip()
				player.points(50)
				print('hit')		
		self.astermove =aster.move(aster.angle) 
		self.curscor = str(player.current())
		self.scorcap = pygame.display.set_caption(currentscore)   
		self.laser.update =update()
		self.alldraw = allsprites.draw(screen)
		self.shpdraw = shp.draw(screen)
		self.screen.blit(nimbus.image,nimbus.rect)
		self.screen.blit(laser.image,laser.rect)
		pygame.display.flip() 

	#quit()
		if end_screen == True:
			self.playerscore = player.player() 
			self.playersscore = 'High Score' + ':' + str(playerscore) 
			self.font = pygame.font.SysFont("Britannic Bold", 40)
			self.intro = font.render("Gameover, press enter to continue", 1,white)
			self.scorer = myfont.render(playerscore, 0 , white) 	
			self. scorer = myfont.render(playerscore, 0 , white)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					return 
			keys = pygame.key.get_pressed()
			if keys[pygame.K_KP_ENTER ]:
				print("test") 
				end_screen = False
				start_screen = True 
		self.screen.blit(intro,(100,100)) 
		self.screen.blit(scorer,(100,50)) 
		pygame.display.flip()

def main():
	window =Controller()
	window.mainLoop() 
main() 

