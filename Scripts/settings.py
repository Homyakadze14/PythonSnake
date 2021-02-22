# Screen settings
WEIGHT = 600
HEIGHT = 600
HALF_WEIGHT = WEIGHT // 2
HALF_HEIGHT = HEIGHT // 2

# Game settings
CAPTION = "Змейка"
RUN = True
FPS = 60
game_score = 0

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 244, 0)
RED = (255, 0, 0)

# Player settings
player_position = (HALF_WEIGHT, HALF_HEIGHT)
player_size = (30, 30)
direction = "Up"
player_speed = 2

# Apple settings
apple_position = (HALF_WEIGHT, HALF_HEIGHT - 50)
apple_size = (30, 30)
move_distance = 30