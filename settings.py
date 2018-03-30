import pygame

class Settings():
    def __init__(self):
        self.screen_width = 700
        self.screen_height = 600
        
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_speed_factor = 7

        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load("тут має бути шлях до вашої картинки фону")
        self.bg = pygame.transform.scale(self.bg, (1920, 1080))

        self.bullet_img = pygame.image.load("тут має бути шлях до вашої картинки лазеру знову")

