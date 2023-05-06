import pygame.font

class Interface:
    """Klasa przeznaczona do zarządzania interfejsem"""

    def __init__(self, ai_game):
        """Inicjalizacja właściwości i zasobów interfejsu"""

        #Pobieranie zmiennych z głównego pliku
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.level = ai_game.level

        #Czcionka punktacji
        self.score_color = (238, 228, 30)
        self.score_font = pygame.font.SysFont('VCR OSD Mono', 60)
        #Czcionka etapu
        self.stage_color = (238, 228, 30)
        self.stage_font = pygame.font.SysFont('VCR OSD Mono', 17)
        #Czcionka porażki
        self.lose_color = (238, 228, 30)
        self.lose_font = pygame.font.SysFont('VCR OSD Mono', 150)

        #Zdrowie statku
        self.total_health = self.settings.ship_health
        self.left_health = self.total_health
        self.heart = pygame.image.load('images/heart.bmp')
        self.heart_empty = pygame.image.load('images/heart_empty.bmp')
        self.rect_heart = self.heart.get_rect()
        self.rect_heart.topleft = self.screen_rect.topleft

        #Metody warunkujace grafikę interfejsu
        self.prep_score()
        self.prep_stage()
        self.prep_lose()

    def prep_score(self):
        """Przekształcanie punktacji na obraz"""

        score_str = str(self.level.score)

        self.score_image = self.score_font.render(score_str, True, self.score_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20

        self.alien_image = pygame.image.load('images/alien_score.bmp')
        self.alien_rect = self.alien_image.get_rect()
        self.alien_rect.midright = self.score_rect.midleft
        self.alien_rect.top += 3
        

    def prep_stage(self):
        """Przekształcanie stage na obraz"""

        stage_str = (str('STAGE ') + str(self.level.number))
        self.stage_image = self.stage_font.render(stage_str, True, self.stage_color)

        self.stage_rect = self.stage_image.get_rect()
        self.stage_rect.right = self.screen_rect.right - 22
        self.stage_rect.top = self.score_rect.bottom

    def prep_lose(self):
        """Przekształcanie komunikatu porażki na obraz"""
        
        lose_str = ('YOU LOSE')
        self.lose_image = self.lose_font.render(lose_str, True, self.lose_color)

        self.lose_rect = self.lose_image.get_rect()
        self.lose_rect.center = self.screen_rect.center


    def print_score(self):
        """Wyświetlenie elementów interfejsu"""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.stage_image, self.stage_rect)
        self.screen.blit(self.alien_image, self.alien_rect)
        if self.left_health <= 0:
            self.screen.blit(self.lose_image, self.lose_rect)


    def print_health(self, _max, left):
        """Metoda wyświetlająca wskazaną ilość zdrowia"""

        #Wyświetlanie maksymalnego zdrowia
        for _ in range(_max):
            self.screen.blit(self.heart_empty, self.rect_heart)
            self.rect_heart.x += (self.rect_heart.width)
        self.rect_heart.topleft = self.screen_rect.topleft
        
        #Wyświetlanie minimalnego zdrowia
        for _ in range(left):
            self.screen.blit(self.heart, self.rect_heart)
            self.rect_heart.x += (self.rect_heart.width)
        self.rect_heart.topleft = self.screen_rect.topleft