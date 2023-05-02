class Level:
    """Monitorowanie przebiegu, etapu oraz statystyk z gry"""

    def __init__(self, ai_game):
        """Inicjalizacja właściwości i zasobów poziomu"""

        self.settings = ai_game.settings
        self.aliens = ai_game.aliens
        self.score = 0
        #Domyślny poziom
        self.level_0()


    def reset_level(self):
        """Resetowanie stanu gry"""
        
        #Powrót do poziomu 0
        self.level_0()
        #Przywrócenie zdrowia
        self.ship_health = self.settings.ship_health
        #Reset wyniku
        self.score = 0


    def level_0(self):
        """Zmiana poziomu gry na poziom 0"""

        #Ustalanie właściwości poziomu
        self.fleet_size = 5
        self.alien_speed = 0.5
        self.alien_health = 1
        self.number = 0
        #Usuwanie planszy obcych
        for alien in self.aliens:
            self.aliens.remove(alien)

    def level_1(self):
        """Zmiana poziomu gry na poziom 1"""

        #Ustalanie właściwości poziomu
        self.fleet_size = 10
        self.alien_speed = 1
        self.alien_health = 1
        self.number = 1
        #Usuwanie planszy obcych
        for alien in self.aliens:
            self.aliens.remove(alien)

    def level_2(self):
        """Zmiana poziomu gry na poziom 2"""

        #Ustalanie właściwości poziomu
        self.fleet_size = 10
        self.alien_speed = 1
        self.alien_health = 2
        self.number = 2
        #Usuwanie planszy obcych
        for alien in self.aliens:
            self.aliens.remove(alien)