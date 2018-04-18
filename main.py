import pygame
from settings import Settings
from ship import Ship
import game_function as g_f
from pygame.sprite import Group 

def init_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height)) # Abo 800 na 600
    ship = Ship(screen)
    pygame.display.set_caption("Space-bound")
    bullets = Group()
    meteors = Group()
    
    while True:
        g_f.check_events(game_settings, ship, screen, bullets)
        g_f.update_screen(screen, game_settings, ship, bullets, meteors)
        g_f.update_meteors(meteors, game_settings, screen)
        ship.update()
        bullets.update()
        if len(meteors) == 0:
            g_f.create_meteors(game_settings, screen, meteors)
        collision = pygame.sprite.groupcollide(meteors, bullets, True, True)
                   
init_game()
