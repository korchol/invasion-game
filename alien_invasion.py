import sys
import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Zarządzanie zasobami i sposób działania gry"""

    def __init__(self):
        """Inizjalizacja gry i utworzenie zasobów"""
        pygame.init()
        #Utworzenie egzemplarza domyślnych ustawień
        self.settings = Settings()
        #Ekran gry zarządzany przez ustawienia
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), self.settings.fullscreen)
        #Utworzenie egzemplarza statku
        self.ship = Ship(self)
        #Podpis okna wskazany w ustawieniach
        pygame.display.set_caption(self.settings.window_caption)
        #Definiowanie kolejki na wystrzelone pociski
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Główna pętla gry"""
        while True:
            self._check_events()
            self.ship.update_position()
            self._update_bullets()
            self._update_screen()

    def _update_screen(self):
        """Wyświetlanie obrazów gry"""
        self.screen.blit(self.settings.background, self.settings.rect)
        for bullet in self.bullets.sprites():
            bullet.shot_bullet()
        self.ship.print_ship()
        for alien in self.aliens.sprites():
            alien.print_alien()
        
        pygame.display.flip()

    def _check_events(self):
        """Pobieranie oraz reagowanie na poszczególne grupy wydarzeń"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._key_up_events(event)
    
    def _key_down_events(self, event):
        """Wydarzenie typu: wciśnięty klawisz"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._shot()
        elif event.key == pygame.K_q:
            sys.exit()

    def _key_up_events(self, event):
        """Wydarzenie typu: zwolniony klawisz"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False       
    
    def _shot(self):
        """Utworzenie egzemplarza pocisku oraz dodanie go do grupy istniejących"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        #Update położenia pocisków
        self.bullets.update()
        #Usuwamnie pocisku poza ekranem
        for bullet in self.bullets:
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Utworzenie egzemplarza obcego oraz dodanie go do grupy istniejących"""
        new_alien = Alien(self)
        self.aliens.add(new_alien)




if __name__ == '__main__':
    #Utworzenie egzemplarza gry i wywołanie metody rozpoczynającej pętlę gry
    ai = AlienInvasion()
    ai.run_game()