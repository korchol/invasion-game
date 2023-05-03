import pygame.font


class Button():
    def __init__(self, ai_game, msg, y, nr):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 45
        self.button_color = (238, 228, 30)
        self.text_color = (255, 255, 255)
        self.text_highlighted = (255, 0, 0)
        self.font = pygame.font.SysFont('VCR OSD Mono', 100)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y = self.rect.y + y
        self.button_number = nr
        
        self.prep_button(msg)
    
    def prep_button(self, text):

        self.msg_image_highlighted = self.font.render(text, True, self.text_highlighted)
        self.msg_image = self.font.render(text, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def print_button(self, highlighted):
        if self.button_number == highlighted:
            self.screen.blit(self.msg_image_highlighted, self.msg_image_rect)
        else:
            self.screen.blit(self.msg_image, self.msg_image_rect)
