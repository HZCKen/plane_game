class Setting(object):

    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.backgrounColor = (230, 230, 230)

        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        self.alien_speed_factor = 1
        self.flect_drop_speed = 50
        # 方向 1为右移 -1 为左移
        self.fleet_direction = 1