# Imports moduls
import pygame
from settings import *
from player import Player
from apple import Apple

# Game
pygame.init()

# Display set
screen = pygame.display.set_mode([WEIGHT, HEIGHT])
clock = pygame.time.Clock()
player = Player()
apple = Apple()

while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    screen.fill(BLACK)

    # Player
    player.set_direction()
    direction = player.dir
    player.movement(direction)
    pygame.draw.rect(screen, GREEN, [player.pos, player_size])

    # Apple
    distance = apple.distance(player.pos[0], player.pos[1], apple.pos[0], apple.pos[1])
    apple.move_apple(distance)
    pygame.draw.rect(screen, RED, [apple.pos, apple_size])

    # Display update
    CAPTION = f"Score: {apple.now_score}"
    pygame.display.set_caption(CAPTION)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()