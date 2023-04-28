import pygame

class Settings:
    """Klasa przechowująca ustawienia gry"""

    def __init__(self):
        """Inicjalizacja ustawień"""
        #Ustawienia ekranu
        self.background = pygame.image.load('images/tło.bmp')
        self.rect = self.background.get_rect()
        self.window_caption = "Inwazja obcych"

        self.screen_width = 1200
        self.screen_height = 800
        self.full_screen = False
        if self.full_screen == False:
            self.fullscreen = 0
        else:
            self.fullscreen = pygame.FULLSCREEN

        self.bullet_speed = 1.0
        self.ship_speed = 1.2




