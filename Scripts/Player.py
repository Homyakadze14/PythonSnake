import pygame
from settings import *

class Player:
    def __init__(self):
        self.x, self.y = player_position
        self.direction = direction

    @property
    def pos(self):
        return (self.x, self.y)

    @property
    def dir(self):
        return self.direction

    def set_direction(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.direction = "Left"
        if keys[pygame.K_d]:
            self.direction = "Right"
        if keys[pygame.K_w]:
            self.direction = "Up"
        if keys[pygame.K_s]:
            self.direction = "Down"

    def movement(self, direction):
        if direction == "Right" and self.x < WEIGHT - player_size[0]:
            self.x += player_speed
        elif direction == "Left" and self.x > 0:
            self.x -= player_speed
        elif direction == "Up" and self.y > 0:
            self.y -= player_speed
        elif direction == "Down" and self.y < HEIGHT - player_size[0]:
            self.y += player_speed
