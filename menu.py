from sys import exit
import pygame.font
from button import Button


class Menu():
    """Klasa przeznaczona do zarządzania menu"""

    def __init__(self, ai_game):
        """Inicjalizacja właściwości i zasobów menu"""

        #Pobranie ustawień ekranu
        self.screen = ai_game.screen
        self.screen_rect = ai_game.settings.rect
        self.background = ai_game.settings.background

        #Umiejscowienie przycisków na ekranie
        self.button_resume = Button(ai_game, 'RESUME', -225, 0)
        self.button_start = Button(ai_game, 'NEW GAME', -75, 1)
        self.button_settings = Button(ai_game, 'SETTINGS', 75, 2)
        self.button_exit = Button(ai_game, 'EXIT', 225, 3)

        #Inicjacja zmiennej wskazującej, który z przycisków jest 'aktywny'
        self.button_active = 0


    def update_menu(self):
        """Nałożenie tła oraz pozycji menu w odpowiedniej formie"""

        #Nałożenie tła
        self.screen.blit(self.background, self.screen_rect)
        #Nałożenie przycisków po sprawdzeniu czy przycisk jest aktywny
        self.button_start.print_button(self.button_active)
        self.button_resume.print_button(self.button_active)
        self.button_settings.print_button(self.button_active)
        self.button_exit.print_button(self.button_active)


    def button_down(self):
        """Zmiana aktywnego przycisku na jeden wyżej"""

        if self.button_active < 3:
            self.button_active += 1


    def button_up(self):
        """Zmiana aktywnego przycisku na jeden niżej"""

        if self.button_active  > 0:
            self.button_active -= 1


    def button_click(self, ai_game):
        """Funkcja każdej z pozycji menu (0, 1, 2, 3)"""

        if self.button_active == 0:
            ai_game.game_active = True
        elif self.button_active == 1:
            self.button_active == 0
            ai_game.game_active = True
            ai_game.level.reset_level()
            ai_game.interface.prep_score()
            ai_game.interface.prep_stage()
            ai_game.interface.left_health = ai_game.settings.ship_health
        elif self.button_active == 2:
             pass
        elif self.button_active == 3:
            exit()


