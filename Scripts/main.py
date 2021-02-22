import pygame
from settings import *
from player import Player
from apple import Apple

pygame.init()
screen = pygame.display.set_mode([WEIGHT, HEIGHT])
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()
player = Player()
apple = Apple()

while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    player.movement()
    distance = apple.distance(player.pos[0], player.pos[1], apple.pos[0], apple.pos[1])
    apple.move_apple(distance)

    screen.fill(BLACK)

    #player
    pygame.draw.rect(screen, GREEN, [player.pos, player_size])

    #apple
    pygame.draw.rect(screen, RED, [apple.pos, apple_size])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()