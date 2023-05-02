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
        self.boom_image = pygame.image.load('images/boom.bmp')

        #Prędkość obcego oraz jego i ustawienia spawnu (granica, losowość)
        self.alien_speed = ai_game.level.alien_speed
        self.alien_border = 1200 - self.rect.width
        self.random_spawn(self.aliens)

        #Wartość położenia 'y' jako float aby zwiększyć dokładność
        self.y = float(self.rect.y)

        #Punkty zdrowia oraz status życia
        self.health_points = ai_game.level.alien_health
        self.live = True

        self.collision = False

        self.time_dead = 0


    def update(self, ai_game):
        """Metoda odpowiedzialna za właściwości obcego"""
        #Przesunięcie obcego o 1 alien_speed
        self.y += ai_game.level.alien_speed
        #Aktualizacja położenia y
        self.rect.y = self.y



    def print_alien(self):
        """Metoda generująca obcego"""
        
        #Generowanie pojedynczego obcego
        self.screen.blit(self.image, self.rect)


    def random_spawn(self, aliens):
        """Metoda rekurencyjnie szuka wolnego miejsca na mapie"""

        #Wybór nowego losowego miejsca
        self.rect.x = random.randint(1, self.alien_border)
        self.rect.y = float(random.randint(-500 , 0))

        #Sprawdzenie czy miejsce jest wolne
        for alien in aliens:
            if self.rect.colliderect(alien.rect):
                #Jeżeli nie, metoda wywłuje się do skutku
                self.random_spawn(self.aliens)

    
    def alien_boom(self):
        self.image = self.boom_image
        self.screen.blit(self.image, self.rect)


    def hit(self):
        """Metoda sprawdzająca czy obcy został trafiony"""
        #Status 'zabitego' jeżeli obcy został trafiony
        for bullet in self.bullets:
            if self.rect.colliderect(bullet.rect):
                self.health_points -= 1
                self.bullets.remove(bullet)
                if self.health_points == 0:
                    self.live = False