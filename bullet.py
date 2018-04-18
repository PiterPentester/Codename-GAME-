import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game_settings, ship, screen):
        super().__init__()

        self.screen = screen
        
        self.bullet = pygame.image.load("images/laser.png")
        self.bullet = pygame.transform.scale(self.bullet,(8, 25))
        
        self.rect = self.bullet.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        self.rect.y -= self.speed_factor
        
        if self.rect.bottom < 0:
            self.kill()

    def draw_bullet(self):
        self.screen.blit(self.bullet, self.rect)
