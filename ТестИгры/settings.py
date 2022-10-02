import pygame as pg
class Settings():

    def __init__(self):

        self.screen_width = 1000
        self.screen_height = 700
        self.bg_image = pg.image.load("images/sky.bmp")
        self.bg_color = (230, 230, 230)
        self.caption = "Тестовая игра"

        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        self.fleet_drop_speed = 10
        self.speedup_scale = 1.5
        self.pointup_scale = 2
        self.init_dynamic_settings()
        #self.fleet_direction = 1

    def init_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1
        self.alien_speed = 0.1
        self.alien_points = 10

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.pointup_scale)