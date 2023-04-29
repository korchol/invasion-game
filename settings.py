import pygame

class Settings:
    """Klasa przechowująca ustawienia gry"""

    def __init__(self):
        """Inicjalizacja właściwości ustawień"""

        #Ustawienia ekranu (tło, obszar tła, nazwa okna)
        self.background = pygame.image.load('images/tło.bmp')
        self.rect = self.background.get_rect()
        self.window_caption = "Inwazja obcych"

        #Rozdzielczość
        self.screen_width = 1200
        self.screen_height = 800

        #Fullscreen
        self.full_screen = False
        if self.full_screen == False:
            self.fullscreen = 0
        else:
            self.fullscreen = pygame.FULLSCREEN

        #Ustawienia dynamiki (szybkość pocisku, szybkość statku)
        self.bullet_speed = 0.5
        self.ship_speed = 1.2




