import pygame

class Ship:
    """Klasa przeznaczona do zarządzania statkiem"""

    def __init__(self, ai_game):
        """Inicjalizacja właściwości i zasobów statku"""
        super().__init__()

        #Zasoby z gry
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Obraz oraz obszar statku
        self.forward = pygame.image.load('images/statek.bmp')
        self.right = pygame.image.load('images/statek_prawo.bmp')
        self.left = pygame.image.load('images/statek_lewo.bmp')
        self.rect = self.forward.get_rect()

        #Obraz oraz obszar płomienia
        self.medium = pygame.image.load('images/flame.bmp')
        self.huge = pygame.image.load('images/flame_huge.bmp')
        self.small = pygame.image.load('images/flame_small.bmp')
        self.rect_flame = self.medium.get_rect()

        #Początkowe położenie statku
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect_flame.midbottom = self.rect.midbottom

        #Położenie statku jako float aby zwiększyć dokładność
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Poruszanie się statku po inicjacji
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Uaktualnienie położenia statku"""

        #Ustawianie forward i medium jako domyślna tekstura
        self.image = self.forward
        self.flame = self.medium

        #Płomień przypięty do statku
        self.rect_flame.midbottom = self.rect.midbottom

        #Starowanie statkiem po ekranie i wybieranie odpowiedniej tektury
        #Warunki gwarantują, że statek nie wyleci za ekran
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

        #Przypisywanie zaktualizowanych koordynatów do rzeczywistej pozycji statku
        self.rect.x = self.x
        self.rect.y = self.y


    def print_ship(self):
        """Metoda generująca statek"""
        
        #Generowanie statku
        self.screen.blit(self.image, self.rect)
        #Generowanie płomienia
        self.screen.blit(self.flame, self.rect_flame)
