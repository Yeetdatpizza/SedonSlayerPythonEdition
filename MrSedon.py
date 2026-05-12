import pygame
from pygame import Vector2

starting_health = 100
starting_ammo = 12
starting_speed = 5
starting_direction = 1
sedon_distance = 1

just_jumped = False

sedon_jump_height = 5

class Sedon:

    def __init__(self, health, ammo, speed, direction, position):
        self.sedon_health = health
        self.sedon_ammo = ammo
        self.sedon_speed = speed
        self.sedon_direction = direction
        self.sedon_position = position
        self.is_jumping = False
        self.sedon_force = 0

    def update_health(self, health):
        self.sedon_health += health

    def update_ammo(self, ammo):
        self.sedon_ammo += ammo

    def update_speed(self, speed):
        self.sedon_speed += speed

    def update_is_jumping(self):
        self.is_jumping = not self.is_jumping

    def update_direction(self, direction):
        self.sedon_direction = direction

    def update_position_x(self, pixels):
        self.sedon_position = Vector2(self.sedon_position.x + pixels, self.sedon_position.y)

    def update_position_y(self, pixels):
        self.sedon_position = Vector2(self.sedon_position.x, self.sedon_position.y + pixels)

    def update_position(self, vector2):
        self.sedon_position = vector2

    def update_force(self, force):
        self.sedon_force = force

    def get_health(self):
        return self.sedon_health

    def get_ammo(self):
        return self.sedon_ammo

    def get_speed(self):
        return self.sedon_speed

    def get_direction(self):
        return self.sedon_direction

    def get_position(self):
        return self.sedon_position

    def get_is_jumping(self):
        return self.is_jumping

    def get_force(self):
        return self.sedon_force