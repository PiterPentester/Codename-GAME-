import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game_settings, ship, screen):
        super().__init__()

        self.screen = screen

        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)


        self.bullet_img = pygame.image.load("/home/ostap/PycharmProjects/Game1/Game1/images/new_bullet.png")
        self.image = self.bullet_img

        self.rect = self.image.get_rect()

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        self.rect.y -= self.speed_factor

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)