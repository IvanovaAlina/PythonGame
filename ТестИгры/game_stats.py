
class GameStats():

    def __init__(self, ai_game):
        self.setting = ai_game.settings
        self.game_active = False
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.setting.ship_limit
        self.score = 0
        self.level = 1
        