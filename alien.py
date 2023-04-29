import random
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa przeznaczona do zarządzania obcym"""

    def __init__(self, ai_game):
        """Inicjalizacja właściwości i zasobów obcego"""
        super().__init__()

        #Zasoby z gry
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.aliens = ai_game.aliens
        self.bullets = ai_game.bullets

        #Obraz oraz obszar obcego
        self.image = pygame.image.load('images/alien1.bmp')
        self.rect = self.image.get_rect()

        #Prędkość obcego oraz jego i ustawienia spawnu (granica, losowość)
        self.alien_speed = 0.5
        self.alien_border = 1200 - self.rect.width
        self.random_spawn()

        #Wartość położenia 'y' jako float aby zwiększyć dokładność
        self.y = float(self.rect.y)


    def print_alien(self):
        self.screen.blit(self.image, self.rect)


    def random_spawn(self):
        self.rect.x = random.randint(1, self.alien_border)
        self.rect.y = float(random.randint(-500 , 0))
        while self.colision(self.aliens):
            self.rect.x = random.randint(1, self.alien_border)
            self.rect.y = random.randint(-500 , 0)


    def colision(self, aliens):
            for alien in aliens:
                if self.rect.colliderect(alien.rect):
                    return True
    

    def update(self):
        self.y += self.alien_speed
        self.rect.y = self.y
    

    # def hit(self):
    #     """Metoda sprawdzająca czy pocisk został napotkany"""

    #     #Usuwanie konkretnego pocisku po kontakcie z obcym
    #     for bullet in self.bullets:
    #         if self.rect.colliderect(bullet.rect):
    #             self.aliens.remove(bullet)
    #             return True

