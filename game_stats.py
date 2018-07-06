class GameStats():
    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.reset_stats()
        self.game_active = False
        print(self.ship_life)


    def reset_stats(self):
        self.ship_life = self.ai_setting.ship_limit