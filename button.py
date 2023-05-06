import pygame.font


class Button():
    """Klasa przeznaczona do zarządzania przyciskami"""

    def __init__(self, ai_game, msg, y, nr):
        """Inicjalizacja właściwości i zasobów przycisku"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.settings.rect

        #Właściwości przycisku (rozmiar, kolor i czcionka tekstu, kolor zaznaczenia) )
        self.width, self.height = 200, 45
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('VCR OSD Mono', 100)
        self.text_highlighted = (255, 0, 0)

        #'Pole' przycisku i jego położenie
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y = self.rect.y + y

        #Oznaczenie egzemplarza przycisku
        self.button_number = nr
        
        self.prep_button(msg)
    
    def prep_button(self, text):
        """Przygotowanie właściwości do nałożenia"""

        #Położenie przycisku oraz wygląd aktywnego i nieaktywnego
        self.msg_image_highlighted = self.font.render(text, True, self.text_highlighted)
        self.msg_image = self.font.render(text, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def print_button(self, highlighted):
        """Nałożenie przycisku do wyświetlenia"""

        #Jeżeli jest przyciskiem wybranym
        if self.button_number == highlighted:
            self.screen.blit(self.msg_image_highlighted, self.msg_image_rect)
        #Jeżeli nie jest przyciskiem wybranym
        else:
            self.screen.blit(self.msg_image, self.msg_image_rect)
