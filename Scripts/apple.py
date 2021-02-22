import random
import math
from settings import *

class Apple:
    def __init__(self):
        self.x, self.y = apple_position

    @property
    def pos(self):
        return (self.x, self.y)

    def distance(self, x1, y1, x2, y2):
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return dist

    def move_apple(self, distance):
        if distance <= move_distance:
            self.x = random.randint(0, HEIGHT - apple_size[0])
            self.y = random.randint(0, HEIGHT - apple_size[0])