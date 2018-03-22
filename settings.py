import pygame

class Settings():
    def __init__(self):
        self.screen_width = 700
        self.screen_height = 600
        self.bg_color = (0,123,123)

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 2

        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load("/home/ostap/PycharmProjects/Game1/Game1/images/background1.jpg")
        self.bg = pygame.transform.scale(self.bg, (1920, 1080))

        #self.bullet_img = pygame.image.load("/home/ostap/PycharmProjects/Game1/Game1/images/new_bullet.png").convert()
