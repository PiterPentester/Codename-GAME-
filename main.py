import pygame, sys
from settings import Settings
from ship import Ship
import game_function as g_f

def init_game():
    pygame.init()

    game_settings = Settings()

    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption("Mine Game")

    while True:
        g_f.check_events(ship)
        g_f.update_screen(screen, game_settings, ship)
        ship.update()


init_game()
