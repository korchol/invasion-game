class Level:
    """Monitorowanie przebiegu, etapu oraz statystyk z gry"""

    def __init__(self, ai_game):
        """Inicjalizacja właściwości i zasobów poziomu"""

        self.settings = ai_game.settings
        self.aliens = ai_game.aliens

        self.score = 0
        #Domyślny poziom
        self.level_0()
        self.number = 0


    def reset_level(self):
        """Resetowanie stanu gry"""

        #Przywrócenie zdrowia
        self.ship_health = self.settings.ship_health
        #Reset wyniku
        self.score = 0
        self.number = 0


    def level_0(self):
        """Zmiana poziomu gry na poziom 0"""

        #Ustalanie właściwości poziomu
        self.fleet_size = 4
        self.alien_speed = 0.4
        self.alien_health = 1
        self.number = 1
        #Usuwanie planszy obcych
        for alien in self.aliens:
            self.aliens.remove(alien)

    def level_1(self):
        """Zmiana poziomu gry na poziom 1"""

        #Ustalanie właściwości poziomu
        self.fleet_size = 6
        self.alien_speed = 0.6
        self.alien_health = 1
        self.number = 2
        #Usuwanie planszy obcych
        for alien in self.aliens:
            self.aliens.remove(alien)

    def level_2(self):
        """Zmiana poziomu gry na poziom 2"""

        #Ustalanie właściwości poziomu
        self.fleet_size = 8
        self.alien_speed = 0.7
        self.alien_health = 1
        self.number = 3
        #Usuwanie planszy obcych
        for alien in self.aliens:
            self.aliens.remove(alien)

    def level_3(self):
        """Zmiana poziomu gry na poziom 2"""

        #Ustalanie właściwości poziomu
        self.fleet_size = 10
        self.alien_speed = 0.8
        self.alien_health = 1
        self.number = 4
        #Usuwanie planszy obcych
        for alien in self.aliens:
            self.aliens.remove(alien)

    def level_4(self):
        """Zmiana poziomu gry na poziom 2"""

        #Ustalanie właściwości poziomu
        self.fleet_size = 10
        self.alien_speed = 0.8
        self.alien_health = 2
        self.number = 5
        #Usuwanie planszy obcych
        for alien in self.aliens:
            self.aliens.remove(alien)