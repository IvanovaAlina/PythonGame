import pygame.font
from pygame.sprite import Group
from shipForLife import ShipForLife

class Scoreboard():

    def __init__(self, ai_game):

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 22)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        self.ships = Group()
        for ship_num in range(self.stats.ships_left):
            ship = ShipForLife(self.ai_game)
            ship.rect.x = 10 + ship_num*ship.rect.width*1.3
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self):
        level_str = "Уровень: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        rounded_high_score = round(self.stats.high_score, -1)
        score_str = "Лучший результат: "  "{:,}".format(rounded_high_score) 
        self.high_score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.centerx
        self.high_score_rect.top  = self.score_rect.top

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "Текущий счёт: " "{:,}".format(rounded_score) 
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top  = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()