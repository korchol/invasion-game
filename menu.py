from sys import exit
import pygame.font
from button import Button


class Menu():
    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.background = pygame.image.load('images/tło.bmp')

        self.button_resume = Button(ai_game, 'RESUME', -225, 0)
        self.button_start = Button(ai_game, 'NEW GAME', -75, 1)
        self.button_settings = Button(ai_game, 'SETTINGS', 75, 2)
        self.button_exit = Button(ai_game, 'EXIT', 225, 3)

        self.button_highlighted = 0

        self.update_menu()

    def update_menu(self):
        self.screen.blit(self.background, self.screen_rect)
        self.button_start.print_button(self.button_highlighted)
        self.button_resume.print_button(self.button_highlighted)
        self.button_settings.print_button(self.button_highlighted)
        self.button_exit.print_button(self.button_highlighted)

    def button_down(self):
        if self.button_highlighted < 3:
            self.button_highlighted += 1

    def button_up(self):
        if self.button_highlighted  > 0:
            self.button_highlighted -= 1

    def button_click(self, ai_game):
        if self.button_highlighted == 0:
            ai_game.game_active = True
        elif self.button_highlighted == 1:
            self.button_highlighted == 0
            ai_game.game_active = True
            ai_game.level.reset_level()
            ai_game.scoreboard.prep_score()
            ai_game.scoreboard.prep_stage()
            ai_game.scoreboard.left_health = ai_game.settings.ship_health
        elif self.button_highlighted == 2:
             pass
        elif self.button_highlighted == 3:
            exit()


