import sys
import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Zarządzanie zasobami i sposób działania gry"""

    def __init__(self):
        """Inicjalizacja właściwości i zasobów gry"""

        pygame.init()
        #Utworzenie egzemplarza domyślnych ustawień
        self.settings = Settings()
        #Ekran gry zarządzany przez ustawienia
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), self.settings.fullscreen)
        #Utworzenie egzemplarza statku
        self.ship = Ship(self)
        #Podpis okna wskazany w ustawieniach
        pygame.display.set_caption(self.settings.window_caption)
        #Grupa na wystrzelone pociski
        self.bullets = pygame.sprite.Group()
        #Grupa na wygenerowanych obcych
        self.aliens = pygame.sprite.Group()


    def run_game(self):
        """Główna pętla gry"""

        while True:
            self._check_events()
            self._update_ship()
            self._update_bullets()
            self._update_fleet()
            self._update_screen()


    def _update_screen(self):
        """Zarządzanie oraz wyświetlanie obrazów gry"""

        #Tło
        self.screen.blit(self.settings.background, self.settings.rect)
        #Pociski na tło
        for bullet in self.bullets.sprites():
            bullet.print_bullet()
        #Obczy na pociski na tło
        for alien in self.aliens.sprites():
            alien.print_alien()
        #Statek na obcych na pociski na tło
        self.ship.print_ship()

        #Wyświetlenie kompozycji
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
        """Reakcja na wydarzenie typu: wciśnięty klawisz"""

        #Poruszanie prawo, lewo, góra, dół
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        #Dodanie nowego pocisku do grupy
        elif event.key == pygame.K_SPACE:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        #Wyłączenie gry
        elif event.key == pygame.K_q:
            sys.exit()


    def _key_up_events(self, event):
        """Reakcja na wydarzenie typu: zwolniony klawisz"""

        #Zatrzymywanie poruszania prawo, lewo, góra, dół
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False  


    def _update_bullets(self):
        """Zarządzanie grupą istniejących pocisków"""

        #PRzesunięcie pocisku o 1 jednostkę prędkości
        self.bullets.update()
        #Usuwanie pocisku poza ekranem
        for bullet in self.bullets:
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        #Usuwanie zetkniętych pocisków oraz obcych
        for bullet in self.bullets:
            if bullet.hit():
                self.bullets.remove(bullet)


    def _update_fleet(self):
        """Zarządzanie oraz dodawanie obcych do grupy"""

        #Przesunięcie obcego o 1 jednostkę prędkości
        self.aliens.update()

        #Dodawanie obcych, do momentu osiągnięcia odpowiedniego rozmiaru floty
        if len(self.aliens) < 10:
            new_alien = Alien(self)
            self.aliens.add(new_alien)

        #Usuwanie obcych którzy dotarli do końca ekranu
        for alien in self.aliens:
            if alien.rect.bottom > 800:
                self.aliens.remove(alien)

    
    def _update_ship(self):
        self.ship.update()


if __name__ == '__main__':

    #Utworzenie egzemplarza gry i wywołanie metody rozpoczynającej pętlę gry
    ai = AlienInvasion()
    #Wywołanie egzemplarza gry
    ai.run_game()