# Screen settings
WEIGHT = 300
HEIGHT = 300

# Game settings
score = 0
CAPTION = "Змейка"
RUN = True
FPS = 3

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 230, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 207, 255)

# Playground
playground_size = 10
border = 2
block_position = []

# Player settings
player_last_position = (0, 0)
player_position = (150, 150)
player_size = (30, 30)
direction = "Up"
player_speed = 30
tails = [player_position]

# Apple settings
apple_position = (150, 60)
apple_size = (30, 30)
move_distance = player_size[0] - 10