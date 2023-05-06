import sys
import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien
from level import Level
from interface import Interface
from menu import Menu

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
        #Utworzenie egzemplarza levela
        self.level = Level(self)
        #Utworzenie egzemplarza tablicy
        self.interface = Interface(self)
        #Innicjalizacja zmiennej przerwy
        self.fleet_cd = 0
        #Utworzenie egzemplarza menu
        self.menu = Menu(self)
        #Status aktywności rozgrywki
        self.game_active = False





    def run_game(self):
        """Główna pętla gry"""

        while True:
            self._check_events()
            if self.game_active:
                self._update_level()
                self._update_ship()
                self._detect_hit()
                self._update_fleet()
                self._update_bullets()
            self._update_screen()


    def _update_screen(self):
        """Zarządzanie oraz wyświetlanie obrazów gry"""

        #Nałożenie warstw menu
        if self.game_active == False:
            self.menu.update_menu()
        #Jeżeli gra aktywna nałożenie warstw gry
        else:
            #Tło
            self.screen.blit(self.settings.background, self.settings.rect)
            #Pociski na tło
            for bullet in self.bullets.sprites():
                bullet.print_bullet()
            #Obcy na pociski na tło
            for alien in self.aliens.sprites():
                alien.print_alien()
            #Statek na obcych na pociski na tło
            self.ship.print_ship()
            #Pasek zdrowia na statek na obcych na pociski na tło
            self.interface.print_health(self.interface.total_health, self.interface.left_health)
            self.interface.print_score()
        
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
            if self.game_active == False:
                self.menu.button_up()
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
            if self.game_active == False:
                self.menu.button_down()
        #Wyjście do menu
        elif event.key == pygame.K_ESCAPE:
            self.game_active = False
        #Dodanie nowego pocisku do grupy
        elif event.key == pygame.K_SPACE:
            if self.game_active:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
            else:
                self.menu.button_click(self)
            


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


    def _update_level(self):
        """Sprawdzanie wyniku i aktualizowanie egzemplarza poziomu"""
        
        if self.level.number == 0:
            self.level.level_0()
        elif self.level.score == 10 and self.level.number == 1:
            self.level.level_1()
            self.interface.prep_stage()
        elif self.level.score == 20 and self.level.number == 2:
            self.level.level_2()
            self.interface.prep_stage()
        elif self.level.score == 30 and self.level.number == 3:
            self.level.level_3()
            self.interface.prep_stage()
        elif self.level.score == 40 and self.level.number == 4:
            self.level.level_4()
            self.interface.prep_stage()
        # elif self.level.score == 50 and self.level.number == 4:
        #     self.level.level_5()
        #     self.interface.prep_stage()


    def _update_bullets(self):
        """Zarządzanie grupą istniejących pocisków"""

        #Przesunięcie pocisku o 1 jednostkę prędkości
        self.bullets.update()
        #Usuwanie pocisku poza ekranem
        for bullet in self.bullets:
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)


    def _update_fleet(self):
        """Zarządzanie grupą istniejących obcych oraz jej formowanie"""

        #Aktualizowanie właściwości obcego
        self.aliens.update(self)

        #Dodawanie obcych w odstępach fleet_cd, do momentu osiągnięcia odpowiedniego rozmiaru floty
        if self.fleet_cd < 100:
            self.fleet_cd += 1
        else:
            if len(self.aliens) < self.level.fleet_size:
                new_alien = Alien(self)
                self.aliens.add(new_alien)
                self.fleet_cd = 0
            self.fleet_cd = 0

        #Usuwanie obcych którzy dotarli do końca ekranu
        for alien in self.aliens:
            if alien.rect.bottom > 800:
                self.aliens.remove(alien)
        
        #Wybuchanie trafionych obcych
        for alien in self.aliens:
            if alien.live == False:
                alien.alien_boom()
                alien.time_dead += 1
                if alien.time_dead > 100:
                    self.aliens.remove(alien)
                    self.level.score += 1
                    self.interface.prep_score()


    def _detect_hit(self):
        """Wykrywanie oraz zarządzanie zderzeniami"""

        #Zderzenie obcego z pociskiem lub statkiem
        for alien in self.aliens:
            alien.hit()
            if self.ship.rect.colliderect(alien.rect):
                self.interface.left_health -= 1
                self.aliens.remove(alien)


    def _update_ship(self):
        self.ship.update()



if __name__ == '__main__':

    #Utworzenie egzemplarza gry i wywołanie metody rozpoczynającej pętlę gry
    ai = AlienInvasion()
    #Wywołanie egzemplarza gry
    ai.run_game()