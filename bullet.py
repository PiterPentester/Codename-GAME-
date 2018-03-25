import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game_settings, ship, screen):
        super().__init__()

        self.screen = screen
        
        self.bullet_img = pygame.image.load("C:/Users/Xakep/Documents/GitHub/Codename-GAME-/images/laserBlue06.png")
        
        self.image = pygame.transform.scale(self.bullet_img,(5,15))
        
        self.rect = self.image.get_rect()
        
        self.screen_rect = self.screen.get_rect()
        
        self.rect.centerx = ship.rect.centerx
        
        self.rect.top = ship.rect.top

        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        self.rect.y -= self.speed_factor

    def draw_bullet(self):
        self.screen.blit(self.bullet_img, self.rect)
