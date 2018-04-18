import pygame, sys
from bullet import Bullet
from meteors import Meteors

def check_events(game_settings, ship, screen, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_SPACE:
                if len(bullets) < 5:
                    new_bullets = Bullet(game_settings, ship, screen)
                    bullets.add(new_bullets)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            




def update_screen(screen, game_settings, ship, bullets, meteors):
    
    screen.blit(game_settings.bg, (0, 0))
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    meteors.draw(screen)
    pygame.display.flip()
    
def create_meteors(game_settings, screen, meteors):
	
	meteor = Meteors(game_settings, screen)
	meteor_width = meteor.rect.width
	available_space_x = game_settings.screen_width - 2 * meteor_width
	number_meteors_x = int(available_space_x / (2 * meteor_width))
	for meteor_number in range(8):
		meteor = Meteors(game_settings, screen)
		meteor.x = meteor_width + 2 * meteor_width * meteor_number
		meteor.rect.x = meteor.x
		meteors.add(meteor) 
		
def update_meteors(meteors, game_settings, screen):
	meteors.update()


	
	
