import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Klasa przeznaczona do zarządzania pociskiem"""

    def __init__(self, ai_game):
        """Inicjalizacja właściwości i zasobów pocisku"""
        super().__init__()

        #Zasoby z gry
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.aliens = ai_game.aliens

        #Inicjalizacja grafiki i powierzchni pocisku oraz jego początkowe umiejscowienie na ekranie
        self.image = pygame.image.load('images/bullet_1.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        #Wartość położenia 'y' jako float aby zwiększyć dokładność
        self.y = float(self.rect.y)


    def update(self):
        """Metoda przesuwająca pocisk w góre ekranu o 1 bullet_speed"""

        #Przesunięcie pocisku o 1 bullet_speed
        self.y -= self.settings.bullet_speed
        #Aktualizacja położenia y
        self.rect.y = self.y


    def print_bullet(self):
        """Metoda generująca pocisk"""
        
        #Generowanie pojedynczego pocisku
        self.screen.blit(self.image, self.rect)


    def hit(self):
        """Metoda sprawdzająca czy pocisk trafił w obcego"""

        #Usuwanie konkretnego obcego po kontakcie z pociskiem
        for alien in self.aliens:
            if self.rect.colliderect(alien.rect):
                self.aliens.remove(alien)
                return True