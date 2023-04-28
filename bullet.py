import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Klasa przeznaczona do zarządzania pociskami"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/bullet_1.bmp')
        self.rect = self.image.get_rect()

        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)
        self.shot = False

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        
    def shot_bullet(self):
        self.screen.blit(self.image, self.rect)
