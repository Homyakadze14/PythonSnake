import pygame
from settings import *
import pyglet

pygame.init()

#display
screen = pygame.display.set_mode([WEIGHT, HEIGHT])
pygame.display.set_caption(caption)
screen.fill(BLACK)

#flip
pygame.display.flip()



#exit and game
game_run = True
while game_run:
    sound = pyglet.media.load('проверка.mp3',)
    sound.play()
    pyglet.app.run()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game_run = False

pygame.quit()