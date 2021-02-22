import pygame
from settings import *
from player import Player

pygame.init()
screen = pygame.display.set_mode([WEIGHT, HEIGHT])
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()
player = Player()

while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    player.movement()
    screen.fill(BLACK)

    pygame.draw.rect(screen, GREEN, [player.pos, player_size])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()