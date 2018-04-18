import pygame

class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_speed_factor = 10
        self.meteors_speed_factor = 5

        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load("images/background.jpg")
       


