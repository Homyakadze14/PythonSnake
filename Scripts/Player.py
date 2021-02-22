import pygame
from settings import *

class Player:
    def __init__(self):
        self.x, self.y = player_position

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > 0:
            self.x -= player_speed
        if keys[pygame.K_d] and self.x < WEIGHT - player_size[0]:
            self.x += player_speed
        if keys[pygame.K_w] and self.y > 0:
            self.y -= player_speed
        if keys[pygame.K_s] and self.y < HEIGHT - player_size[0]:
            self.y += player_speed
