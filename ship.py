import pygame

class Ship:
    """Klasa do zarządzania statkiem"""
    def __init__(self, ai_game):
        """Inicjalizacja statku i jego położenia"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Wyświetlanie modelu oraz lokalizacja modelu
        self.forward = pygame.image.load('images/statek.bmp')
        self.right = pygame.image.load('images/statek_prawo.bmp')
        self.left = pygame.image.load('images/statek_lewo.bmp')
        self.rect = self.forward.get_rect()
        self.medium = pygame.image.load('images/flame.bmp')
        self.huge = pygame.image.load('images/flame_huge.bmp')
        self.small = pygame.image.load('images/flame_small.bmp')
        self.rect_flame = self.medium.get_rect()

        #Położenie statku podpisuje jako środek dół EKRANU gry
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect_flame.midbottom = self.rect.midbottom

        #Położenie poziome statku jako float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Opcje poruszania się statku
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update_position(self):
        self.image = self.forward
        self.flame = self.medium
        self.rect_flame.midbottom = self.rect.midbottom
        """Uaktualnienie położenia statku"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            self.image = self.right
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            self.image = self.left
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
            self.flame = self.huge
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
            self.flame = self.small

        self.rect.x = self.x
        self.rect.y = self.y
    
    def print_ship(self):
        """Wyświetlanie modelu w lokalizacji modelu"""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.flame, self.rect_flame)