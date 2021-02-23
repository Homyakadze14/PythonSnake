# Imports modules
import pygame
import math
import random
from settings import *


# Draw playground
def draw_playground(size):
    x = 0
    y = 0
    for i in range(size):
        for j in range(size):
            pygame.draw.rect(screen, BLACK, [[x, y], player_size], border)
            if (x, y) not in block_position:
                block_position.append((x, y))
            x += player_size[0]
        y += player_size[0]
        x = 0


# Set direction
def set_direction(dir):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and dir != "Down":
        dir = "Up"
    elif keys[pygame.K_s] and dir != "Up":
        dir = "Down"
    elif keys[pygame.K_a] and dir != "Right":
        dir = "Left"
    elif keys[pygame.K_d] and dir != "Left":
        dir = "Right"

    return dir


# Die check
def die_check(x, y):
    for i in range(1, len(tails)):
        if player_position == tails[i]:
            die()
            return False
    return True


# Teleport
def teleport():
    x = player_position[0]
    y = player_position[1]
    pos = (x, y)

    if x < 0:
        pos = (300, y)
    elif x + player_size[0] > WEIGHT:
        pos = (0, y)
    elif y < 0:
        pos = (x, 300)
    elif y + player_size[0] > HEIGHT:
        pos = (x, 0)

    return pos


# Move
def player_movement(dir, X, Y, tails):
    x = X
    y = Y

    if die_check(x, y):
        if dir == "Up":
            y -= player_speed
        elif dir == "Down":
            y += player_speed
        elif dir == "Right":
            x += player_speed
        elif dir == "Left":
            x -= player_speed

    tails.pop(0)
    tails.insert(0, player_position)

    for i in range(len(tails)):
        if (i + 1) < len(tails):
            tails[i], tails[i + 1] = tails[i + 1], tails[i]

    return (x, y)


# Distance
def get_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


# Apple move
def apple_movement(blockPos, distance):
    randomPosition = random.choice(blockPos)
    x = randomPosition[0]
    y = randomPosition[1]
    while (x, y) in tails:
        randomPosition = random.choice(blockPos)
        x = randomPosition[0]
        y = randomPosition[1]
    return (x, y)

def die():
    file = open('score.txt', 'w')
    file.write(f"Score: {score}")
    file.close()


# Game
pygame.init()

# Display set
screen = pygame.display.set_mode([WEIGHT, HEIGHT])
clock = pygame.time.Clock()

while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    # Fill display
    screen.fill(GREEN)

    # Events
    draw_playground(playground_size)

    direction = set_direction(direction)
    player_last_position = player_position
    player_position = player_movement(direction, player_position[0], player_position[1], tails)
    player_position = teleport()

    distance = get_distance(player_position[0], player_position[1], apple_position[0], apple_position[1])
    if move_distance >= distance:
        score += 1
        apple_position = apple_movement(block_position, distance)
        tails.append(player_last_position)

    # Draw elements
    for i in range(1, len(tails)):
        pygame.draw.rect(screen, BLUE, [tails[i], player_size])
    pygame.draw.rect(screen, LIGHT_BLUE, [player_position, player_size])

    pygame.draw.rect(screen, RED, [apple_position, apple_size])

    # Display update
    pygame.display.set_caption(CAPTION)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()